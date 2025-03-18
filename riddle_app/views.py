from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from .models import Riddle
from .forms import NewRiddleForm, GuessRiddleForm

def index(request):
    random_riddle = Riddle.objects.order_by('?')[0]

    params = {
        "random_riddle": random_riddle
    }
    
    response = render(request, 'riddle_app/index.html', params)
    return response

def new_riddle(request):
    if request.method == "POST":
        form = NewRiddleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("riddle_app:index"))
    else:
        form = NewRiddleForm()

    params = {
        "form": form
    }
    
    return render(request, "riddle_app/new_riddle_form.html", params)

def guess_riddle(request, pk):

    riddle = Riddle.objects.get(id = pk)

    params = {
        'riddle': riddle
    }

    if request.method == "POST":
        form = GuessRiddleForm(request.POST)
        if form.is_valid():
            form_cleaned = form.cleaned_data 
            user_guess = form_cleaned['guess']

            if riddle.check_guess(user_guess) == True:
                params['message'] = 'Correct'   

            else:
                params['message'] = 'Incorrect'
            
    else:
        form = GuessRiddleForm()
    
    
    params['form'] = form

    return render(request, "riddle_app/guess_riddle.html", params)

