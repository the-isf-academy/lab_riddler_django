from django.urls import path

from riddle_app import views

app_name = "riddle_app"

urlpatterns = [
    path('', views.index ,name='index'),
    path('new/', views.new_riddle, name='new'),
    path('guess/<int:pk>', views.guess_riddle, name='guess'),
]





