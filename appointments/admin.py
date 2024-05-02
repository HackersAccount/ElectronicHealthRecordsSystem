from django.contrib import admin
from .models import (
    Appointment,
    Participant,
    Actor,
    Slot,
    Reason,
    ServiceCategory,
    ServiceType,
    Specialty,
)


class ParticipantInline(admin.TabularInline):
    model = Participant
    extra = 1


class ActorAdmin(admin.ModelAdmin):
    list_display = ("name",)  # Ensure this references valid fields
    search_fields = ("name",)


class AppointmentAdmin(admin.ModelAdmin):
    list_display = (
        "start",
        "status",
        "appointment_type",
        "service_category",
        "service_type",
        "specialty",
    )
    search_fields = (
        "start",
        "status",
        "appointment_type",
        "service_category__name",
        "service_type__name",
        "specialty__name",
    )
    inlines = [ParticipantInline]
    list_filter = (
        "status",
        "appointment_type",
        "service_category",
        "service_type",
        "specialty",
    )


admin.site.register(ServiceCategory)
admin.site.register(ServiceType)
admin.site.register(Specialty)
admin.site.register(Slot)
admin.site.register(Reason)
admin.site.register(Actor, ActorAdmin)
admin.site.register(Appointment, AppointmentAdmin)
