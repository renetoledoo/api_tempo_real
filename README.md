# API de Previsão do Tempo

![Python](https://img.shields.io/badge/python-3.11+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.109.0-green.svg)
![Tests](https://github.com/SEU_USUARIO/weather-api-cicd/workflows/CI/CD%20Pipeline/badge.svg)
![Coverage](https://img.shields.io/badge/coverage-83%25-brightgreen.svg)

API REST simples para consultar previsão do tempo usando OpenWeatherMap.

## 🚀 Como usar

### Instalar dependências
```bash
pip install -r requirements.txt
pip install -e .
```

### Configurar API Key

Crie um arquivo `.env`:
```
OPENWEATHER_API_KEY=sua_chave_aqui
```

### Rodar
```bash
python -m app.main
```

Acesse: http://localhost:8000/docs

## 📡 Endpoints

- `GET /` - Status da API
- `GET /clima/{cidade}` - Clima de uma cidade
- `GET /cidades/populares` - Lista de cidades

## 🧪 Testes
```bash
pytest tests/ -v
```

## 🛠️ Tecnologias

- FastAPI
- Pytest
- GitHub Actions
- OpenWeatherMap API

## 📝 Autor

Projeto para disciplina de Qualidade de Software - UNIRIOS
