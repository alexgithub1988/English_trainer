from dataclasses import dataclass, field

@dataclass
class Sentence:
    russian: str
    english: str
    words: list = field(default_factory=list)
    fake_pronouns: list = field(default_factory=list)
    fake_verbs: list = field(default_factory=list)




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

    def get_words(self) -> list:
        return self.words

@dataclass
class Lesson:
    sentence: Sentence = field(default_factory=Sentence)
    fake_pronouns: list = field(default_factory=list)
    fake_verbs: list = field(default_factory=list)




