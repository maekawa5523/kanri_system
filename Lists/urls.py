from django.urls import path
from . import views

#Lists/
urlpatterns = [
    path("", views.ListsView.as_view(), name="lists"),
    path("case_create", views.CaseCreate.as_view(), name="case_create"),
    path("<int:pk>", views.Detail.as_view(), name="detail"),
    path("<int:pk>/update", views.Update.as_view(), name="update"),
    path("<int:pk>/delete", views.Delete.as_view(), name="delete"),
]