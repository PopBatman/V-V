from rest_framework import viewsets

# Create your views here.

class AbstractViewSet(viewsets.ModelViewSet):
    ordering_fields = ['updated', 'created']
    ordering = ['-updated']
