from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import NoteListView, NoteDetailView, NoteCreateView, NoteUpdateView, NoteDeleteView


urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', views.home, name='home'),
    path('notes/', NoteListView.as_view(), name='note_list'),
    path('notes/<int:pk>/', NoteDetailView.as_view(), name='note_detail'),
    path('notes/new/', NoteCreateView.as_view(), name='note_create'),
    path('notes/<int:pk>/edit/', NoteUpdateView.as_view(), name='note_update'),
    path('notes/<int:pk>/delete/', NoteDeleteView.as_view(), name='note_delete'),
]
