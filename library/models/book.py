import uuid
from enum import Enum

from library.models import BaseModel
from marshmallow import Schema, fields, validate, ValidationError, validates
from datetime import datetime

from library.models.author import AuthorSchema


class Category(Enum):
    MYSTERY = "mystery"
    THRILLER = "thriller"
    COMEDY = "comedy"
    DRAMA = "drama"
    ROMANCE = "romance"
    FANTASY = "fantasy"
    SCIENCE_FICTION = "science fiction"
    HORROR = "horror"
    ADVENTURE = "adventure"
    YOUNG_ADULT = "young adult"
    DYSTOPIAN = "dystopian"
    PARANORMAL = "paranormal"
    CONTEMPORARY = "contemporary"
    CHICK_LIT = "chick lit"
    GRAPHIC_NOVEL = "graphic novel"
    PSYCHOLOGICAL_THRILLER = "psychological thriller"
    GOTHIC = "gothic"
    CRIME = "crime"
    SUPERNATURAL = "supernatural"
    ARCHAEOLOGY = "archeology"
    PUZZLE = "puzzle"
    ACTION = "action"


class Book(BaseModel):
    __slots__ = ['title', 'author', 'year', 'short_description', 'long_description', 'categories', 'ebook',
                 'audiobook'] + BaseModel.__slots__

    def __init__(self, book_id: uuid, title: str, author: dict, year: int, short_description: str = None,
                 long_description: str = None, categories: set[Category] = None, ebook: bool = False,
                 audiobook: bool = False):
        super().__init__(model_id=book_id)
        self.title = title
        self.author = author
        self.year = year
        self.short_description = short_description
        self.long_description = long_description
        self.categories = categories
        self.ebook = ebook
        self.audiobook = audiobook


class BookSchema(Schema):
    id = fields.UUID(required=True, default=lambda: str(uuid.uuid4()), dump_only=True)
    title = fields.String(required=True, validate=validate.Length(min=1, max=100))
    author = fields.Nested(AuthorSchema, only=['first_name', 'second_name'])
    year = fields.Integer(validate=validate_year, required=True)
    short_description = fields.String(required=False, allow_none=True)
    long_description = fields.String(required=False, allow_none=True)
    categories = fields.List(fields.String(), required=False, allow_none=True)
    ebook = fields.Boolean(default=False, required=False)
    audiobook = fields.Boolean(default=False, required=False)

    @validates('year')
    def validate_year(self, value):
        current_year = datetime.now().year
        if value > current_year:
            raise ValidationError(f"Year must not be greater than the current year ({current_year}).")
        if value <= 0:
            raise ValidationError(f"Year must be greater than 0.")


book_schema = BookSchema()
