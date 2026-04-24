from fastapi import APIRouter, Request, HTTPException
from fastapi.responses import RedirectResponse
import os
from dotenv import load_dotenv
from authlib.integrations.starlette_client import OAuth

# Load the environment
load_dotenv()

# Set up router.
auth_router = APIRouter()

# Google Client ID
g_client_id = os.getenv("google_client_id")
g_client_secret = os.getenv("client_secret")


# Set up of OAuth
oauth = OAuth()
oauth.register(
    name="google",
    client_id=g_client_id,
    client_secret=g_client_secret,
    server_metadata_url="https://accounts.google.com/.well-known/openid-configuration",
    client_kwargs={"scope": "openid email profile"},
)


@auth_router.get("/auth/google/login")
async def login(req: Request):
    redirect_uri = "http://localhost:8000/auth/google/callback"
    return await oauth.google.authorize_redirect(req, redirect_uri)


@auth_router.get("/auth/google/callback")
async def callback(req: Request):
    token = await oauth.google.authorize_access_token(req)
    user_info = token.get("userinfo")
    user_email = user_info.get("email")

    if user_email == os.getenv("owner_email"):
        req.session["user"] = user_email
        RedirectResponse(url=os.getenv("frontend_url"))
    else:
        raise HTTPException(status_code=401, detail="User not Authorized.")


@auth_router.get("/auth/me")
async def auth_status(req: Request):

    if req.session.get("user") == os.getenv("owner_email"):
        return {"status_code": 200, "message": "Welcome Runner"}
    else:
        return {"status_code": 401, "message": "User not authorized."}


def require_auth(req: Request):
    if not req.session.get("user", None):
        raise HTTPException(status_code=401, detail="Not Authorized")
