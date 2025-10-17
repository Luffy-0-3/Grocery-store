from fastapi import FastAPI
from db import engine
import models
from routers import products
from fastapi.middleware.cors import  CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)

app.include_router(products.router)

# models.Base.metadata.create_all(bind=engine)



@app.get("/")
def intro():
    return "Welcome to the Grocery Store"
