from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category
from rango.models import Page
from rango.forms import CategoryForm


def index(request):
	category_list = Category.objects.order_by('-likes') [:5]
	page_list = Page.objects.order_by('-views') [:5]
	context_dict = {'categories': category_list, 'pages': page_list}
	return 	render(request, 'rango/index.html', context=context_dict)

def about(request):
	context_dict = {'boldmessage': "About Page"}
	return render(request, 'rango/about.html', context=context_dict)
	return HttpResponse("rango says here is the about page")

def show_category(request, category_name_slug):
	context_dict = {}

	try:
		category = Category.objects.get(slug=category_name_slug)
		pages = Page.objects.filter(category=category)
		context_dict['pages'] = pages
		context_dict['category'] = category
	except Category.DoesNotExist:
		context_dict['category'] = None
		context_dict['pages'] = None
	return render(request, 'rango/category.html', context_dict)

def add_category(request):
		form = CategoryForm()
		if request.method == 'POST':
        		form = CategoryForm(request.POST)
        # Have we been provided with a valid form?
        	if form.is_valid():
            # Save the new category to the database.
            		form.save(commit=True)
            # Now that the category is saved
            # We could give a confirmation message
            # But since the most recent category added is on the index page
            # Then we can direct the user back to the index page.
            		return index(request)
        	else:
				print(form.errors)
		return render(request, 'rango/add_category.html', {'form': form})
