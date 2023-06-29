
#before we actually start we need to set the environment and run the server locally in our computer
#Standard environment
#Clone the repo
 #git clone https://github.com/nasa/apod-api
#cd into the new directory
 #cd apod-api
#Install dependencies into the project's lib
 #pip install -r requirements.txt -t lib
#Add lib to your PYTHONPATH and run the server
 #set PYTHONPATH=./lib && python application.py


#https://github.com/nasa/apod-api#standard_env rebo



import requests

# Define the API endpoint URL
url = "https://images-api.nasa.gov/search"

# Define the parameters for the request
params = {
    "q": "moon",  # Your search query
    "media_type": "image"  # Retrieve only images
}

# Send the GET request to the API
response = requests.get(url, params=params)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()

    # Extract the list of items from the response
    items = data["collection"]["items"]

    # Iterate over each item in the response
    for item in items:
        # Retrieve the information about the image
        links = item["links"]
        image_url = next((link["href"] for link in links if link["rel"] == "preview"), None)

        # Do further processing with the retrieved data
        # ...

        # Print the retrieved information
        print("Image URL:", image_url)
        print("\n")

else:
    # Handle the case when the request was not successful
    print("Error:", response.status_code)







