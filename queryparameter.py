
  @app.get("/")
  def main():
      return {"message":"hello guys kaise ho"}





    #flipkard.com/items/item_id
  @app.get("/items/{item_id}")
  def index(item_id:int):
      return {"Product_id": item_id}




  @app.get("/items/")
  def index(q:int=0):
      return {"product_id"q}

