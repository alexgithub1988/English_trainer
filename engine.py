from dataclasses import dataclass, field
import random


@dataclass
class Sentence:
    russian : str
    english: str


    

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
    sentence: Sentence
    fake_pronouns: list = field(default_factory=list)
    fake_verbs: list = field(default_factory=list)

    @property
    def get_russian_sentence(self) -> str:
        return self.sentence.get_russian_sentence()

    @property
    def get_english_sentence(self) -> str:
        return self.sentence.get_english_sentence()


    def split_russian_sentence(self) -> list[str]:
        return self.get_russian_sentence.split()

    def split_english_sentence(self) -> list[str]:
        return self.get_english_sentence.split()


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

    def mix_with_fakes(self) -> list:
        """
        Получаем лист предложение плюс фейки потом делаем микс
        :return:
        """
        list_for_mixing = (self.split_english_sentence() + random.sample(self.fake_pronouns, 2)
          + random.sample(self.fake_verbs, 2))
        mixed_list = random.sample(list_for_mixing, len(list_for_mixing))
        return mixed_list


    def dict_construct(self):
        return { "russian_sentence": self.get_russian_sentence,
                 "english_mixed_sentence": self.mix_with_fakes(),

        }







        





