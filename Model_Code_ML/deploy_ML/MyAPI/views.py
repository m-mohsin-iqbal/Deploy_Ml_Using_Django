from django.shortcuts import render
from django.http import HttpResponse
# from .forms import myForm
from .forms import ApprovalForm
from rest_framework import viewsets
from rest_framework.decorators import api_view
from django.core import serializers
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from .models import approvals
from .serializers import approvalsSerializers
import pickle
from sklearn.externals import joblib
import json
import numpy as np
from sklearn import preprocessing
import pandas as pd
from django.contrib import messages
# Create your views here.

#
# class ApprovalsView(viewsets.ModelViewSet):
#     queryset = approvalsSerializers.objects.all()
#     serializer_class = approvalsSerializers
#
#
def ohevalue(df):
    ohe_col=joblib.load('E:\machine learning\MyML\loan_model.pkl')
    cat_columns=['Gender','Married','Graduatededucation','Selfemployed','Area']
    df_processed=pd.get_dummies(df,columns=cat_columns)
    print(df_processed)
    newdict={}
    for i in ohe_col:
        if i in df_processed.columns:
            newdict[i]=df_processed[i].values
        else:
            newdict[i]=0
    newdf=pd.DataFrame(newdict)
    return newdf
#
#
# # @api_view(["POST"])
def approvereject(request):
    try:
        mdl=joblib.load("E:\machine learning\MyML\loan_model.pkl")
        mydata=request.data
        unit=np.array(list(mydata.values()))
        unit=unit.reshape(1,-1)
        y_pred=mdl.predict(unit)
        newdf=pd.DataFrame(y_pred,columns=['Status'])
        newdf=newdf.replace({True:'Approved',False:'Rejected'})
        return ('Your Status is {}'.format(newdf))
    except ValueError as e:
        return Response(e.args[0],status.HTTP_400_BAD_REQUEST)


def cxcontact(request):
    if request.method=='POST':
        form=ApprovalForm(request.POST)
        if form.is_valid():
            Firstname=form.cleaned_data['Firstname']
            Lastname=form.cleaned_data['Lastname']
            Depandants = form.cleaned_data['Depandants']
            Applicationincome = form.cleaned_data['Applicationincome']
            Coapplicationincome = form.cleaned_data['Applicationincome']
            Loanamt = form.cleaned_data['Loanamt']
            Loanterm = form.cleaned_data['Loanterm']
            Credithistory = form.cleaned_data['Credithistory']
            Gender = form.cleaned_data['Gender']
            Married = form.cleaned_data['Married']
            Graduatededucation = form.cleaned_data['Graduatededucation']
            Selfemployed = form.cleaned_data['Selfemployed']
            Area = form.cleaned_data['Area']
            myDict=(request.POST).dict()
            df=pd.DataFrame(myDict,index=[0])
            answer=approvereject(ohevalue(df))
            messages.success(request,'Application status {}'.format(answer))

    form=ApprovalForm()
    return render(request,'myform/form.html',{'form':form})

# def album(request):
#     return HttpResponse("Hellow How are you")