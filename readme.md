<h1>Django实现ajax上传文件实例</h1>

html:

    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Title</title>
    </head>
    <body>
    <div>
        {{ up.ExcelFile }}
        <input type="file" name="ExcelFile" id="id_ExcelFile"/>
        <input type="button" id="submitj" value="提交"/>
    </div>
    
    
    <script src="/static/js/jquery-1.10.2.min.js"></script>
    <script>
        $('#submitj').bind("click", function () {
            var file = $('#id_ExcelFile')[0].files[0];
            var form = new FormData();
            form.append('ExcelFile', file);
            $.ajax({
                type: 'POST',
                url: '',
                data: form,
                processData: false,  // tell jQuery not to process the data
                contentType: false,  // tell jQuery not to set contentType
                success: function (arg) {
                    alert(arg);
                }
            })
        })
    </script>
    </body>
    </html>
    
Form:
    
    #!/usr/bin/env python
    #coding:utf-8
    from django import forms
    class FileForm(forms.Form):
        ExcelFile = forms.FileField()
        
models:

    from django.db import models
    # Create your models here.
    
    class UploadFile(models.Model):
        userid = models.CharField(max_length=30)
        file = models.FileField(upload_to='./upload/')
        date = models.DateTimeField(auto_now_add=True)
    
        def __str__(self):
            self.userid

View:

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
        
urls:

    from django.conf.urls import url
    from django.contrib import admin
    from app01 import views as app01
    urlpatterns = [
        url(r'^admin/', admin.site.urls),
        url(r'^upload/', app01.UploadFile),
    ]
    
