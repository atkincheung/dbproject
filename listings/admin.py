from django.contrib import admin
from listings.models import Comment  # Import the Comment model

from django.contrib import admin

# Or, you can specify the fields to be displayed
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'body', 'postId', 'likes', 'user_id', 'username', 'full_name')



# Register your models here.
# Register the Comment model with the custom admin interface
admin.site.register(Comment, CommentAdmin)

# Register your models here.
