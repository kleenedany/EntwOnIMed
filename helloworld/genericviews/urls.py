from django.urls import path

from . import views

app_name = 'genericviews'
urlpatterns = [
     path('', views.IndexView.as_view(), name='index'),
     path('<int:pk>', views.DetailView.as_view(), name='detail'),
     path('form/', views.CreatePersonView.as_view(), name='createperson'),
     path('<int:pk>/delete/', views.DeletePersonView.as_view(), name='delete'),
     path('<int:pk>/update/', views.UpdatePersonView.as_view(), name='update'),
]