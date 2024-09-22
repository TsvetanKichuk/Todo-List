from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from tasks.forms import TaskCreationForm, TaskUpdateForm, TagCreationForm
from tasks.models import Task, Tag


def index(request: HttpRequest) -> HttpResponse:
    return render(request, "tasks/task_list.html")


class TaskListView(generic.ListView):
    model = Task
    paginate_by = 5
    context_object_name = "tasks_list"
    # template_name = "tasks/task_list.html"
    queryset = Task.objects.all().prefetch_related("tags__tasks")


# class TaskDetailView(generic.DetailView):
#     model = Task
#     queryset = Task.objects.all().prefetch_related("task__tags")


class TaskCreateView(generic.edit.CreateView):
    model = Task
    form_class = TaskCreationForm
    template_name = "tasks/task_form.html"


class TaskUpdateView(generic.edit.UpdateView):
    model = Task
    form_class = TaskUpdateForm
    success_url = reverse_lazy("tasks:index")
    template_name = "tasks/task_form.html"


class TaskDeleteView(generic.edit.DeleteView):
    model = Task
    success_url = reverse_lazy("tasks:index")
    template_name = "tasks/task_confirm_delete.html"


class TagListView(generic.ListView):
    model = Tag
    context_object_name = "tag_list"
    template_name = "tasks/tag_list.html"
    paginate_by = 2
    queryset = Tag.objects.all()


class TagCreateView(generic.edit.CreateView):
    model = Tag
    form_class = TagCreationForm
    template_name = "tasks/tag_form.html"


class TagUpdateView(generic.edit.UpdateView):
    model = Tag
    form_class = TagCreationForm
    success_url = reverse_lazy("tasks:index")


class TagDeleteView(generic.edit.DeleteView):
    model = Tag
    success_url = reverse_lazy("tasks:index")


def complete_task(request, pk):
    complete = Task.objects.filter(boolean=True)
    if complete:
        return f"Complete"
    return f"Undo"
