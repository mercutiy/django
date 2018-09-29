from django.urls import re_path
from .views import products, collections, errors

urlpatterns = [
    re_path(r'^products/?$', products.products),
    re_path(r'^product/(?P<sku>\w+)/?$', products.product),
    re_path(r'^collections/?$', collections.all_collections),
    re_path(r'^collection/(?P<collection>\w+)/products/?$', products.products_by_collect),
    re_path(r'.', errors.error404),
]

