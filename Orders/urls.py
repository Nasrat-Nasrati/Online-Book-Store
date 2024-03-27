from django.urls import path
from.import views

urlpatterns=[
    path('',views.index_order_management,name='index_order_management')
]