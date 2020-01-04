from django.shortcuts import render

# Create your views here.
def friends_list(request):
    return render(request, 'friends/friends.html')