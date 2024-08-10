import uuid
from enum import Enum

from library.models import BaseModel
from datetime import datetime, timezone
from marshmallow import Schema, fields, validate


class Role(Enum):
    READER = 'reader'
    LIBRARIAN = 'librarian'
    ADMIN = 'admin'


class User(BaseModel):
    __slots__ = ['name', 'surname', 'email', 'password', 'roles', 'is_blocked',
                 'created_date_time'] + BaseModel.__slots__

    def __init__(self, user_id: uuid = None, name: str = None, surname: str = None, email: str = None,
                 password: str = None, roles: set[Role] = None, created_date_time: datetime = None,
                 is_blocked: bool = False):
        super().__init__(model_id=user_id)
        self.name = name
        self.surname = surname
        self.email = email
        self.password = password
        self.roles = roles or {Role.READER}
        self.created_date_time = created_date_time or datetime.now(timezone.utc)
        self.is_blocked = is_blocked


class UserSchema(Schema):
    id = fields.UUID(required=True, dump_only=True, default=lambda: uuid.uuid4())
    name = fields.String(required=True, validate=validate.Length(min=1, max=50))
    email = fields.Email(required=True)
    password = fields.String(required=True, load_only=True)
    roles = fields.List(required=None, default=lambda: [Role.READER])
    created_date_time = fields.DateTime(dump_only=True, format="%d-%m-%Y %H:%M:%S %Z",
                                        default=lambda: datetime.now(timezone.utc))
    is_blocked = fields.Boolean(default=lambda: False)
