from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.schemas.auth import (
    RegisterRequest,
    LoginRequest,
    UserResponse,
    TokenResponse
)

from app.repositories.user_repository import UserRepository
from app.core.hashing import Hash
from app.core.jwt import JWTHandler


class AuthService:

    @staticmethod
    def register_user(
        db: Session,
        request: RegisterRequest
    ) -> UserResponse:

        username_exists = UserRepository.get_by_username(
            db,
            request.username
        )

        if username_exists:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Username already exists."
            )

        email_exists = UserRepository.get_by_email(
            db,
            request.email
        )

        if email_exists:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already exists."
            )

        hashed_password = Hash.hash_password(request.password)

        user = UserRepository.create_user(
            db=db,
            username=request.username,
            email=request.email,
            password=hashed_password,   
            role=request.role
        )

        return UserResponse.model_validate(user)

    @staticmethod
    def login_user(
        db: Session,
        request: LoginRequest
    ) -> TokenResponse:
        """
        Authenticate user and return JWT token.
        """

        # Find user
        user = UserRepository.get_by_email(
            db,
            request.email
        )

        if user is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid email or password."
            )

        # Check password
        if not Hash.verify_password(
            request.password,
            user.password
        ):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid email or password."
            )

        # Check account status
        if not user.is_active:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Account is inactive."
            )
        # Generate Access Token
        access_token = JWTHandler.create_access_token(
            {
                "sub": user.email,
                "role": user.role,
                "user_id": user.id
            }
        )

        # Generate Refresh Token
        refresh_token = JWTHandler.create_refresh_token(
            {
                "sub": user.email,
                "user_id": user.id
            }
        )

        return TokenResponse(
            access_token=access_token,
            refresh_token=refresh_token,
            token_type="bearer"
        )
    @staticmethod
    def refresh_token(refresh_token:str)->TokenResponse:
        """"Generete a new Access Token using the provided Refresh Token"""
        payload = JWTHandler.verify_token(refresh_token)
        if payload is None:
            raise HTTPException(
                status_code = status.HTTP_401_UNAUTHORIZED,
                detail  = "Invalid refresh token."
            )
        if payload.get("type") != "refresh":
            raise HTTPException(
                status_code = status.HTTP_401_UNAUTHORIZED,
                detail = "Invalid token type"
            )
            
        access_token = JWTHandler.create_acces_token(
            {
                "sub":payload["sub"],
                "user_id" : payload["user_id"]
            }
        )
        return TokenResponse(
            access_token = access_token,
            refresh_token = refresh_token,
            token_type = "bearer"
        )