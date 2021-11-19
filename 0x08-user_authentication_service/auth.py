#!/usr/bin/env python3
""" Authentication module
"""

import bcrypt
import uuid
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> str:
    """Password hashing method
    """

    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def _generate_uuid() -> str:
    """Generate uuid
    """
    return str(uuid.uuid4())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Register a new user
        """
        try:
            User = self._db.find_user_by(email=email)
            raise ValueError("{} already exists".format(email))
        except NoResultFound:
            hashedpwd: str = _hash_password(password)
            return self._db.add_user(email=email, hashed_password=hashedpwd)

    def valid_login(self, email: str, password: str) -> bool:
        """Validate correct user password
        """
        try:
            user = self._db.find_user_by(email=email)
            return bcrypt.checkpw(password.encode('utf-8'),
                                  user.hashed_password)
        except NoResultFound:
            return False

    def create_session(self, email: str) -> str:
        """Create session for user
        """
        try:
            user = self._db.find_user_by(email=email)
            self._db.update_user(user.id, session_id=_generate_uuid())
            return user.session_id
        except NoResultFound:
            return None

    def get_user_from_session_id(self, session_id: str) -> User:
        """Get user from session id
        """
        try:
            return self._db.find_user_by(session_id=session_id)
        except NoResultFound:
            return None

    def destroy_session(self, user_id: int) -> None:
        """Remove user session id
        """
        self._db.update_user(user_id, session_id=None)

    def get_reset_password_token(self, email: str) -> str:
        """Genrate and add reset token to user
        """
        try:
            user = self._db.find_user_by(email=email)
            self._db.update_user(user.id, reset_token=_generate_uuid())
            return user.reset_token
        except NoResultFound:
            raise ValueError

    def update_password(self, reset_token: str, password: str) -> None:
        """Reset user password
        """
        try:
            user = self._db.find_user_by(reset_token=reset_token)
            hashedpwd: str = _hash_password(password)
            self._db.update_user(user.id, password=hashedpwd, reset_token=None)
        except NoResultFound:
            raise ValueError
