from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

def index (request):
    return render(request,'words/index.html')


def submit(request):
    new_word = {}
    for
    if request.method == "POST":
        if 'words' not in request.session:
            request.session['word'] = request.POST['word']
            request.session['color'] = request.POST['color']
            if request.POST['BOLD'] == "on":
                request.session['BOLD'] = "bold"
            else:
                request.session['BOLD'] = "normal"
            return render(request,'words/index.html')
