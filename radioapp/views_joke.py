from django.shortcuts import render

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Joke, Topic


class JokeListView(ListView):
    model = Joke
    template_name = 'joke/joke_list.html'
    context_object_name = 'jokes'
    ordering = ['-id']

class JokeDetailView(DetailView):
    model = Joke
    template_name = 'joke/joke_detail.html'

class JokeCreateView(CreateView):
    model = Joke
    template_name = 'joke_form.html'
    fields = ['question', 'answer', 'topic']
    success_url = reverse_lazy('joke-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['topics'] = Topic.objects.all()  # Retrieve all topics
        return context

class JokeUpdateView(UpdateView):
    model = Joke
    template_name = 'joke/joke_form.html'
    fields = ['question', 'answer', 'topic']  # Include the 'topic' field
    success_url = reverse_lazy('joke-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['topics'] = Topic.objects.all()
        return context

class JokeDeleteView(DeleteView):
    model = Joke
    template_name = 'joke/joke_confirm_delete.html'
    success_url = reverse_lazy('joke-list')
