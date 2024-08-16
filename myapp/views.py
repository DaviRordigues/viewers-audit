from django.shortcuts import render, redirect
from .forms import DocumentForm
from .models import Document


def index(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = DocumentForm()

    documents = Document.objects.all()
    return render(request, 'index.html', {'form': form, 'documents': documents})
