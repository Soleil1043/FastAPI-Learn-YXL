from fastapi import FastAPI, Path, Query
from enum import Enum
from typing import Optional, List
import uvicorn

app = FastAPI(
    title="Day2-请求参数学习",
    description="深入学习路径参数、查询参数和类型验证",
    version="1.0.0"
)

# ============ 1. 路径参数 ============

# 基本路径参数
@app.get("/users/{user_id}")
async def get_user(user_id: int):
    """获取用户信息 - 基础路径参数"""
    return {"user_id": user_id, "message": f"用户{user_id}的信息"}

# 路径参数验证
@app.get("/items/{item_id}")
async def get_item(item_id: int = Path(...,
                                       title="物品ID",
                                       description="要获取的物品的唯一标识符",
                                       ge=1, # 大于等于1
                                       le=1000 # 小于等于1000
                                       )
                   ):
    """获取物品信息 - 带验证的路径参数"""
    if item_id > 900:
        return {"item_id": item_id, "special": True, "message": "这是一个特殊物品"}
    return {"item_id": item_id, "message": "普通物品信息"}

# 枚举路径参数
class UserRole(str, Enum):
    ADMIN = "admin"
    USER = "user"
    GUEST = "guest"
    MODERATOR = "moderator"

@app.get("/users/roles/{role}")
async def get_users_by_role(role: UserRole):
    """根据角色获取用户 - 枚举路径参数"""
    roles_info = {
        UserRole.ADMIN: {"permission": "full", "can_delete": True},
        UserRole.USER: {"permission": "normal", "can_delete": False},
        UserRole.GUEST: {"permission": "readonly", "can_delete": False},
        UserRole.MODERATOR: {"permission": "moderate", "can_delete": True},
    }

    return {
        "role": role,
        "info": roles_info[role],
        "users": [
            f"用户{i}" for i in range(1, 4)
        ]
    }

@app.get("/departments/{dept_id}/employees/{emp_id}")
async def get_department_employee(dept_id: int, emp_id: int):
    """获取部门中的员工 - 多个路径参数"""
    return {
        "department_id": dept_id,
        "employee_id": emp_id,
        "full_id": f"DEP{dept_id}-EMP{emp_id}",
        "info": f"部门 {dept_id} 的员工 {emp_id}"
    }
