from sqlalchemy import Column, String, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Cutover(Base):
    __tablename__ = "netapp_migration_table"
    source_cluster=Column(String, nullable=False)
    destination_cluster=Column(String, nullable=False)
    source_path=Column(String, nullable=False)
    source_vserver=Column(String, nullable=False)
    source_volume=Column(String,primary_key=True)
    destination_path=Column(String, nullable=False)
    destination_vserver=Column(String, nullable=False)
    destination_volume=Column(String, nullable=False)
    type=Column(String, nullable=False)
    state=Column(String)
    status=Column(String)
    healthy=Column(Boolean)
    relationship_id=Column(String)
    lag_time=Column(String)
    migration_status=Column(String)

    def __repr__(self):
        return f"{self.__dict__}"   


