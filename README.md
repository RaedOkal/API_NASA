# NASA Image and Video Library

## The overall project aims to utilize the NASA Image and Video Library API to search for and retrieve images related to a specific topic, in this case, the moon. The project involves writing code to interact with the API, retrieve the desired images, and perform further processing or analysis on the retrieved data.

Here's an overview of the project steps:

1. Import the necessary libraries: The project begins by importing the `requests` library, which allows making HTTP requests to the API.

2. Define the API endpoint and parameters: The code defines the API endpoint URL as `"https://images-api.nasa.gov/search"` and sets the parameters for the request. In this case, the search query is set to "moon" and the media type is set to "image" to retrieve only images related to the moon.

3. Send the API request: The `requests.get()` function is used to send a GET request to the API, passing the endpoint URL and parameters. This initiates the request and fetches the response.

4. Check the request status: The code checks the status code of the response to ensure that the request was successful (status code 200). If the status code indicates success, the code proceeds to parse the JSON response. Otherwise, it handles the case when the request was not successful.

5. Parse the JSON response: The JSON response is parsed using `response.json()`, converting it into a Python dictionary that can be easily accessed.

6. Extract image URLs: The code extracts the list of items from the response, which represents the retrieved images related to the search query. It then iterates over each item and retrieves the image URL from the `"links"` field. Specifically, it looks for the link with `"rel"` equal to "preview" and retrieves the associated `"href"`.

7. Further processing: At this stage, you can perform additional processing or analysis on the retrieved image URLs. For example, you can download the images, display them, or apply any image processing techniques.

8. Output the results: The code prints the retrieved image URLs, allowing you to view the URLs of the images related to the moon.

The overall project provides a starting point for interacting with the NASA Image and Video Library API and retrieving images based on a specific search query. You can customize the search query, media type, and further processing steps to suit your specific needs and goals.



output:

https://images-assets.nasa.gov/image/PIA23237/PIA23237~thumb.jpg

https://images-assets.nasa.gov/image/iss069e008558/iss069e008558~thumb.jpg

https://images-assets.nasa.gov/image/PIA09921/PIA09921~thumb.jpg

https://images-assets.nasa.gov/image/PIA07615/PIA07615~thumb.jpg

https://images-assets.nasa.gov/image/PIA06066/PIA06066~thumb.jpg

https://images-assets.nasa.gov/image/PIA06603/PIA06603~thumb.jpg

https://images-assets.nasa.gov/image/PIA07679/PIA07679~thumb.jpg

https://images-assets.nasa.gov/image/PIA10569/PIA10569~thumb.jpg
