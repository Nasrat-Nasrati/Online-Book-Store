from django.urls import path
from.import views
from .views import search_books

urlpatterns=[
     path('search/', search_books, name='search_books'),

     
    path('',views.index_of_book,name='index_of_book')
    
]