from typing import List
from beanie import PydanticObjectId
from database.connections import Database
from fastapi import APIRouter, Depends, HTTPException, status
from models.users import User

router = APIRouter(
    tags=["Users"]
)

users_collection = Database(User)


# 회원 가입
# REF : http://127.0.0.1:8000/users_api/
@router.post("/")
async def create_event(body: User) -> dict:
    document = await users_collection.save(body)
    return {
        "message": "회원가입이 완료되었습니다."
        ,"datas": document
    }


# 로그인
# REF: http://127.0.0.1:8000/users_api/65ae1bca73c5bb45ed4b7785/password456
@router.get("/{id}/{pswd}", response_model=User)
async def retrieve_event(id: PydanticObjectId, pswd) -> User:                    # retrieve : 검색 
    user = await users_collection.get(id)
    if not user:
        raise HTTPException(                                                # raise : exception
            status_code=status.HTTP_404_NOT_FOUND,
            detail="존재하지 않는 ID 입니다!"
        )
    if pswd != user.pswd:
        raise HTTPException(                                                # raise : exception
            status_code=status.HTTP_404_NOT_FOUND,
            detail="비밀번호가 다릅니다!"
        )        
    return user


# 회원 탈퇴
# REF: http://127.0.0.1:8000/users_api/65ae1282cb16067edfc6025e
@router.delete("/{id}")
async def delete_event(id: PydanticObjectId) -> dict:
    user = await users_collection.get(id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="입력한 ID가 존재하지 않습니다."
        )
    user = await users_collection.delete(id)

    return {
        "message": "회원탈퇴가 완료되었습니다!"
        ,"datas": user
    }

# 회원 수정
# REF http://127.0.0.1:8000/users_api/65ae16b191ca1740caee2a70
from fastapi import Request
@router.put("/{id}", response_model=User)
async def update_event_withjson(id: PydanticObjectId, request:Request) -> User:
    user = await users_collection.get(id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="입력하신 ID가 없습니다."
        )
    body = await request.json()
    updated_user = await users_collection.update_withjson(id, body)
    if not updated_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="입력하신 ID와 관련된 정보가 없습니다."
        )
    return updated_user
