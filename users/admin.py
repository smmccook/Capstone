from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username',]


admin.site.register(CustomUser, CustomUserAdmin)

# admin.site.unregister(Group)
#
# # class GroupAdmin(admin.ModelAdmin):
# #     form = GroupAdminForm
# #     filter_horizontal = ['permissions']
#
#
# admin.site.register(Group, GroupAdmin)