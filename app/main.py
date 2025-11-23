from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from app.models import WeatherResponse
from app.services import WeatherService


app = FastAPI(
    title="API de Previsão do Tempo",
    description="API REST para consulta de previsão do tempo usando OpenWeatherMap",
    version="1.0.0"
)

# Configuração CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Instância do serviço
weather_service = WeatherService()

@app.get("/", tags=["Health Check"])
async def root():

    return {
        "mensagem": "API de Previsão do Tempo",
        "versao": "1.0.0",
        "status": "online"
    }

@app.get("/clima/{cidade}", response_model=WeatherResponse, tags=["Clima"])
async def obter_clima(
    cidade: str,
    pais: str = Query(default="BR", description="Código do país (ISO 3166)")
):

    try:
        data = await weather_service.get_weather(cidade, pais)
        weather_data = weather_service.format_weather_data(data)
        return weather_data
        
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Erro interno do servidor")

@app.get("/clima", response_model=WeatherResponse, tags=["Clima"])
async def obter_clima_query(
    cidade: str = Query(..., description="Nome da cidade"),
    pais: str = Query(default="BR", description="Código do país (ISO 3166)")
):

    return await obter_clima(cidade, pais)

@app.get("/cidades/populares", tags=["Cidades"])
async def cidades_populares():

    return {
        "cidades": [
            {"nome": "Paulo Afonso", "estado": "BA"},
            {"nome": "Recife", "estado": "PE"},
            {"nome": "São Paulo", "estado": "SP"},
            {"nome": "Rio de Janeiro", "estado": "RJ"},
            {"nome": "Brasília", "estado": "DF"},
            {"nome": "Salvador", "estado": "BA"},
            {"nome": "Fortaleza", "estado": "CE"},
            {"nome": "Belo Horizonte", "estado": "MG"},
            {"nome": "Manaus", "estado": "AM"},
            {"nome": "Curitiba", "estado": "PR"},
            {"nome": "Porto Alegre", "estado": "RS"}
        ]
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )