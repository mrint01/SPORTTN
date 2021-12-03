from django.shortcuts import render
from .models import Proteines,Materiels,Vetements
# Create your views here.
def ProtAction(request):
        prot  = Proteines.objects.all()
        return render(request,"product/ProtProduct.html" , {'prot' :prot})
def ProtDetailAction(request,pk):
        protdetails  = Proteines.objects.get(id=pk)
        prot  = Proteines.objects.order_by('?')[:4]
        context = {
                "protdetails" : protdetails,
                "prot" : prot
        }
        return render(request,"product/ProtProductDetails.html" , context)