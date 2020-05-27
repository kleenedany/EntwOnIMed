from django.db import models

class User(models.Model):
    GENDER_CHOICES = [
        ('NONE', 'Undefiniert'),
        ('MALE', 'Männlich'),
        ('FEMALE', 'Weiblich'),
        ('OTHER', 'Weitere')
    ]

    user_name = models.CharField(max_length = 10)
    user_image = models.FileField(upload_to = 'uploads/', max_length = 100)
    password = models.CharField(max_length = 30)
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    e_mail = models.EmailField(max_length = 255)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length = 30, choices = GENDER_CHOICES, default = 'NONE')
    street = models.CharField(max_length = 30)
    house_number = models.CharField(max_length = 5)
    post_code = models.IntegerField(max_length = 5)
    domicile = models.CharField(max_length = 30)