import pytest
from fastapi.testclient import TestClient
from app.main import app
import os
import sys

client = TestClient(app)
sys.path.append(os.path.dirname(os.path.dirname(__file__)))


class TestClimaEndpoints:
    
    def test_clima_cidade_valida(self):
        response = client.get("/clima/Recife?pais=BR")
        assert response.status_code == 200
        data = response.json()
        
        assert "cidade" in data
        assert "temperatura" in data
        assert "umidade" in data
        assert "descricao" in data
        assert "pais" in data
        
        assert isinstance(data["temperatura"], (int, float))
        assert isinstance(data["umidade"], int)
        assert isinstance(data["cidade"], str)
    
    def test_clima_cidade_invalida(self):
        response = client.get("/clima/CidadeInexistente123?pais=BR")
        assert response.status_code == 404
    
    def test_clima_query_params(self):
        response = client.get("/clima?cidade=Paulo Afonso&pais=BR")
        assert response.status_code == 200
        data = response.json()
        assert "cidade" in data
        assert "temperatura" in data
    
    def test_clima_cidade_sem_pais(self):
        response = client.get("/clima/Recife")
        assert response.status_code == 200
        data = response.json()
        assert data["pais"] == "BR"

class TestCidadesPopulares:
    
    def test_cidades_populares_retorna_lista(self):
        response = client.get("/cidades/populares")
        assert response.status_code == 200
        data = response.json()
        assert "cidades" in data
        assert isinstance(data["cidades"], list)
        assert len(data["cidades"]) > 0
    
    def test_cidades_populares_estrutura(self):
        response = client.get("/cidades/populares")
        data = response.json()
        
        for cidade in data["cidades"]:
            assert "nome" in cidade
            assert "estado" in cidade
            assert isinstance(cidade["nome"], str)
            assert isinstance(cidade["estado"], str)

class TestResponseModels:
    
    def test_weather_response_campos_obrigatorios(self):
        response = client.get("/clima/Recife")
        assert response.status_code == 200
        data = response.json()
        
        campos_obrigatorios = [
            "cidade", "temperatura", "sensacao_termica",
            "temperatura_min", "temperatura_max", "pressao",
            "umidade", "descricao", "velocidade_vento", "pais"
        ]
        
        for campo in campos_obrigatorios:
            assert campo in data, f"Campo {campo} ausente na resposta"
    
    def test_valores_temperatura_validos(self):
        response = client.get("/clima/Recife")
        assert response.status_code == 200
        data = response.json()
        
        assert -50 <= data["temperatura"] <= 60
        assert -50 <= data["temperatura_min"] <= 60
        assert -50 <= data["temperatura_max"] <= 60
    
    def test_umidade_valida(self):
        response = client.get("/clima/Recife")
        assert response.status_code == 200
        data = response.json()
        
        assert 0 <= data["umidade"] <= 100

class TestAPIDocumentation:
    
    def test_openapi_docs_acessivel(self):
        response = client.get("/docs")
        assert response.status_code == 200
    
    def test_openapi_json_acessivel(self):
        response = client.get("/openapi.json")
        assert response.status_code == 200
        data = response.json()
        assert "openapi" in data
        assert "info" in data
        assert "paths" in data

