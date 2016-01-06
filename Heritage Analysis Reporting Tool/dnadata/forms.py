from django.forms import ModelForm,Form,FileField
from .models import DNAKitUpload

class UploadForm(ModelForm):
    class Meta:
        model = DNAKitUpload
        fields = "__all__"
        exclude = ['uploaded','uploadType','filename','log','status']



class FileUploadForm(Form):
    """File upload Form"""
    uploadFile = FileField()
