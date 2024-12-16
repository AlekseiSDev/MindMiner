from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field, HttpUrl


class Settings(BaseSettings):
    api_key: str = Field(alias="GROQ_API_KEY")
    proxy: str = HttpUrl

    qdrant_host: str = HttpUrl
    collection_name: str = Field()

    fastapi_host: str = HttpUrl

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()
