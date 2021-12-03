from django.shortcuts import render
from datetime import datetime
def index(request):
    date = datetime.today()
    name ="HATEM SFAR"
    cont = {"dateToday":date, "name":name}
    
    return render(request,"sportTN/index.html",cont)
    