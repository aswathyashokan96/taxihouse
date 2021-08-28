"""taxihouse URL Configuration

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
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from adminapp.views import *
from employeeapp.views import *
from publicapp.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'registration/$',registration,name='registration'),
    url(r'home/$',home,name='home'),
    url(r'add_item/$',add_item,name='add_item'),
    url(r'view_item/$',view_item,name='view_item'),
    url(r"edit_item/(?P<itemid>[0-9]+)",edit_item,name='edit_item'),
    url(r"delete_item/(?P<itemid>[0-9]+)",delete_item,name='delete_item'),
    url(r'logout/$',logout,name='logout'),
    url(r'admin_profile/$',admin_profile,name='admin_profile'),
    url(r'booking_item/(?P<itemid>[0-9]+)',booking_item,name='booking_item'),
    url(r'delever_item/(?P<itemid>[0-9]+)',delever_item,name='delever_item'),
    url(r'employee_profile/$',employee_profile,name='employee_profile'),
    url(r'view_available_items/$',view_available_items,name="view_available_items")
]

urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
