from django.contrib import admin, messages
from django.shortcuts import redirect
from django.utils.translation import gettext_lazy as _

from one.base.utils.admin import FORMFIELD_OVERRIDES_DICT

from .models import App, EtsyAuth, Listing, ListingFile, Shop


@admin.register(App)
class AppAdmin(admin.ModelAdmin):
    formfield_overrides = FORMFIELD_OVERRIDES_DICT
    list_display = ("name", "keystring", "redirect_uri", "scopes")
    actions = ["request_auth"]

    @admin.action(description="👤 Request Etsy auth")
    def request_auth(modeladmin, request, queryset):
        if queryset.count() == 1:
            return redirect(queryset.first().request_auth_url)
        messages.error(request, _("Select just one object"))


@admin.register(EtsyAuth)
class UserShopAuthAdmin(admin.ModelAdmin):
    list_display = ("__str__", "etsy_user_id", "shop_id", "app", "user", "expires_at")
    readonly_fields = [f.name for f in EtsyAuth._meta.fields]
    actions = ["refresh"]

    def has_add_permission(self, request):
        return False

    @admin.action(description="🔄 Refresh token")
    def refresh(modeladmin, request, queryset):
        for obj in queryset:
            api = obj.get_api_client()
            api.refresh()


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    formfield_overrides = FORMFIELD_OVERRIDES_DICT
    list_display = ("shop_name", "etsy_auth")



@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    list_display = ("title", "etsy_auth")
    readonly_fields = (
        "state",
        "creation_timestamp",
        "created_timestamp",
        "ending_timestamp",
        "original_creation_timestamp",
        "last_modified_timestamp",
        "updated_timestamp",
        "state_timestamp",
        "featured_rank",
        "url",
        "num_favorers",
        "non_taxable",
        "is_private",
        "language",
        "state",
        "creation_timestamp",
        "created_timestamp",
        "ending_timestamp",
        "original_creation_timestamp",
        "last_modified_timestamp",
        "updated_timestamp",
        "state_timestamp",
        "featured_rank",
        "url",
        "num_favorers",
        "non_taxable",
        "is_private",
        "language",
    )


@admin.register(ListingFile)
class ListingFileAdmin(admin.ModelAdmin):
    pass


