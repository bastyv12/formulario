from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Contacto
from .forms import ContactoForm

class ListaContactosView(ListView):
    model = Contacto
    template_name = 'contactos/lista_contactos.html'
    context_object_name = 'contactos'

class CrearContactoView(CreateView):
    model = Contacto
    form_class = ContactoForm
    template_name = 'contactos/formulario_contacto.html'
    success_url = reverse_lazy('lista_contactos')

class EditarContactoView(UpdateView):
    model = Contacto
    form_class = ContactoForm
    template_name = 'contactos/formulario_contacto.html'
    success_url = reverse_lazy('lista_contactos')

class EliminarContactoView(DeleteView):
    model = Contacto
    template_name = 'contactos/confirmar_eliminar.html'
    success_url = reverse_lazy('lista_contactos')
