from django.contrib import admin

from .models import List1, List2, List3, User_list, User_question

admin.site.register(List1)
admin.site.register(List2)
admin.site.register(List3)
admin.site.register(User_list)
admin.site.register(User_question)