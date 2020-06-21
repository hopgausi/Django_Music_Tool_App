from django.urls import path
from  . import views

urlpatterns = [
    path('', views.home, name='lyrics-home'),
    path('lyrics/', views.get_lyrics, name='lyrics-get-lyrics'),
    path('artist', views.lyrics, name='lyrics-lyrics'),
]