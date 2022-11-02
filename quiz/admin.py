from django.contrib import admin
from quiz.models import Category, Question, Pet, Game

class CategoryAdmin(admin.ModelAdmin):
    list_display= ['id', 'name']

class PetAdmin(admin.ModelAdmin):
    list_display= ['id', 'name']

class QuestionAdmin(admin.ModelAdmin):
    list_display= ['id', 'category', 'true_answer']

class GameAdmin(admin.ModelAdmin):
    list_display= ['id', 'category', 'pet', 'player_name', 'is_finished', 'total_score']

admin.site.register(Category, CategoryAdmin)
admin.site.register(Pet, CategoryAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Game, GameAdmin)