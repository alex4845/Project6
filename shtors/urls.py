from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path

from shtors.views import main_page, in_list1, in_list2, registration, enter_user, exit_user, calendar, question

urlpatterns = [
    path('', main_page, name="Главная"),
    path('in_list1/<int:pk>', in_list1, name="Категории"),
    path('in_list2/<int:pk>', in_list2, name="Категории2"),
    path('registration', registration, name="Регистрация"),
    path('enter_user', enter_user, name="Вход"),
    path('exit_user', exit_user, name="Выход"),
    path('calendar', calendar, name="Календарь"),
    path('question', question, name="Вопрос"),
]





