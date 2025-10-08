from datetime import datetime
from meteostat import Point, Daily, Hourly

# Location and date
lat, lon = 40.7128, -74.0060   # New York City
start = datetime(2023, 7, 15)
end = datetime(2023, 7, 16)    # same day (for hourly you can span more)

# Create point (lat, lon, elevation optional)
location = Point(lat, lon)

# DAILY data
daily = Daily(location, start, end)
daily = daily.fetch()
print(daily)   # pandas DataFrame with tavg, tmin, tmax, prcp, wdir, wspd, pres, etc.

# HOURLY data (for full-day hourly)
hourly = Hourly(location, start, end)
hourly = hourly.fetch()
print(hourly)  # hourly DataFrame