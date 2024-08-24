from django.contrib import admin

from .models import Post



# Config for admin posts 

@admin.register(Post) #register the model here 
class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'modified') 
    list_display = ('title', 'created', 'modified') 
    date_hierarchy = 'created' 

