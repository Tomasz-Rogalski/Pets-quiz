from django.contrib import admin
from quiz.models import Category, Question, Pet, Game

class CategoryAdmin(admin.ModelAdmin):
    '''class to represent category model in admin panel'''
    list_display= ['id', 'name']

class PetAdmin(admin.ModelAdmin):
    '''class to represent pet model in admin panel'''
    list_display= ['id', 'name']

class QuestionAdmin(admin.ModelAdmin):
    '''class to represent question model in admin panel'''
    list_display= ['id', 'category', 'true_answer']

class GameAdmin(admin.ModelAdmin):
    '''class to represent game model in admin panel'''
    list_display= ['id', 'category', 'pet', 'player_name', 'is_finished', 'total_score']

admin.site.register(Category, CategoryAdmin)
admin.site.register(Pet, CategoryAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Game, GameAdmin)
