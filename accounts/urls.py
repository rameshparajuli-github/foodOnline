from . import views
from django.urls import path

app_name = 'accounts'
urlpatterns = [
    path('registerUser/', views.registerUser, name='registerUser' )
]
