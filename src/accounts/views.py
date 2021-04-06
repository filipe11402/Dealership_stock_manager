from django.shortcuts import render, redirect
from .forms import RegisterUserForm
from django.contrib.auth import authenticate, login, logout
from .decorators import unauthenticated_user


@unauthenticated_user
def registerview(request):
	form = RegisterUserForm()

	if request.method == 'POST':
		form = RegisterUserForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('stock:home')

	context = {
		'form': form,
	}
	return render(request, 'accounts/register.html', context)

@unauthenticated_user
def loginview(request):
	if request.method == 'POST':
		email = request.POST.get('email')
		password = request.POST.get('password')

		user = authenticate(email=email, password=password)
		if user is not None:
			login(request, user)
			return redirect('stock:home')

	return render(request, 'accounts/login.html')


def logoutview(request):
	logout(request)

	return redirect('accounts:login')