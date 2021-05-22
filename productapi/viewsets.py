from rest_framework import viewsets
from . import models
from . import serializers

class productViewset(viewsets.ModelViewSet):
    queryset = models.product.objects.all()
    serializer_class = serializers.productSerializers
