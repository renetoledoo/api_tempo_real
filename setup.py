from setuptools import setup, find_packages

setup(
    name="weather-api",
    version="2.0.0",
    description="API de Previsão do Tempo com CI/CD",
    author="Seu Nome",
    packages=find_packages(),
    install_requires=[
        "fastapi>=0.109.0",
        "uvicorn[standard]>=0.27.0",
        "httpx>=0.26.0",
        "pydantic>=2.5.3",
        "python-dotenv>=1.0.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.4.4",
            "pytest-asyncio>=0.23.3",
            "pytest-cov>=4.1.0",
            "flake8>=7.0.0",
        ]
    },
    python_requires=">=3.11",
)