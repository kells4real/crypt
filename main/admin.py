from django.contrib import admin
from .models import Transaction, AvailableBtc
from .models import AuthUser
from django.contrib.auth.admin import UserAdmin
# Register your models here.
class CustomUserAdmin(UserAdmin):

    fieldsets = (
        *UserAdmin.fieldsets,  # original form fieldsets, expanded
        (                      # new fieldset added on to the bottom
            'Custom Field Heading',  # group heading of your choice; set to None for a blank space instead of a header
            {
                'fields': (
                    ),
            },
        ),
    )
    def get_queryset(self, request):
        query = super(UserAdmin, self).get_queryset(request)
        query_set = query.filter(is_superuser=False)
        return query_set

admin.site.register(AuthUser, CustomUserAdmin)
admin.site.register(Transaction)
admin.site.register(AvailableBtc)