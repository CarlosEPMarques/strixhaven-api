from pydantic_settings import BaseSettings, SettingsConfigDict

class JWTSettings(BaseSettings):
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    SESSION_TTL: int = 7200
    SESSION_MAX: int = 1000
    
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8', extra='allow', env_prefix='JWT_')

jwt_settings = JWTSettings()
