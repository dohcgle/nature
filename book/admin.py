from django import forms
from django.contrib import admin
from book.models import Topic, Page
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class TopicAdminForm(forms.ModelForm):
    content = forms.CharField(label="Kontent", widget=CKEditorUploadingWidget())

    class Meta:
        model = Topic
        fields = '__all__'


class TopicAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    form = TopicAdminForm


admin.site.register(Topic, TopicAdmin)


class PapeAdminForm(forms.ModelForm):
    content = forms.CharField(label="Kontent", widget=CKEditorUploadingWidget())

    class Meta:
        model = Page
        fields = '__all__'


class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'is_published', 'created_at')
    list_display_links = ('title',)
    list_editable = ('category', 'is_published',)
    search_fields = ('title', 'category', 'content')
    prepopulated_fields = {"slug": ("title",)}
    form = PapeAdminForm


admin.site.register(Page, PageAdmin)
