from django.http import HttpResponse, FileResponse
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from django.shortcuts import render, redirect, get_object_or_404

from datetime import datetime

from .filters import StockFilter
from .forms import StockCreateForm, grnCreateForm, GRNMaterailForm
from production.models import ProductionMaterial
from .models import Stock, Material, Cutter, GoodsReceivedNote


class StockView(ListView):
    model = Stock
    template_name = 'stock/home.html' 

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context.update({
            'filter': StockFilter(self.request.GET,
                                  queryset=self.get_queryset()),
            'materials': Material.objects.all().order_by('name'),
            'cutters': Cutter.objects.all().order_by('-name'),
            })
        return context


class CreateStock(CreateView):

    def get(self, request, *args, **kwargs):

        context = {'form': StockCreateForm()}
        return render(request, 'stock/create_stock.html', context)

    def post(self, request, *args, **kwargs):

        form = StockCreateForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('stock')

        for index, i in enumerate(Stock.objects.all()):
            i.id = index + 1
            i.save()

        return render(request, 'stock/create_stock.html', {'form': form})


def TakeStock(request, id1, id2):

    productionMaterial = ProductionMaterial.objects.get(id=id1)
    stock = Stock.objects.get(id=id2)

    productionStocks = productionMaterial.stocks.update_or_create(
        number=id2,
        length=stock.length,
        width=stock.width,
        material=stock.material,
        )

    stock.width = 0
    stock.length = 0
    stock.save()

    return redirect('edit-production', productionMaterial.production.id )


def AddStock(request, id):

    stock = Stock.objects.get(id=id)
    form = StockCreateForm()

    if request.method == 'POST':
        form = StockCreateForm(request.POST)
        if form.is_valid():
            form = StockCreateForm(request.POST)
            form.save(commit=False)
            stock.width = request.POST['width']
            stock.length = request.POST['length']
            stock.material.id = request.POST['material']
            stock.save()
            return redirect('stock')

    return render(request, 'stock/create_stock.html', {'form': form})


def CutterSharp(request, id):

    cutter = Cutter.objects.get(id=id)

    return redirect('stock')


def CutterBuy(request, id):

    cutter = Cutter.objects.get(id=id)


def GRN(request):

    grns = GoodsReceivedNote.objects.all().order_by('-date')
    form = grnCreateForm()

    if request.method == 'POST':
        form = grnCreateForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()

            return redirect('edit-grn', id=obj.id)
        else:
            form = grnForm()

    ctx = {
        'grns': grns,
        'form': form,
           }

    return render(request, 'production/grn.html', ctx)


def EditGRN(request, id):

    grns = GoodsReceivedNote.objects.all().order_by('date')
    grn = GoodsReceivedNote.objects.get(id=id)
    materials = grn.grnmaterial_set.all()
    form = GRNMaterailForm()

    if request.method == 'POST':
        form = GRNMaterailForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)

            if int(float(request.POST['area']) * 1000) % int(float(obj.material.material_area ) * 1000 ) == 0:

                material = Material.objects.get(id=request.POST['material'])
                material.quantity += float(request.POST['area']) / float(material.material_area)
                material.save()

                obj.grn = grn
                obj.save()

                return redirect('edit-grn', id=grn.id)

            else:
                error = "Wprowadziłeś ilość materiału równą {}m2.<br>\
                         Jedna płyta ma powierzchnie {}m2<br>\
                         Nie wychodzą równe sztuki płyt, wróć do PZtki i popraw metry  ".format(request.POST['area'], obj.material.material_area)
                return HttpResponse(error)
        else:
            form = GRNMaterailForm()

    ctx = {
        'grns': grns,
        'grn': grn,
        'form': form,
        'materials': materials,
        }

    return render(request, 'production/edit_grn.html', ctx)


def DetailGRN(request, id):

    grns = GoodsReceivedNote.objects.all().order_by('date')
    grn = GoodsReceivedNote.objects.get(id=id)
    materials = grn.grnmaterial_set.all()

    ctx = {
        'grns': grns,
        'grn': grn,
        'materials': materials,
        }

    return render(request, 'production/detail_grn.html', ctx)
