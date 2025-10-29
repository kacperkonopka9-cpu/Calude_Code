"""Template download routes."""

from fastapi import APIRouter
from fastapi.responses import StreamingResponse

from ..services.template_service import generate_excel_template

router = APIRouter()


@router.get("/excel")
async def download_excel_template() -> StreamingResponse:
    """
    Download Excel template for Ulga B+R project data.

    Returns:
        StreamingResponse: Excel file with Polish headers and validation rules.
    """
    try:
        buffer = generate_excel_template()

        return StreamingResponse(
            buffer,
            media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            headers={"Content-Disposition": 'attachment; filename="Szablon-Ulga-BR.xlsx"'},
        )
    except Exception as e:
        raise RuntimeError(f"Failed to generate template: {str(e)}") from e
