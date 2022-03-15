from django.shortcuts import render, redirect
from .models import Search
from .forms import SearchForm
import folium
import geocoder

from .models import Search
from django.shortcuts import render





def map(request):
    if request.method =='POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.user = request.user
            form.save()
            return redirect('map:map')
    else:
        form =SearchForm()
    address = Search.objects.all().last()
    #address = request.POST.get('address')
    location = geocoder.osm(address)
    lat = location.lat
    lng = location.lng
    country = location.country

    #Create Map Object
    m = folium.Map(location=[51.312711, 9.479746], zoom_start=6)
    folium.Marker([50.922423, 6.363912], tooltip='Click for more', popup='Jülich').add_to(m)
    
    # -> new
    if location is not None and location.current_result is not None:
        folium.Marker(location=[lat, lng], tooltip='Click for more', popup=country).add_to(m)
    # <-
    
    #Get HTML Representation of Ma Object
    m = m._repr_html_()
    context = {
        'm': m,
        'form': form,
    }
    return render(request,'map/map.html', context )

