import requests
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import WeatherData
from .serializers import WeatherDataSerializer

# To get data from DB
# This will return the complete data, if city name is given in query parameter then it will return the data for that particular city only
class WeatherDataListCreate(generics.ListCreateAPIView):
    serializer_class = WeatherDataSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = WeatherData.objects.all()
        city = self.request.query_params.get('city', None)
        if city is not None:
            queryset = queryset.filter(city__icontains=city)
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if not queryset.exists():
            return Response({
                'message': 'No data available for the specified city.',
                'status': 'success',
                'data': []
            }, status=status.HTTP_200_OK)
        
        serializer = self.get_serializer(queryset, many=True)
        return Response({
            'message': 'Data retrieved successfully.',
            'status': 'success',
            'data': serializer.data
        }, status=status.HTTP_200_OK)


 # To get the data from Weather API & save it to the DB
class FetchAndSaveWeatherData(APIView):
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        api_key = '17f29b536df4403db3790441242106'  
        city = request.query_params.get('city')  
        url = f'http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=no'

        try:
            response = requests.get(url)
            response.raise_for_status() 
            data = response.json()

            weather_data = WeatherData(
                city=data['location']['name'],
                temperature=data['current']['temp_c'],
                description=data['current']['condition']['text']
            )
            weather_data.save()
            serializer = WeatherDataSerializer(weather_data)
            return Response({
                'message': 'Weather data fetched and saved successfully.',
                'status': 'success',
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)

        except requests.exceptions.RequestException as e:
            return Response({
                'message': f'Failed to fetch weather data: {str(e)}',
                'status': 'error',
                'data': []
            }, status=status.HTTP_400_BAD_REQUEST)
