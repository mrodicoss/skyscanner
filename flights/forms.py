from django import forms

class FlightsForm(forms.Form):
    originplace = forms.CharField(label='Origin', max_length=30)
    destinationplace = forms.CharField(label='Destination', max_length=30)
    outboundpartialdate = forms.DateField(label='Outbound Date', widget=forms.SelectDateWidget(empty_label="Nothing"))