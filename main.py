from fastapi import FastAPI, Request, HTTPException, Response;
import uvicorn
from routers.orders import router as orders_router

app = FastAPI(
    title="bot_whatsapp_sheets",
    description="Recibe webhooks de whatsapp y los escribe en google sheets",
    version="1.0.0"
);

app.include_router(orders_router, prefix="/api/v1")

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

