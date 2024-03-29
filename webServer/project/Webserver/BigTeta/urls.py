from django.urls import path
from . import views
from . import api

app_name = 'BigTeta'
urlpatterns = [
    path('', views.showFiles, name='showVideos'),
    path('home', views.index, name='home'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout_user, name='logout'),
    path('show', views.show_video, name='showVideo'),
    path('showFiles', views.showFiles, name='showFiles'),
    path('upload', views.upload, name='upload'),
    path('update', views.update_video, name='update'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('getvideos', api.get_video_by_title, name='getVideos'),
    path('delete/<int:id>',views.deletevideo,name="delete"),
    path('getdependencies', api.get_dependecies_from_video_id, name='getdependencies'),
    path('getvotes', api.get_votes_from_video_id, name='getvotes'),
    path('postvote', api.post_vote, name='postvote'),
]
