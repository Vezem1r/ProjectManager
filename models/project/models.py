from django.db import models

class Project(models.Model):
    """
    Project model
    """

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField()
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"

    def __str__(self):
        return self.name


class Task(models.Model):
    """
    Task model
    """

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    category = models.ForeignKey("TaskCategory", on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Task"
        verbose_name_plural = "Tasks"

    def __str__(self):
        return self.name


class TaskAssignment(models.Model):
    """
    Task assignment model
    """

    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="assignments")
    user = models.ForeignKey("user.UserModel", on_delete=models.CASCADE)
    assigned_date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = "Task Assignment"
        verbose_name_plural = "Task Assignments"

    def __str__(self):
        return f"{self.task} - {self.user}"


class TaskComment(models.Model):
    """
    Task comment model
    """

    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey("user.UserModel", on_delete=models.CASCADE)
    comment = models.TextField()
    commented_date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = "Task Comment"
        verbose_name_plural = "Task Comments"

    def __str__(self):
        return f"{self.task} - {self.user}"


class TaskCategory(models.Model):
    """
    Task category model
    """

    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Task Category"
        verbose_name_plural = "Task Categories"

    def __str__(self):
        return self.name