from pydantic_settings import BaseSettings
from pathlib import Path

Base_Dir = Path(__file__).parent.parent
class Settings(BaseSettings):
    prefix_api_v1: str = "/api/v1"
    URL_DB: str = f"sqlite+aiosqlite:///{Base_Dir}/db.sqlite3"
    echo_db: bool = False


settings = Settings()
