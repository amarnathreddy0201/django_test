from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect

from django.urls import reverse
from datetime import date,time

import logging
# add this line
from django.templatetags.static import static
from django.shortcuts import render
from django.contrib import messages
from .forms import EventsForm
from django.shortcuts import render
from rest_framework import generics
import io, csv, pandas as pd
from rest_framework.response import Response
from rest_framework import status


from .serializers import FileUploadSerializer
from .models import Files



def index(request):
    return render(request,"index.html")

 
# remember to import the File model
# remember to import the FileUploadSerializer and SaveFileSerializer
class UploadFileView(generics.CreateAPIView):
    serializer_class = FileUploadSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        file = serializer.validated_data['file']
        reader = pd.read_csv(file,low_memory=False)
        rows10=[]
        for _, row in reader.iterrows():
            rows10.append(row)
            new_file = Files(
                banknifty = row['BANKNIFTY'],
                date= row["DATE"],
                time= row['TIME'],
                open= row["OPEN"],
                high= row["HIGH"],
                low=row["LOW"],
                close=row["CLOSE"],
                volume=row["VOLUME"],
            )
            new_file.save()
            ro_ws10=rows10[0:11]

            d=ro_ws10[0][2]
            highest_time=None
            for data in ro_ws10:
                if(time(d)> time(data[2])):
                    highest_time=data

            print(highest_time)
        return Response({"status": "success"},status.HTTP_201_CREATED)