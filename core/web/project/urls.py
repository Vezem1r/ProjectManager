from django.urls import path

from core.web.project.views import (
    project_create_view,
    project_get_view,
    project_update_view,
    project_delete_view,
    task_create_view,
    task_get_view,
    task_update_view,
    task_delete_view,
    task_delete_from_project_view,
    task_comment_create_view,
    task_comment_delete_view,
    task_assignment_create_view,
    task_assignment_delete_view,
)


app_name = "project"
urlpatterns = [
    path("create/", project_create_view, name="create"),
    path("<int:pk>/", project_get_view, name="get"),
    path("<int:pk>/update/", project_update_view, name="update"),
    path("<int:pk>/delete/", project_delete_view, name="delete"),
    path("<int:project_pk>/task/create/", task_create_view, name="task_create"),
    path("task/<int:task_pk>/", task_get_view, name="task_get"),
    path("task/<int:task_pk>/update/", task_update_view, name="task_update"),
    path("task/<int:task_pk>/delete/", task_delete_view, name="task_delete"),
    path(
        "<int:project_pk>/task/<int:task_pk>/delete-from-project/",
        task_delete_from_project_view,
        name="task_delete_from_project",
    ),
    path(
        "task/<int:task_pk>/comment/create/",
        task_comment_create_view,
        name="task_comment_create",
    ),
    path(
        "task/<int:task_pk>/comment/<int:comment_pk>/delete/",
        task_comment_delete_view,
        name="task_comment_delete",
    ),
    path(
        "task/<int:task_pk>/assignment/create/",
        task_assignment_create_view,
        name="task_assignment_create",
    ),
    path(
        "task/<int:task_pk>/assignment/<int:assignment_pk>/delete/",
        task_assignment_delete_view,
        name="task_assignment_delete",
    ),
]
