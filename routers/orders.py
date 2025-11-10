from fastapi import APIRouter, HTTPException, Request, Response
from core.config import env_settings
import services.google_sheets as sheets

router = APIRouter()


@router.get("/")
def root():
    return { "Status": "Servidor FastAPI funcionando. Ve a /api/v1/docs para ver la API." }

@router.get("/test-sheets")
def test ():
    try:
        data_row = ["LG-04", "1-Sep-2025", "Wilmer alexander ayas", "312 547 8594", "Mosquera", "CUNDINAMARCA", "1 kairo", 3];
        sheets.sales.append_row(data_row);
        print(f"INFO: datos agregados { data_row }");
        return {"status": "prueba existosa!"};

    except Exception as error:
        print(f"ERROR:    Error al escribir en Google Sheets: { error }")
        raise HTTPException(status_code=500, detail=f"Error al escribir en Sheets: { error }")
