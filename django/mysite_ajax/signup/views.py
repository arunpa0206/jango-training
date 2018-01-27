from django.shortcuts import render

from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView

class SignUpView(CreateView):
    template_name = 'signup/signup.html'
    form_class = UserCreationForm

from django.contrib.auth.models import User
from django.http import JsonResponse

def validate_username(request):
    username = request.GET.get('username', None)
    data = {
        'is_taken': User.objects.filter(username__iexact=username).exists()
    }
    return JsonResponse(data)
