from django.shortcuts import render
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
from django.core.files import File
# Create your views here.
class FileView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(FileView, self).dispatch(*args, **kwargs)
   
    def post(self, request):
        data=request.body
        
        f=open("{0}.txt","w+").format(data['title'])
        f.write("{1}").format(data['content'])
        f.close()
        
        return HttpResponse(status=200)