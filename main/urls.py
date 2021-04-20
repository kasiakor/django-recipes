from django.urls import path
from .views import home

# url for the home page first, create a view for it 
urlpatterns = [
	path('', home, name='home'),
]