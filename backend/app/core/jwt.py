from datetime import datetime, timedelta, timezone
from jose import JWTError, jwt

from app.config import settings


class JWTHandler:

    @staticmethod
    def create_access_token(data: dict) -> str:
        to_encode = data.copy()

        expire = datetime.now(timezone.utc) + timedelta(
            minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
        )

        to_encode.update(
            {
                "exp": expire,
                "type": "access"
            }
        )

        return jwt.encode(
            to_encode,
            settings.SECRET_KEY,
            algorithm=settings.ALGORITHM
        )

    @staticmethod
    def create_refresh_token(data: dict) -> str:
        to_encode = data.copy()

        expire = datetime.now(timezone.utc) + timedelta(days=7)

        to_encode.update(
            {
                "exp": expire,
                "type": "refresh"
            }
        )

        return jwt.encode(
            to_encode,
            settings.SECRET_KEY,
            algorithm=settings.ALGORITHM
        )

    @staticmethod
    def verify_token(token: str):
        try:
            return jwt.decode(
                token,
                settings.SECRET_KEY,
                algorithms=[settings.ALGORITHM]
            )

        except JWTError:
            return None