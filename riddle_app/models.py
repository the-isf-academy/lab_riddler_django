from django.db import models
from fuzzywuzzy import fuzz

class Riddle(models.Model):
    question = models.CharField(max_length=500)
    answer = models.CharField(max_length=500)
    date_added = models.DateTimeField(auto_now_add = True)

    DIFFICULTY_CHOICES = [
        (1, 'Easy'),
        (2,'Medium'),
        (3, 'Hard'),
    ]

    difficulty = models.CharField(
        max_length=1,
        choices=DIFFICULTY_CHOICES,
        default=None,
    )

    def check_guess(self,guess):
        MIN_FUZZ_RATIO = 70
        similarity = fuzz.ratio(guess.lower(), self.answer.lower())
      
        if similarity >= MIN_FUZZ_RATIO:
            return True
        else:
            return False
    