from fastapi import APIRouter
from starlette.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request
from database.connections import Database
from models.toyteam import question,answer

router = APIRouter()

templates = Jinja2Templates(directory="templates/")

# 응시한 애들 값
@router.get("/data_list", response_class=HTMLResponse) # 펑션 호출 방식
async def forms(request:Request):
    return templates.TemplateResponse(name="toyteam/data_list.html", context={'request':request})

@router.post("/data_list", response_class=HTMLResponse) # 펑션 호출 방식
async def forms(request:Request):
    return templates.TemplateResponse(name="toyteam/data_list.html", context={'request':request})


# 문제 페이지
@router.get("/exam_test", response_class=HTMLResponse) # 펑션 호출 방식
async def forms(request:Request):
    return templates.TemplateResponse(name="toyteam/exam_test.html", context={'request':request})

@router.post("/exam_test", response_class=HTMLResponse) # 펑션 호출 방식
async def forms(request:Request):
    return templates.TemplateResponse(name="toyteam/exam_test.html", context={'request':request})
