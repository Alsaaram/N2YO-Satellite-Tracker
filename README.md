# N2YO Satellite Tracker
This script is designed to furnish users with real-time information on a targeted satellite by utilizing its unique satellite ID. With this tool, users can effortlessly track 
multiple satellites and retrieve key details including latitude, longitude, azimuth, elevation, right ascension (in degrees), and declination (in degrees).

# Script Use
For the execution of the script, ensure that the 'requests' library for Python is installed, as the script actively makes requests to the API for information retrieval. Users also 
have the flexibility to input their specific longitude and latitude, as the default position is set to New York City. Modifying the user's position will yield satellite position data 
tailored to the observer's location.

# Terms of Usage
An API key is necessary for the proper functioning of this script. To obtain one, visit the N2YO website, create an account, and request an API key. Once obtained, simply insert 
it into the 'api_key' variable within the script. This step is crucial, as the website requires proper authorization for data retrieval.
