from datetime import datetime

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View, generic

from users.forms import CustomUserCreationForm
from .forms import LoginForm, PasswordChangeForm
from .forms import RequestForm, ReviewForm, ViewForm, AttachmentsForm
from .models import Request as RequestModel


# Create your views here.


# need to make home view and pass in all requests
class HomeView(View):
    def get(self, request):
        if (request.user.is_authenticated):
            requests = RequestModel.objects.filter(requested_by=request.user)
            return render(request, 'home.html', {'requests': requests})
        return render(request, 'home.html')


class AllRequestsView(View):
    def get(self, request):
        if (request.user.is_authenticated):
            requests = RequestModel.objects.all()
            return render(request, 'all_requests.html', {'requests': requests})
        return render(request, 'all_requests.html')


class BoundRequestView(View):
    def get(self, request, pk):
        bound_request = RequestModel.objects.get(pk=pk)
        bound_form = ViewForm(instance=bound_request)
        return render(request, 'bound_request.html', {'form': bound_form, 'pk':pk, 'requestObject':bound_request})


class EditRequestView(View):
    def get(self, request, pk):
        bound_request = RequestModel.objects.get(pk=pk)
        bound_form = RequestForm(instance=bound_request)
        return render(request, 'request.html', {'form': bound_form, 'edit':True , 'pk':pk})

    def post(self, request, pk):
        bound_request = RequestModel.objects.get(pk=pk)
        form = RequestForm(request.POST, request.FILES, instance=bound_request)

        if form.is_valid():
            form.save()

        bound_form = RequestForm(instance=bound_request)
        return render(request, 'request.html', {'form': bound_form, 'edit':True, 'pk':pk})

class RelatedAttachmentsView(View):
    def get(self, request, pk):
        bound_request = RequestModel.objects.get(pk=pk)
        bound_form = AttachmentsForm(instance=bound_request)
        mine = False
        if bound_request.requested_by == request.user:
            mine = True
        return render(request, 'attachments.html', {'requestform': bound_form, 'mine':mine})
    def post(self, request, pk):
        bound_request = RequestModel.objects.get(pk=pk)
        form = AttachmentsForm(request.POST, request.FILES, instance=bound_request)
        bound_form = AttachmentsForm(instance=bound_request)
        mine = False
        if bound_request.requested_by is request.user:
            mine = True
        if(form.is_valid()):
            bound_request.save()
            form = AttachmentsForm(instance=bound_request)
        return render(request, 'attachments.html', {'requestform': form, 'mine':mine})

class ReviewRequestView(View):
    def get(self, request, pk):
        bound_request = RequestModel.objects.get(pk=pk)
        bound_form = ReviewForm(instance=bound_request)
        return render(request, 'request.html', {'form': bound_form, 'review':True})

    def post(self, request, pk):
        bound_request = RequestModel.objects.get(pk=pk)
        form = ReviewForm(request.POST, instance=bound_request)
        if form.is_valid():
            form.save()
        requests = RequestModel.objects.all()
        return render(request, 'all_requests.html', {'requests': requests})

class ChangePassword(View):
    def post(self, request):
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('home')
        return render(request, 'accounts/change_password.html', {'form': form})

    def get(self, request):
        form = PasswordChangeForm(request.user)
        return render(request, 'accounts/change_password.html', {'form': form})


class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'


class Request(View):
    def get(self, request):
        form = RequestForm()
        return render(request, 'request.html', {'form': form})

    def post(self, request):
        form = RequestForm(request.POST, request.FILES)


        if form.is_valid():

            new_request = RequestModel.objects.create(
                requested_by=request.user,
                app_name=form.cleaned_data['app_name'],
                URL=form.cleaned_data['URL'],
                second_URL=form.cleaned_data['second_URL'],
                description=form.cleaned_data['description'],
                approved_by_legal=form.cleaned_data['approved_by_legal'],
                free=form.cleaned_data['free'],
                group_licensing=form.cleaned_data['group_licensing'],
                PHI=form.cleaned_data['PHI'],
                PII=form.cleaned_data['PII'],
                PCI=form.cleaned_data['PCI'],
                contract_exists=form.cleaned_data['contract_exists'],
                contract = form.cleaned_data['contract'],
                BAA_exists=form.cleaned_data['BAA_exists'],
                BAA=form.cleaned_data['BAA'],
                external_access_required=form.cleaned_data['external_access_required'],
                external_services=form.cleaned_data['external_services'],
                access_forms = form.cleaned_data['access_forms'],
                other_applications=form.cleaned_data['other_applications'],
                OS_version=form.cleaned_data['OS_version'],
                device=form.cleaned_data['device'],
                min_OS_version=form.cleaned_data['min_OS_version'],
                latest_release_date=form.cleaned_data['latest_release_date'],
                notes=form.cleaned_data['notes'],
                security_notes=form.cleaned_data['security_notes'],
                status=1,
                time_submitted=datetime.now()
                # time_reviewed=
            )
            new_request.save()
            requests = RequestModel.objects.filter(requested_by=request.user)
            return render(request, 'home.html', {'requests': requests})
        else:
            return render(request, 'request.html', {'form': form})


class Help(View):
    def get(self, request):
        return render(request, 'help.html')


class LoginView(generic.FormView):
    form_class = LoginForm
    success_url = reverse_lazy('home')
    template_name = 'accounts/login.html'

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)

        if user is not None and user.is_active:
            login(self.request, user)
            return super(LoginView, self).form_valid(form)
        else:
            return self.form_invalid(form)


class LogOutView(generic.RedirectView):
    url = reverse_lazy('login')

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(LogOutView, self).get(request, *args, **kwargs)
