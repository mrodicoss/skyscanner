from django.shortcuts import render
from django.http import JsonResponse
from flights.forms import FlightsForm
import requests
from django.conf import settings

# Create your views here.
def search_flights(request):
	data = {}
	if request.method == 'POST':
		form = FlightsForm(request.POST)
		if form.is_valid():
			url = 'https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/browsequotes/v1.0/US/USD/en-US/'+ form.cleaned_data['originplace'] + '/' + form.cleaned_data['destinationplace'] + '/' + (form.cleaned_data['outboundpartialdate']).strftime("%Y-%m-%d")
			headers = {'X-RapidAPI-Key': settings.RAPIDAPI_API_KEY}

			api_response = requests.get(url, headers=headers)
			if api_response.status_code == 200:
				data = {'data': api_response.json()}
			elif api_response.status_code == 400:
				data = {'data': api_response.json().get("ValidationErrors")[0].get('Message')}
			else:
				data = {'data': (form.cleaned_data['outboundpartialdate']).strftime("%Y-%m-%d")}			
	else:
		form = FlightsForm()
	data['form'] = form
	return render(request, 'flights.html', data)

def search_locations(request):
	if request.is_ajax():
		url = 'https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/autosuggest/v1.0/UK/GBP/en-GB/'
		headers = {'X-RapidAPI-Key': settings.RAPIDAPI_API_KEY}
		params = {'query': request.GET.get('query')}

		api_response = requests.get(url, headers=headers, params=params)
		if api_response.status_code == 200:
			return JsonResponse(api_response.json())
		else:
			return JsonResponse(api_response.json({'data': 'Greska'}))
	else:
		return JsonResponse({'data':'Nije ajax'})

def search_country_details(request):
	if request.is_ajax():
		url = 'https://restcountries-v1.p.rapidapi.com/name/' + request.GET.get('country')
		headers = {'X-RapidAPI-Key': settings.RAPIDAPI_API_KEY}

		api_response = requests.get(url, headers=headers)
		if api_response.status_code == 200:
			return render(request, 'country_details.html', {'data': api_response.json()})
		else:
			return render(request, 'country_details.html', {'message': 'Greska!'})
	else:
		return render(request, 'country_details.html', {'message': 'Nije ajax!'})
