from db.engine import engine
from sqlalchemy.orm import sessionmaker 

Session = sessionmaker(engine=engine)
