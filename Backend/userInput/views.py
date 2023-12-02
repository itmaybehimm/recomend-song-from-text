from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
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