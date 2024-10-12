from rest_framework.views import APIView
from .models import Balance
from .serializers import BalanceSerilaizer

# Create your views here.
class Create_InvoiceView(APIView):
    def post(self, request):
        serilalizers = BalanceSerilaizer(data =request.data)
        if serilalizers.is_valid():
            serilalizers.save()
            