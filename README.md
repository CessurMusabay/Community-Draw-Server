# Community Draw Server

This project is the server portion of a clone of the popular website r/place, built using Django REST API and Channels.
## About this project

This project is a clone of r/place, built using Django REST API and Channels. It allows users to place pixels on a blank canvas, using a limited palette of colors. The canvas is shared among all users, and updates in real-time, so users can see each other's contributions as they happen.
## Getting started

To run this project locally, you will need to have Python installed on your computer. Once you have these installed, follow these steps:

1. Clone this repository to your local machine.
2. Navigate to the project directory in your terminal.
3. Create a new virtual environment using the command `python -m venv env`.
4. Activate the virtual environment using the command `source env/bin/activate` on Linux or `env\Scripts\activate` on Windows.
5. Install the project dependencies using the command `pip install -r requirements.txt`.
6. Start the Django Channels development server using the command `uvicorn CommunityDraw.asgi:application --host 0.0.0.0 --port 8000`
7. Open your browser and go to `http://localhost:8000` to view the app.


## Usage

To use this app, simply click on the canvas to place a pixel. You can choose from a limited palette of colors by clicking on the color buttons at the bottom of the screen. The canvas updates in real-time, so you can see your pixel and other users' pixels as they are placed.