from django.urls import path
from . import views

app_name = __package__
urlpatterns = [
	path('', views.home, name='home'),
	path('search/', views.search, name='search'),
	path('<slug:city>/<slug:category>/<int:post_id>/<str:title>', views.show_post)
]