from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("auth/sign-in", views.signIn, name="sign-in"),
    path("auth/sign-on", views.signOn, name="sign-on"),
    path("auth/logout", views.logout, name="logout"),
    path("orders", views.ordersList, name="orders"),
    path("partners/search-dealers", views.searchDealers, name="partners-search-dealers"),
    path("catalog/", views.catalog, name="catalog-index"),
    path("catalog/category/<int:category_id>", views.catalogCategory, name="catalog-category"),
    path("catalog/product/<int:product_id>/", views.catalogProduct, name="catalog-product"),
    path("catalog/product/<int:product_id>/order", views.catalogProductOrder, name="catalog-product-order"),
    path("order-success/", views.orderSuccess, name="order-success"),
]