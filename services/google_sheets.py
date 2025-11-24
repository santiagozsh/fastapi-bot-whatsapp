import gspread
import re
from core.config import env_settings

# google sheets connection
try:
    # auth with google using service_account.json file
    key_auth = gspread.service_account(filename="service_account.json");
    # open the spreadsheet with the specific name 
    spreadsheet = key_auth.open(env_settings.GOOGLE_SHEET_NAME);

    sales = spreadsheet.worksheet("Ventas");
    # transaction = spreadsheet.worksheet("Ingresos transacciones");
    print(f"INFO: google sheet connection: {env_settings.GOOGLE_SHEET_NAME} success!");

except Exception as error:
    print("ERROR: Google connection is not working. Check service_account.json or permissions!");
    print(f"Trace Exception: { error }");
