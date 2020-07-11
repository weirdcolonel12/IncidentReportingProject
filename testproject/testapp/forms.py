from django import forms
from .models import ReportingModel, Subincidenttype
from django.forms import ModelForm
from django.forms.widgets import CheckboxSelectMultiple

class ReportingForm(forms.ModelForm):

    class Meta:
        model = ReportingModel
        fields = '__all__'
        labels = {
        "location":"Location",
        "incidentdescription":"Incident Description",
        "date":"*Date and Time of Incident",
        "incidentlocation":"Incident Location",
        "internalseverity":"Internal Severity",
        "suspectedcause":"Suspected Cause",
        "immediateactionstaken":"Immediate Actions Taken",
        "subincidenttypes":"Sub Incident Types",
        "reportedby":"Reported By"
        }

    def __init__ (self, *args, **kwargs):
        super(ReportingForm, self).__init__(*args, **kwargs)
        self.fields["incidentdescription"].widget = forms.widgets.Textarea(attrs={'class': 'form-control'})
        self.fields["incidentlocation"].widget = forms.widgets.Textarea(attrs={'class': 'form-control'})
        self.fields["suspectedcause"].widget = forms.widgets.Textarea(attrs={'class': 'form-control'})
        self.fields["immediateactionstaken"].widget = forms.widgets.Textarea(attrs={'class': 'form-control'})
        self.fields["subincidenttypes"].widget = forms.widgets.CheckboxSelectMultiple()
        self.fields["subincidenttypes"].queryset = Subincidenttype.objects.all()
        self.fields["date"] = forms.DateTimeField(
        input_formats = ['%Y-%m-%dT%H:%M'],
        widget = forms.DateTimeInput(
            attrs={
                'type': 'datetime-local',
                'class': 'form-control'},
            format='%Y-%m-%dT%H:%M')
    )
