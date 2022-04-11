from django.shortcuts import render
from django.http.response import JsonResponse, HttpResponse
from rest_framework import status
from Book_store.models import *
from Book_store.serializers import *
from rest_framework.decorators import api_view, parser_classes

# Create your views here.
@api_view(['GET','POST','DELETE','PUT'])

def BOOK(request):
    if request.method=="POST":
        finop_data = request.data
        print(finop_data)
        fo_serializer = BKSerializer(data=finop_data,many=True)
        if fo_serializer.is_valid():
            print(fo_serializer)
            fo_serializer.save()
        return JsonResponse(fo_serializer.data,safe=False)
    if request.method=="GET":
        c=request.GET.get('filter')
        d=request.GET.get('category')
        print(d)
        if c == 'ALL' :
            finop_data = Books.objects.all()
        if c == 'CATEGORY':
            finop_data = Books.objects.filter(type_book=d)
        vm_serializer = BKSerializer(finop_data,many=True)
        return JsonResponse(vm_serializer.data,safe=False)
    if request.method=="DELETE":
        id=request.GET.get('id')
        finop_data = Books.objects.filter(book_id=id).delete()
        
        return JsonResponse('deleted',safe=False)

    if request.method=="PUT":
        id=request.GET.get('id')
        print(id)
        data=request.data
        finop_data = Books.objects.filter(book_id=id)
        
            
        return JsonResponse('errors',safe=False)


@api_view(['GET','POST','DELETE'])

def USERS(request):
    finop_data = request.data
    print(finop_data)
    fo_serializer = URSerializer(data=finop_data,many=True)
    if fo_serializer.is_valid():
        print(fo_serializer)
        fo_serializer.save()
    return JsonResponse(fo_serializer.data,safe=False)