from django.shortcuts import render
from .models import Audit

def audit_list(request):
    audits = Audit.objects.all()  # Busca todos os registros da tabela
    return render(request, 'audit_list.html', {'audits': audits})
