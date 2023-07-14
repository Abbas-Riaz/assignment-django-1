from django.shortcuts import render ,redirect
from django.http import HttpResponse

# Create your views here.
room =['one' ,'two' , 'three ' , 'four' ] 
courses= ['python' ,'javascript' ,'HTML']
def home (request) :
    my_dict= {'Pages' : ['one' ,'two' , 'three ' , 'four' ] ,
              'Courses' : ['backend' ,'frontend']}
    
    return render (request , 'app/detail.html', context=my_dict)
def index (request) :
   my_dict= {'Pages' : room , 'Courses'  : courses}
   return render (request , 'app/index.html', context=my_dict)
def red (request) :
    return redirect ('ab:ind')
