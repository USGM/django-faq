from django.contrib import admin
from models import Question, Topic

class QuestionAdmin(admin.ModelAdmin):
    list_display = ['text', 'sort_order', 'status']
    list_editable = ['sort_order', 'status']
        
admin.site.register(Question, QuestionAdmin)
admin.site.register(Topic, admin.ModelAdmin)
