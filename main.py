from fastapi import FastAPI
import services as _services
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Add CORS middleware
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Welcome to the https://www.jumbo.cl/carniceria/vacuno products Scraper [FastAPI]"}


@app.get("/products")
async def all_products():
    return _services.get_products()
