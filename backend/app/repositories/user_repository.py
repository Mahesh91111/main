from typing import Optional

from sqlalchemy.orm import Session

from app.models.user import User


class UserRepository:

    @staticmethod
    def create_user(
        db: Session,
        username: str,
        email: str,
        password: str,
        role: str = "patient"
    ) -> User:
        """
        Create a new user.
        """

        user = User(
            username=username,
            email=email,
            password=password,
            role=role
        )

        db.add(user)
        db.commit()
        db.refresh(user)

        return user

    @staticmethod
    def get_by_id(
        db: Session,
        user_id: int
    ) -> Optional[User]:
        """
        Get user by ID.
        """

        return (
            db.query(User)
            .filter(User.id == user_id)
            .first()
        )

    @staticmethod
    def get_by_email(
        db: Session,
        email: str
    ) -> Optional[User]:
        """
        Get user by email.
        """

        return (
            db.query(User)
            .filter(User.email == email)
            .first()
        )

    @staticmethod
    def get_by_username(
        db: Session,
        username: str
    ) -> Optional[User]:
        """
        Get user by username.
        """

        return (
            db.query(User)
            .filter(User.username == username)
            .first()
        )

    @staticmethod
    def get_all_users(
        db: Session
    ):
        """
        Get all users.
        """

        return db.query(User).all()

    @staticmethod
    def update_password(
        db: Session,
        user: User,
        hashed_password: str
    ) -> User:
        """
        Update user password.
        """

        user.password = hashed_password

        db.commit()

        db.refresh(user)

        return user

    @staticmethod
    def verify_user(
        db: Session,
        user: User
    ) -> User:
        """
        Mark user as verified.
        """

        user.is_verified = True

        db.commit()

        db.refresh(user)

        return user

    @staticmethod
    def deactivate_user(
        db: Session,
        user: User
    ) -> User:
        """
        Deactivate user account.
        """

        user.is_active = False

        db.commit()

        db.refresh(user)

        return user

    @staticmethod
    def activate_user(
        db: Session,
        user: User
    ) -> User:
        """
        Activate user account.
        """

        user.is_active = True

        db.commit()

        db.refresh(user)

        return user

    @staticmethod
    def delete_user(
        db: Session,
        user: User
    ) -> bool:
        """
        Delete user.
        """

        db.delete(user)

        db.commit()

        return True