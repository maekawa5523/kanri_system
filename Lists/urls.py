from django.urls import path
from . import views

#Lists/
urlpatterns = [
    path("", views.ListsView.as_view(), name="lists"),
    path("customer", views.CustomerListsView.as_view(), name="customer_lists"),
    path("contractor", views.ContractorListsView.as_view(), name="contractor_lists"),
    path("case_create", views.CaseCreate.as_view(), name="case_create"),
    path("customer_create", views.CustomerCreate.as_view(), name="customer_create"),
    path("contractor_create", views.ContractorCreate.as_view(), name="contractor_create"),
    path("product_create/<int:pk>", views.ProductCreate.as_view(), name="product_create"),
    path("<int:pk>", views.Detail.as_view(), name="detail"),
    path("<int:pk>/case_update", views.CaseUpdate.as_view(), name="case_update"),
    path("<int:pk>/product_update", views.ProductUpdate.as_view(), name="product_update"),
    path("<int:pk>/customer_update", views.CustomerUpdate.as_view(), name="customer_update"),
    path("<int:pk>/contractor_update", views.ContractorUpdate.as_view(), name="contractor_update"),
    path("<int:pk>/delete", views.Delete.as_view(), name="delete"),
]