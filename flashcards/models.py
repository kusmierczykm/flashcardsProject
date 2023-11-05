from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    removed = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'categories'


class Flashcard(models.Model):
    id = models.AutoField(primary_key=True)
    eng_word = models.CharField(max_length=30)
    pl_word = models.CharField(max_length=30)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.eng_word} - {self.pl_word}'

    class Meta:
        verbose_name_plural = 'flashcards'
