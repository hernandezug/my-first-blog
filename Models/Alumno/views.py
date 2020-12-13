from django.http import HttpRequest
from django.shortcuts import render

from Models.Alumno.forms import FormularioAlumno


class FormularioAlumnoView(HttpRequest):

    def index(request):
        alumno = FormularioAlumno()
        return render(request, "AlumnoIndex.html", {"form":alumno})

    def procesar_formulario(request):
        alumno = FormularioAlumno(request.POST)
        if alumno.is_valid():
            alumno.save()
            alumno = FormularioAlumno()
        return render(request, "AlumnoIndex.html", {"form":alumno, "mesaje": 'ok'})