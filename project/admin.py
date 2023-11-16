from django.contrib import admin
from project.models import Blog, Rating, Comment, Notification

admin.site.register(Blog)
admin.site.register(Rating)
admin.site.register(Notification)
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ( 'content', 'blog', 'created_at', 'active')
    list_filter = ('active', 'created_at')  # Добавляем фильтры для активности и времени создания
    search_fields = ('user',  'content')  # Добавляем поля для поиска
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)  # Кастомная команда для установки active в True для выбранных комментариев
    approve_comments.short_description = 'Approve selected comments'  # Описание для действия в админ-панели
