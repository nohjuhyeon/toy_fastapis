from typing import Optional, List

from beanie import Document, Link
from pydantic import BaseModel, EmailStr

class question(Document):
    question: Optional[str] = None
    options: Optional[list] = None
    answer: Optional[str] = None
    score: Optional[str] = None
  
    class Qustion_Settings:
        name = "toyteam_question"


class answer(Document):
    name:Optional[str] = None
    qustion1:Optional[str] = None
    qustion2:Optional[str] = None
    qustion3:Optional[str] = None
    qustion4:Optional[str] = None
    qustion5:Optional[str] = None

    class answer_Settings:
        name = 'toyteam_answer'