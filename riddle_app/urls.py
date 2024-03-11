from django.urls import path

from .views import  NewRiddleForm, RiddleListView, RiddleDetailView, riddle_like, guess_riddle

app_name = "riddle_app"

urlpatterns = [
    path('', RiddleListView.as_view(),name='index'),
    path('riddle/new', NewRiddleForm.as_view(),name='riddle-new'),
    path('riddle/detail/<int:pk>/', RiddleDetailView.as_view(), name='riddle-detail'),
    path('riddle/like/<int:pk>/', riddle_like, name="riddle-like"),
    path('riddle/guess/<int:pk>/', guess_riddle, name="riddle-guess"),
]