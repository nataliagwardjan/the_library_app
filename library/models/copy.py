import uuid
from enum import Enum

from library.models import BaseModel


class Status(Enum):
    AVAILABLE = 'available'
    RESERVED = 'reserved'
    BORROWED = 'borrowed'


class Copy(BaseModel):
    __slots__ = ['book_id', 'status'] + BaseModel.__slots__

    def __init__(self, copy_id: uuid, book_id: uuid, status: Status = Status.BORROWED):
        super().__init__(model_id=copy_id)
        self.book_id = book_id
        self.status = status
