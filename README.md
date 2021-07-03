# NASA-APOD-Viewer

A Python-based desktop application to get daily Astro Images using NASA APOD API.You can install this applicaiton

## Get started

- Clone the Repo using `git@github.com:codewithdev/NASA-APOD-Viewer.git`in your system.
- Install the requirements using `pip install -r requirements.txt`command.
- Run the application.

## API Information

Most of the NASA open source catelog are availble on the site itself. You can use the Open API Keys to develop the projects and application for your own use. Using the methods and describing the payloads you can develop application with the help of open API keys for Image, catalogs, and other informations.

#### About APOD API

With GET request to the {URL} you can fetch the images and related information instantly on a particular date.

For this application:

- Find your NASA API Key by signing up on `https://api.nasa.gov/` and find the APOD API.
- You can skip the above process and use the `DEMO_API`.
- Update your workflow by adding the API key in the GitHub `/Secrets` or use built-in function to add the api in your local environment as a variable and import is using `os.environ.get('your_var_name')`.

**_NOTE_**: You can convert the application to exe using the "auto-py-to-exe" package.
