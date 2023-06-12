from django.contrib import admin

from app.models import UserStandardAnswers, StandardQuestions


class UserStandardAnswersInline(admin.TabularInline):
    model = UserStandardAnswers
    extra = 0


class StandardQuestionsAdmin(admin.ModelAdmin):
    inlines = [UserStandardAnswersInline]


admin.site.register(StandardQuestions, StandardQuestionsAdmin)