from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from accounts.models import User\


"""
The UserAdmin class defines how the user admin panel 
will look like..

search_fields => this specifies how to search for users
list_display => how and what fields to display in admin panel
readonly_fields => non editable fields

ordering and fieldsets have to set to empty list or tuple
"""


class AdminUser(UserAdmin):
	search_fields 		= ('email',)
	list_display 		= ('email', 'is_staff', 'last_login')
	readonly_fields 	= ('pk', 'last_login', 'date_joined')

	ordering 			= ()
	fieldsets 			= ()



admin.site.register(User, AdminUser)
