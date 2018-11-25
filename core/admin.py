from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Project, FirstPageProjects, ContactUs, SlideShowPicture, Award, Founder, Artist, Client, Service \
    , AboutUs


class ProjectAdmin(admin.ModelAdmin):
    pass


class FirstPageProjectsAdmin(admin.ModelAdmin):
    filter_horizontal = ('projects',)

    def has_add_permission(self, request):
        model = self.model
        if model.objects.count() > 0:
            return False
        return True


class ContactUsAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        model = self.model
        if model.objects.count() > 0:
            return False
        return True


class AboutUsAdmin(SummernoteModelAdmin):
    filter_horizontal = ('slide_show_pictures', 'awards', 'founders', 'artists', 'clients', 'services')
    summernote_fields = ('about_us_text',)

    def has_add_permission(self, request):
        model = self.model
        if model.objects.count() > 0:
            return False
        return True


admin.site.register(Project, admin.ModelAdmin)
admin.site.register(FirstPageProjects, FirstPageProjectsAdmin)
admin.site.register(ContactUs, ContactUsAdmin)
admin.site.register(SlideShowPicture, admin.ModelAdmin)
admin.site.register(Award, admin.ModelAdmin)
admin.site.register(Founder, admin.ModelAdmin)
admin.site.register(Artist, admin.ModelAdmin)
admin.site.register(Client, admin.ModelAdmin)
admin.site.register(Service, admin.ModelAdmin)
admin.site.register(AboutUs, AboutUsAdmin)

admin.site.site_header = 'Aduren Administration'
admin.site.site_title = 'Aduren'
admin.site.index_title = 'Aduren'
