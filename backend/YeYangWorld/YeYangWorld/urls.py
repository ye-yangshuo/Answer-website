"""
URL configuration for YeYangWorld project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from django.urls import path
from django.contrib import admin

from userApp.views import login_verify , send_code , register_verify, user_verify

from datiApp.views import get_problem,submit_problem
urlpatterns = [
    path('admin/', admin.site.urls),

    path('user/login_verify/',login_verify, name='login_verify'),

    path('user/send_code/',send_code, name='send_code'),

    path('user/register_verify/',register_verify, name='register_verify'),

    path('user/user_verify/',user_verify, name='user_verify'),

    path('dati/get_problem/',get_problem, name='get_problem'),

    path('dati/submit_problem/',submit_problem, name='submit_problem')
]
