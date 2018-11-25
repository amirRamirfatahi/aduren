from django.contrib import admin
from .models import Project, FirstPageProjects, ContactUs, SlideShowPicture, Prize, Founder, Artist, Client, Service\
    , AboutUs


class ProjectAdmin(admin.ModelAdmin):
    pass


admin.site.register(Project, admin.ModelAdmin)
admin.site.register(FirstPageProjects, admin.ModelAdmin)
admin.site.register(ContactUs, admin.ModelAdmin)
admin.site.register(SlideShowPicture, admin.ModelAdmin)
admin.site.register(Prize, admin.ModelAdmin)
admin.site.register(Founder, admin.ModelAdmin)
admin.site.register(Artist, admin.ModelAdmin)
admin.site.register(Client, admin.ModelAdmin)
admin.site.register(Service, admin.ModelAdmin)
admin.site.register(AboutUs, admin.ModelAdmin)

admin.site.site_header = 'Aduren Administration'
admin.site.site_title = 'Aduren'
admin.site.index_title = 'Aduren'
