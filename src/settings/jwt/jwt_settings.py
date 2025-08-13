from pydantic import BaseSettings

class JWTSettings(BaseSettings):
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    SESSION_TTL: int = 7200
    SESSION_MAX: int = 1000
    
    class Config:
        env_prefix = "JWT_"
        env_file = ".env"

jwt_settings = JWTSettings()
