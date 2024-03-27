from django.urls import path
from.import views

urlpatterns=[
    path('',views.index_of_carts,name='index_of_carts')
]