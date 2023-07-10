from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import mysql.connector

@csrf_exempt
def SearchPage(request):
    if request.method == 'POST':
        # Establish database connection
        db = mysql.connector.connect(host="localhost", user="root", password="", database="library_book_search")
        cursor = db.cursor()
        
        # Execute the query
        query = "SELECT * FROM books_books WHERE title LIKE '%oracle%'"
        cursor.execute(query)
        
        # Fetch all the rows
        rows = cursor.fetchall()
        
        # Prepare the data
        data = []
        for row in rows:
            data.append({
                'id': row[0],
                'title': row[1],
                'author': row[2],
                # Add more fields as needed
            })
        
        # Close database connection
        cursor.close()
        db.close()
        
        return render(request, 'search_page.html', {'search_results': data})

    return render(request, 'search_page.html')
