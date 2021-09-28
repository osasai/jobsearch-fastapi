from sqlalchemy import Column, Integer, String, Boolean, Date , ForeignKey
from sqlalchemy.orm import relationship

from db.base_class import Base

class Job(Base):
    id = Column(Integer,primary_key=True,index=True, autoincrement=True)
    jobid = Column(String,nullable=False)
    title = Column(String,nullable=False)
    job_category = Column(String)
    industry = Column(String)
    company = Column(String,nullable=False)
    company_information = Column(String,nullable=False)
    company_url = Column(String)
    location = Column(String,nullable=False)
    description = Column(String)
    must_requirement = Column(String)
    want_requirement = Column(String)
    salary_max = Column(Integer)
    salary_min = Column(Integer)
    date_posted = Column(Date)
    is_active = Column(Boolean(),default = True)
    owner_id = Column(Integer,ForeignKey('user.id'))
    owner = relationship("User",back_populates="jobs")