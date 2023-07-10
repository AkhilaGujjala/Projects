from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import mysql.connector
#from .models import Book

@csrf_exempt
def SearchPage(request):
    if request.method == 'POST':
        # Handle the POST request and perform the search logic
        search_term = request.POST.get('search')

        # Perform the search logic
        results = []

        # Convert results to JSON
        data = []
        for book in results:
            data.append({
                'id': book.id,
                'title': book.title,
                'author': book.author,
                # Add more fields as needed
            })

        return JsonResponse(data, safe=False)

    return render(request, 'search_page.html')

# Create your views here.
