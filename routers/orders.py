from inspect import indentsize
from fastapi import APIRouter, HTTPException, Request, Response
from starlette import responses
from core.config import env_settings
import services.google_sheets as sheets
import json
import services.whatsapp_clean_json as cleanjson

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

@router.get("/webhook")
async def verification_whatsapp(request: Request):

    # Datos enviados por meta desde la URL
    verify_token= request.query_params.get("hub.verify_token")
    challenge = request.query_params.get("hub.challenge")
    
    if verify_token == env_settings.WHATSAPP_VERIFY_TOKEN:
        print("INFO: Webhook verificado!")
        return Response(content=challenge)
    return { Response( status_code=200 )}

@router.post("/webhook")
async def seeing_data(request:Request):
    data_body = await request.json()

    # print(json.dumps(data_body, indent=2))

    data = cleanjson.extract_message_data(data_body)

    if data:
        print("DATOS:")
        print(f"Numero de telefono: {data['phone']}")
        print(f"Tipo: {data['type']}")
        print(f"Texto: {data['text']}")
        print(f"image+id: {data['image_id']}")
    else: 
        print("Evento ignorado")
    return { Response( status_code=200 )}
