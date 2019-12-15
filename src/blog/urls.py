from django.urls import path 
from .views import blog , post , comment

urlpatterns = [
	path('', blog , name='blog'),
	path('<int:post_id>', post, name='post'),
	path('comment', comment, name='comment')
]