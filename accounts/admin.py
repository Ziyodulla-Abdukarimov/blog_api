from django.contrib import admin
from .models import User, UserConfirmation


# Register your models here.
class UserModel(admin.ModelAdmin):
    list_display = ["id", "email"]


class UserConfirmationAdmin(admin.ModelAdmin):
    list_display = ('id',)


admin.site.register(User, UserModel)
admin.site.register(UserConfirmation, UserConfirmationAdmin)
