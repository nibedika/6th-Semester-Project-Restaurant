from django.urls import path
from apps.backend_apps.food import views
 
urlpatterns = [
    path('add-food/', views.Food.add_food, name='add_food'),
    path('all-food/', views.Food.all_food, name='all_food'),
    path('edit-food/<id>/', views.Food.edit_food, name='edit_food'),
    path('delete-food/<id>/', views.Food.delete_food, name='delete_food'),
]