from django.shortcuts import render #importing the rendering facilites
from django.http import HttpResponse
def index(request):
     return render(request,'index.html')     #render is the function is the function which takes first argument request and second templetes name and third is if you want to give parameters


def analyzer(request):  #analyzer is an end point which used in urls.py
     djtext =(request.POST.get('text','default'))   #this is method to take the responce from html form used by action attributes   here text is name of field in html form
     repunct=request.POST.get('repunctuations','default')
     caps=request.POST.get('caps','default')
     newlre=request.POST.get('newlre','default')
     charc=request.POST.get('charc','default')

     # print(djtext)
     # print(repunct)

     if(repunct=='on'):    #repunct is a check box in html fiel so here we are we are checking the responce of checkbox to perform the desiered action
         analyzed = ""
         pu="!@#$%^&*(){}:;''[]/?.,><"
         for char in djtext:
             if char not in pu:
                 analyzed=analyzed+char
         djtext=analyzed
     if(caps=='on'):
         analyzed = ""
         for char in djtext:
             analyzed=analyzed+ char.upper()
         djtext=analyzed
     if (newlre == 'on'):
         analyzed = ""
         for char in djtext:
             if(char!="\n"):
              analyzed=analyzed+char
         djtext=analyzed

     param = {'purpose': 'To convert uper case', 'analyzed_text': djtext}
     return render(request, 'analyze.html', param)



# def removechar(request):
#      return HttpResponse('''char remover <a href="http://127.0.0.1:8000/"> back</a>''')
#
#
# def capfirstletter(request):
#      return HttpResponse('''capitilize first char <a href="http://127.0.0.1:8000/"> back</a>''')
#
#
# def spaceremover(request):
#      return HttpResponse('''space remover <a href="http://127.0.0.1:8000/"> back</a>''')
#
#
# def charcount(request):
#      return HttpResponse('''char counter <a href="http://127.0.0.1:8000/"> back</a>''')