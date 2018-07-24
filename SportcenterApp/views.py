from django.shortcuts import render
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.views import View
from django.contrib.auth.decorators import login_required
from SportcenterApp.models import Sportcenters, Photo
from Authorize.models import Proposal
from django.views.generic.edit import CreateView

#def home(request):
#    return render(request,'SportcenterApp/home.html')
def regcomplete(request):
    return render(request,'Sportcenter/userDash.html')

def userDash(request):
    return render(request,'Sportcenter/userDash.html')


@login_required   #I'm going to replace this decorator by using the middleware that I used for my frist project
def get_sportcenters(request):
    sportcenter_list = Sportcenters.objects.all()
    for sportcenter in sportcenter_list:
        sportcenter.thumbnail= Photo.objects.filter(sportcenter=sportcenter).first()
        return render(request,'Sportcenter/showsportcenters.html',{'Sportcenters': sportcenter_list})


class partnerProposal(CreateView):

    model = Proposal
    fields = ['CompanyName','CompanyEmail','HQAddress','Vision']
    def get_success_url(self):
        url = reverse('SportcenterApp:userDash')
        return url
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(partnerProposal, self).form_valid(form)


def checkstatus(request):
    proposal_list = Proposal.objects.filter(user=request.user)
    return render(request,"Sportcenter/check.html",{'proposal': proposal_list})

@login_required
# show sportcenters for a partner
def showsportcenters(request,pk):
    user = request.user
    partner = Sportcenters.objects.filter(Partner=partner)
    sportcenter_list = Sportcenters.objects.get(id=pk)
    return render(request,'Sportcenter/showsportcenters.html',{'Sportcenters': sportcenter_list})
#show the sportcenter
def showsportcenter(request,pk):
    sportcenter = Sportcenter.objects.get(id=pk)
    return render(request,'SportcenterApp/showsportcenter.html',{'Sportcenter': sportcenter})




'sportcenter'
'TerrainType'
'minimumCapacity'
'maximumCapacity'
'Price'
'opening'
'closing'
