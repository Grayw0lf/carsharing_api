from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CarShareUserChangeForm, CarShareUserCreationForm
from .models import CarShareUser


class CarShareUserAdmin(UserAdmin):
    add_form = CarShareUserCreationForm
    form = CarShareUserChangeForm
    model = CarShareUser
    list_display = ['email', 'username', 'user_lang']


admin.site.register(CarShareUser, CarShareUserAdmin)
