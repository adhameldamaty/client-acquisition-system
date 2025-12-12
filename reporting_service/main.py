
from fastapi import FastAPI
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import random
import time

app = FastAPI()

DATABASE_URL = "postgresql://user:password@db:5432/report_db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class Report(Base):
    __tablename__ = "reports"
    id = Column(Integer, primary_key=True, index=True)
    status = Column(String, index=True)
    value = Column(Integer)

def create_tables():
    try:
        Base.metadata.create_all(bind=engine)
    except:
        pass

create_tables()

@app.get("/")
def read_root():
    return {"Service": "Reporting Service", "Status": "Active", "DB": "Connected"}

@app.get("/stats")
def get_stats():
    db = SessionLocal()
    
   
    new_report = Report(status="Processed", value=random.randint(1, 100))
    db.add(new_report)
    db.commit()
    
   
    db.refresh(new_report)
    
    
    report_value = new_report.value
    count = db.query(Report).count()
    
    
    db.close()
    
    return {
        "Action": "Report Saved to DB",
        "Total_Reports_In_DB": count,
        "New_Value": report_value 
    }
