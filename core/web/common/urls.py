from django.urls import path

from core.web.common.views import index

urlpatterns = [path("", index, name="index")]
