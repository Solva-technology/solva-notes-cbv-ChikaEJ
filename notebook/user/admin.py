from django.contrib import admin
from django.contrib.auth import get_user_model
from note.models import Category, Note, Status
from user.models import UserProfile

User = get_user_model()


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username'] + [field.name for field in User._meta.fields if
                                   field.name != 'username']
    list_display_links = ('username',)
    ordering = ('id',)
    fields = [field.name for field in User._meta.fields if
              field.name not in ('id', 'password')]


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio', 'birth_date')
    list_display_links = ('user',)
    search_fields = ('user__username', 'bio')
    ordering = ('user',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    list_display_links = ('title',)
    search_fields = ('title',)
    ordering = ('title',)


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_final')
    list_display_links = ('name',)
    list_filter = ('is_final',)
    ordering = ('name',)


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = (
        'short_text',
        'created_at',
        'author',
        'status',
        'categories'
    )
    list_display_links = ('short_text',)
    search_fields = ('text', 'author__name')
    list_filter = ('status', 'categories')
    ordering = ('-created_at',)
    filter_horizontal = ('categories',)

    def categories(self, obj):
        return ", ".join([c.name for c in obj.categories.all()])

    categories.short_description = "Категории"

    def short_text(self, obj):
        return (obj.text[:20] + '...') if len(obj.text) > 20 else obj.text

    short_text.short_description = "Текст"
