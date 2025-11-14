from django.urls import path
from . import views

#Lists/
urlpatterns = [
    # view
    path("", views.ListsView, name="lists"),
    path("customer", views.CustomerListsView, name="customer_lists"),
    path("contractor", views.ContractorListsView, name="contractor_lists"),
    # create
    path("case_create", views.CaseCreate, name="case_create"),
    path("customer_create", views.CustomerCreate, name="customer_create"),
    path("contractor_create", views.ContractorCreate, name="contractor_create"),
    path("product_create/<int:case_id>", views.ProductCreate, name="product_create"),
    path("price_create/<int:case_id>/<int:gaityu_id>", views.PriceCreate, name="price_create"),
    path("gaityu_create/<int:case_id>", views.GaityuCreate, name="gaityu_create"),
    # update
    path("<int:case_id>/case_update", views.CaseUpdate, name="case_update"),
    path("<int:customer_id>/customer_update", views.CustomerUpdate, name="customer_update"),
    path("<int:contractor_id>/contractor_update", views.ContractorUpdate, name="contractor_update"),
    path("<int:product_id>/product_update", views.ProductUpdate, name="product_update"),
]