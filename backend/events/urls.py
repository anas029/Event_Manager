from django.urls import path
from .import views 

urlpatterns = [
    path('events/',views.EventListCreate.as_view(),name='event_list_create'),
    path('event/<int:pk>/',views.EventRetrieveUpdateDestroy.as_view(),name='event_detail'),
]
