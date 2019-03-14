from django.urls import path
from . import views

app_name = 'boards'

urlpatterns = [
    # path('<int:pk>/update/', views.update, name='update'),
    path('<int:pk>/edit/', views.edit, name='edit'),  # GET(EDIT) / POST(UPDATE)
    path('<int:pk>/delete/', views.delete, name='delete'),    # POST(DELETE)
    path('<int:pk>/', views.detail, name='detail'),
    # path('create/', views.create, name='create'),
    path('new/', views.new, name='new'),    # GET(NEW) / POST(CREATE)
    path('', views.index, name='index'),
    ]