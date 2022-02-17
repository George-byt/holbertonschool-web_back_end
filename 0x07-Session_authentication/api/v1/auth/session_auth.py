#!/usr/bin/env python3
""" Python file that contains the SessionAuth class """
from api.v1.auth.auth import Auth
import uuid
from models.user import User


class SessionAuth(Auth):
    """
    SeccionAuth class that inherits from Auth.
    Args:
        Auth ([type]): Inherits from Auth class
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """
        Method that creates a Session ID
        for a user_id
        """
        if not user_id or not isinstance(user_id, str):
            return None
        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id
