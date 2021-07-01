from django.contrib import admin
from .models import Question, Choice

#for changing the view of admin area
admin.site.site_header = 'PollApp Admin'
admin.site.site_title = 'PollApp Admin Panel'
admin.site.index_title = 'POllapp'


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

#modelAdmin has several options for dealing with customizing the interface. all options are defined on the modelAdmin SUBCLASS
#To display multiple fields on the same line, wrap those fields in their own tuple. 
#fieldsets is a list of two-tuples, in which each two-tuple represents a <fieldset> on the admin form page. (A <fieldset> is a “section” of the form.)
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['question_text']}),
                 ('Date Information', {'fields': ['pub_date'], 'classes':['collapse']}), ]
    inlines = [ChoiceInline]


# admin.site.register(Question)
# admin.site.register(Choice)
admin.site.register(Question, QuestionAdmin)
