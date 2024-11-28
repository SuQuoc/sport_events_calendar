"""
URL configuration for sport_calendar project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
from django.core.management import call_command
from events.views import home, list_models, add_model, edit_model, delete_model

urlpatterns = [
    path('admin/', admin.site.urls),
    path('events/', include('events.urls')),
    # path('', include('events.urls')),
    path('', home, name='home'),

    path('<str:model_name>/list', list_models, name='list_models'),
    path('<str:model_name>/add', add_model, name='add_model'),
    path('<str:model_name>/edit/<int:model_id>', edit_model, name='edit_model'),
    path('<str:model_name>/delete/<int:model_id>', delete_model, name='delete_model'),
]


