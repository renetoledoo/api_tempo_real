import httpx
import os
from typing import Dict, Any
from dotenv import load_dotenv


load_dotenv()

class WeatherService:
    def __init__(self):
        self.api_key = os.getenv("OPENWEATHER_API_KEY")
        self.base_url = "https://api.openweathermap.org/data/2.5/weather"
    
    async def get_weather(self, cidade: str, pais: str = "BR") -> Dict[str, Any]:
        print(f'API Key: {self.api_key}')
        async with httpx.AsyncClient() as client:
            params = {
                "q": f"{cidade},{pais}",
                "appid": self.api_key,
                "units": "metric",
                "lang": "pt_br"
            }

            response = await client.get(self.base_url, params=params)

            if response.status_code == 404:
                raise ValueError("Cidade não encontrada")
            elif response.status_code == 401:
                raise ValueError("API Key inválida ou não ativada")
            elif response.status_code != 200:
                raise ValueError(f"Erro na API: {response.status_code} - {response.text}")

            return response.json()
    
    def format_weather_data(self, data: Dict[str, Any]) -> Dict[str, Any]:
        return {
            "cidade": data["name"],
            "temperatura": round(data["main"]["temp"], 1),
            "sensacao_termica": round(data["main"]["feels_like"], 1),
            "temperatura_min": round(data["main"]["temp_min"], 1),
            "temperatura_max": round(data["main"]["temp_max"], 1),
            "pressao": data["main"]["pressure"],
            "umidade": data["main"]["humidity"],
            "descricao": data["weather"][0]["description"],
            "velocidade_vento": round(data["wind"]["speed"], 1),
            "pais": data["sys"]["country"]
        }
