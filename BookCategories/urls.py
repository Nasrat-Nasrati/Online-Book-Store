from django.urls import path
from.import views

urlpatterns=[
    path('',views.index_book_category,name='index_book_category')
    
]