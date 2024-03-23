from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.index, name='index'),
    path('home/',views.home, name = 'home'),
    path('search/',views.search, name= 'search'),
    path('create/',views.create, name = 'create'),
    
]
