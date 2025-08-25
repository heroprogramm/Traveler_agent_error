from fastapi import FastAPI, Request, HTTPException
from clerk import Clerk

app = FastAPI()

# Use your Clerk Secret Key here
clerk = Clerk(api_key="YOUR_CLERK_SECRET_KEY")

@app.get("/protected")
async def protected_route(request: Request):
    auth_header = request.headers.get("Authorization")
    if not auth_header:
        raise HTTPException(status_code=401, detail="Unauthorized")

    token = auth_header.split(" ")[1]  # Get JWT from header

    try:
        user = clerk.users.verify_jwt(token)
        return {"message": f"Hello {user['email']}!"}
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid token")
