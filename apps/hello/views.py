from django.shortcuts import render
from .models import Users


def home(request):
	user = Users.objects.filter(login = "login")
	return render(request, 'index.html', {'user': user[0]})

