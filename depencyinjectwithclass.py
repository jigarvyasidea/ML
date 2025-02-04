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

@app.post("items")
def index():
    return "hello word"

# Dependency injection :- deepdency is like when one function depenced on ohter function is dependecy

# jab depcy hum code me inject ya add karte h to vo depncy enjection hoga h let do in code

# async def common_param(q:Optional[str]=None, skip:int=0 , limit:int=10):
#     return {"q":q, "skip":skip, "limit":limit}
# humne ue depcy function create kar diya jo logi hum use karna chiate hai

##let create ohter function
@app.get("/manektech")
async def read_item(common: common_param = Depends(common_param)):
   res={ }
   return common.q + common.skip + common+limit

@app.get("/course")
async def course_item(common: common_param = Depends(common_param)):
    res = {}
    return common.q + common.skip + common + limit




# we can also create class of it
from typing import Optional


class CommonParam:
    """
    A class to represent common query parameters used in API endpoints.

    Attributes:
        q (Optional[str]): A search query string (default is None).
        skip (int): Number of records to skip for pagination (default is 0).
        limit (int): Maximum number of records to return (default is 10).
    """

    def __init__(self, q: Optional[str] = None, skip: int = 0, limit: int = 10):
        self.q = q
        self.skip = skip
        self.limit = limit
