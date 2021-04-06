from django.urls import path
from .views import *


app_name = 'accounts'


urlpatterns = [
	path('register/', registerview, name='register'),
	path('login/', loginview, name='login'),
	path('logout/', logoutview, name='logout'),
]