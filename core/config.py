from pathlib import Path
from pydantic import BaseModel
from pydantic_settings import BaseSettings


BASE_DIR = Path(__file__).parent.parent

DB_PATH = BASE_DIR / "db.sqlite3"


class DBSettings(BaseModel):
    """Settings class for SQLAchemy ORM

    Attributes:
        url (str): Database url.
            Default value is `sqlite+aiosqlite:///{DB_PATH}`
        echo (bool): Configure ORM echo option
            Default value is `False`
    """
    url: str = f"sqlite+aiosqlite:///{DB_PATH}"
    echo: bool = False


class Settings(BaseSettings):
    api_v1_prefix: str = "/api/v1"
    db: DBSettings = DBSettings()


settings = Settings()