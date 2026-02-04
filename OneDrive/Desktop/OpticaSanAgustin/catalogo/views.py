from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# Mantén tu vista 'index' que ya tenías...
def index(request):
    return render(request, 'index.html')

# Agrega esta nueva vista para el registro
def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) # Inicia sesión automáticamente al registrarse
            return redirect('index') # Lo manda al inicio
    else:
        form = UserCreationForm()
    return render(request, 'registro.html', {'form': form})