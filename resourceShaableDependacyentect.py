
async def common_param(q:Optional[str]=None, skip:int=0 , limit:int=10):
    return {"q":q, "skip":skip, "limit":limit}
# humne ue depcy function create kar diya jo logi hum use karna chiate hai

##let create ohter function
@app.get("/manektech")
async def read_item(common: dict = Depends(common_param)):
    return common

@app.get("/course")
async def course_item(common: dict = Depends(common_param)):
    return common
