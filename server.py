from mcp.server.fastmcp import FastMCP
import httpx

BACKEND_URL = "http://127.0.0.1:8000"   # your FastAPI backend

mcp = FastMCP("student_data_mcp")

# ------------------------------------------------------
# 🔍 GET STUDENT BY ID
# ------------------------------------------------------
@mcp.tool()
async def get_student(student_id: int) -> dict:
    """
    Fetch a student's profile from FastAPI using their ID.
    """
    api_url = f"{BACKEND_URL}/api/v1/add_student/{student_id}"

    try:
        async with httpx.AsyncClient() as client:
            resp = await client.get(api_url, timeout=10)
            resp.raise_for_status()
            return resp.json()

    except Exception as e:
        return {"error": str(e)}


# ------------------------------------------------------
# ➕ ADD NEW STUDENT
# ------------------------------------------------------
@mcp.tool()
async def add_student(data: dict) -> dict:
    """
    Add a new student to the backend.
    Your backend expects a JSON body.
    """
    api_url = f"{BACKEND_URL}/api/v1/add_student/"

    try:
        async with httpx.AsyncClient() as client:
            resp = await client.post(api_url, json=data, timeout=10)
            resp.raise_for_status()
            return resp.json()

    except Exception as e:
        return {"error": str(e)}


# ------------------------------------------------------
# ✏ UPDATE STUDENT (EDIT)
# ------------------------------------------------------
@mcp.tool()
async def update_student(student_id: int, data: dict) -> dict:
    """
    Update student info (edit student).
    Uses PUT /student_id + JSON body.
    """
    api_url = f"{BACKEND_URL}/api/v1/add_student/{student_id}"

    try:
        async with httpx.AsyncClient() as client:
            resp = await client.put(api_url, json=data, timeout=10)
            resp.raise_for_status()
            return resp.json()

    except Exception as e:
        return {"error": str(e)}


# ------------------------------------------------------
# MAIN
# ------------------------------------------------------
def main():
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
