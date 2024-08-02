import uuid


class BaseModel:
    __slots__ = ['_id']

    def __init__(self, model_id: uuid = uuid.uuid4()):
        self._id = model_id

    @property
    def id(self):
        return self._id

    def number_of_attributes(self) -> int:
        return sum(len(getattr(cls, '__slots__', [])) for cls in self.__class__.__mro__)

    def to_dict(self) -> dict:
        result = {}
        for cls in self.__class__.__mro__:
            if hasattr(cls, '__slots__'):
                for item in cls.__slots__:
                    attr_name = item if item[0] != '_' else item[1:]
                    value = getattr(self, item)
                    if isinstance(value, set) or isinstance(value, tuple):
                        value = list(value)
                    result[attr_name] = value
        return result
