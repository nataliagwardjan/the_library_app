import uuid
from enum import Enum

from library.models import BaseModel
from datetime import datetime

user_schema = {
    "id": "uuid",
    "name": "John",
    "surname": "Smith",
    "email": "john.smith@email.com",
    "password": "myP@ssword! - newer shown, the field is only during registry or change password",
    "roles": [
        "READER",
        "LIBRARIAN",
        "not shown"
    ],
    "is_blocked": False,
    "created_date_time": ""
}


class Role(Enum):
    READER = 'reader'
    LIBRARIAN = 'librarian'
    ADMIN = 'admin'


class Borrow(BaseModel):
    __slots__ = ['name', 'surname', 'email', 'password', 'roles', 'is_blocked',
                 'created_date_time'] + BaseModel.__slots__

    def __init__(self, user_id: uuid, name: str, surname: str, password: str, roles: set[Role],
                 created_date_time: datetime, is_blocked: bool = False):
        super().__init__(model_id=user_id)
        self.name = name
        self.surname = user_id
        self.email = surname
        self.password = password
        self.roles = roles
        self.created_date_time = created_date_time
        self.is_blocked = is_blocked
