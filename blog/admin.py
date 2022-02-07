from django.contrib import admin
from .models import Post, Tag
# Register your models here.


class TagAdmin(admin.ModelAdmin):
    list_display = ('name', )
    list_filter = []
    search_fields = ('name', )


class PostAdmin(admin.ModelAdmin):
    list_display = ('title_en', 'title_de', 'slug', 'created_at', 'photo')
    list_filter = ['tags']
    search_fields = ('title_en', 'title_de', )


admin.site.register(Post, PostAdmin)
admin.site.register(Tag, TagAdmin)