from django.forms import ImageField
from django.shortcuts import render, redirect
from .forms import MessageForm
from django.http import HttpResponse
from .forms import *
from .models import *
from django.core.files.storage import FileSystemStorage
from yolov5 import detect
from django.shortcuts import render
import pyrebase

# rest of the code above
# Below is the post method of a 
# ObjectDetectionTemplateView
def post(self, image):
    #img_id = kwargs.get("id")
    #image_qs = ImageField.objects.get(id=img_id)
    detect.run(source=image.image.path, 
               iou_thres=0.45, line_thickness=1,
               project="media/runs/detect")  
  
def success(request):
    return HttpResponse('successfully uploaded')