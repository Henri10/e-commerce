from django.urls import path
from .views import index, smartphone, Smartphone_details

urlpatterns = [
    path("base/", index),
    path("home/", smartphone),
    path("smartphone/<uuid:pk>/", Smartphone_details.as_view(), name="detail-phone"),
]