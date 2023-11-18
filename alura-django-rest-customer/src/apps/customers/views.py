from customers.models import Customer
from customers.serializers import CustomerSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class CustomersViewSet(viewsets.ModelViewSet):
    """Listando customers"""

    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    ordering_fields = [
        "name",
    ]
    search_fields = [
        "name",
        "cpf",
    ]
    filterset_fields = [
        "active",
    ]
    authentication_classes = [
        BasicAuthentication,
    ]
    permission_classes = [
        IsAuthenticated,
    ]
