import uuid

from django.contrib.auth.models import User
from django.db import models


class StandardQuestions(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    question_text = models.CharField(null=True, blank=True)

    class Meta:
        verbose_name = 'Standard Questions'
        verbose_name_plural = 'Standard Questions'
        db_table = 'standard_question'

    def __str__(self):
        return self.question_text


class UserStandardAnswers(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    answer = models.CharField(null=True, default='')

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    question = models.ForeignKey(StandardQuestions, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = 'User Standard Answer'
        verbose_name_plural = 'User Standard Answers'
        db_table = 'user_standard_answers'

    def __str__(self):
        return f'{self.user} :: {self.question} :: {self.answer}'
