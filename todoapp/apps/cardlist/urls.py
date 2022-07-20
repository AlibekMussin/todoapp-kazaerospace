from django.urls import path
from todoapp.apps.cardlist import views

urlpatterns = [

    path('card/', views.CardViewSet.as_view(
        {'get': 'list',
         'post': 'create'},
    ),
         name='card'),
]