from django.urls import path
from .views import details  , products
urlpatterns = [
    path('', products , name='products'),
    path('<int:product_id>', details, name='details'),

] 