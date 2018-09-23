# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Teacher(models.Model):
    LoginID = models.CharField(max_length=12)
    Password = models.CharField(max_length=250)
    Name = models.CharField(max_length=250)

    def __str__(self):
        return self.LoginID + " " + self.Password + " " + self.Name

class File(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    question_file_type = models.CharField(max_length=250)
    answer_file_type = models.CharField(max_length=250)

class Student(models.Model):
    LoginID = models.CharField(max_length=12)
    Password = models.CharField(max_length=250)
    Name = models.CharField(max_length=250)
    Score = models.IntegerField(default=0)

    def __str__(self):
        return self.LoginID + " " + self.Password + " " + self.Name + " " + (str(self.Score))

class Answer_table(models.Model):
    Question_no = models.IntegerField()
    Answer_value = models.CharField(max_length=1)

    def __str__(self):
        return (str(self.Question_no)) + " " + self.Answer_value
