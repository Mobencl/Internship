from django.conf.urls import url
from SportcenterApp.views import get_sportcenters, userDash
from SportcenterApp.views import partnerProposal


app_name ='SportcenterApp'
urlpatterns = [
     url(r'^$', get_sportcenters, name='sportcenterindex'),
     url(r'^profile/$', userDash, name='userDash'),
     #url(r'^sportcenters/(?P<pk>[0-9]+)/$', views.sportcenterdetails, name='sportcenterdetails'),#It doesn't work yet
     url(r'^partner/apply$', partnerProposal.as_view(), name='newproposal'),                                                                                              #(problem with the function sportdetails in views.py)

]
