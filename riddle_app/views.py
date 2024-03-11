from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import FormView, ListView, DetailView, TemplateView
from django.urls import reverse_lazy
from django.http import HttpResponse
from .models import Riddle
from .forms import NewRiddleForm, GuessRiddleForm

class RiddleListView(ListView):
    model = Riddle
    template_name = "riddle_app/riddle_list.html"

    queryset = Riddle.objects.all()

class RiddleDetailView(DetailView):
    model = Riddle
    template_name = "riddle_app/riddle_detail.html"

class NewRiddleForm(FormView):
    template_name = "riddle_app/new_riddle_form.html"
    form_class = NewRiddleForm
    success_url = reverse_lazy('index')


    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


def riddle_like(request, pk):
    riddle = Riddle.objects.get(id=pk)
    riddle.increase_likes()

    return HttpResponseRedirect(reverse_lazy('riddle_app:riddle-detail', args=[str(pk)]))


def guess_riddle(request,pk):
    riddle = Riddle.objects.get(id=pk)

    if request.method == 'POST':

        context = {
            'riddle': riddle,
            'message': '',
            'pk': riddle.id
            }

        form = GuessRiddleForm(request.POST)

        if form.is_valid():
            form_cleaned= form.cleaned_data
            
            if form_cleaned['guess'] == riddle.answer:
                context['message'] = 'Correct'
            else:
                context['message'] = 'False'

            return render(request, 'riddle_app/riddle_guess.html', context)

    else:
        context = {
            'riddle': riddle,
            'form': GuessRiddleForm()
            }
        
        return render(request, 'riddle_app/riddle_guess.html', context)