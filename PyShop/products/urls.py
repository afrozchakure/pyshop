from django.urls import path
from . import views  # Import the views module into urls module  (.) means current folder

# /products
# /products/1/detail
# /products/new
urlpatterns = [
    path('', views.index),  # Here the path is the root (we are not calling the function, just passing the reference to it)
    path('new', views.new)
]
