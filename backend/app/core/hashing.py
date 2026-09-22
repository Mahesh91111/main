"""
Password Hashing Utilities

This module provides helper functions to:
1. Hash passwords before storing them.
2. Verify passwords during login.
"""

from passlib.context import CryptContext

# Configure Passlib to use bcrypt
pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)


class Hash:

    @staticmethod
    def hash_password(password: str) -> str:
        """
        Hash a plain text password.
        """
        return pwd_context.hash(password)

    @staticmethod
    def verify_password(plain_password: str, hashed_password: str) -> bool:
        """
        Verify a plain password against its hashed value.
        """
        return pwd_context.verify(
            plain_password,
            hashed_password
        )