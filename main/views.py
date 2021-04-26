from django.shortcuts import render
from .models import Recipe
from django.db.models import Q
from django.core.paginator import PageNotAnInteger, Paginator, EmptyPage


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
		topic = 'breakfast'

	elif request.GET.get('appetizers'):
		# filter results by category selected by user
		results = queryset.filter(Q(topic__title__icontains='appetizers'))
		topic = 'appetizers'

	elif request.GET.get('lunch'):
		# filter results by category selected by user
		results = queryset.filter(Q(topic__title__icontains='lunch'))
		topic = 'lunch'

	elif request.GET.get('salads'):
		# filter results by category selected by user
		results = queryset.filter(Q(topic__title__icontains='salads'))
		topic = 'salads'

	elif request.GET.get('dinner'):
		# filter results by category selected by user
		results = queryset.filter(Q(topic__title__icontains='dinner'))
		topic = 'dinner'

	elif request.GET.get('dessert'):
		# filter results by category selected by user
		results = queryset.filter(Q(topic__title__icontains='dessert'))
		topic = 'dessert'

	elif request.GET.get('easy'):
		# filter results by category selected by user
		results = queryset.filter(Q(topic__title__icontains='easy'))
		topic = 'easy'

	elif request.GET.get('hard'):
		# filter results by category selected by user
		results = queryset.filter(Q(topic__title__icontains='hard'))
		topic = 'hard'

	total = results.count()

	# paginate result
	# define paginator object
	paginator = Paginator(results, 3)

	# get number of the curent page
	page = request.GET.get('page')

	# create results page object
	try:
		results = paginator.page(page)
	except PageNotAnInteger:
		# display first page
		results = paginator.page(1)
	except EmptyPage:
		# display last page
		results = paginator.page(paginator.num_pages)

	context = {
	'topic': topic,
	'page': page,
	'total': total,
	'query': query,
	'results': results,

	}
	return render(request, 'search.html', context)

def detail(request, slug):
	return render(request, 'detail.html', {})