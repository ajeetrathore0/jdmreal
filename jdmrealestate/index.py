from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render
from django.http import request,response,JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

def index(request):
    return redirect('/assets')

def check_data(request):
    data=request.GET.get('name')
    print(data)
    return HttpResponse(data)


import ssl
from urllib.request import urlopen
ssl._create_default_https_context = ssl._create_unverified_context


@csrf_exempt
def ignougradecard(request):
    if request.method=='POST':
       bd=json.loads(request.body)
       type=bd['type']
       enrollmentno=bd['enrollmentno']
       program=bd['program']
       url = 'https://gradecard.ignou.ac.in/gradecard/view_gradecard.aspx?eno='+enrollmentno+'&prog='+program+'&type='+type;

       try:
    # Open the URL
         with urlopen(url) as response:
        # Read the HTML content
              html = response.read().decode('utf-8')  # Assuming the content is in UTF-8 encoding

        # Print the HTML
             
              return JsonResponse({'html':html})
              print(html)
       except Exception as e:
         return JsonResponse({'html':'thisisht'})

    else:
       return HttpResponse('thisisgragedcardapi') 


@csrf_exempt
def assignmentstatus(request):
    if request.method=='POST':
       bd=json.loads(request.body)
       type=bd['type']
       enrollmentno=bd['enrollmentno']
       program=bd['program']
    #    url = 'https://gradecard.ignou.ac.in/gradecard/view_gradecard.aspx?eno='+enrollmentno+'&prog='+program+'&type='+type;
       url='https://isms.ignou.ac.in/changeadmdata/StatusAssignment.asp?submit=1&enrno='+enrollmentno+'&program='+program;

       try:
    # Open the URL
         with urlopen(url) as response:
        # Read the HTML content
              html = response.read().decode('utf-8')  # Assuming the content is in UTF-8 encoding

        # Print the HTML
             
              return JsonResponse({'html':html})
              print(html)
       except Exception as e:
         return JsonResponse({'html':'thisisht'})

    else:
       return HttpResponse('thisisgragedcardapi') 

