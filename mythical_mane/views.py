from django.shortcuts import render

# Create your views here.

from .models import Patient


def patients_list(request):
	"""Render a list of patients with their owner and universe.

	Uses select_related to efficiently fetch related Owner and Universe.
	"""
	patients = Patient.objects.select_related("owner", "universe").all()
	return render(request, "patients.html", {"patients": patients})
