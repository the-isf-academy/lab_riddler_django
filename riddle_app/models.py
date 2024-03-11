from django.db import models
from fuzzywuzzy import fuzz


# Create your models here.

class Riddle(models.Model):
    question = models.CharField(max_length=500)
    answer = models.CharField(max_length=500)
    likes = models.IntegerField(default=0)
    date_added = models.DateTimeField(auto_now_add = True)

    DIFFICULTY_CHOICES = [
        ('E', 'Easy'),
        ('M','Medium'),
        ('H', 'Hard'),
    ]

    difficulty = models.CharField(
        max_length=1,
        choices=DIFFICULTY_CHOICES,
        default=None,
    )

    def __str__(self):
        return f"{self.question}"
    
    def check_guess(self,guess):
        MIN_FUZZ_RATIO = 70
        similarity = fuzz.ratio(guess.lower(), self.answer.lower())
      
        if similarity >= MIN_FUZZ_RATIO:
            return True
        else:
            return False
    
    def increase_likes(self):
        self.likes += 1
        self.save()


        