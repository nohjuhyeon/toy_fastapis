from typing import Any, List, Optional
from beanie import init_beanie, PydanticObjectId
from models.users import User
from models.events import Event
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseModel
# 변경 후 코드
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # DATABASE_URL: Optional[str] = None
    DATABASE_URL : Optional[str] = None
      # async-await == 네크워크의 속도와 맞추기 위해 넣는 기능(방식은 비동기)
    async def initialize_database(self):
        client = AsyncIOMotorClient(self.DATABASE_URL)
        await init_beanie(database=client.get_default_database(),
                          document_models=[User,Event])
    class Config:
        env_file = ".env"


import json

class Database:
    # model 즉 collection
    def __init__(self, model) -> None:
        self.model = model
        pass
        # 전체 리스트
    async def get_all(self):
        documents = await self.model.find_all().to_list()
        pass
        return documents
    
    # 상세 보기
    async def get(self, id:PydanticObjectId) -> Any:
        doc = await self.model.get(id)
        if doc:
            return doc
        return False
    
    # 저장
    async def save(self, document) -> None:
        doc = await document.create()
        return doc
    
    async def delete(self, id: PydanticObjectId):
        doc = await self.get(id)
        if not doc:
            return False
        await doc.delete()
        return True
    
    # update with params json
    async def update_withjson(self, id: PydanticObjectId, body: json):
        doc_id = id

        # des_body = {k: v for k, v in des_body.items() if v is not None}
        update_query = {"$set": {**body}}

        doc = await self.get(doc_id)
        if not doc:
            return False
        await doc.update(update_query)
        return doc