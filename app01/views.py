from django.shortcuts import render, HttpResponse, HttpResponsePermanentRedirect, redirect
from app01 import models
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

# Create your views here.
from app01 import forms


def UploadFile(request):
    uf = forms.FileForm(request.POST, request.FILES)
    if uf.is_valid():
        upload = models.UploadFile()
        upload.userid = 1
        upload.file = uf.cleaned_data['ExcelFile']
        upload.save()

        print(upload.file)
    if request.is_ajax():
        return JsonResponse("上传成功",safe=False)
    return render(request, 'upload.html', locals())
