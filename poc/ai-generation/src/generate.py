#!/usr/bin/env python3
"""
AI Generation POC - Main Generation Script
R&D Tax Relief Project Card Generator

This script implements the 3-stage generation pipeline:
- Stage 1: Project Analysis & R&D Identification
- Stage 2: Section-by-Section Generation
- Stage 3: Coherence Review & Compliance Validation
"""

import os
import sys
import json
import time
from pathlib import Path
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass, asdict
from datetime import datetime

import pandas as pd
from dotenv import load_dotenv
from anthropic import Anthropic
from openai import AzureOpenAI
import tiktoken
from tqdm import tqdm

# Load environment variables
load_dotenv()

# Configuration
@dataclass
class Config:
    """POC Configuration"""
    anthropic_api_key: str = os.getenv("ANTHROPIC_API_KEY", "")
    azure_api_key: str = os.getenv("AZURE_OPENAI_API_KEY", "")
    azure_endpoint: str = os.getenv("AZURE_OPENAI_ENDPOINT", "")
    azure_deployment: str = os.getenv("AZURE_OPENAI_DEPLOYMENT", "gpt-4")

    output_dir: Path = Path(os.getenv("POC_OUTPUT_DIR", "results"))
    models: List[str] = None

    temperature: float = float(os.getenv("MODEL_TEMPERATURE", "0.3"))
    max_tokens: int = int(os.getenv("MODEL_MAX_TOKENS", "8000"))
    top_p: float = float(os.getenv("MODEL_TOP_P", "0.95"))

    max_retries: int = int(os.getenv("MAX_RETRIES", "3"))
    retry_delay: int = int(os.getenv("RETRY_DELAY_SECONDS", "5"))

    few_shot_count: int = int(os.getenv("FEW_SHOT_COUNT", "2"))

    def __post_init__(self):
        if self.models is None:
            models_str = os.getenv("POC_MODELS", "claude")
            self.models = [m.strip() for m in models_str.split(",")]

        # Create output directories
        self.output_dir.mkdir(parents=True, exist_ok=True)
        (self.output_dir / "claude").mkdir(exist_ok=True)
        (self.output_dir / "gpt4").mkdir(exist_ok=True)
        (self.output_dir / "metadata").mkdir(exist_ok=True)


@dataclass
class TestCase:
    """Test case data structure"""
    test_id: str
    nazwa_projektu: str
    opis: str
    data_rozpoczecia: str
    data_zakonczenia: str
    cel_projektu: str
    osoba_odpowiedzialna: str
    industry: str
    complexity: str
    input_quality: str


@dataclass
class GenerationResult:
    """Result of generation pipeline"""
    test_id: str
    model: str
    stage1_output: str
    stage2_output: str
    stage3_output: str
    final_card: str
    quality_score: int
    input_tokens: int
    output_tokens: int
    total_tokens: int
    cost_usd: float
    cost_eur: float
    duration_seconds: float
    timestamp: str
    error: Optional[str] = None


class AIClient:
    """Unified AI client for Claude and GPT-4"""

    def __init__(self, config: Config):
        self.config = config
        self.anthropic_client = None
        self.azure_client = None

        if config.anthropic_api_key:
            self.anthropic_client = Anthropic(api_key=config.anthropic_api_key)

        if config.azure_api_key and config.azure_endpoint:
            self.azure_client = AzureOpenAI(
                api_key=config.azure_api_key,
                api_version="2024-02-15-preview",
                azure_endpoint=config.azure_endpoint
            )

        # Token encoder for counting
        self.encoder = tiktoken.get_encoding("cl100k_base")

    def count_tokens(self, text: str) -> int:
        """Count tokens in text"""
        return len(self.encoder.encode(text))

    def call_claude(self, prompt: str, max_tokens: int = None) -> Tuple[str, int, int]:
        """
        Call Claude API
        Returns: (response_text, input_tokens, output_tokens)
        """
        if not self.anthropic_client:
            raise ValueError("Anthropic API key not configured")

        max_tokens = max_tokens or self.config.max_tokens

        response = self.anthropic_client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=max_tokens,
            temperature=self.config.temperature,
            messages=[{"role": "user", "content": prompt}]
        )

        output_text = response.content[0].text
        input_tokens = response.usage.input_tokens
        output_tokens = response.usage.output_tokens

        return output_text, input_tokens, output_tokens

    def call_gpt4(self, prompt: str, max_tokens: int = None) -> Tuple[str, int, int]:
        """
        Call GPT-4 via Azure OpenAI
        Returns: (response_text, input_tokens, output_tokens)
        """
        if not self.azure_client:
            raise ValueError("Azure OpenAI not configured")

        max_tokens = max_tokens or self.config.max_tokens

        response = self.azure_client.chat.completions.create(
            model=self.config.azure_deployment,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=max_tokens,
            temperature=self.config.temperature,
            top_p=self.config.top_p
        )

        output_text = response.choices[0].message.content
        input_tokens = response.usage.prompt_tokens
        output_tokens = response.usage.completion_tokens

        return output_text, input_tokens, output_tokens

    def generate(self, model: str, prompt: str, max_tokens: int = None) -> Tuple[str, int, int]:
        """
        Universal generate method with retry logic
        """
        for attempt in range(self.config.max_retries):
            try:
                if model == "claude":
                    return self.call_claude(prompt, max_tokens)
                elif model == "gpt4":
                    return self.call_gpt4(prompt, max_tokens)
                else:
                    raise ValueError(f"Unknown model: {model}")

            except Exception as e:
                if attempt < self.config.max_retries - 1:
                    print(f"⚠️  Attempt {attempt + 1} failed: {e}. Retrying in {self.config.retry_delay}s...")
                    time.sleep(self.config.retry_delay)
                else:
                    raise


class PromptLoader:
    """Load and format prompts"""

    def __init__(self, prompts_dir: Path):
        self.prompts_dir = prompts_dir
        self._cache = {}

    def load(self, stage: str) -> str:
        """Load prompt template for stage"""
        if stage in self._cache:
            return self._cache[stage]

        prompt_file = self.prompts_dir / f"{stage}.txt"
        if not prompt_file.exists():
            raise FileNotFoundError(f"Prompt file not found: {prompt_file}")

        with open(prompt_file, 'r', encoding='utf-8') as f:
            prompt = f.read()

        self._cache[stage] = prompt
        return prompt

    def format_stage1(self, test_case: TestCase) -> str:
        """Format Stage 1 prompt with test case data"""
        template = self.load("stage1-analysis")

        return template.format(
            project_name=test_case.nazwa_projektu,
            project_description=test_case.opis,
            start_date=test_case.data_rozpoczecia,
            end_date=test_case.data_zakonczenia,
            project_goal=test_case.cel_projektu,
            responsible_person=test_case.osoba_odpowiedzialna
        )

    def format_stage2(self, test_case: TestCase, stage1_output: str, examples: str = "") -> str:
        """Format Stage 2 prompt with test case data and Stage 1 analysis"""
        template = self.load("stage2-generation")

        # Insert examples if provided
        if examples:
            examples_section = f"\n\n===== EXAMPLE REFERENCE CARDS =====\n\n{examples}\n\n"
        else:
            examples_section = ""

        formatted = template.format(
            project_name=test_case.nazwa_projektu,
            project_description=test_case.opis,
            start_date=test_case.data_rozpoczecia,
            end_date=test_case.data_zakonczenia,
            project_goal=test_case.cel_projektu,
            responsible_person=test_case.osoba_odpowiedzialna,
            stage1_analysis=stage1_output
        )

        # Insert examples after INPUT DATA section
        if examples:
            formatted = formatted.replace("===== YOUR TASK =====", examples_section + "===== YOUR TASK =====")

        return formatted

    def format_stage3(self, test_case: TestCase, stage2_output: str) -> str:
        """Format Stage 3 prompt with test case data and Stage 2 generated card"""
        template = self.load("stage3-review")

        return template.format(
            project_name=test_case.nazwa_projektu,
            project_description=test_case.opis,
            start_date=test_case.data_rozpoczecia,
            end_date=test_case.data_zakonczenia,
            project_goal=test_case.cel_projektu,
            responsible_person=test_case.osoba_odpowiedzialna,
            stage2_generated_card=stage2_output
        )


class ExampleManager:
    """Manage few-shot examples"""

    def __init__(self, examples_dir: Path):
        self.examples_dir = examples_dir
        self._examples = {}
        self._load_examples()

    def _load_examples(self):
        """Load all example files"""
        if not self.examples_dir.exists():
            print(f"⚠️  Examples directory not found: {self.examples_dir}")
            return

        for example_file in self.examples_dir.glob("*.txt"):
            example_name = example_file.stem
            with open(example_file, 'r', encoding='utf-8') as f:
                self._examples[example_name] = f.read()

    def get_examples_for_industry(self, industry: str, count: int = 2) -> str:
        """Get appropriate examples for given industry"""
        # Simple strategy: return first N examples
        # TODO: Implement domain matching logic

        example_names = list(self._examples.keys())[:count]
        examples_text = []

        for i, name in enumerate(example_names, 1):
            examples_text.append(f"**PRZYKŁAD {i}:** {name}\n\n{self._examples[name]}")

        return "\n\n---\n\n".join(examples_text)


class Generator:
    """Main generation pipeline"""

    def __init__(self, config: Config):
        self.config = config
        self.ai_client = AIClient(config)
        self.prompt_loader = PromptLoader(Path("prompts"))
        self.example_manager = ExampleManager(Path("prompts/examples"))

    def generate_card(self, test_case: TestCase, model: str) -> GenerationResult:
        """
        Run complete 3-stage generation pipeline
        """
        start_time = time.time()
        total_input_tokens = 0
        total_output_tokens = 0

        try:
            # Stage 1: Analysis
            print(f"  Stage 1: Analysis...")
            stage1_prompt = self.prompt_loader.format_stage1(test_case)
            stage1_output, s1_in, s1_out = self.ai_client.generate(model, stage1_prompt, max_tokens=2000)
            total_input_tokens += s1_in
            total_output_tokens += s1_out

            # Stage 2: Generation
            print(f"  Stage 2: Generation...")
            examples = self.example_manager.get_examples_for_industry(
                test_case.industry,
                count=self.config.few_shot_count
            )
            stage2_prompt = self.prompt_loader.format_stage2(test_case, stage1_output, examples)
            stage2_output, s2_in, s2_out = self.ai_client.generate(model, stage2_prompt, max_tokens=6000)
            total_input_tokens += s2_in
            total_output_tokens += s2_out

            # Stage 3: Review
            print(f"  Stage 3: Review...")
            stage3_prompt = self.prompt_loader.format_stage3(test_case, stage2_output)
            stage3_output, s3_in, s3_out = self.ai_client.generate(model, stage3_prompt, max_tokens=8000)
            total_input_tokens += s3_in
            total_output_tokens += s3_out

            # Extract final card and quality score from Stage 3
            final_card = self._extract_final_card(stage3_output)
            quality_score = self._extract_quality_score(stage3_output)

            # Calculate cost
            cost_usd = self._calculate_cost(model, total_input_tokens, total_output_tokens)
            cost_eur = cost_usd * 0.93

            duration = time.time() - start_time

            return GenerationResult(
                test_id=test_case.test_id,
                model=model,
                stage1_output=stage1_output,
                stage2_output=stage2_output,
                stage3_output=stage3_output,
                final_card=final_card,
                quality_score=quality_score,
                input_tokens=total_input_tokens,
                output_tokens=total_output_tokens,
                total_tokens=total_input_tokens + total_output_tokens,
                cost_usd=cost_usd,
                cost_eur=cost_eur,
                duration_seconds=duration,
                timestamp=datetime.now().isoformat(),
                error=None
            )

        except Exception as e:
            duration = time.time() - start_time
            print(f"❌ Error: {e}")
            return GenerationResult(
                test_id=test_case.test_id,
                model=model,
                stage1_output="",
                stage2_output="",
                stage3_output="",
                final_card="",
                quality_score=0,
                input_tokens=total_input_tokens,
                output_tokens=total_output_tokens,
                total_tokens=total_input_tokens + total_output_tokens,
                cost_usd=0.0,
                cost_eur=0.0,
                duration_seconds=duration,
                timestamp=datetime.now().isoformat(),
                error=str(e)
            )

    def _extract_final_card(self, stage3_output: str) -> str:
        """Extract final project card from Stage 3 output"""
        # Look for "CZĘŚĆ B: OSTATECZNA KARTA PROJEKTU" section
        marker = "CZĘŚĆ B: OSTATECZNA KARTA PROJEKTU"
        if marker in stage3_output:
            return stage3_output.split(marker)[1].strip()

        # Fallback: return entire output
        return stage3_output

    def _extract_quality_score(self, stage3_output: str) -> int:
        """Extract quality score from Stage 3 output"""
        # Look for "Szacunkowy wynik jakości" or similar
        import re
        pattern = r"(?:Szacunkowy wynik jakości|Estimated quality score|quality_score)[:\s]+(\d{1,3})"
        match = re.search(pattern, stage3_output, re.IGNORECASE)

        if match:
            return int(match.group(1))

        # Default if not found
        return 0

    def _calculate_cost(self, model: str, input_tokens: int, output_tokens: int) -> float:
        """Calculate cost in USD"""
        if model == "claude":
            input_cost = (input_tokens / 1_000_000) * 3.0
            output_cost = (output_tokens / 1_000_000) * 15.0
        elif model == "gpt4":
            input_cost = (input_tokens / 1_000_000) * 5.0
            output_cost = (output_tokens / 1_000_000) * 15.0
        else:
            return 0.0

        return input_cost + output_cost

    def save_result(self, result: GenerationResult):
        """Save generation result to files"""
        # Save final card as markdown
        output_file = self.config.output_dir / result.model / f"{result.test_id}.md"
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(result.final_card)

        # Save metadata as JSON
        metadata_file = self.config.output_dir / "metadata" / f"{result.test_id}-{result.model}.json"
        with open(metadata_file, 'w', encoding='utf-8') as f:
            json.dump(asdict(result), f, indent=2, ensure_ascii=False)

        print(f"✅ Saved: {output_file}")


def load_test_cases(csv_path: Path) -> List[TestCase]:
    """Load test cases from CSV file"""
    df = pd.read_csv(csv_path)

    test_cases = []
    for _, row in df.iterrows():
        test_cases.append(TestCase(
            test_id=row['Test ID'],
            nazwa_projektu=row['Nazwa projektu'],
            opis=row['Opis'],
            data_rozpoczecia=row['Data rozpoczęcia'],
            data_zakonczenia=row['Data zakończenia'],
            cel_projektu=row['Cel projektu'],
            osoba_odpowiedzialna=row['Osoba odpowiedzialna'],
            industry=row['Industry'],
            complexity=row['Complexity'],
            input_quality=row['Input Quality']
        ))

    return test_cases


def main():
    """Main execution"""
    print("=" * 60)
    print("AI Generation POC - R&D Tax Relief Project Cards")
    print("=" * 60)
    print()

    # Load configuration
    config = Config()

    # Load test cases
    test_cases_path = Path("test-cases.csv")
    if not test_cases_path.exists():
        print(f"❌ Test cases file not found: {test_cases_path}")
        sys.exit(1)

    test_cases = load_test_cases(test_cases_path)
    print(f"📋 Loaded {len(test_cases)} test cases")
    print()

    # Initialize generator
    generator = Generator(config)

    # Run generation for each model and test case
    all_results = []

    for model in config.models:
        print(f"\n🤖 MODEL: {model.upper()}")
        print("-" * 60)

        for test_case in tqdm(test_cases, desc=f"Generating with {model}"):
            print(f"\n{test_case.test_id}: {test_case.nazwa_projektu}")

            result = generator.generate_card(test_case, model)
            generator.save_result(result)
            all_results.append(result)

            print(f"  Quality Score: {result.quality_score}/100")
            print(f"  Cost: €{result.cost_eur:.3f} (${result.cost_usd:.3f})")
            print(f"  Duration: {result.duration_seconds:.1f}s")
            print(f"  Tokens: {result.total_tokens:,} ({result.input_tokens:,} in, {result.output_tokens:,} out)")

    # Summary
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)

    for model in config.models:
        model_results = [r for r in all_results if r.model == model]
        successful = [r for r in model_results if r.error is None]

        if successful:
            avg_quality = sum(r.quality_score for r in successful) / len(successful)
            total_cost_eur = sum(r.cost_eur for r in successful)
            avg_duration = sum(r.duration_seconds for r in successful) / len(successful)

            print(f"\n{model.upper()}:")
            print(f"  Successful: {len(successful)}/{len(model_results)}")
            print(f"  Avg Quality Score: {avg_quality:.1f}/100")
            print(f"  Total Cost: €{total_cost_eur:.2f}")
            print(f"  Avg Duration: {avg_duration:.1f}s")
            print(f"  Pass Rate (≥70): {sum(1 for r in successful if r.quality_score >= 70)}/{len(successful)}")

    print("\n✅ POC Generation Complete!")
    print(f"📁 Results saved to: {config.output_dir}")


if __name__ == "__main__":
    main()
