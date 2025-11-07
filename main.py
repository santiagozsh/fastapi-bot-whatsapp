import os;
import re;
import gspread;
from fastapi import FastAPI, Request, HTTPException, Response;
from dotenv import load_dotenv;

app = FastAPI();

print("Loading .env vars");
load_dotenv();

whatsapp_token = os.getenv("WHATSAPP_VERIFY_TOKEN");
google_sheet_name = os.getenv("GOOGLE_SHEET_NAME");
trigger_word = os.getenv("TRIGGER_WORD", "!pedido");

# print(f"wt: { whatsapp_token }, gsn: { google_sheet_name }, tw: { trigger_word }")

print(f"{ google_sheet_name }");

# google sheets connection
try:
    # auth with google using service_account.json file
    key_auth = gspread.service_account(filename="service_account.json");
    # open the spreadsheet with the specific name 
    spreadsheet = key_auth.open(google_sheet_name);

    sales = spreadsheet.worksheet("Ventas");
    # transaction = spreadsheet.worksheet("Ingresos transacciones");
    print(f"INFO: google sheet connection: {google_sheet_name} success!");

except Exception as error:
    print("ERROR: Google connection is not working. Check service_account.json or permissions!");
    print(f"Trace Exception: { error }");


@app.get("/")
async def root():
    return {"hola": "mundo"}

@app.get("/append-data")
def test ():
    try:
        data_row = ["LG-03", "1-Sep-2025", "Wilmer alexander ayas", "312 547 8594", "Mosquera", "CUNDINAMARCA", "1 kairo", 3];
        sales.append_row(data_row, value_input_option="RAW");
        print(f"INFO: datos agregados { data_row }");
        return {"status": "prueba existosa!"};

    except Exception as error:
        print(f"ERROR:    Error al escribir en Google Sheets: { error }")
        raise HTTPException(status_code=500, detail=f"Error al escribir en Sheets: { error }")
