from django.urls import path
from . import views

urlpatterns = [
    path('category/', views.get_category, name='category'),
    path('submit-joke', views.submit_joke, name='submit_joke'),
    path('get/<category>', views.get_joke, name='joke'),
]
