from fastapi import FastAPI

from core.config import get_settings

def create_app() -> FastAPI:
    
    settings = get_settings()
    
    docs_url = None
    redoc_url = None
    if settings.ENVIRONMENT != "prod":
        docs_url = "/docs"
        redoc_url = "/redoc"
    
    app = FastAPI(
        title="Hello World",
        docs_url=docs_url,
        redoc_url=redoc_url,
    )
    
    @app.get("/")
    def root():
        return {
            "Title": "Hello World",
        }
    
    return app


app = create_app()