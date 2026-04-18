from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpRequest
from .models import Plant
from .forms import PlantForm
# Create your views here.

def all_plants_view(request: HttpRequest):
    plants = Plant.objects.all().order_by('-created_at')
    return render(request, "plants/all_plants.html", {"plants": plants})
 

def plant_detail_view(request, plant_id):
    plant = Plant.objects.get(id=plant_id)
    
    related_plants = Plant.objects.filter(category=plant.category).exclude(id=plant.id)[:4]
    
    return render(request, 'plants/plant_detail.html', {
        'plant': plant,
        'related_plants': related_plants 
    })


def add_plant_view(request):
    if request.method == "POST":
        form = PlantForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("plants:all_plants_view")
    else:
        form = PlantForm()
    return render(request, "plants/add_plant.html", {"form": form})

def update_plant_view(request, plant_id):
    plant = get_object_or_404(Plant, id=plant_id)
    if request.method == "POST":
        form = PlantForm(request.POST, request.FILES, instance=plant)
        if form.is_valid():
            form.save()
            return redirect("plants:plant_detail_view", plant_id=plant.id)
    else:
        form = PlantForm(instance=plant)
    return render(request, "plants/update_plant.html", {"form": form, "plant": plant})


def delete_plant_view(request, plant_id):
    plant = Plant.objects.get(id=plant_id)
    plant.delete()
    return redirect("plants:all_plants_view")


def search_view(request):
    if "search" in request.GET and len(request.GET["search"]) >= 2:
        results = Plant.objects.filter(name__icontains=request.GET["search"])
    else:
        results = [] 
        
    return render(request, "plants/search.html", {"results": results})