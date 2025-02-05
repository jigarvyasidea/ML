from typing import Optional

from fastapi import FastAPI , Depends
from setuptools.command.setopt import option_base

app = FastAPI()
#
# @app.get("/")
# def main():
#     return {"message":"hello guys kaise ho"}


#path paramereter in flast api
# i hope aapko path parameter to pata hoga


# # flipkard.com/items/item_id
# @app.get("/items/{item_id}")
# def index(item_id:int):
#     return {"Product_id": item_id}


# query parameter

# @app.get("/items/")
# def index(q:int=0):
#     return {"product_id"q}


# req.body

# @app.post("items")
# def index():
#     return "hello word"

# Dependency injection :- deepdency is like when one function depenced on ohter function is dependecy

# jab depcy hum code me inject ya add karte h to vo depncy enjection hoga h let do in code

# async def common_param(q:Optional[str]=None, skip:int=0 , limit:int=10):
#     return {"q":q, "skip":skip, "limit":limit}
# humne ue depcy function create kar diya jo logi hum use karna chiate hai

# ##let create ohter function
# @app.get("/manektech")
# async def read_item(common: common_param = Depends(common_param)):
#    res={ }
#    return common.q + common.skip + common+limit
#
# @app.get("/course")
# async def course_item(common: common_param = Depends(common_param)):
#     res = {}
#     return common.q + common.skip + common + limit




# we can also create class of it
from typing import Optional


# class CommonParam:
#     """
#     A class to represent common query parameters used in API endpoints.
#
#     Attributes:
#         q (Optional[str]): A search query string (default is None).
#         skip (int): Number of records to skip for pagination (default is 0).
#         limit (int): Maximum number of records to return (default is 10).
#     """
#
#     def __init__(self, q: Optional[str] = None, skip: int = 0, limit: int = 10):
#         self.q = q
#         self.skip = skip
#         self.limit = limit

# hum sqlachmy database se connect karege FASTAPI ko

# abvisly we work with data or anything we need some module
# simillarly we work with alalcmy so we need some modile so connect with fastapi

from sqlalchemy import create_engine, column, Integer
# ye db se conect karne ke liye ya db engine create karta h

from sqlalchemy.ext.declarative import declarative_base
#ye declarative base model banae ue liye use hoga h and tavle ko represent karne me

from sqlalchemy.orm import sessionmaker
#ye dm se session ko manager karne me use hota h and hue request per new session create karna h


# ab humne requerd module import kar liye

# ab db se connect karna padega for that ue have

DATABASE_URL = "sqlite:///./test.db"

# there is above url we have different thig to interes with database sqlit is also help us to interact with dv and /// is pater and ./ is  currect directory text.db is the name of dbv

#ab humko create karna padega abhi tak to import kare h kuch module and Basebase URL but engine vo sab bhi create karne padege


create_engine(
DATABASE_URL,
    # humne uaha per sqlite ka use kara h --> sqlite support only singlte threted humko fast karna chita h humara kaam so hum kya chaite h mulipe thereed milte so humara kaam parelle execute ho.
connect_args={"check_same_thread":False}
)
#humne kya kar diya current thred ko flase so jo single thre per chal rahi due to sqlit us single thred ko false kiya h so ye ab multiple thred per chalegi


# step - 4 db ke sath kaam karte h to session bohot importatn hota h so i want to create s

SessionLocal =sessionmaker(
    autocommit = False, # humne automtic commit ko flase kar  diya ee bhai tu automatic commit mat karna me manually karunga commit tu mat karna please

    autoflush=False, # ssame flush me karuga manuall to automatic mat karna session baba # becourse ye har request ko creata kar rha h

    bind = engine, #bine+engine ye database se connect karnta h kisko connnect karna h enggine ko becourse we working is session makter
)

# step 5 :- creating base class ab hum base class ko create karege

Base = declarative_base()

# base class is used jo bhi model hum create karege si vi sab nidek base class ko inherte karege so sqlalchmy ko pta karlege ko db table ko represt kar rahe h

## Till now we create SQLite databae ko


# this bhaiya aap uper mdoel ki baar kar rahe te model ko create kar dete h

# we create model jha per hum model ko detials shore karege


# for creating model in create a clalss

# class User(Base):
#     __tablename__ = "users"
#     # ye bta rha h databaseme table ka name user hoga
#
#     # table ka name de diya ab us table me columne create karne honge
#     # so lets focus on columnet 1
#         id=column(Integer, Primary_key=True , index=True)
#         name = column(string, unique=True, index=True )


class User(Base):
    __tablename__ = "users"
    # Ye bata raha hai ki database mein table ka naam "users" hoga

    # Table ka naam de diya, ab us table mein columns create karenge
    id = column(Integer, Primary_key=True, index=True)
    name = column(string, unique=True, index=True)
    email = column(string, unique=True , index=True)

# now we create baseTable
Base.metadata.create_all(bind=engine)

# issme humara DB ready ho jayga.

