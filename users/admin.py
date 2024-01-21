from django.contrib import admin
from users.models import User, UserProfile


class UserAdmin(admin.ModelAdmin):

    model = User

    list_display = ["email", "phone_number", "otp",
                    "user_suspended", "is_active",
                    "created_at", "updated_at"]
    list_filter = ("user_suspended", "is_active",
                   "created_at")
    search_fields = ["email", "phone_number"]


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("user_first_name", "user_email",
                    "user_is_active", "user_created_at")
    list_filter = ("user__is_active", "user__created_at")
    search_fields = ["user__email", "user__phone_number"]

    def user_first_name(self, obj):
        return obj.user.first_name

    def user_email(self, obj):
        return obj.user.email

    def user_is_active(self, obj):
        return obj.user.is_active

    def user_created_at(self, obj):
        return obj.user.created_at


admin.site.register(User, UserAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
