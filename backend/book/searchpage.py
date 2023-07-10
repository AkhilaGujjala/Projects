from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import mysql.connector
#from .models import Book

@csrf_exempt
def SearchPage(request):
    if request.method == 'POST':
        search_term = request.POST.get('search')
        
        # Establish database connection
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="library_book_search"
        )
        
        # Execute the query
        cursor = db.cursor()
        query = f"SELECT * FROM books_books WHERE title LIKE '%{search_term}%'"
        cursor.execute(query)
        results = cursor.fetchall()
        
        # Convert results to JSON
        data = []
        for row in results:
            data.append({
                'id': row[0],
                'title': row[1],
                'author': row[2],
                # Add more fields as needed
            })
        
        # Close database connection
        cursor.close()
        db.close()
        
        return JsonResponse(data, safe=False)

    return render(request, 'search_page.html')
