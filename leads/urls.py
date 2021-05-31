from django.urls import path
from .views import *

app_name = "leads"

urlpatterns = [
    path('', LeadListView.as_view(), name="home"),
    path('<int:pk>/', LeadDetailView.as_view(), name="lead-view"),
    path('create/', LeadCreateView.as_view(), name="lead-create"),
    path('<int:pk>/update', lead_update, name="lead-update"),
    path('<int:pk>/delete', lead_delete, name="lead-delete")
]