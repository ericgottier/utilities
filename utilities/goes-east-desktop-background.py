#script to automatically change the desktop background to the GOES-East full disk image every day at 1710UTC

#url datetime format is in the following format
#where yyyy is the four digit year, ddd is the Julian day of the year, and hhmm is the 24-hour time
urlDateTimeFormat = "yyyydddhhmm"

# Importing the required modules
import requests # For downloading images from URLs
import datetime # For getting the current year and Julian day
from datetime import timedelta
import os # For deleting files and setting wallpaper
import ctypes # For setting wallpaper
from ctypes import wintypes

# Defining some constants
URL_TEMPLATE = "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/FD/GEOCOLOR/{year}{day}1700_GOES19-ABI-FD-GEOCOLOR-21696x21696.jpg" # The URL template with placeholders for year and day
FOLDER = "C:\\Users\\Eric\\OneDrive\\Pictures\\Wallpapers\\GOES-East" # The predetermined folder where images are saved
FILE_TEMPLATE = "GOES-East_Full_Disk_Geocolor_{year}{day}1700.jpg" # The file name template with placeholders for year and day
MAX_FILES = 10 # The maximum number of files to keep in the folder

# Getting the current year and Julian day
now = datetime.datetime.utcnow() # Getting the current time in UTC

# If the current UTC time is before 1700, then default to the previous day's image...
if now.hour < 17:
    year = (now - timedelta(days = 1)).strftime("%Y") # Formatting the year as four digits, less 1 day since the image for the current UTC day does not yet exist
    day = (now - timedelta(days = 1)).strftime("%j") # Formatting the Julian day as three digits, less 1 day since the image for the current UTC day does not yet exist
else:
    year = now.strftime("%Y") # Formatting the year as four digits
    day = now.strftime("%j") # Formatting the Julian day as three digits

# Replacing the placeholders in the URL and file name templates with actual values
url = URL_TEMPLATE.format(year=year, day=day) # Using string formatting to replace {year} and {day} with actual values
file_name = FILE_TEMPLATE.format(year=year, day=day) # Same as above

# Downloading the image from the URL and saving it to the folder
img_data = requests.get(url).content # Getting the binary image content from the URL
file_path = os.path.join(FOLDER, file_name) # Joining the folder and file name to get the full file path
with open(file_path, 'wb') as f: # Opening a new file in write binary mode
    f.write(img_data) # Writing the binary image content to the file

# Deleting the 11th oldest image in the folder if it exists
files = os.listdir(FOLDER) # Listing all files in the folder
files.sort() # Sorting files by name (which also sorts by date)
if len(files) > MAX_FILES: # Checking if there are more than 10 files in the folder
    oldest_file = files[0] # Getting the first (oldest) file name
    oldest_file_path = os.path.join(FOLDER, oldest_file)
    os.remove(oldest_file_path)


# Some constants for SystemParametersInfo
SPI_SETDESKWALLPAPER = 0x0014
SPIF_UPDATEINIFILE = 0x0001
SPIF_SENDWININICHANGE = 0x0002

# Get a handle to user32.dll
user32 = ctypes.WinDLL("user32")

# Define argtypes and restype for SystemParametersInfoW
SystemParametersInfo = user32.SystemParametersInfoW
SystemParametersInfo.argtypes = ctypes.c_uint,ctypes.c_uint,ctypes.c_void_p,ctypes.c_uint
SystemParametersInfo.restype = wintypes.BOOL

# Call SystemParametersInfoW with SPI_SETDESKWALLPAPER and other arguments
result = SystemParametersInfo(SPI_SETDESKWALLPAPER, 0, file_path, SPIF_UPDATEINIFILE | SPIF_SENDWININICHANGE)

# Check if the function succeeded
if result:
    print("Wallpaper changed successfully")
else:
    print("Wallpaper change failed")