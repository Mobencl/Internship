from django.contrib import admin
from Authorize.models import Role
from Authorize.models import Partners
from Authorize.models import UserRole, Proposal
admin.site.register(Role)
admin.site.register(Partners)
admin.site.register(UserRole)
admin.site.register(Proposal)
