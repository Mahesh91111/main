from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.session import get_db

from app.schemas.auth import(
    RegisterRequest,
    LoginRequest,
    RefreshTokenRequest,
    UserResponse,
    TokenResponse,
    MessageResponse
)
from app.services.auth_service import AuthService

router = APIRouter(
   prefix="/api/v1/auth",
   tags=["Authentication"]
)

##Register
@router.post("/register",response_model=UserResponse,status_code= 201)
def register(
    request: RegisterRequest,
    db: Session = Depends(get_db)
):
    return AuthService.register_user(db, request)
##Login
@router.post("/Login",response_model=TokenResponse)
def login(request:LoginRequest,
        db:Session=Depends(get_db)):
    return AuthService.login_user(db, request)


###Refresh token
@router.post("/refreshToken",response_model=TokenResponse)
def refresh_token(
    request:RefreshTokenRequest
):
    return AuthService.refresh_token(request.refresh_token)

# ----------------------------
# Logout
# ----------------------------
@router.post(
    "/logout",
    response_model=MessageResponse
)
def logout():
    """
    Client should delete stored tokens.
    If you later store refresh tokens in DB/Redis,
    invalidate them here.
    """
    return MessageResponse(
        message="Logout successful."
    )