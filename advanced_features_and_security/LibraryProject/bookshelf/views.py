from django.http import HttpResponse
from .models import CustomUserModel
from django.contrib.auth.models import Permission


def create_user(request):
    if request.method == "POST":
        user = CustomUserModel.objects.create(request.POST)
        return HttpResponse({'message': 'user created succes'})