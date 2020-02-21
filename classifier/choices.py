from .models import City, Category

def cities():
	return City.objects.all()

#CITIES = (city for city in Cities())

def categories():
	#return Category.objects.all()
	result = []
	others = []
	for cat in Category.objects.filter(parent_cat__isnull=True):
		if cat.slug == 'others':
			others.append(cat)
			others.extend(Category.objects.filter(parent_cat=cat.pk))
			continue
		result.append(cat)
		result.extend(Category.objects.filter(parent_cat=cat.pk))

	result.extend(others)
	return result
#CATEGORIES = (cat for cat in Categories())
