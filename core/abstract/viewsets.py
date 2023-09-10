from rest_framework import  viewsets
from rest_framework import filters

class AbstractViewSet(viewsets.ModelViewSet):
    filter_backends = [filters.OrderingFilter]
    odering_fields = ['created', 'updated']
    ordering = ['-updated']