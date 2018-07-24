from django.conf.urls import url
#from HotelApp import views
from booking import views

# Url patters for authorization such as accepting , deleting and removing a partner.
app_name = 'booking'
urlpatterns = [
         url(r'^$', views.showSportcenters, name='home'),
         url(r'^newsportcenter/$', views.addSportcenter.as_view(), name='createSportcenter'),
         #url(r'^sportcenter$', views.showhotels, name='showSportcenter'),
        # url(r'^sportcenters/(?P<pk>[0-9]+)/edit$',views.editSportcenter.as_view() , name='editSportcenter'),
         url(r'^sportcenters/(?P<id>[0-9]+)/delete$',views.deleteSportcenter , name='deletesportcenter'),
         url(r'^sportcenters/(?P<id>[0-9]+)/terrains/$', views.showTerrains, name='showterrains'),
         url(r'^newterrain/$', views.addTerrain.as_view(), name='createTerrain'),
]
