#!/usr/bin/env python
#coding:utf-8
from django import forms
class FileForm(forms.Form):
    ExcelFile = forms.FileField()