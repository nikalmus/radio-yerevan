"""
URL configuration for radio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from radioapp import views

app_name = 'radioapp'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('topics/', views.TopicListView.as_view(), name='topic-list'),
    path('topics/<int:pk>/', views.TopicDetailView.as_view(), name='topic-detail'),
    path('topics/create/', views.TopicCreateView.as_view(), name='topic-create'),
    path('topics/<int:pk>/update/', views.TopicUpdateView.as_view(), name='topic-update'),
    path('topics/<int:pk>/delete/', views.TopicDeleteView.as_view(), name='topic-delete'),

    path('jokes/', views.JokeListView.as_view(), name='joke-list'),
    path('jokes/<int:pk>/', views.JokeDetailView.as_view(), name='joke-detail'),
    path('jokes/create/', views.JokeCreateView.as_view(), name='joke-create'),
    path('jokes/<int:pk>/update/', views.JokeUpdateView.as_view(), name='joke-update'),
    path('jokes/<int:pk>/delete/', views.JokeDeleteView.as_view(), name='joke-delete'),
]
