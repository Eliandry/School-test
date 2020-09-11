from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Theme(models.Model):
    name = models.CharField(max_length=300)
    def __str__(self):
        return self.name


class Question(models.Model):
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE,related_name='foreign')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    text=models.TextField("Задача")
    image=models.ImageField(upload_to="question/",blank=True)
    answer=models.FloatField()
    point=models.SmallIntegerField()

class Variant(models.Model):
    number=models.SmallIntegerField()
    questions=models.ManyToManyField(Question)