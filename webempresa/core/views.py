from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    #return HttpResponse('home')
    return render(request,'core/home.html') #se retorna o renderiza el requeste junto a la vista

def about(request):
    return render(request, 'core/about.html')

def store(request):
    return render(request, 'core/store.html')