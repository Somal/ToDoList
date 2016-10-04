from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import ToDo
from django.http import HttpResponse
from ToDoList import settings


@login_required
def profile(request):
	"""
	Render main page
	:param request: Django's request
	:return: rendered Html Response
	"""
	if request.method == "POST":
		ToDo.objects.create(user=request.user, task=request.POST['task'])

	context = {'user': request.user, 'list': ToDo.objects.all()}
	return render(request, "todolist.html", context=context)


@login_required
def selection(request, id):
	"""
	Change task's condition by request
	:param request: Django's request
	:param id: id of task
	:return: type of result
	"""
	task = ToDo.objects.get(id=int(id))
	task.condition = settings.DONE if task.condition == settings.ACTIVE else settings.ACTIVE
	task.save()
	return HttpResponse("Ok")


@login_required
def deletion(request, id):
	"""
	Delete the specific task by id
	:param request: Django's request
	:param id: task's id
	:return: type of result
	"""
	ToDo.objects.get(id=int(id)).delete()
	return HttpResponse("Ok")
