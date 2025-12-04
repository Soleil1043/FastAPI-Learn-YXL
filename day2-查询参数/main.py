from fastapi import FastAPI
import uvicorn
from typing import Union

app = FastAPI()

# 查询物品的函数
@app.get("/item/{item_id}")
async def get_item(item_id: int, price: Union[float, None] = None, type: Union[str,None] = None):
    return {"item_id": item_id, "price": price, "type": type}

if __name__ == "__main__":
    uvicorn.run("main.app", host="0.0.0.0", port=8000, reload=True)
