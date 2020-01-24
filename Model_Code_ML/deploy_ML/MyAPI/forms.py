from django import forms


class ApprovalForm(forms.Form):
    Firstname = forms.CharField(max_length=15)
    Lastname = forms.CharField(max_length=15)
    Depandants = forms.IntegerField()
    Applicationincome = forms.IntegerField()
    Coapplicationincome = forms.IntegerField()
    Loanamt = forms.IntegerField()
    Loanterm = forms.IntegerField()
    Credithistory = forms.IntegerField()
    Gender = forms.ChoiceField( choices=[('Male','Male'),('Female','Female')])
    Married = forms.ChoiceField( choices=[('Yes','Yes'),('No','No')])
    Graduatededucation = forms.ChoiceField(choices=[('Graduated','Graduated'),('Not_Graduate','Not_Graduated')])
    Selfemployed = forms.ChoiceField(choices=[('Yes','Yes'),('No','No')])
    Area = forms.ChoiceField(choices=[('Rural','Rural'),('Semiurban','Semiurban'),('Urban','Urban')])
