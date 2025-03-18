#python manage.py test -v 2

from django.test import TestCase
from .models import Riddle

class RiddleModelTest(TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        print("="*50)
        print("\n--- SETTING UP RIDDLE TEST --- \n")
        cls.riddle = Riddle.objects.create(
            question="What has hands and a face, but can’t smile?",
            answer="A clock",
            difficulty=1
        )

    def test_fields(self):
        self.assertEqual(self.riddle.question, "What has hands and a face, but can’t smile?")
        self.assertEqual(self.riddle.answer, "A clock")
        self.assertEqual(self.riddle.difficulty, 1)
    
    def test_methods(self):
        correct_guess = self.riddle.check_guess('A clock')
        self.assertEqual(correct_guess, True)

        incorrect_guess = self.riddle.check_guess('pizza')
        self.assertEqual(incorrect_guess, True)
        