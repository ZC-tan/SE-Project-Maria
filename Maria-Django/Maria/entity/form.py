# from ckeditor_uploader.widgets import CKEditorUploadingWidget
# from ckeditor.widgets import CKEditorWidget
from django import forms
from entity.models import *

class DocForm(forms.ModelForm):
    # content = forms.CharField(widget=CKEditorUploadingWidget,label='详情',required=True)
    class Meta:
        model = Doc
        fields = ['title','content',]