from django.contrib import admin
from .models import *
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms


class QuestionAdminForm(forms.ModelForm):
    text = forms.CharField(label="Задача", widget=CKEditorUploadingWidget())
    class Meta:
        model=Question
        fields = '__all__'

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Theme)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'point')
    list_filter = ('category',)
    form=QuestionAdminForm

@admin.register(Variant)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('number',)
