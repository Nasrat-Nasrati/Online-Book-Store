from django.shortcuts import render
from django.http import HttpResponse
from .models import Book

from django.db.models import Q  # Import Q object

def search_books(request):
    query = request.GET.get('query')
    if query:
        # Perform search query using Q objects
        results = Book.objects.filter(
            Q(title__icontains=query) |
            Q(isbn__icontains=query) |
            Q(category__name__icontains=query)
        )
    else:
        results = Book.objects.all()

    return render(request, 'search_results.html', {'results': results, 'query': query})



def index_of_book(request):
    # return HttpResponse("Dear viewer welecome to the page of Book")

    # this command will redirect the index html
    Books=Book.objects
    return render(request,'index_of_book.html',{'Books':Books})
