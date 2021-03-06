#	admin.py
#
#	This file allows us to register/unregister
#	models from the admin interface, as well as
#	define what attributes of those models we
#	wish to be visible
#

from django.contrib import admin
from events.models import Event#, Person
from django.contrib.admin.views.main import ChangeList
from django.contrib.admin import DateFieldListFilter

# Change heading on user control
from django.contrib.auth.apps import AuthConfig
AuthConfig.verbose_name = ("Manage Alumni Office Users")

# Remove user groups, we don't need them in this application
from django.contrib.auth.models import Group
admin.site.unregister(Group)


class EventAdmin(admin.ModelAdmin):
	list_display =('title','date','status','numberAttendees',)
	actions = ['approve']
	# search_fields=('title','location')
	fields = ['title', 'location', 'date', 'time', 'description', 'host_first_name', 'host_last_name', 'host_graduation','host_major','numberAttendees']
	list_filter=('status',('date', DateFieldListFilter))

	# enables ability to display attendees in admin interface
	def Attendees(self, obj):
		return ", ".join([p.first_name for p in obj.attendees.all()])

	# add the ability to approve/delete events from admin interface
	def approve(self, request, queryset):
		queryset.update(status='a')
	approve.short_description = "Approve selected events"

admin.site.register(Event, EventAdmin)
#admin.site.register(Person)
admin.site.site_header="SCU Alumni Events"
