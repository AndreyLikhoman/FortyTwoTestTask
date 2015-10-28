from django.db import models
from django.contrib.auth.models import User

class Users(models.Model):
	login = models.CharField(max_length=250, db_index=True, unique=True, default="", verbose_name="Логин")
	name = models.CharField(max_length=250, db_index=True, unique=True, blank=True, default="", verbose_name="Имя")
	sername = models.CharField(max_length=250, db_index=True, unique=True, blank=True, default="", verbose_name="Фамилия")
	date = models.DateField(verbose_name="Дата рождения")
	bio = models.TextField(verbose_name="О себе")
	mail = models.CharField(max_length=250, db_index=True, unique=True, blank=True, default="", verbose_name="Почта")
	phone = models.CharField(max_length=250, db_index=True, unique=True, blank=True, default="", verbose_name="Телефон")

				