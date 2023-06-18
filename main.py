from fastapi import FastAPI, Query
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


@app.get("/prueba")
async def all_categories():
    return _services.get_products()


@app.get("/buscar/{palabra_clave}")
def buscar(palabra_clave: str, supermercado: str = Query(None), categoria: str = Query(None), subcategoria: str = Query(None)):
    productos_encontrados = _services.buscar_productos(
        palabra_clave, supermercado, categoria, subcategoria)
    return {"productos_encontrados": productos_encontrados}
