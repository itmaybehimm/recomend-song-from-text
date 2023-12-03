from django.shortcuts import render, redirect
from django.http import HttpResponse
from .utils.spotify_integration import main_function

def home(request):
    return render(request, 'index.html')

def process(request):
    if request.method == 'POST':
        text_input = request.POST.get('textPrompt', '')

        file = request.FILES.get('fileInput')

        #process here
        
    
        #just printt
        print('Text Input:', text_input)
        print('File:', file)

    return HttpResponse("Successs")

def integrate_spotify(request, username, mood):
    mood = float(mood)
    main_function(username, mood)  
    return HttpResponse("Spotify integration complete!")


