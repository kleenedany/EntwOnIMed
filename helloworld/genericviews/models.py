from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)

    def __str__(self):
        return self.last_name

class PersonalInformation(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    street = models.CharField(max_length = 30)
    number = models.IntegerField(max_length = 5)
    postcode = models.IntegerField(max_length = 5)
    domicile = models.CharField(max_length = 30)

