from pydantic_settings import BaseSettings

class EnviormentSettings(BaseSettings):
    WHATSAPP_VERIFY_TOKEN: str
    GOOGLE_SHEET_NAME: str
    TRIGGER_WORD: str = "!pedido"
    WHATSAPP_API_TOKEN: str
    WHATSAPP_PHONE_NUMBER_ID: str
    WHATSAPP_BUSINESS_ACCOUNT_ID: str 

    class Config:
        env_file = ".env"

env_settings = EnviormentSettings() # type: ignore 

print(f"INFO: config load is: { env_settings.WHATSAPP_VERIFY_TOKEN } { env_settings.GOOGLE_SHEET_NAME } { env_settings.WHATSAPP_API_TOKEN }")

