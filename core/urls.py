from django.urls import path, include


urlpatterns = [
    path("", include("core.web.common.urls")),
    path("user/", include("core.web.user.urls")),
    path("project/", include("core.web.project.urls")),
]
