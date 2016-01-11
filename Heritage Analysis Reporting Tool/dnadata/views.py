from django.shortcuts import render,redirect,get_object_or_404,HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from .models import DNAKitUpload,Family,ExampleModel
from .forms import UploadForm,FileUploadForm
from .readFile import readFile
@login_required
def upload(request):
    if request.method == 'POST':
        dnakitupload = DNAKitUpload(status='Success',filename='tbd',log='xxx', filesInfo=request.POST.get("files",""))
        #dnakitupload.files.get_attname()
        form = UploadForm(request.POST, request.FILES, instance=dnakitupload)
        if form.is_valid():
            form.save()
            dnakitupload.filesInfo=request.POST.get("filesInfo","")
            dnakitupload.save()
            readFile(dnakitupload.kit,dnakitupload.filesInfo.path)
            return render(request, "dnadata/uploadresults.html")
        else:
            return render(request,'dnadata/upload.html', {'form': form })
    else:
        form = UploadForm()
        return render(request,'dnadata/upload.html', {'form': form })
# Create your views here.

@login_required
def new_uploadresults(request):
    return render(request, "dnadata/uploadresults.html")


@login_required
def family(request, pk):
    familyId= get_object_or_404(Family, pk=pk)
    return render(request, "dnadata/family.html")


def uploadFile(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if True: #form.is_valid():
            m = ExampleModel()
            m.model_pic = form['uploadFile']
            m.save()
            return HttpResponse('image upload success')
        else:
            return HttpResponse('image upload failure')
    else:
        return render(request,'dnadata/uploadFile.html')