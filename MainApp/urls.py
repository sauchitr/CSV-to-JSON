from django.urls import path
from . import views


urlpatterns = [
    path("", views.upload_csv, name="upload-csv"),
    # path("json/", views.convert_csv, name="convert-csv"),
]