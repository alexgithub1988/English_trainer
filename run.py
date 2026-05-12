from engine import Lesson
from lesson_1_templates import sentences,fake_verbs,fake_pronounce
import random


generate_random_sentence = random.choice(sentences)
lesson = Lesson(1,generate_random_sentence,fake_verbs,fake_pronounce)


var = lesson.dict_construct()
print(var)


