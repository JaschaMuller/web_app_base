"""web_app_base URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path

from django.conf.urls import url
import django.contrib.auth.views

from geo_app.models import WaterConsumption

import geo_app.views
#from geo_app.views import waterconsumption_dataset, top10_consumers


urlpatterns = [
    url(r'^$', geo_app.views.home, name='home'),
    #url(r'^waterconsumption_data/$', waterconsumption_dataset, name='waterconsumption'),
    #url(r'^top10_consumers/$', top10_consumers, name='top10consumers'),
    path('admin/', admin.site.urls),
]
