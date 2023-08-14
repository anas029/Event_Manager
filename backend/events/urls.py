from django.urls import path
from .import views 

urlpatterns = [
    path('events/',views.EventListCreate.as_view(),name='event_list_create'),
    path('event/<int:pk>/',views.EventRetrieveUpdateDestroy.as_view(),name='event_detail'),
    path('venues/',views.VenueListCreate.as_view(),name='venue_list_create'),
    path('venue/<int:pk>/',views.VenueRetrieveUpdateDestroy.as_view(),name='venue_detail'),
]
