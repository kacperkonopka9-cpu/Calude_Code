# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This repository uses the **BMad Method** (Breakthrough Method for Agile AI-Driven Development), a comprehensive AI agent framework for structured agile development. BMad provides specialized AI agents and workflows for planning, development, testing, and documentation.

## BMad Method Architecture

### Core Components

- **`.bmad-core/`**: Framework core containing agents, tasks, workflows, and templates
- **`.claude/commands/BMad/`**: Claude Code slash commands for BMad agents and tasks
  - `agents/`: Role-based agent commands (analyst, architect, dev, pm, po, qa, sm, ux-expert, etc.)
  - `tasks/`: Specific task commands (create-next-story, shard-doc, qa-gate, etc.)
- **`docs/`**: Project documentation (PRD, architecture, epics, stories, QA assessments)

### Agent Roles

1. **Analyst** (`/analyst`): Market research, competitor analysis, project briefs
2. **Product Manager** (`/pm`): Creates PRDs with functional requirements, NFRs, epics, and stories
3. **UX Expert** (`/ux-expert`): Front-end specifications and UI design prompts
4. **Architect** (`/architect`): System architecture, tech stack, coding standards
5. **Product Owner** (`/po`): Document validation, sharding, master checklists
6. **Scrum Master** (`/sm`): Story creation and sprint management
7. **Developer** (`/dev`): Story implementation following architecture and coding standards
8. **QA/Test Architect** (`/qa`): Risk assessment, test design, NFR validation, QA gates
9. **BMad Orchestrator** (`/bmad-orchestrator`): Workflow coordination
10. **BMad Master** (`/bmad-master`): High-level project guidance

### Configuration

BMad configuration is managed in `.bmad-core/core-config.yaml`:

```yaml
# Document locations
prd:
  prdFile: docs/prd.md
  prdShardedLocation: docs/prd
architecture:
  architectureFile: docs/architecture.md
  architectureShardedLocation: docs/architecture
devStoryLocation: docs/stories
qa:
  qaLocation: docs/qa

# Developer workflow
devLoadAlwaysFiles:
  - docs/architecture/coding-standards.md
  - docs/architecture/tech-stack.md
  - docs/architecture/source-tree.md
devDebugLog: .ai/debug-log.md
```

## Development Workflows

### Greenfield Projects (New Projects)

**Planning Phase** (typically in web UI with powerful models):
1. `/analyst` - Create project brief (optional: brainstorming, research)
2. `/pm` - Create PRD from brief with FRs, NFRs, epics, stories
3. `/ux-expert` - Create front-end spec (if UI-heavy)
4. `/architect` - Create architecture from PRD (and UX spec if applicable)
5. `/po` - Run master checklist to validate document alignment
6. `/po` + `/shard-doc` - Shard PRD and architecture into epics/stories

**Development Cycle** (in IDE):
1. **Story Creation**: `/sm` → `*draft` (creates next story in `docs/stories/`)
2. **Pre-Development QA** (recommended):
   - `/qa` + `*risk {story}` - Identify integration/regression risks
   - `/qa` + `*design {story}` - Create test strategy for developer
3. **Implementation**: `/dev` → `*develop-story {story}` - Execute story checklist
4. **Mid-Development QA** (optional):
   - `/qa` + `*trace {story}` - Verify test coverage
   - `/qa` + `*nfr {story}` - Validate quality attributes
5. **Post-Development QA** (required): `/qa` + `*review {story}` - Comprehensive assessment
6. **QA Gate Decision**: `/qa` + `*gate {story}` - Update quality decision

### Brownfield Projects (Existing Codebases)

For existing projects, see `.bmad-core/working-in-the-brownfield.md` for specialized workflows including:
- Brownfield story creation (`/brownfield-create-story`)
- Epic creation from existing code (`/brownfield-create-epic`)
- Legacy code integration strategies

Available workflows in `.bmad-core/workflows/`:
- `brownfield-fullstack.yaml`
- `brownfield-service.yaml`
- `brownfield-ui.yaml`
- `greenfield-fullstack.yaml`
- `greenfield-service.yaml`
- `greenfield-ui.yaml`

## Common Commands

### Agent Commands
```bash
# Load agents (use @ prefix in Claude Code)
@analyst          # Market research and project briefs
@pm              # Product management and PRD creation
@architect       # System architecture
@po              # Product owner tasks and validation
@sm              # Scrum master and story management
@dev             # Developer implementation
@qa              # Quality assurance and testing
@ux-expert       # UX/UI design
```

### Task Commands
```bash
# Story and epic management
*create-next-story              # Create next user story
*create-brownfield-story        # Create story for existing code
*brownfield-create-epic         # Create epic from existing code

# Documentation
*shard-doc                      # Shard PRD/architecture into epics/stories
*document-project               # Generate project documentation
*create-doc                     # Create specific documentation

# QA tasks
*risk-profile                   # Risk assessment for story (shorthand: *risk)
*test-design                    # Test strategy creation (shorthand: *design)
*trace-requirements             # Verify test coverage (shorthand: *trace)
*nfr-assess                     # NFR validation (shorthand: *nfr)
*review-story                   # Story review (shorthand: *review)
*qa-gate                        # QA gate decision (shorthand: *gate)
*apply-qa-fixes                 # Apply QA recommendations

# Planning and validation
*execute-checklist              # Run task checklists
*validate-next-story            # Validate story before approval
*correct-course                 # Project course correction
*advanced-elicitation           # Requirements elicitation
```

## Key Files to Reference

### Essential Documentation
- `.bmad-core/user-guide.md` - Complete BMad Method guide with workflows and diagrams
- `.bmad-core/enhanced-ide-development-workflow.md` - Step-by-step IDE workflow
- `.bmad-core/working-in-the-brownfield.md` - Brownfield project strategies
- `.bmad-core/core-config.yaml` - BMad configuration

### When Implementing Stories
Always load these files (auto-loaded by `/dev` agent):
- `docs/architecture/coding-standards.md` - Project coding standards
- `docs/architecture/tech-stack.md` - Technology stack specifications
- `docs/architecture/source-tree.md` - Project structure and organization

### Project Artifacts
- `docs/prd.md` - Product Requirements Document
- `docs/architecture.md` - System architecture document
- `docs/epics/` - Sharded epic documents
- `docs/stories/` - User story documents
- `docs/qa/assessments/` - QA risk and test assessments
- `docs/qa/gates/` - QA gate decisions

## BMad Best Practices

1. **Planning Phase**: Use powerful models (web UI) for PRD, architecture, and planning documents
2. **Document Sharding**: Always shard PRD and architecture before starting development
3. **Story Status**: Update story status from "Draft" to "Approved" before implementation
4. **QA Integration**: Run risk assessment and test design after story approval, before development
5. **Story Review**: Always run QA review after completing story implementation
6. **One Story at a Time**: Focus on completing one story fully before starting the next
7. **Debug Logging**: Track decisions and issues in `.ai/debug-log.md`

## Project Structure Conventions

```
/workspaces/Calude_Code/
├── .bmad-core/              # BMad framework (do not modify)
├── .claude/commands/BMad/   # Claude Code commands (do not modify)
├── docs/
│   ├── prd.md              # Product Requirements Document
│   ├── architecture.md     # System Architecture
│   ├── epics/              # Sharded epics
│   ├── stories/            # User stories
│   ├── architecture/       # Architecture details (coding standards, tech stack, etc.)
│   └── qa/
│       ├── assessments/    # QA risk and test assessments
│       └── gates/          # QA gate decisions
├── .ai/
│   └── debug-log.md        # Development decision log
└── [source code directories based on architecture]
```

## Integration with Claude Code

BMad is specifically configured for Claude Code. All agents are available as slash commands in the `.claude/commands/BMad/` directory. Use the `@` prefix to load agents and `*` prefix for task commands.

**Example Workflow in Claude Code:**
```
User: @sm *draft
Claude: [Creates next story in docs/stories/]

User: @qa *risk docs/stories/epic-1.story-2.md
Claude: [Generates risk assessment]

User: @dev *develop-story docs/stories/epic-1.story-2.md
Claude: [Implements story following architecture and standards]

User: @qa *review docs/stories/epic-1.story-2.md
Claude: [Conducts comprehensive QA review]
```

## Additional Resources

- User Guide: `.bmad-core/user-guide.md`
- IDE Workflow: `.bmad-core/enhanced-ide-development-workflow.md`
- Brownfield Guide: `.bmad-core/working-in-the-brownfield.md`
- BMad Website: https://bmadcodes.com/
