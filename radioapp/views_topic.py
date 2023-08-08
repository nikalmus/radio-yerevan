from django.shortcuts import render

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Topic

class TopicListView(ListView):
    model = Topic
    template_name = 'topic_list.html'
    context_object_name = 'topics'
    ordering = ['-id']

class TopicDetailView(DetailView):
    model = Topic
    template_name = 'topic_detail.html'

class TopicCreateView(CreateView):
    model = Topic
    template_name = 'topic_form.html'
    fields = ['keyword']
    success_url = reverse_lazy('topic-list')

class TopicUpdateView(UpdateView):
    model = Topic
    template_name = 'topic_form.html'
    fields = ['keyword']

class TopicDeleteView(DeleteView):
    model = Topic
    template_name = 'topic_confirm_delete.html'
    success_url = reverse_lazy('topic-list')
