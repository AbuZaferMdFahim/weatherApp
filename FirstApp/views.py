from django.shortcuts import render
import requests
import datetime

def index(request):

    if 'city' in request.POST:
        city = request.POST['city']
    else:
        city = 'dhaka'

    appid = '243614ca09eeeb3581d5e84ec9d59dc9'
    URL = 'https://api.openweathermap.org/data/2.5/weather'
    PARAMETER = {'q': city, 'appid': appid, 'units': 'metric'}

    r= requests.get(url=URL, params=PARAMETER)
    res = r.json()
    description = res['weather'][0]['description']
    icon = res['weather'][0]['icon']
    temp = res['main']['temp']
    day = datetime.date.today()
    return render(request, 'weatherapp/index.html',{'description': description, 'icon': icon,'day': day, 'temp': temp,'city': city})

















'''from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from FirstApp.models import Contact
from FirstApp.serializers import ContactSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import Http404
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import generics
from rest_framework.authentication import SessionAuthentication, BasicAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.reverse import reverse'''

'''HyperLink Start
@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'contact': reverse('contact-list', request=request, format=format),
        
    })
    Hyperlink'''

''' Model View API Start
@csrf_exempt
def restapi_list(request):
    if request.method == 'GET':
        objectall = Contact.objects.all()
        serializer = ContactSerializer(objectall, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ContactSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    
@csrf_exempt
def restapi_detail(request, pk):
    try:
        detailsall = Contact.objects.get(pk=pk)
    except Contact.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ContactSerializer(detailsall)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ContactSerializer(detailsall, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        Contact.delete()
        return HttpResponse(status=204)
       
    Model View API End '''

''' View Decorator API

@api_view(['GET', 'POST'])
def restapi_list(request):
    if request.method == 'GET':
        req = Contact.objects.all()
        serializer = ContactSerializer(req, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET', 'PUT', 'DELETE'])
def restapi_detail(request, pk):
  
    try:
        res = Contact.objects.get(pk=pk)
    except Contact.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ContactSerializer(res)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ContactSerializer(res, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        res.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    View Decorator End'''

'''Class BASED VIEW START

class BlogList(APIView):
 
    def get(self, request, format=None):
        a = Contact.objects.all()
        serializer = ContactSerializer(a, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ApiDetail(APIView):
    def get_object(self, pk):
        try:
            return Contact.objects.get(pk=pk)
        except Contact.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        a = self.get_object(pk)
        serializer = ContactSerializer(a)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        a = self.get_object(pk)
        serializer = ContactSerializer(a, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        a = self.get_object(pk)
        a.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

Class Based view END '''

'''Using mixing Start
class ContactList(generics.ListCreateAPIView, mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    #authentication_classes = [SessionAuthentication, BasicAuthentication]
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)
    
class GenericApiDetail(generics.RetrieveUpdateDestroyAPIView, mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    
    Using mixing END'''

'''View And Routers Start
from django.shortcuts import get_object_or_404
from FirstApp.serializers import ContactSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from FirstApp.models import Contact
from rest_framework import status

class ContactViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Contact.objects.all()
        serializer = ContactSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Contact.objects.all()
        contact = get_object_or_404(queryset, pk=pk)
        serializer = ContactSerializer(contact)
        return Response(serializer.data)
    
    def create(self,request):
        serializer = ContactSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
    def update(self, request, pk=None):
        contact = Contact.objects.get(pk=pk)
        serializer = ContactSerializer(contact,data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
View And Routers END'''


