import os
import re
import gspread
# import uvicorn
from fastapi import FastAPI, Request, HTTPException, Response
from dotenv import load_dotenv

app = FastAPI()


@app.get("/")
async def root():
    return {"hola": "mundo"}

