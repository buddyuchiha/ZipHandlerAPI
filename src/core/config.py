from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=(".env"),
        case_sensitive=False
    )
    
    APP_POSTGRES_DB: str
    APP_POSTGRES_USER: str
    APP_POSTGRES_PASSWORD: str
    APP_POSTGRES_URL: str
    APP_POSTGRES_PORT: int
    
    KC_POSTGRES_DB: str
    KC_POSTGRES_USER: str
    KC_POSTGRES_PASSWORD: str
    KC_POSTGRES_URL: str
    KC_POSTGRES_PORT: int
    KC_ADMIN: str 
    KC_ADMIN_PASSWORD: str 
    KC_HOSTNAME: str 
    KC_PORT: int
    KC_CLIENT_ID:str
    KC_CLIENT_SECRET: str
    KC_USER: str
    KC_USER_PASS: str
    KC_REALM: str
    
    MINIO_URL: str
    MINIO_ACCESS_KEY: str
    MINIO_SECRET_KEY: str
    MINIO_PORT: int
    MINIO_API_PORT: int
    
    APP_HOST: str 
    APP_PORT: int
    
    LOGGING_FILE: str
        
    
settings = Settings()