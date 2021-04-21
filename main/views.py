from django.shortcuts import render
from .models import Recipe
# Create your views here.
def home(request):
	total_recipes = Recipe.objects.all().count()
	context = {
	'title': 'Homepage',
	'total_recipes': total_recipes,
	}
	return render(request, 'home.html', context)