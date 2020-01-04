from django.shortcuts import render

# Create your views here.
def bookmarks_list(request):
    return render(request, 'bookmarks/bookmarks.html')