from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Note
from django.contrib import messages
from django.http import Http404


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

def home(request):
    return render(request, 'home.html')


class NoteListView(LoginRequiredMixin, ListView):
    model = Note
    template_name = 'notes/note_list.html'
    context_object_name = 'notes'
    paginate_by = 10

    def get_queryset(self):
        return Note.objects.filter(user=self.request.user)

class NoteDetailView(LoginRequiredMixin, DetailView):
    model = Note
    template_name = 'notes/note_detail.html'

class NoteCreateView(LoginRequiredMixin, CreateView):
    model = Note
    template_name = 'notes/note_form.html'
    fields = ['title', 'body']
    success_url = reverse_lazy('note_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, 'Note created successfully!')
        return super().form_valid(form)

class NoteUpdateView(LoginRequiredMixin, UpdateView):
    model = Note
    template_name = 'notes/note_form.html'
    fields = ['title', 'body']
    success_url = reverse_lazy('note_list')

    def form_valid(self, form):
        messages.success(self.request, 'Note updated successfully!')
        return super().form_valid(form)

class NoteDeleteView(LoginRequiredMixin, DeleteView):
    model = Note
    template_name = 'notes/note_confirm_delete.html'
    success_url = reverse_lazy('note_list')

    def get_object(self, queryset=None):
        """ Hook to ensure object is owned by request.user. """
        obj = super().get_object(queryset=queryset)
        if not obj.user == self.request.user:
            raise Http404
        return obj

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Note deleted successfully!')
        return super().delete(request, *args, **kwargs)
