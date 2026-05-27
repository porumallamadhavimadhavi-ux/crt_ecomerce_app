
from django.urls import path
from .views import add_product,view_all_product,delete_by_id


# http://127.0.0.1:8000/product/add_product
# http://127.0.0.1:8000/product/dele_by_id/id


urlpatterns = [
   path("add_product",add_product),
    path("view_all_product",view_all_product, name="view_all_product"),
    path("delete_by_id/<int:id>",delete_by_id,name="delete_by_id")
]