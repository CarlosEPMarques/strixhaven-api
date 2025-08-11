from urllib import parse
from pydantic_settings import BaseSettings, SettingsConfigDict
from sqlalchemy.engine import URL
from src.settings.globals import EnvironmentEnum, global_settings


class DatabaseSettings(BaseSettings):
    DB_USERNAME: str | None = None
    DB_PASSWORD: str | None = None
    DB_HOST: str | None = None
    DB_PORT: int | None = None
    DB_DATABASE: str | None = None
    POSTGRESQL_DRIVERNAME: str = 'postgresql+asyncpg'
    
    @property
    def postgresql_url(self) -> str:
        if global_settings.ENVIRONMENT == EnvironmentEnum.TESTING:
            return f'{self.POSTGRESQL_DRIVERNAME}://postgres:postgres@localhost:5434/postgres'
        
        url = URL.create(
            drivername=self.POSTGRESQL_DRIVERNAME,
            username=self.DB_USERNAME,
            password=self.DB_PASSWORD,
            host=self.DB_HOST,
            port=self.DB_PORT,
            database=self.DB_DATABASE
        ).render_as_string(hide_password=False)
        return parse.unquote(url)
    
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8', extra='allow')
    
database_settings = DatabaseSettings()