from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CarShareUser


class CarShareUserCreationForm(UserCreationForm):

    class Meta:
        model = CarShareUser
        fields = ('username', 'email', 'user_lang')


class CarShareUserChangeForm(UserChangeForm):

    class Meta:
        model = CarShareUser
        fields = ('username', 'email', 'user_lang')
