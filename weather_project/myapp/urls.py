from django.urls import path
from .views import FetchAndSaveWeatherData, WeatherDataListCreate
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('weather_data_from_db/', WeatherDataListCreate.as_view(), name='weather_data_list_create'),  # Will fetch the data from the DB, can get all data & data search by city
    path('fetch-weather_from_api/', FetchAndSaveWeatherData.as_view(), name='fetch_weather_data'),    # Get the data by cit name from weather api & save it to the DB
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),  #To get the token with the username:"user1" & password as "test@123", Also can set the another credentials by using powershell
]
