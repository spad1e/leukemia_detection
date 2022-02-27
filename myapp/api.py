from doctest import BLANKLINE_MARKER
from email.mime import image
from importlib.resources import path
from msilib import schema
from random import SystemRandom
from ninja import NinjaAPI, Form, Path, Schema, File
from ninja.files import UploadedFile

from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.core.files.storage import FileSystemStorage

from .models import myModel
from .forms import *
from .views import *

import base64

import os, sys, shutil

from PIL import Image

api = NinjaAPI()


@api.get("/add")
def add(request, a: int, b: int):
    return {"result": a + b}

@api.get("/test")
def add2(request):
    return HttpResponse("<h>Hello World!</h>")

@api.get("/upload")
def index(request):
    folder = 'media/images'
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))
    return render(request, 'index2.html', {'form': MessageForm()})

@api.post("/upload", url_name='upload')
def upload(request, blood_smear_image: UploadedFile = File(...)):
    path = blood_smear_image
    a = myModel()
    a.image = path
    a.save()
    folder = 'media/runs/detect'

    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))

    detect.run(source=a.image.path, iou_thres=0.45, line_thickness=1, project="media/runs/detect")  
    detectDesc = os.listdir('media/runs/detect/exp/labels')
    print("-------------------------------------")
    print("-------------------------------------")
    print("-------------------------------------")
    detectImgUrl = '../../media/runs/detect/exp/' + a.image.url.removeprefix("/media/images/")
    img = Image.open('media/runs/detect/exp/' + a.image.url.removeprefix("/media/images/"))

    names = ['Atypical lymphocyte', 'Band Neutrophil', 'Basophil', 'Blast', 'Eosinophil', 'Lymphocyte', 'Metamyelocyte', 'Monocyte', 'Myelocyte', 'NRC', 'Promyelocyte', 'Segmented neutrophil']
    myproject_path = os.getcwd()
    os.chdir('media')
    os.chdir('runs')
    os.chdir('detect')
    os.chdir('exp')
    os.chdir('labels')
    infolist = []
    namelist = []
    with open(detectDesc[0]) as f:
        i = 1
        while True:
            line = f.readline()
            print(line)
            if not line:
                break
            linelist = line.split()
            print(linelist)
            print(len(linelist))
            linelist[0] = names[int(linelist[0])]
            infolist.append(linelist)
            i += 1
    print(infolist)
    os.chdir(myproject_path)
    print(len(infolist[0]))
    return render(request, 'index3.html', {'data': a, 'data2': detectImgUrl, 'info': infolist, 'name': namelist})