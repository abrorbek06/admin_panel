from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

VALUE_TYPE = (
    ('qashqadaryo', 'Qashqadaryo'),
    ('andijon', 'Andijon'),
    ('samarqand', 'Samarqand'),
    ('buxoro', 'Buxoro'),
    ('namangan', 'Namangan'),
    ('guliston', 'Guliston'),
    ("farg'ona", "Farg'ona"),
    ('toshkent', 'Toshkent'),
    ('surxondaryo', 'Surxondaryo'),
    ('xorazm', 'Xorazm'),
    ("navoiy", 'Navoiy'),
    ('sirdaryo', 'Sirdaryo'),
    ('jizzax', 'Jizzax')
)


class SendMessage(models.Model):
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    email = models.EmailField()
    place = models.CharField(max_length=120, choices=VALUE_TYPE)
    phone_number = models.CharField(max_length=13)
    message = models.TextField()

    def __str__(self):
        return self.first_name

