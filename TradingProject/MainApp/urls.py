from django.urls import path
from .views import UploadFileView,index


urlpatterns = [
    path('',index),
    path('read_csv/',UploadFileView.as_view(),name="upload-file"),
    ]