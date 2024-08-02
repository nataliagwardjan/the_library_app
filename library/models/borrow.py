import uuid
from enum import Enum

from library.models import BaseModel
from datetime import datetime, date


class BorrowType(Enum):
    BOOK = 'book'
    AUDIOBOOK = 'audiobook'
    EBOOK = 'ebook'


class Borrow(BaseModel):
    __slots__ = ['borrow_type', 'user_id', 'book_or_copy_id', 'borrow_date_time', 'return_date', 'real_return_date_time',
                 'is_returned'] + BaseModel.__slots__

    def __init__(self, borrow_id: uuid, borrow_type: BorrowType, user_id: uuid, book_or_copy_id: uuid,
                 borrow_date_time: datetime, return_date_time: date, real_return_date_time: datetime,
                 is_returned: bool = False):
        super().__init__(model_id=borrow_id)
        self.borrow_type = borrow_type
        self.user_id = user_id
        self.book_or_copy_id = book_or_copy_id
        self.borrow_date_time = borrow_date_time
        self.return_date_time = return_date_time
        self.real_return_date_time = real_return_date_time
        self.is_returned = is_returned
