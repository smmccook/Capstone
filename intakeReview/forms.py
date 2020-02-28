from .models import Request
from django import forms

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import forms as auth_forms
from django.utils.translation import ugettext_lazy as _

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, ButtonHolder, Submit, Field, Div

YES_NO = [
    ('', '---'),
    (True, 'Yes'),
    (False, 'No'),
]
STATUS = [
    (0, 'Incomplete'),
    (1, 'Pending'),
    (2, 'Approved'),
    (3, 'Denied')
]


class AttachmentsForm(forms.ModelForm):
    contract = forms.FileField(required=False)
    BAA = forms.FileField(required=False)
    access_forms = forms.FileField(required=False)

    class Meta:
        model = Request
        fields = ['contract', 'BAA', 'access_forms']


class ViewForm(forms.ModelForm):
    approved_by_legal = forms.ChoiceField(widget=forms.Select(), choices=[('', '---'), (True, 'Yes'), (False, 'No'), ],
                                          required=True
                                          , initial=None, label='Has this been approved by legal?')
    free = forms.ChoiceField(widget=forms.Select(), choices=[('', '---'), (True, 'Yes'), (False, 'No'), ], required=True
                             , initial=None, label='Is it free?')
    group_licensing = forms.ChoiceField(widget=forms.Select(), choices=[('', '---'), (True, 'Yes'), (False, 'No'), ],
                                        required=False
                                        , initial=None, label='If it is not free, is it available for group licensing?')
    PHI = forms.ChoiceField(widget=forms.Select(), choices=[('', '---'), (True, 'Yes'), (False, 'No'), ], required=True
                            , initial=None, label='Will any Protected Health Information (PHI) be stored?')
    PII = forms.ChoiceField(widget=forms.Select(), choices=[('', '---'), (True, 'Yes'), (False, 'No'), ], required=True
                            , initial=None, label='Will any Personally Identifiable Information (PII) be stored?')
    PCI = forms.ChoiceField(widget=forms.Select(), choices=[('', '---'), (True, 'Yes'), (False, 'No'), ], required=True
                            , initial=None, label='Will any Payment Card Industry Information (PCI) be stored?')
    contract_exists = forms.ChoiceField(widget=forms.Select(), choices=[('', '---'), (True, 'Yes'), (False, 'No'), ],
                                        required=True
                                        , initial=None, label='Is there a signed contract with a third party?')
    BAA_exists = forms.ChoiceField(widget=forms.Select(), choices=[('', '---'), (True, 'Yes'), (False, 'No'), ],
                                   required=True
                                   , initial=None, label='Is there a signed Business Associate Agreement (BAA)?')
    external_access_required = forms.ChoiceField(widget=forms.Select(),
                                                 choices=[('', '---'), (True, 'Yes'), (False, 'No'), ], required=True
                                                 , initial=None, label='Will there be a need for external access to'
                                                                       ' AAH systems?')
    external_services = forms.CharField(widget=forms.Textarea(), required=True,
                                        label='Does the app rely on external services or servers?'
                                              ' (i.e Email, cloud, etc) If so, please explain')
    other_applications = forms.CharField(widget=forms.Textarea(), required=True,
                                         label='Will the app need to interface with other applications or '
                                               '              services on the device? '
                                               '(i.e. Email, Camera, Photos, etc.) If so, please explain')
    notes = forms.CharField(widget=forms.Textarea(), required=False, label="Additional Notes")
    security_notes = forms.CharField(widget=forms.Textarea(), required=False, label="Security Notes")
    contract = forms.FileField(required=False,
                               label='If so please attach the contract: (selected files will not appear here, but will be uploaded on submission)')
    BAA = forms.FileField(required=False,
                          label='If so please attach the BAA: (selected files will not appear here, but will be uploaded on submission)')
    access_forms = forms.FileField(
        label='If so, please attach the pertinent completed access forms: (selected files will not appear here, but will be uploaded on submission)',
        required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['second_URL'].disabled = True
        self.fields['approved_by_legal'].disabled = True
        self.fields['free'].disabled = True
        self.fields['group_licensing'].disabled = True
        self.fields['PHI'].disabled = True
        self.fields['PCI'].disabled = True
        self.fields['PII'].disabled = True
        self.fields['contract_exists'].disabled = True
        self.fields['BAA_exists'].disabled = True
        self.fields['BAA'].disabled = True
        self.fields['OS_version'].disabled = True
        self.fields['external_access_required'].disabled = True
        self.fields['external_services'].disabled = True
        self.fields['other_applications'].disabled = True
        self.fields['contract'].disabled = True
        self.fields['app_name'].disabled = True
        self.fields['URL'].disabled = True
        self.fields['description'].disabled = True
        self.fields['access_forms'].disabled = True
        self.fields['device'].disabled = True
        self.fields['min_OS_version'].disabled = True
        self.fields['latest_release_date'].disabled = True
        self.fields['notes'].disabled = True
        self.fields['status'].disabled = True
        self.fields['security_notes'].disabled = True

    class Meta:
        model = Request
        fields = ['app_name', 'URL', 'second_URL', 'description', 'approved_by_legal',
                  'free', 'group_licensing', 'PHI', 'PII', 'PCI', 'contract_exists', 'contract', 'BAA_exists', 'BAA',
                  'external_access_required', 'access_forms', 'OS_version',
                  'device', 'min_OS_version', 'latest_release_date', 'external_services', 'other_applications',
                  'notes', 'status', 'security_notes']


class ReviewForm(forms.ModelForm):


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['status'].requried = True
        self.fields['security_notes'].required = True

    class Meta:
        model = Request
        fields = ['status', 'security_notes']


class RequestForm(forms.ModelForm):
    approved_by_legal = forms.ChoiceField(widget=forms.Select(), choices=[('', '---'), (True, 'Yes'), (False, 'No'), ],
                                          required=True
                                          , initial=None, label='Has this been approved by legal?')
    free = forms.ChoiceField(widget=forms.Select(), choices=[('', '---'), (True, 'Yes'), (False, 'No'), ], required=True
                             , initial=None, label='Is it free?')
    group_licensing = forms.ChoiceField(widget=forms.Select(), choices=[('', '---'), (True, 'Yes'), (False, 'No'), ],
                                        required=False
                                        , initial=None, label='If it is not free, is it available for group licensing?')
    PHI = forms.ChoiceField(widget=forms.Select(), choices=[('', '---'), (True, 'Yes'), (False, 'No'), ], required=True
                            , initial=None, label='Will any Protected Health Information (PHI) be stored?')
    PII = forms.ChoiceField(widget=forms.Select(), choices=[('', '---'), (True, 'Yes'), (False, 'No'), ], required=True
                            , initial=None, label='Will any Personally Identifiable Information (PII) be stored?')
    PCI = forms.ChoiceField(widget=forms.Select(), choices=[('', '---'), (True, 'Yes'), (False, 'No'), ], required=True
                            , initial=None, label='Will any Payment Card Industry Information (PCI) be stored?')
    contract_exists = forms.ChoiceField(widget=forms.Select(), choices=[('', '---'), (True, 'Yes'), (False, 'No'), ],
                                        required=True
                                        , initial=None, label='Is there a signed contract with a third party?')
    BAA_exists = forms.ChoiceField(widget=forms.Select(), choices=[('', '---'), (True, 'Yes'), (False, 'No'), ],
                                   required=True
                                   , initial=None, label='Is there a signed Business Associate Agreement (BAA)?')
    external_access_required = forms.ChoiceField(widget=forms.Select(),
                                                 choices=[('', '---'), (True, 'Yes'), (False, 'No'), ], required=True
                                                 , initial=None, label='Will there be a need for external access to'
                                                                       ' AAH systems?')
    external_services = forms.CharField(widget=forms.Textarea(), required=True,
                                        label='Does the app rely on external services or servers?'
                                              ' (i.e Email, cloud, etc) If so, please explain')
    other_applications = forms.CharField(widget=forms.Textarea(), required=True,
                                         label='Will the app need to interface with other applications or '
                                               '              services on the device? '
                                               '(i.e. Email, Camera, Photos, etc.) If so, please explain')
    notes = forms.CharField(widget=forms.Textarea(), required=False, label="Additional Notes")
    security_notes = forms.CharField(widget=forms.Textarea(), required=False, label="Security Notes")
    contract = forms.FileField(required=False,
                               label='If so please attach the contract: (selected files will not appear here, but will be uploaded on submission)')
    BAA = forms.FileField(required=False,
                          label='If so please attach the BAA: (selected files will not appear here, but will be uploaded on submission)')
    access_forms = forms.FileField(
        label='If so, please attach the pertinent completed access forms: (selected files will not appear here, but will be uploaded on submission)',
        required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['second_URL'].required = False
        self.fields['security_notes'].disabled = True
        self.fields['status'].disabled = True



    class Meta:
        model = Request
        fields = ['app_name', 'URL', 'second_URL', 'description', 'approved_by_legal',
                  'free', 'group_licensing', 'PHI', 'PII', 'PCI', 'contract_exists', 'contract', 'BAA_exists', 'BAA',
                  'external_access_required', 'access_forms', 'OS_version',
                  'device', 'min_OS_version', 'latest_release_date', 'external_services', 'other_applications',
                  'notes', 'status', 'security_notes']


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field('username', label="Username: "),
            Field('password', label="Password: ", ),
            ButtonHolder(
                Submit('login', 'Login', css_class='btn-primary'),
            ),
        )


class PasswordChangeForm(auth_forms.PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super(PasswordChangeForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.layout = Layout(
            Div(Field('old_password', autoFocus="autofocus"), 'new_password1', 'new_password2'),
            ButtonHolder(Submit('save', _('Change password'), css_class='btn-primary'))
        )
