from django.shortcuts import render, redirect
from django.http import HttpResponse
from rest_framework.decorators import action
from rest_framework import viewsets, filters, generics
from .models import User
from .forms import UserForm
from .serializers import UserSerializer
# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        user_name = self.request.query_params.get('user_name')
        if user_name is not None:
            result = User.objects.filter(user_name__icontains=user_name)
        else:
            result = User.objects.all()
        return result


def newUser(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'contact/added.html',)
    else:
        form = UserForm()
    return render(request, 'contact/new_user.html', {"form": form})
