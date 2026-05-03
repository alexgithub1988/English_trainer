from dataclasses import dataclass, field

@dataclass
class Sentence:
    russian : str
    english: str


    def check(self, answer: str) -> bool:
        """
        Сверяем ответ
        :param answer:
        :return:
        """
        if self.english == answer:
            return True
        else:
            return False

    def get_english_sentence(self) -> str:
        """

        :return: english sentence
        """
        return self.english

    def get_russian_sentence(self) -> str:
        """
        :return: russian sentence

        """
        return self.russian




@dataclass
class Lesson:
    lesson_number : int
    sentence: Sentence = field(default_factory=Sentence)
    fake_pronouns: dict = field(default_factory=dict) | None
    fake_verbs: dict = field(default_factory=dict)   | None

    def split_sentence(self, sentence: str) -> list:
        """
        :param sentence:

        :return: возвращаем список обрезанных слов
        """
        return sentence.split().strip()





