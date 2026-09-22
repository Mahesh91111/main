from pydantic import BaseModel, EmailStr, Field, ConfigDict
from typing import Optional
from datetime import datetime


# ============================
# Register User Request
# ============================
class RegisterRequest(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    email: EmailStr
    password: str = Field(..., min_length=6, max_length=100)
    role: str = Field(default="patient")


# ============================
# Login Request
# ============================
class LoginRequest(BaseModel):
    email: EmailStr
    password: str


# ============================
# User Response
# ============================
class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    role: str
    is_active: bool
    is_verified: bool
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


# ============================
# JWT Token Response
# ============================
class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"


# ============================
# Refresh Token Request
# ============================
class RefreshTokenRequest(BaseModel):
    refresh_token: str


# ============================
# Forgot Password Request
# ============================
class ForgotPasswordRequest(BaseModel):
    email: EmailStr


# ============================
# Change Password Request
# ============================
class ChangePasswordRequest(BaseModel):
    old_password: str
    new_password: str = Field(..., min_length=6)


# ============================
# Reset Password Request
# ============================
class ResetPasswordRequest(BaseModel):
    token: str
    new_password: str = Field(..., min_length=6)


# ============================
# Generic API Response
# ============================
class MessageResponse(BaseModel):
    message: str


# ============================
# Current User Response
# ============================
class CurrentUser(BaseModel):
    id: int
    username: str
    email: EmailStr
    role: str

    model_config = ConfigDict(from_attributes=True)

class TokenrResponse(BaseModel):
    access_toekn  :  str
    refresh_token : str
    token_type :  str = "bearer"