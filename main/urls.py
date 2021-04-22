from django.urls import path
from .views import home, search, detail


# url for the home page first, create a view for it 
urlpatterns = [
	path('', home, name='home'),
	path('search', search, name='search'),
	path('<slug>', detail, name='detail'),
]