from rest_framework.viewsets import ModelViewSet

from livraria.models import Autor, Livro
from livraria.serializers import AutorSerializer, LivroSerializer, LivroDetailSerializer, LivroListSerializer

class AutorViewSet(ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
  

class LivroViewSet(ModelViewSet):
    queryset = Livro.objects.all()
    def get_serializer_class(self):
        if self.action == "list":
            return LivroListSerializer
        elif self.action == "retrieve":
            return LivroDetailSerializer
        return LivroSerializer
