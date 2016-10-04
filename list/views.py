from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import ToDo
from django.http import HttpResponse
from ToDoList import settings


@login_required
def profile(request):
	if request.method == "POST":
		ToDo.objects.create(user=request.user, task=request.POST['task'])

	context = {'user': request.user, 'list': ToDo.objects.all()}
	return render(request, "todolist.html", context=context)


@login_required
def selection(request, id):
	print(id)
	task = ToDo.objects.get(id=int(id))
	task.condition = settings.DONE if task.condition == settings.ACTIVE else settings.ACTIVE
	task.save()
	return HttpResponse("Ok")
