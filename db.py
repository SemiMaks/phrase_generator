import typing
import random
from pydantic import BaseModel
from pydantic import Field


# Первая модель - входная фраза.
class PhraseInput(BaseModel):
    """Phrase model"""

    # Создаем имя автора- если не передано, используется по умолчанию.
    author: str = "Anonymous"
    # Текст фразы, максмальное значение - 200 символов.
    text: str = Field(..., title="Text", description="Text of phrase", max_length=200)


# Вторая модель - выходная фраза.
class PhraseOutput(PhraseInput):
    # ID фразы в нашей базе данных.
    id: typing.Optional[int] = None


# Создадим простой класс для работы с БД.
class Database:
    """Our **fake** database"""

    def __init__(self):
        # id: model
        self._items: typing.Dict[int, PhraseOutput] = {}

    def get_random(self) -> int:
        # получение случайной фразы
        return random.choice(self._items.keys())

    def get(self, id: int) -> typing.Optional[PhraseOutput]:
        # Получение фразы по ID
        return self._items.get(id)

    def add(self, phrase: PhraseInput) -> PhraseOutput:
        # Добавление фразы
        id = len(self._items) + 1
        phrase_out = PhraseOutput(id=id, **phrase.dict())
        self._items[phrase_out.id] = phrase_out
        return phrase_out

    def delete(self, id: int) -> typing.Union[typing.NoReturn, None]:
        # Удаление фразы.
        if id in self._items:
            del self._items[id]
        else:
            raise ValueError("Phrase doesn't exist")
