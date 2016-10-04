from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import ToDo


@login_required
def profile(request):
	if request.method == "POST":
		ToDo.objects.create(user=request.user, task=request.POST['task'])

	context = {'user': request.user, 'list': ToDo.objects.all()}
	return render(request, "todolist.html", context=context)
