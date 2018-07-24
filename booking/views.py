from django.shortcuts import render
from SportcenterApp.models import Terrain, Sportcenters
from django.contrib.auth.models import User
from booking.models import Booking
from django.contrib.auth.decorators import login_required
# Create your views here.
from Authorize.models import Partners
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView
from django.core.urlresolvers import reverse
from django.http import HttpResponse,HttpResponseRedirect

#def bookingTerrain(request,sportcenterid,terrainid):
#    sportcenter= Sportcenters.objects.get(id=sportcenterid)
#    terrain = Terrain.objects.get(id=terrainid)
#    booking_list = Booking.objects.all()
#    terrain_ondemand = booking.terrain
#    for booking in booking_list:
#        if terrainid == terrain_ondemand.terrainid:
#            if (booking.)

#Form functions for the partner:
#This fucnction is dedicated to the partner so he can store the terrain availibility
def manageTerrainAvailibilityView(request,terrainid,sportcenterid):
    if request.method =='POST':
        opening = request.POST.get('opening')
        closing = request.POST.get('closing')
        availableFrom = request.POST.get('availableFrom')
        availableTill = request.POST.get('availableTill')
        user = request.user
        sportcenter = Sportcenters.objects.get(id=sportcenterid)
        terrain=Terrain.objects.get(id=hotelid)
        terrainAvailibility = TerrainAvilibility()
        terrain.opening = opening
        terrain.closing = closing
        terrainAvailibility.sportcenter = sportcenter
        terrainAvailibility.user = user
        terrainAvailibility.terrain = terrain
        terrainAvilibility.availableFrom=availableFrom
        terrainAvailibility.availableTill=availableTill
        terrainAvailibility.save()
        link = reverse('booking:home')
        return HttpResponseRedirect(link)
    else:
        url = reverse('booking:home')
        return url
#def updateTerrainAvailibility(request,terrainid,sportcenterid)
##show list of sportcenters for the partner
#show sportcenter details for the partnerwith the opening and closing address and telephone number and everything
#show terrains and availibilities for the partner
@login_required
def showSportcenters(request):
    user = request.user
    partner = Partners.objects.get(userID = user)
    sportcenters_list = Sportcenters.objects.filter(Partner=partner)
    context = {'Sportcenters': sportcenters_list}
    return render(request,'Sportcenter/showsportcenters.html',context)



class addSportcenter(CreateView):
    model =Sportcenters
    fields = [
    'Name',
    'Address',
    'City',
    'Country',
    'TelephoneNumber',
    'Description']
    def get_success_url(self):
        return reverse('booking:home')
    def form_valid(self,form):
        user=self.request.user
        partner=Partners.objects.get(userID=user)
        form.instance.Partner_id   = partner.id
        return super(addSportcenter, self).form_valid(form)

def deleteSportcenter(request,id):
    sportcenter=Sportcenters.objects.get(id=id)
    sportcenter.delete()
    return  HttpResponseRedirect(reverse('booking:home'))

def showTerrains(request,id):
    sportcenter =Sportcenters.objects.get(id=id)
    terrain_list = Terrain.objects.filter(sportcenter=sportcenter)
    return render(request,'booking/showterrains.html',{'Terrain': terrain_list})

class addTerrain(CreateView):
    model =Terrain
    fields = [
    
    'TerrainType',
    'minimumCapacity',
    'maximumCapacity',
    'Price',
    'opening',
    'closing',]
    def get_success_url(self):
        return reverse('booking:showterrains')
    def form_valid(self,form):
        form.instance.Terrain_id   = self.kwargs['id']
        return super(addTerrain, self).form_valid(form)



def deleteTerrain(request):
    pass

def updateTerrain(request):
    pass

def Availibility(request):
    pass
    # so there is an edit button a delete button and an Availibility Button(goes to a page that shows availibilities)
def updateAvailibility(request):
    pass


#def bookingTerrain(request,sportcenterid,terrainid):
#    sportcenter= Sportcenters.objects.get(id=sportcenterid)
#    terrain = Terrain.objects.get(id=terrainid)
#    price = terrain.Price
#    booking_duration = Booking.time_period
#    check_in = Booking.date
#    totalCost = booking_duration*price
#    context ={check_in:'check_in',stayduration':StayDuration,'sportcenter':sportcenter,'terrain':terrain,'price':price,
#    'totalcost':TotalCost}
#    return render(request,'Booking/booking.html',context)




#show users their reservation
#def userBooking(request):
#    booking = Booking.objects.filter(user=request.user)
#    return render(request,'Booking/userBooking.html',{'booking':booking})
