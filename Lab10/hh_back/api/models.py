from django.db import models

class Company(models.Model):
    name = models.CharField()
    description = models.TextField()
    city = models.CharField()
    address = models.TextField()

    def __str__(self):
        return self.name

class Vacancy(models.Model):
    name = models.CharField()
    description = models.TextField()
    salary = models.FloatField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='vacancies')

    def __str__(self):
        return self.name
