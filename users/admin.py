from django.contrib import admin

from users.models import CustomUser, Post, Comment

# class LessonAdmin(admin.ModelAdmin):
#     list_display = ['name', 'preview', 'description', 'reference']

admin.site.register(CustomUser)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    list_display = ['post_author']
    list_filter = ['date_creation']

admin.site.register(Comment)
# class ProductAdmin(admin.ModelAdmin):
#     # '','preview', , 'date_of_creation', 'date_last_change'
#     list_display = ['id', 'product_name', 'category', 'price_per_unit']
#     list_filter = ['category']
#     search_fields = ("product_name", "product_description", )
