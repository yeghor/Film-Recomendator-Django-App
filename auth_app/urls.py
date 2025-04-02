from django.urls import include, path
from . import views

app_name = 'auth'
urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
]