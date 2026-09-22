from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.sql import func

from app.database.database import Base


class User(Base):
    __tablename__ = "users"

    # Primary Key
    id = Column(Integer, primary_key=True, index=True)

    # User Information
    username = Column(String(100), unique=True, nullable=False, index=True)

    email = Column(String(150), unique=True, nullable=False, index=True)

    # Hashed Password
    password = Column(String(255), nullable=False)

    # Roles
    # Admin
    # Doctor
    # Patient
    # Student
    # Faculty
    role = Column(String(50), nullable=False, default="patient")

    # Account Status
    is_active = Column(Boolean, default=True)

    is_verified = Column(Boolean, default=False)

    # Audit Columns
    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )

    def __repr__(self):
        return (
            f"<User(id={self.id}, "
            f"username='{self.username}', "
            f"email='{self.email}', "
            f"role='{self.role}')>"
        )