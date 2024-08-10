import uuid

from library.models import BaseModel
from marshmallow import Schema, fields, validate, validates, ValidationError, validates_schema
from datetime import date, datetime
from library.models.book import BookSchema


class Author(BaseModel):
    __slots__ = ['name', 'surname', 'birth_date', 'death_date', 'biography'] + BaseModel.__slots__

    def __init__(self, author_id: uuid, name: str, surname: str, birth_date: date, death_date: date = None,
                 biography: str = None):
        super().__init__(model_id=author_id)
        self.name = name
        self.surname = surname
        self.birth_date = birth_date
        self.death_date = death_date
        self.biography = biography


class AuthorSchema(Schema):
    id = fields.UUID(required=True, default=lambda: str(uuid.uuid4()), dump_only=True)
    first_name = fields.String(required=True, validate=validate.Length(min=1, max=50))
    second_name = fields.String(required=True, validate=validate.Length(min=1, max=50))
    birth_date = fields.Date("%d-%m-%Y", required=False)
    death_date = fields.Date("%d-%m-%Y", required=False, allow_none=True)
    biography = fields.String(required=False, allow_none=True)
    books = fields.List(fields.Nested(BookSchema(exclude=['author'])))

    @staticmethod
    def validate_date(value: date, description: str):
        if value > datetime.now().date():
            raise ValidationError(f"{description} must be before or equal to {datetime.now().date()}")

    @validates('birth_date')
    def validate_birth_date(self, value):
        AuthorSchema.validate_date(value, 'Birth date')

    @validates('death_date')
    def validate_death_date(self, value):
        AuthorSchema.validate_date(value, 'Death date')

    @validates_schema
    def validate_dates(self, data, **kwargs):
        birth_date = data.get('birth_date')
        death_date = data.get('death_date')
        if birth_date and death_date and birth_date > death_date:
            raise ValidationError('Birth date must be earlier than death date.')


author_schema = AuthorSchema()
