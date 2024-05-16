from pydantic_settings import BaseSettings
from pathlib import Path

Base_Dir = Path(__file__).parent.parent
class Settings(BaseSettings):
    URL_DB: str = f"sqlite+aiosqlite:///{Base_Dir}/db.sqlite3"
    echo_db: bool = True


settings = Settings()
