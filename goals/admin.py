from django.contrib import admin

from goals.models.category import GoalCategory
from goals.models.comment import GoalComment
from goals.models.goal import Goal


class GoalAdmin(admin.ModelAdmin):
    list_display = ('title',
                    'description',
                    'status',
                    'priority',
                    'due_date',
                    'user',
                    'category',
                    'created',
                    'updated'
                    )
    search_fields = ('title',
                     'user',
                     'status',
                     'priority',
                     'category',
                     'due_date'
                     )


class GoalCategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'created', 'updated')
    search_fields = ('title', 'user')


class GoalCommentAdmin(admin.ModelAdmin):
    list_display = ('text', 'goal', 'user', 'created', 'updated')
    search_fields = ('title', 'user', 'goal')


admin.site.register(Goal, GoalAdmin)
admin.site.register(GoalCategory, GoalCategoryAdmin)
admin.site.register(GoalComment, GoalCommentAdmin)