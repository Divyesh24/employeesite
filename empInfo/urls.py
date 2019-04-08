from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('', login_required(views.info_list), name='info_list'),
    path('info/<int:pk>/', views.info_detail, name='info_detail'),
    path('info/new/', views.add_new, name='add_new'),
    path('info/<int:pk>/edit/', views.info_edit, name='info_edit'),
    path('info/<int:pk>/delete/', views.info_delete, name='info_delete'),
    path('logout/',views.logout_view, name='logout'),
]