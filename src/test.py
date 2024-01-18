from config import config
from models import db_table
from utilities import db_functions
from sqlalchemy import create_engine
from pprint import pprint
import json
import os 
file_path = os.getcwd() + "/src/cluster_output.json"


file_path = "src/cluster_output.json"

engine = create_engine(config.DATABASE_URI)

# def read_json_file(file_path):
#     """
#     """
#     import json
#     with open(file_path, "r") as f:
#         data = json.load(f)
#     return data

if __name__ == "__main__":
    db_functions.create_table(db_table.Base)
    print("Table created")
    s = db_functions.create_session()
    print("Session created")
    k = s.query(db_table.Cutover).all()
    q = db_functions.sqlalchemy_obj_to_dict(k)
    pprint(q)
    # check the out of the above query and insert the data read from the json file only if the source volume is not present in the database table
    # if the source volume is present in the database table then update the record with the latest data from the json file
    # if the source volume is not present in the database table then insert the record in the database table
    print("Inserting data in to the database table")
    data = read_json_file(file_path)
    for i in data:
        print(i)
        s.add(db_table.Cutover(**i))
        s.commit()
    print("Data inserted in to the database table")

    print("Reading data from the database table")
    k = s.query(db_table.Cutover).all()
    for i in k["source_volume"]:
        print(i)
    q = db_functions.sqlalchemy_obj_to_dict(k)
    pprint(q)
    print("Data read from the database table")
    s.close()
