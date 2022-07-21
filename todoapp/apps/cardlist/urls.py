from django.urls import path
from todoapp.apps.cardlist import views

urlpatterns = [

    path('card/', views.CardViewSet.as_view(
        {'get': 'list',
         'post': 'create'},
    ), name='card'),
    path('card/<int:pk>/', views.CardViewSet.as_view({
            'get': 'retrieve',
            'put': 'partial_update',
            'delete': 'destroy'
         }),
         name='card'),
    path('card_admin/', views.CardAdminViewSet.as_view(
        {'get': 'list'},
    ), name='card_admin'),
]