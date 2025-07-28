from django.urls import path 
from . import views

app_name = 'cases'

urlpatterns = [
    #Define URL For home page
    path('', views.HomeView.as_view(), name='home'),
    
    #Define URL for client 
    path('clients/', views.ClientListView.as_view(), name='client_list'),
    path('clients/create/', views.ClientCreateView.as_view(), name='client_create'),
    path('clients/<int:pk>/update/', views.ClientUpdateView.as_view(), name='client_update'),
    path('clients/<int:pk>/delete/', views.ClientDeleteView.as_view(), name='client_delete'),
    
    #Define URL for lawyer
    path('lawyers/', views.LawyerListView.as_view(), name='lawyer_list'),
    path('lawyers/create/', views.LawyerCreateView.as_view(), name='lawyer_create'),
    path('lawyers/<int:pk>/update/', views.LawyerUpdateView.as_view(), name='lawyer_update'),
    path('lawyers/<int:pk>/delete/', views.LawyerDeleteView.as_view(), name='lawyer_delete'),
    
    #Define URL for case
    path('cases/', views.CaseListView.as_view(), name='case_list'),
    path('cases/create/', views.CaseCreateView.as_view(), name='case_create'),
    path('cases/<int:pk>/update/', views.CaseUpdateView.as_view(), name='case_update'),
    path('cases/<int:pk>/delete/', views.CaseDeleteView.as_view(), name='case_delete'),
]
