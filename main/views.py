from django.shortcuts import render
from .models import Recipe
from django.db.models import Q
# Create your views here.
def home(request):
	total_recipes = Recipe.objects.all().count()
	context = {
	'title': 'Homepage',
	'total_recipes': total_recipes,
	}
	return render(request, 'home.html', context)


def search(request):
	recipes = Recipe.objects.all()

	# search?breakfast=on&search=Cookies

	if 'search' in request.GET:
		# we need to get the object the user is searching for
		query = request.GET.get('search')
		# filter recipes by title that contains query
		queryset = recipes.filter(Q(title__icontains=query))

	if request.GET.get('breakfast'):
		# filter results by category selected by user
		results = queryset.filter(Q(topic__title__icontains='breakfast'))

		print('\n\n\n')
		print(results)

	context = {
	'total': results.count(),
	'query': query,
	'results': results,

	}
	return render(request, 'search.html', context)

def detail(request, slug):
	return render(request, 'detail.html', {})