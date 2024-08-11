from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from core.web.project.forms import (
    ProjectCreateForm,
    TaskCreateForm,
    TaskCommentCreateForm,
    TaskAssignmentCreateForm,
)
from models.project.models import (
    Project,
    Task,
    TaskAssignment,
    TaskComment,
    TaskCategory,
)


@login_required(login_url="user/login/")
def project_create_view(request):
    """
    Project create view
    """
    form = ProjectCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("index")
    return render(request, "project/project_create.html", {"form": form})


@login_required(login_url="user/login/")
def project_get_view(request, pk):
    """
    Project get view
    """
    project = get_object_or_404(Project, pk=pk)
    tasks = Task.objects.filter(project=project)
    return render(
        request, "project/project_get.html", {"project": project, "tasks": tasks}
    )


@login_required(login_url="user/login/")
def project_update_view(request, pk):
    """
    Project update view
    """
    project = get_object_or_404(Project, pk=pk)
    form = ProjectCreateForm(request.POST or None, instance=project)
    if form.is_valid():
        project.is_active = request.POST.get("is_active") == "on"
        form.save()
        return redirect("index")
    return render(request, "project/project_update.html", {"form": form})


@login_required(login_url="user/login/")
def project_delete_view(request, pk):
    """
    Project delete view
    """
    project = get_object_or_404(Project, pk=pk)
    project.delete()
    return redirect("index")


@login_required(login_url="user/login/")
def task_create_view(request, project_pk):
    """
    Task create view
    """
    project = get_object_or_404(Project, pk=project_pk)

    form = TaskCreateForm(request.POST or None)
    if form.is_valid():
        task = form.save(commit=False)
        task.project = project
        task.save()
        return redirect("project:get", pk=project_pk)
    return render(
        request, "project/task_create.html", {"form": form, "project": project}
    )


@login_required(login_url="user/login/")
def task_get_view(request, task_pk):
    """
    Task get view
    """
    task = get_object_or_404(Task, pk=task_pk)
    comments = TaskComment.objects.filter(task=task)
    assignments = TaskAssignment.objects.filter(task=task)
    return render(
        request,
        "project/task_get.html",
        {"task": task, "comments": comments, "assignments": assignments},
    )


@login_required(login_url="user/login/")
def task_update_view(request, task_pk):
    """
    Task update view
    """
    task = get_object_or_404(Task, pk=task_pk)
    form = TaskCreateForm(request.POST or None, instance=task)
    if form.is_valid():
        form.save()
        return redirect("project:task_get", task_pk=task_pk)
    return render(request, "project/task_update.html", {"form": form, "task": task})


@login_required(login_url="user/login/")
def task_delete_from_project_view(request, project_pk, task_pk):
    """
    Task delete view
    """
    task = get_object_or_404(Task, pk=task_pk)
    task.delete()
    return redirect("project:get", pk=project_pk)


@login_required(login_url="user/login/")
def task_delete_view(request, task_pk):
    """
    Task delete view
    """
    task = get_object_or_404(Task, pk=task_pk)
    task.delete()
    return redirect("index")


@login_required(login_url="user/login/")
def task_comment_create_view(request, task_pk):
    """
    Task comment create view
    """
    task = get_object_or_404(Task, pk=task_pk)
    form = TaskCommentCreateForm(request.POST or None)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.task = task
        comment.user = request.user
        comment.save()
        return redirect("project:task_get", task_pk=task_pk)
    return render(
        request, "project/task_comment_create.html", {"form": form, "task": task}
    )


@login_required(login_url="user/login/")
def task_comment_delete_view(request, task_pk, comment_pk):
    """
    Task comment delete view
    """
    comment = get_object_or_404(TaskComment, pk=comment_pk)
    comment.delete()
    return redirect("project:task_get", task_pk=task_pk)


@login_required(login_url="user/login/")
def task_assignment_create_view(request, task_pk):
    """
    Task assignment create view
    """
    task = get_object_or_404(Task, pk=task_pk)
    form = TaskAssignmentCreateForm(request.POST or None)
    if form.is_valid():
        assignment = form.save(commit=False)
        assignment.task = task
        assignment.save()
        return redirect("project:task_get", task_pk=task_pk)
    return render(
        request, "project/task_assignment_create.html", {"form": form, "task": task}
    )


@login_required(login_url="user/login/")
def task_assignment_delete_view(request, task_pk, assignment_pk):
    """
    Task assignment delete view
    """
    assignment = get_object_or_404(TaskAssignment, pk=assignment_pk)
    assignment.delete()
    return redirect("project:task_get", task_pk=task_pk)
