from django.urls import path
from .views import index, products, Product_details, smartphone, smartwatch

urlpatterns = [
    path("base/", index),
    path("home/", products, name="home"),
    path("smartphone/", smartphone, name="smartphone"),
    path("smartphone/<uuid:pk>/", Product_details.as_view(), name="detail-phone"),
    path("smartwatch/", smartwatch, name="smartwatch")
]