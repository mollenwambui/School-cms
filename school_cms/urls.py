"""
URL configuration for school_cms project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
# from django.contrib import admin
# from django.urls import path

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]
# from django.urls import path
# from school import views

# # urlpatterns = [
# #     path('attendance/mark/', views.mark_attendance, name='mark_attendance'),
# #     path('attendance/view/', views.view_attendance, name='view_attendance'),
# ]

from django.contrib import admin
from django.urls import path
from school import views  # <-- make sure you import this

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # <-- home page
    path('attendance/mark/', views.mark_attendance, name='mark_attendance'),
    path('attendance/view/', views.view_attendance, name='view_attendance'),
]
