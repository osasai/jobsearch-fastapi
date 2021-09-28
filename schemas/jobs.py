from typing import Optional
from pydantic import BaseModel
from datetime import date, datetime


class JobBase(BaseModel):
    title: Optional[str] = None
    company: Optional[str] = None
    company_url: Optional[str] = None
    location: Optional[str] = "Remote"
    description: Optional[str] = None
    date_posted: Optional[date] = datetime.now().date()
    job_category: Optional[str] = None
    industry: Optional[str] = None
    company_information: Optional[str] = None
    must_requirement: Optional[str] = None
    want_requirement:Optional[str] = None
    salary_max: Optional[int] = None
    salary_min: Optional[int] = None


class JobCreate(JobBase):
    title: str
    company: str
    location: str
    description: str


class ShowJob(JobBase):
    title: str
    company: str
    company_url: Optional[str]
    location: str
    date_posted: date
    description: Optional[str]
    job_category: str
    industry: str
    company_information: str
    must_requirement: str
    want_requirement: str
    salary_max: int
    salary_min: int

    class Config():
        orm_mode = True


