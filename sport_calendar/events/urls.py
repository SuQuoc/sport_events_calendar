from django.urls import path
from . import views

urlpatterns = [
    # path('', views.home, name='home'),
    path('', views.events, name='events'),
    path('add', views.add_event, name='add_event'),
    path('edit/<int:event_id>', views.edit_event, name='edit_event'),
    path('delete/<int:event_id>', views.delete_event, name='delete_event'),

    path('<str:model_name>/add', views.add_model, name='add_model'),
]
