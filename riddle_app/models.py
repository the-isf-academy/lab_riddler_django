from django.db import models
from fuzzywuzzy import fuzz

class Riddle(models.Model):
    question = models.CharField(max_length=500)
    answer = models.CharField(max_length=500)
    date_added = models.DateTimeField(auto_now_add = True)
    # total_guesses = models.IntegerField(default=0)
    # correct_guesses = models.IntegerField(default=0)

    DIFFICULTY_CHOICES = [
        (1, 'Easy'),
        (2,'Medium'),
        (3, 'Hard'),
    ]

    difficulty = models.IntegerField(
        choices=DIFFICULTY_CHOICES,
        default=1,
    )

    def check_guess(self,guess):
        MIN_FUZZ_RATIO = 70
        similarity = fuzz.ratio(guess.lower(), self.answer.lower())

        # self.total_guesses += 1

        if similarity >= MIN_FUZZ_RATIO:
            # self.correct_guesses += 1

            # self.save()
            return True
        else:
            # self.save()
            return False
    