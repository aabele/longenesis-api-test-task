from django.db import models
from django.contrib.auth import get_user_model


class Questionnary(models.Model):
    name = models.CharField(max_length=1024)


class Question(models.Model):
    contents = models.CharField(max_length=1024)
    questionnary = models.ForeignKey('questionnaries.Questionnary', on_delete=models.CASCADE)

    def __str__(self):
        return self.contents


class Answer(models.Model):
    contents = models.CharField(max_length=1024)
    image = models.ImageField(blank=True, null=True, upload_to='answer-images')
    question = models.ForeignKey('questionnaries.Question', on_delete=models.CASCADE)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    insert_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.contents
