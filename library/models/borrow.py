import uuid
from enum import Enum

from library.models import BaseModel
from marshmallow import Schema, fields, validate, post_load
from datetime import date, datetime, timezone
from dateutil.relativedelta import relativedelta
from flask import current_app


class BorrowType(Enum):
    BOOK = 'book'
    AUDIOBOOK = 'audiobook'
    EBOOK = 'ebook'


class Borrow(BaseModel):
    __slots__ = ['borrow_type', 'user_id', 'book_or_copy_id', 'borrow_date_time', 'return_date',
                 'real_return_date_time',
                 'is_returned'] + BaseModel.__slots__

    def __init__(self, borrow_id: uuid, borrow_type: BorrowType, user_id: uuid, book_or_copy_id: uuid,
                 borrow_date_time: datetime = None, return_date: date = None, real_return_date_time: datetime = None,
                 is_returned: bool = False):
        super().__init__(model_id=borrow_id)
        self.borrow_type = borrow_type
        self.user_id = user_id
        self.book_or_copy_id = book_or_copy_id
        self.borrow_date_time = borrow_date_time or datetime.now(timezone.utc)
        self.return_date = return_date or self.calculate_return_date(borrow_date_time)
        self.real_return_date_time = real_return_date_time
        self.is_returned = is_returned

    @staticmethod
    def calculate_return_date(borrow_datatime: datetime) -> date:
        return (borrow_datatime + relativedelta(
            months=current_app.config.get('DEFAULT_BORROW_TIME_IN_MONTH', 1))).date()


class BorrowSchema(Schema):
    id = fields.UUID(required=True, dump_only=True, default=lambda: uuid.uuid4())
    borrow_type = fields.String(required=True, validate=validate.OneOf([bt.value for bt in BorrowType]))
    user_id = fields.UUID(required=True)
    book_or_copy_id = fields.UUID(required=True)
    borrow_date_time = fields.DateTime(dump_only=True, format="%d-%m-%Y %H:%M:%S %Z",
                                       default=lambda: datetime.now(timezone.utc))
    return_date = fields.Date(dump_only=True, format="%d-%m-%Y")
    real_return_date_time = fields.DateTime(dump_only=True, format="%d-%m-%Y %H:%M:%S %Z", allow_none=True)
    is_returned = fields.Boolean(required=False, missing=False)

    @post_load
    def make_borrow(self, data, **kwargs):
        return Borrow(**data)

    @post_load
    def set_defaults(self, data, **kwargs):
        if 'borrow_date_time' not in data:
            data['borrow_date_time'] = datetime.now(timezone.utc)
        if 'return_date' not in data:
            data['return_date'] = Borrow.calculate_return_date(data['borrow_date_time'])
        return data


borrow_schema = BorrowSchema()
