from django.shortcuts import render, HttpResponse
from home.models import User, Attendance, Absentie
from django import forms
import dlib
import face_recognition
import cv2
import numpy as np
import matplotlib.pyplot as plt
import base64
from io import BytesIO
import json
from datetime import datetime
from django.utils import timezone
from django.template import loader
from django.db.models import Q


# Create your views here.
def home(request):
   return render(request, 'home.html')
 
def attendance(request):
    if request.method=="POST":
        n=request.POST['capturedImageDataa']
        header_removed_data = n.split(',', 1)[-1]
        decoded_image_data = base64.b64decode(header_removed_data)
        image_array = np.frombuffer(decoded_image_data, dtype=np.uint8)
        image = cv2.imdecode(image_array, cv2.IMREAD_COLOR)
        rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        gray_image_eq = cv2.equalizeHist(cv2.cvtColor(image, cv2.COLOR_BGR2GRAY))
        face_locations = face_recognition.face_locations(rgb_image, number_of_times_to_upsample=2,model='hog' )
        face_encoding=face_recognition.face_encodings(rgb_image,face_locations,model="large",num_jitters=10)
        if face_encoding:
            for encoding in face_encoding:
                for face in Attendance.objects.all():
                    f=np.asarray(list(json.loads(face.image)),dtype=np.float64)
                    np.set_printoptions(precision=20)
                    m=face_recognition.compare_faces(known_face_encodings=[encoding],face_encoding_to_check=f,tolerance=0.4)
                    if m[0]:
                        valu = face.nam
                        current_datetime= datetime.now().strftime('%H:%M:%S')
                        dte = timezone.now().date()
                        try:
                          
                          user = User.objects.get(name=valu, date=dte)
                          user.timeout = current_datetime
                          user.save()
                        except User.DoesNotExist:
                          
                          student = User(name=valu, timein=current_datetime, date=dte)
                          student.save()

                        return render(request, 'attendance.html', {'valu': valu, 'current_datetime': current_datetime, 'dte': dte})
            data_to_display = "Sorry! No face matched"
            return render(request, 'attendance.html', {'data_to_display': data_to_display})
        else:
            data = "No face was detected!!!!"
            return render(request, 'attendance.html', {'data': data})
            
    return render(request, 'attendance.html')





def store(request):
    alldata = User.objects.all()
    context = {'task': alldata}
    return render(request, 'storage.html' , context)

    
    
def register(request):
    if request.method=="POST":
        a=request.POST['name']
        b = request.POST['numbe']
        c= request.POST['emailid']
        d = request.POST['capturedImageData']
        header_removed_data = d.split(',', 1)[-1]
        decoded_image_data = base64.b64decode(header_removed_data)
        image_array = np.frombuffer(decoded_image_data, dtype=np.uint8)
        image = cv2.imdecode(image_array, cv2.IMREAD_COLOR)
        rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        gray_image_eq = cv2.equalizeHist(cv2.cvtColor(image, cv2.COLOR_BGR2GRAY))
        face_locations = face_recognition.face_locations(rgb_image, number_of_times_to_upsample=1,model='hog' )
        face_encoding=face_recognition.face_encodings(rgb_image,face_locations,model="large",num_jitters=10)
        if face_encoding:
            face_encoding_list = face_encoding[0].tolist()
            her= Attendance(nam= a, phon=b, emaill=c, image=face_encoding_list)
            her.save()
        

    return render(request, 'register.html')
    

def absenties(request):
    dati = timezone.now().date()
    attended = User.objects.filter(date=dati)
    present_names = set(attended.values_list('name', flat=True))
    absent_students = Attendance.objects.exclude(nam__in=present_names)
    absent_students_set = set(absent_students.values_list('nam', flat=True))
    for i in absent_students_set:
        if  not Absentie.objects.filter(namee=i,dat=dati).exists():
         stu= Absentie.objects.create(namee=i, dat=dati)
         stu.save()
    for j in present_names:
        Absentie.objects.filter(Q(namee=j, dat=dati)).delete()
    context = {'absent_students': absent_students}
    return render(request, 'absenties.html', context)


def absentrecord(request):
    my= Absentie.objects.all()
    templ = loader.get_template('absentrecord.html')
    con ={
        'value': my,
    }
    return HttpResponse(templ.render(con, request))


    
