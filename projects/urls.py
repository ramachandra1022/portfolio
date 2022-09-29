from django.urls import path
from django.conf import settings
from . import views

urlpatterns = [
    path("", views.project_index, name="project_index"),
    path("<int:pk>/", views.project_detail, name="project_detail"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)