from django.contrib import admin
from django.urls import path, include
from home import views

admin.site.site_header = "DATABASE"
admin.site.site_title = "Only Praneeth has the access"
admin.site.index_title = "Welcome Praneeth!!!"


urlpatterns = [
   path('', views.home, name='home'),
   path('attendance', views.attendance, name='attendance'),
   path('storage', views.store, name='storage'),
   path('register', views.register, name='register'),
   path('absenties', views.absenties, name='absenties'),
   path('absentrecord', views.absentrecord, name='absentrecord')
]