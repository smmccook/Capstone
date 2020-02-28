from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, ButtonHolder, Submit
from django.contrib.auth import get_user_model
from .models import CustomUser
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.admin.widgets import FilteredSelectMultiple

User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)


        self.helper = FormHelper()
        self.helper.layout = Layout(
            'email',
            'username',
            'password1',
            'password2',
            ButtonHolder(
                Submit('register', 'Register', css_class='btn-primary')
            )
        )
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name')



class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')


# class GroupAdminForm(forms.ModelForm):
#     class Meta:
#         model = Group
#         exclude = []
#
#     users = forms.ModelMultipleChoiceField(
#         queryset=User.objects.all(),
#         required=False,
#         widget = FilteredSelectMultiple('users', False)
#     )
#
#     def __init__(self, *args, **kwargs):
#         super(GroupAdminForm, self).__init__(*args, **kwargs)
#
#         if self.instance.pk:
#             self.fields['users'].initial = self.instance.user_set.all()
#
#         def save_m2m(self):
#             self.instance.user_set.set(self.cleaned_data['users'])
#
#         def save(self, *args, **kwargs):
#             instance = super(GroupAdminForm, self).save()
#             self.save_m2m()
#             return instance
