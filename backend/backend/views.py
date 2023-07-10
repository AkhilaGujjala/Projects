from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import mysql.connector

@csrf_exempt
def search_page(request):
    if request.method == 'GET':
        search_term = request.GET.get('searchTerm','')

        # Establish database connection
        db = mysql.connector.connect(host="localhost", user="root", password="", database="library_book_search")
        cursor = db.cursor()

        # Execute the query
        query = f"SELECT * FROM books_books WHERE title LIKE '%{search_term}%' OR author LIKE '%{search_term}%'"
        cursor.execute(query)

        # Fetch all the rows
        rows = cursor.fetchall()

        # Prepare the data
        search_result = []
        for row in rows:
            search_result.append({
                'id': row[0],
                'title': row[1],
                'author': row[2],
                # Add more fields as needed
            })
        #print(search_result)
        # Close database connection
        cursor.close()
        db.close()

        return render(request, 'search_page.html', {'search_results':  search_result, 'search_term':search_term},)
        #context={{'search_results': search_result}, {'search_term': search_term}}
        #return JsonResponse(context, safe=False)
    return render(request, 'search_page.html')
