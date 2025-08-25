from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json, requests
from django.conf import settings
from account.models import Account
from .serializer import ResgisterSerializer
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404

class GeminiChatAPIView(APIView):

     def post(self,request):
        # Optional simple token protection
        proxy_token = getattr(settings,'PROXY_TOKEN',None)
        if proxy_token :
             token = request.headers.get('X-PROXY-TOKEN')
             if proxy_token != token:
                  return Response({'error':'unauthorized!'},status = status.HTTP_401_UNAUTHORIZED)
        
        
        #Get prompt from request data
        prompt = request.data.get("prompt")
        if not prompt:
             return Response({'error':"field 'prompt' is required"}, status = status.HTTP_400_BAD_REQUEST)
        #Build Gemini payload
        payload = {"contents": [{"parts": [{"text": prompt}]}]}


        #Build Gemini header
        headers = {
             "Content-Type":"application/json",
             "x-goog-api-key":settings.GEMINI_API_KEY,
        }
        response = requests.post(
             "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent",
             headers = headers,
             json=payload,
             timeout = 20
        )
        if response.status_code != 200 :
             try:
                  return Response(response.json(),status=response.status_code)
             except:
                  return Response({'error':'Gemini error','status':response.status_code},status = response.status_code )
        data = response.json()
        text=""
        try:
             text = data['candidates'][0]['content']['parts'][0].get('text')
        except:
             pass
        return Response({'text':text},status=status.HTTP_200_OK)     
     

@api_view(['POST','GET','PUT','PATCH','DELETE'])
def register(request,id=None):
     
     if request.method == 'POST':
          serializer = ResgisterSerializer(data=request.data)
          if serializer.is_valid():
               serializer.save()
               return Response({'message':'your data has been saved'},status=status.HTTP_200_OK)
          return Response({'message':'something went wrong'},status=status.HTTP_400_BAD_REQUEST)
     
     elif request.method in ['PUT','PATCH']:
          data = request.data
          user = get_object_or_404(Account,id=id)
          partial = request.method == 'PATCH'
          serializer = ResgisterSerializer(user,data,partial=partial)
          if serializer.is_valid():
               serializer.save()
               return Response({'message':'your data has been saved'},status=status.HTTP_200_OK)
          return Response({'message':'something went wrong'},status=status.HTTP_400_BAD_REQUEST)
          
     elif request.method == ''
