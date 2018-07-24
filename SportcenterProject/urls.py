from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from django.conf.urls.static import static
from SportcenterApp import views
from booking import views
from registration.backends.simple.views import RegistrationView
from SportcenterProject import settings

class MyRegistrationView(RegistrationView):
    def get_sucess_url(self,user):
        return '/Sportcenter/user/'

urlpatterns = [
    #url(r'^$', views.home , name = 'home'),
    url(r'^Authorize/', include('Authorize.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^SportcenterApp/', include('SportcenterApp.urls')),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^accounts/register/', MyRegistrationView.as_view(),),
    #url(r'^register/completed$', views.regcomplete , name = 'registration_complete'),
    url(r'^booking/', include('booking.urls')),


]
