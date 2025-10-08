import openmeteo_requests

import pandas as pd
import requests_cache
from retry_requests import retry

# Setup the Open-Meteo API client with cache and retry on error
cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)
retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
openmeteo = openmeteo_requests.Client(session = retry_session)

# Make sure all required weather variables are listed here
# The order of variables in hourly or daily is important to assign them correctly below
def get_weather(latitude, longitude):
	url = "https://api.open-meteo.com/v1/forecast"
	params = {
		"latitude": latitude,
		"longitude": longitude,
		"daily": ["temperature_2m_max", "temperature_2m_min", "sunrise", "sunset", "daylight_duration", "sunshine_duration", "uv_index_max"],
		"hourly": ["temperature_2m", "relative_humidity_2m", "dew_point_2m", "apparent_temperature", "precipitation_probability", "rain", "showers", "snowfall", "surface_pressure", "cloud_cover", "evapotranspiration", "vapour_pressure_deficit", "wind_speed_10m", "wind_speed_120m", "wind_speed_80m", "wind_speed_180m", "wind_direction_10m", "wind_direction_80m", "wind_direction_120m", "wind_direction_180m", "wind_gusts_10m", "temperature_80m", "temperature_120m", "temperature_180m"],
		"current": ["temperature_2m", "relative_humidity_2m", "apparent_temperature", "is_day", "precipitation", "rain", "showers", "snowfall", "cloud_cover", "surface_pressure", "wind_speed_10m", "wind_direction_10m", "wind_gusts_10m"],
		"timezone": "Asia/Tokyo",
		"past_days": 3,
	}
	responses = openmeteo.weather_api(url, params=params)

	# Process first location. Add a for-loop for multiple locations or weather models
	response = responses[0]
	print(f"Coordinates: {response.Latitude()}°N {response.Longitude()}°E")
	print(f"Elevation: {response.Elevation()} m asl")
	print(f"Timezone: {response.Timezone()}{response.TimezoneAbbreviation()}")
	print(f"Timezone difference to GMT+0: {response.UtcOffsetSeconds()}s")

	# Process current data. The order of variables needs to be the same as requested.
	current = response.Current()
	current_temperature_2m = current.Variables(0).Value()
	current_relative_humidity_2m = current.Variables(1).Value()
	current_apparent_temperature = current.Variables(2).Value()
	current_is_day = current.Variables(3).Value()
	current_precipitation = current.Variables(4).Value()
	current_rain = current.Variables(5).Value()
	current_showers = current.Variables(6).Value()
	current_snowfall = current.Variables(7).Value()
	current_cloud_cover = current.Variables(8).Value()
	current_surface_pressure = current.Variables(9).Value()
	current_wind_speed_10m = current.Variables(10).Value()
	current_wind_direction_10m = current.Variables(11).Value()
	current_wind_gusts_10m = current.Variables(12).Value()

	print(f"\nCurrent time: {current.Time()}")
	print(f"Current temperature_2m: {current_temperature_2m}")
	print(f"Current relative_humidity_2m: {current_relative_humidity_2m}")
	print(f"Current apparent_temperature: {current_apparent_temperature}")
	print(f"Current is_day: {current_is_day}")
	print(f"Current precipitation: {current_precipitation}")
	print(f"Current rain: {current_rain}")
	print(f"Current showers: {current_showers}")
	print(f"Current snowfall: {current_snowfall}")
	print(f"Current cloud_cover: {current_cloud_cover}")
	print(f"Current surface_pressure: {current_surface_pressure}")
	print(f"Current wind_speed_10m: {current_wind_speed_10m}")
	print(f"Current wind_direction_10m: {current_wind_direction_10m}")
	print(f"Current wind_gusts_10m: {current_wind_gusts_10m}")

	# Process hourly data. The order of variables needs to be the same as requested.
	hourly = response.Hourly()
	hourly_temperature_2m = hourly.Variables(0).ValuesAsNumpy()
	hourly_relative_humidity_2m = hourly.Variables(1).ValuesAsNumpy()
	hourly_dew_point_2m = hourly.Variables(2).ValuesAsNumpy()
	hourly_apparent_temperature = hourly.Variables(3).ValuesAsNumpy()
	hourly_precipitation_probability = hourly.Variables(4).ValuesAsNumpy()
	hourly_rain = hourly.Variables(5).ValuesAsNumpy()
	hourly_showers = hourly.Variables(6).ValuesAsNumpy()
	hourly_snowfall = hourly.Variables(7).ValuesAsNumpy()
	hourly_surface_pressure = hourly.Variables(8).ValuesAsNumpy()
	hourly_cloud_cover = hourly.Variables(9).ValuesAsNumpy()
	hourly_evapotranspiration = hourly.Variables(10).ValuesAsNumpy()
	hourly_vapour_pressure_deficit = hourly.Variables(11).ValuesAsNumpy()
	hourly_wind_speed_10m = hourly.Variables(12).ValuesAsNumpy()
	hourly_wind_speed_120m = hourly.Variables(13).ValuesAsNumpy()
	hourly_wind_speed_80m = hourly.Variables(14).ValuesAsNumpy()
	hourly_wind_speed_180m = hourly.Variables(15).ValuesAsNumpy()
	hourly_wind_direction_10m = hourly.Variables(16).ValuesAsNumpy()
	hourly_wind_direction_80m = hourly.Variables(17).ValuesAsNumpy()
	hourly_wind_direction_120m = hourly.Variables(18).ValuesAsNumpy()
	hourly_wind_direction_180m = hourly.Variables(19).ValuesAsNumpy()
	hourly_wind_gusts_10m = hourly.Variables(20).ValuesAsNumpy()
	hourly_temperature_80m = hourly.Variables(21).ValuesAsNumpy()
	hourly_temperature_120m = hourly.Variables(22).ValuesAsNumpy()
	hourly_temperature_180m = hourly.Variables(23).ValuesAsNumpy()

	hourly_data = {"date": pd.date_range(
		start = pd.to_datetime(hourly.Time(), unit = "s", utc = True),
		end = pd.to_datetime(hourly.TimeEnd(), unit = "s", utc = True),
		freq = pd.Timedelta(seconds = hourly.Interval()),
		inclusive = "left"
	)}

	hourly_data["temperature_2m"] = hourly_temperature_2m
	hourly_data["relative_humidity_2m"] = hourly_relative_humidity_2m
	hourly_data["dew_point_2m"] = hourly_dew_point_2m
	hourly_data["apparent_temperature"] = hourly_apparent_temperature
	hourly_data["precipitation_probability"] = hourly_precipitation_probability
	hourly_data["rain"] = hourly_rain
	hourly_data["showers"] = hourly_showers
	hourly_data["snowfall"] = hourly_snowfall
	hourly_data["surface_pressure"] = hourly_surface_pressure
	hourly_data["cloud_cover"] = hourly_cloud_cover
	hourly_data["evapotranspiration"] = hourly_evapotranspiration
	hourly_data["vapour_pressure_deficit"] = hourly_vapour_pressure_deficit
	hourly_data["wind_speed_10m"] = hourly_wind_speed_10m
	hourly_data["wind_speed_120m"] = hourly_wind_speed_120m
	hourly_data["wind_speed_80m"] = hourly_wind_speed_80m
	hourly_data["wind_speed_180m"] = hourly_wind_speed_180m
	hourly_data["wind_direction_10m"] = hourly_wind_direction_10m
	hourly_data["wind_direction_80m"] = hourly_wind_direction_80m
	hourly_data["wind_direction_120m"] = hourly_wind_direction_120m
	hourly_data["wind_direction_180m"] = hourly_wind_direction_180m
	hourly_data["wind_gusts_10m"] = hourly_wind_gusts_10m
	hourly_data["temperature_80m"] = hourly_temperature_80m
	hourly_data["temperature_120m"] = hourly_temperature_120m
	hourly_data["temperature_180m"] = hourly_temperature_180m

	hourly_dataframe = pd.DataFrame(data = hourly_data)
	print("\nHourly data\n", hourly_dataframe)

	# Process daily data. The order of variables needs to be the same as requested.
	daily = response.Daily()
	daily_temperature_2m_max = daily.Variables(0).ValuesAsNumpy()
	daily_temperature_2m_min = daily.Variables(1).ValuesAsNumpy()
	daily_sunrise = daily.Variables(2).ValuesInt64AsNumpy()
	daily_sunset = daily.Variables(3).ValuesInt64AsNumpy()
	daily_daylight_duration = daily.Variables(4).ValuesAsNumpy()
	daily_sunshine_duration = daily.Variables(5).ValuesAsNumpy()
	daily_uv_index_max = daily.Variables(6).ValuesAsNumpy()

	daily_data = {"date": pd.date_range(
		start = pd.to_datetime(daily.Time(), unit = "s", utc = True),
		end = pd.to_datetime(daily.TimeEnd(), unit = "s", utc = True),
		freq = pd.Timedelta(seconds = daily.Interval()),
		inclusive = "left"
	)}

	daily_data["temperature_2m_max"] = daily_temperature_2m_max
	daily_data["temperature_2m_min"] = daily_temperature_2m_min
	daily_data["sunrise"] = daily_sunrise
	daily_data["sunset"] = daily_sunset
	daily_data["daylight_duration"] = daily_daylight_duration
	daily_data["sunshine_duration"] = daily_sunshine_duration
	daily_data["uv_index_max"] = daily_uv_index_max	
	
	current_weather = {
        "curent_temperature_2m": current_temperature_2m,
        "curent_relative_humidity_2m": current_relative_humidity_2m,
        "current_apparent_temperature": current_apparent_temperature,
        "is_day": current_is_day,
        "curent_precipitation": current_precipitation,
        "curent_rain": current_rain,
        "curent_showers": current_showers,
        "curent_snowfall": current_snowfall,
        "curent_cloud_cover": current_cloud_cover,
        "curent_surface_pressure": current_surface_pressure,
        "curent_wind_speed_10m": current_wind_speed_10m,
        "curent_wind_direction_10m": current_wind_direction_10m,
        "curent_wind_gusts_10m": current_wind_gusts_10m,
        "curent_time": current.Time(),
    }
	daily_dataframe = pd.DataFrame(data = daily_data)

	print(daily_dataframe)
	return(daily_dataframe, hourly_dataframe, current_weather)

