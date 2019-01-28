from django.contrib import admin
from blog_app.models import Post, Comment, Gallery

# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Gallery)


class GalleryInline(admin.StackedInline):
    model = Gallery
    extra = 0


class PostAdmin(admin.ModelAdmin):
    inlines = [GalleryInline]

    def save_model(self, request, obj, form, change):
        obj.save()

        for afile in request.FILES.getlist('photos'):
            obj.photos.create(image = afile)
