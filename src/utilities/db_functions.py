
from config import config 
from sqlalchemy import create_engine  

from sqlalchemy.orm import sessionmaker

engine = create_engine(config.DATABASE_URI)

def create_table(base):
    """
    """
    try:
        base.metadata.create_all(engine)
        return True
    except Exception as error:
        print(error)
        return False

def create_session():
    Session = sessionmaker(bind=engine)
    session = Session()
    return session

   
def row2dict(row):
    d={}
    if hasattr(row,"__table__"):
        for col in row.__table__.columns:
            d[col.name]=str(getattr(row,col.name))
        return d
    else:
        for col in row:
            d[col]=str(row[col])
        return d


def sqlalchemy_obj_to_dict(records):
    """
    function to convert sqlalcmey records in to dictionaries
    
    """
   
    if isinstance(records, list):
        output=[]
        for i, record in enumerate(records):
            output.append(row2dict(record))
        return output
    else:
        return row2dict(records)
        