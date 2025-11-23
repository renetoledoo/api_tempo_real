from pydantic import BaseModel
from typing import Optional

class WeatherResponse(BaseModel):
    cidade: str
    temperatura: float
    sensacao_termica: float
    temperatura_min: float
    temperatura_max: float
    pressao: int
    umidade: int
    descricao: str
    velocidade_vento: float
    pais: str

class ErrorResponse(BaseModel):
    erro: str
    mensagem: str

class HealthCheck(BaseModel):
    status: str
    versao: str