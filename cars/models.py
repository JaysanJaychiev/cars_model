from enum import unique
from pyexpat import model
from django.db import models
# получеия пользователя
from django.contrib.auth import get_user_model
User = get_user_model()

class Car(models.Model):
    vin = models.CharField(verbose_name='Vin', db_index=True, unique=True, max_length=64)
    color = models.CharField(verbose_name='Color', max_length=64)
    brand = models.CharField(verbose_name='Brand', max_length=64)
    CAR_TYPES = (
        (1, 'Cедан'),
        (2, 'Хечбек'),
        (3, 'Универсал'),
        (4, 'Купе'),
    )
    car_type = models.IntegerField(verbose_name='Car_type', choices=CAR_TYPES)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)


