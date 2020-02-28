"""Capstone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from intakeReview import views
from intakeReview.views import LoginView, LogOutView

urlpatterns = [
    path('admin/', admin.site.urls),
    # url('^$', include('django.contrib.auth.urls')),
    path('home/', views.HomeView.as_view(), name='home'),
    path('register/', views.SignUp.as_view(), name='signup'),
    path('', LoginView.as_view(), name='login'),
    path('logout/', LogOutView.as_view(), name='logout'),
    path('change_password/', views.ChangePassword.as_view(), name='change_password'),
    path('request/', views.Request.as_view(), name='request'),
    path('help/', views.Help.as_view(), name='help'),
    path('allRequests/', views.AllRequestsView.as_view(), name='all_requests'),
    url(r'^viewRequest/(?P<pk>\d+)/$', views.BoundRequestView.as_view(), name='bound_request'),
    url(r'^editRequest/(?P<pk>\d+)/$', views.EditRequestView.as_view(), name='edit_request'),
    url(r'^reviewRequest/(?P<pk>\d+)/$', views.ReviewRequestView.as_view(), name='review_request'),
    url(r'^relatedAttachments/(?P<pk>\d+)/$', views.RelatedAttachmentsView.as_view(), name='attachments')


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = 'Mobile App Intake Review'