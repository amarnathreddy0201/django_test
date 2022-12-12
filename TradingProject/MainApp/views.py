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



# def read_csv(request):
#     data={}
#     if "GET" == request.method:
#         return render(request, "nifty.html", data)
#     try:
#         csv_file = request.FILES["csv_file"]
#         print(csv_file)
        
#         if not csv_file.name.endswith('.csv'):
#             messages.error(request,'File is not CSV type')
#             return HttpResponseRedirect(reverse("read_csv"))
        
#         file_data = csv_file.read().decode("utf-8")
#         lines = file_data.split("\n")
        
#         #loop over the lines and save them in db. If error , store as string and then display
#         for line in lines:
            
#             fields = line.split(",")
            
#             data_dict = {}
# 			#data_dict["name"] = fields[0]
#             data_dict["date"] =fields[1]
            
#             data_dict["time"] = fields[2]
# 			#data_dict[""] = fields[3]
#             #print("data_dict",data_dict)
#             try:
#                 form = EventsForm()
#                 if form.is_valid():
#                     form.save()					
#                 else:
#                     logging.getLogger("error_logger").error(form.errors.as_json())												
#             except Exception as e:
#                 logging.getLogger("error_logger").error(repr(e))
#                 pass
#     except Exception as e:
#         logging.getLogger("error_logger").error("Unable to upload file. "+repr(e))
#         messages.error(request,"Unable to upload file. "+repr(e))

#     return HttpResponseRedirect(reverse("read_csv"))



# remember to import the File model
# remember to import the FileUploadSerializer and SaveFileSerializer
class UploadFileView(generics.CreateAPIView):
    serializer_class = FileUploadSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        file = serializer.validated_data['file']
        reader = pd.read_csv(file,low_memory=False)
        for _, row in reader.iterrows():
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
        return Response({"status": "success"},status.HTTP_201_CREATED,json=new_file)