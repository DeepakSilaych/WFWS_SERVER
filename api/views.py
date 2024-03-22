from django.http import JsonResponse
from .models import Data
import json
from django.views.decorators.csrf import csrf_exempt
from .utils import geolocate_text

@csrf_exempt
def store_data(request):
    if request.method == 'POST':
      try:
        data = json.loads(request.body)
        if data['latitude'] is None or data['longitude'] is None:
            if data['location'] is None:
                print('location is required')
                return JsonResponse({'error': 'Location is required'}, status=400)
            else:
                latitude, longitude = geolocate_text(data['location'])
    
                if latitude is None or longitude is None:
                    return JsonResponse({'error': 'Invalid location'}, status=400)
        else: 
            latitude = data['latitude']
            longitude = data['longitude']
        Data.objects.create(
            name=data['name'],
            waterlevel=data['waterlevel'],
            location=data['location'],
            latitude=latitude,
            longitude=longitude,
        )
        return JsonResponse({'message': 'Data stored successfully'})
      except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)
    else:
      return JsonResponse({'error': 'Method not allowed'}, status=405)



def map_data(request):
    latest_data = Data.objects.order_by('-id')

    serialized_data = [{
        'waterlevel': entry.waterlevel,
        'latitude': entry.latitude,
        'longitude': entry.longitude
    } for entry in latest_data]

    return JsonResponse({'data': serialized_data})
