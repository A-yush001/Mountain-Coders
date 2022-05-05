from django.contrib import admin
from blog.models import Blog,Contact

class BlogAdmin(admin.ModelAdmin):
    class Media:
       
        js=("js/blog.js",)


admin.site.register(Blog, BlogAdmin)
admin.site.register(Contact)
