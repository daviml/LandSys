from django.shortcuts import render,redirect
from .forms import LandsysFormV,LandsysFormC
from .models import Vendedores,Clientes

# Create your views here.

def landsys_listv(request):
    context = {'landsys_listv':Vendedores.objects.all()}
    return render(request,"landsys_register/landsys_list.html",context)

def landsys_formv(request,id=0):
    if request.method == "GET":
        if id==0:
            form = LandsysFormV()
        else:
            landsys = Vendedores.objects.get(pk=id)
            form = LandsysFormV(instance=landsys)
        return render(request,"landsys_register/landsys_form.html",{'form':form})
    else:
        if id == 0:
            form = LandsysFormV(request.POST)
        else:
            landsys = Vendedores.objects.get(pk=id)
            form = LandsysFormV(request.POST,instance= landsys)
        if form.is_valid():
            form.save()
        return redirect('/landsys/listv')

def landsys_deletev(request,id):
    landsys = Vendedores.objects.get(pk=id)
    landsys.delete()
    return redirect('/landsys/listv') 






def landsys_listc(request):
    context = {'landsys_listc':Clientes.objects.all()}
    return render(request,"landsys_register/landsys_listc.html",context)

def landsys_formc(request,id=0):
    if request.method == "GET":
        if id==0:
            form = LandsysFormC()
        else:
            landsys = Clientes.objects.get(pk=id)
            form = LandsysFormC(instance=landsys)
        return render(request,"landsys_register/landsys_form.html",{'form':form})
    else:
        if id == 0:
            form = LandsysFormC(request.POST)
        else:
            landsys = Clientes.objects.get(pk=id)
            form = LandsysFormC(request.POST,instance= landsys)
        if form.is_valid():
            form.save()
        return redirect('/landsys/listc')

def landsys_deletec(request,id):
    landsys = Clientes.objects.get(pk=id)
    landsys.delete()
    return redirect('/landsys/listc') 