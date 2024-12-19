from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field, AnyUrl, HttpUrl


class Settings(BaseSettings):
    api_key: str = Field(alias="GROQ_API_KEY")
    proxy: AnyUrl

    qdrant_host: HttpUrl
    collection_name: str = Field()

    fastapi_host: HttpUrl

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()
