from django.shortcuts import render,HttpResponse
from .models import Anime
# Create your views here.

def index(request):
    return HttpResponse('<p>Hi TEST</p>')


def home(request):
    # anime = Anime.objects.create(anime_name = 'One Piece', anime_episodes = 1111)
    anime_view = Anime.objects.get(id =1)

    context = {
        'anime_view' : anime_view
    }
    
    return render(request,'app_22/home.html',context)


def search(request):
    query_dict = request.GET
    print('Query Dict ---> ',query_dict)
    
    try:
        query =int( query_dict.get('name'))
    except:
        query = None
    data = None
    if query is not None:
        data = Anime.objects.get(id = query)
        context = {
            'data': data
        }
        return render(request,'app_22/search.html',context)
    else:
        return render(request,'app_22/home.html')
    
    
def create(request):
    context= {}
    print(request.POST)
    if request.method == 'POST':
        name = request.POST.get('name')
        number = request.POST.get('number')
        object = Anime.objects.create(anime_name = name,anime_episodes = number)
        context['object'] = object
        context['created'] = True
        
    return render(request,'app_22/create.html',context)