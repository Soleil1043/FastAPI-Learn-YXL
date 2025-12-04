from fastapi import FastAPI
import uvicorn

app = FastAPI()
@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

@app.get("/hello/{name}")
def say_hello(name: str):
    return {"message": f"hello, {name}!"}

@app.get("/users/{user_id}")
def read_user(user_id: int, name: str = None, age: int = None):
    return {
        "user_id": user_id,
        "name": name,
        "age": age,
        "info": f"User {user_id} information"
    }

@app.get("/calculate/{operation}")
def calculate(operation: str,a: float, b: float):
    operations = {
        "add": a + b,
        "subtract": a - b,
        "multiply": a * b,
        "divide": a / b if b != 0 else "Error: Division by zero"
    }

    if operation not in operations:
        return {"error": "Invalid operation"}

    return {
        "operation": operation,
        "a": a,
        "b": b,
        "result": operations[operation]
    }

if __name__ == "__main__":
    uvicorn.run("main.app", host="0.0.0.0", port=8000, reload=True)

