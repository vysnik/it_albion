"""m3_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls import url
from django.shortcuts import render

from m3 import get_app_urlpatterns

def workspace(request):
	"""
	Возвращает view для отображения Рабочего Стола на
	основе шаблона m3
	"""
	return render(
    	    request,
    	    'm3_workspace.html',
    	    context={'debug': settings.DEBUG},
	)


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', workspace),
]

# Собираем шаблоны урлов из app_meta
# подключенных приложений
urlpatterns.extend(get_app_urlpatterns())
