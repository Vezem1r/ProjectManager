from django.contrib import admin

from models.project.models import (
    Project,
    Task,
    TaskAssignment,
    TaskComment,
    TaskCategory,
)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    """
    Project model admin
    """

    list_display = ["name", "start_date", "end_date", "is_active"]
    search_fields = ["name"]
    list_filter = ["is_active"]
    ordering = ["-start_date"]
    fieldsets = (
        (None, {"fields": ("name", "description")}),
        ("Project dates", {"fields": ("start_date", "end_date")}),
        ("Status", {"fields": ("is_active",)}),
    )


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    """
    Task model admin
    """

    list_display = [
        "name",
        "project",
        "category",
        "start_date",
        "end_date",
        "is_active",
    ]
    search_fields = ["name"]
    list_filter = ["is_active"]
    ordering = ["-start_date"]
    fieldsets = (
        (None, {"fields": ("name", "description")}),
        ("Project", {"fields": ("project",)}),
        ("Category", {"fields": ("category",)}),
        ("Task dates", {"fields": ("start_date", "end_date")}),
        ("Status", {"fields": ("is_active",)}),
    )


@admin.register(TaskAssignment)
class TaskAssignmentAdmin(admin.ModelAdmin):
    """
    Task assignment model admin
    """

    list_display = ["task", "user", "assigned_date"]
    search_fields = ["task__name", "user__username"]
    ordering = ["-assigned_date"]
    readonly_fields = ["assigned_date"]


@admin.register(TaskComment)
class TaskCommentAdmin(admin.ModelAdmin):
    """
    Task comment model admin
    """

    list_display = ["task", "user", "comment", "commented_date"]
    search_fields = ["task__name", "user__username"]
    ordering = ["-commented_date"]
    readonly_fields = ["commented_date"]


@admin.register(TaskCategory)
class TaskCategoryAdmin(admin.ModelAdmin):
    """
    Task category model admin
    """

    list_display = ["name"]
    search_fields = ["name"]
    ordering = ["name"]
