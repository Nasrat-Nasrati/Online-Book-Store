from django.shortcuts import render


from django.http import HttpResponse

from .models import BookCategory

def index_book_category(request):
   BookCategories = BookCategory.objects
   return render(request, 'index_book_category.html',{'BookCategories':BookCategories})

