# ClimaTrack: Guide to Building and Deploying your first Full-Stack Weather Monitoring Application with Flask, MongoDB Atlas, and Heroku

## Introduction
ClimaTrack is a real-time weather monitoring and analytics platform that fetches weather data from the Tomorrow.io API and stores it in a MongoDB Atlas database. This tutorial will guide you through setting up the project, from obtaining API keys to deploying the application on Heroku.

## Table of Contents
1. [Project Setup](#project-setup)
2. [Installing Dependencies](#installing-dependencies)
3. [Setting Up MongoDB Atlas](#setting-up-mongodb-atlas)
4. [Getting API Key from Tomorrow.io](#getting-api-key-from-tomorrowio)
5. [Setting Up Environment Variables](#setting-up-environment-variables)
6. [Understanding the Code](#understanding-the-code)
7. [Running the Application Locally](#running-the-application-locally)
8. [Deploying to Heroku](#deploying-to-heroku)
9. [Scheduling the Data Collection](#scheduling-the-data-collection)
10. [Accessing MongoDB Atlas Data](#accessing-mongodb-atlas-data)
11. [Future Works and Contributions](#future-works-and-contributions)
12. [License](#license)
13. [Live Demo](#live-demo)

## Project Setup
1. **Clone the Repository**:
    ```bash
    git clone https://github.com/subhanjandas/climatrack-platform.git
    cd climatrack-platform
    ```

2. **Project Structure**:
    ```
    climatrack/
    │
    ├── src/
    │   ├── templates/
    │   │   ├── index.html
    │   │   ├── weather.html
    │   │   └── analysis.html
    │   ├── __pycache__/
    │   ├── app.py
    │   └── collect_weather_data.py
    │
    ├── venv/
    │
    ├── Procfile
    ├── requirements.txt
    ├── README.md
    └── .gitignore
    ```

## Installing Dependencies
1. **Set Up Virtual Environment**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

2. **Install Required Packages**:
    ```bash
    pip install -r requirements.txt
    ```

## Setting Up MongoDB Atlas
1. **Create an Account**:
    - Sign up for a MongoDB Atlas account at [MongoDB Atlas](https://www.mongodb.com/cloud/atlas).

2. **Create a Cluster**:
    - Navigate to the Atlas dashboard and create a new cluster. Choose the free tier for this project.

3. **Configure Network Access**:
    - Add your current IP address to the IP Whitelist in the Network Access settings.

4. **Create a Database User**:
    - Create a new database user with read and write permissions. Save the username and password for later.

5. **Get Connection String**:
    - Click on "Connect" for your cluster and choose "Connect your application". Copy the connection string and replace `<username>` and `<password>` with your database user credentials.

## Getting API Key from Tomorrow.io
1. **Sign Up**:
    - Sign up for an account at [Tomorrow.io](https://www.tomorrow.io/).

2. **Get API Key**:
    - Navigate to the API section of the dashboard and generate a new API key. Copy this key for later use.

## Setting Up Environment Variables
1. **Create a .env File**:
    - In the root directory of your project, create a `.env` file and add the following variables:
    ```env
    MONGODB_URI="your_mongodb_connection_string"
    TOMORROW_API_KEY="your_tomorrow_io_api_key"
    ```

2. **Load Environment Variables**:
    - Ensure your application loads these variables using `os.getenv()` in your Python scripts.

## Understanding the Code
### `src/app.py`
This file contains the main Flask application that handles the frontend and backend integration.
- **Routes**:
  - `/`: Renders the home page (`index.html`).
  - `/get_weather`: Fetches weather data for a selected city and stores it in MongoDB.
  - `/view_weather`: Displays the most recent weather data for the selected city.
  
- **Functionality**:
  - **MongoDB Setup**: Connects to the MongoDB Atlas using the URI from environment variables.
  - **Weather Data Fetching**: Uses the Tomorrow.io API to get weather data for the selected city.
  - **Data Storage**: Stores the fetched weather data in MongoDB.
  
### `src/collect_weather_data.py`
This script is designed to be run periodically (using a scheduler) to fetch and store weather data.
- **Functionality**:
  - **API Request**: Fetches weather data from Tomorrow.io API.
  - **Data Storage**: Stores the fetched data in MongoDB.

### `src/templates/index.html`
Contains a form for selecting a city and requesting weather data.
- **Cities Included**:
  - Toronto
  - New York
  - Los Angeles
  - London
  - Paris
  - Tokyo
  - Moscow
  - Beijing
  - Delhi
  - Mumbai
  - San Francisco
  - Berlin
  - Shanghai
  - Guangzhou
  - Rome
  - Mexico City
  - Seoul
  - Bangkok
  - Sydney
  - Cairo
  - Dubai
  - Stockholm
  - Hong Kong
  - Ottawa
  - Istanbul
  - Madrid
  - Brussels
  - Amsterdam
  - Budapest
  - Lagos
  - Vienna
  - Kuala Lumpur
  - Milan
  - Singapore
  - Edinburgh
  - Helsinki
  - Varna
  - Osaka
  - Phoenix
  - Athens
  - Nice

### `src/templates/weather.html`
Displays the fetched weather data for the selected city.

## Running the Application Locally
1. **Run the Flask Application**:
    ```bash
    python src/app.py
    ```

2. **Access the Application**:
    - Open your browser and navigate to `http://127.0.0.1:5000/`.

## Deploying to Heroku
1. **Create a Heroku Account**:
    - Sign up for a Heroku account at [Heroku](https://www.heroku.com/).

2. **Create a New Heroku App**:
    - Log in to the Heroku dashboard.
    - Click on "New" and then "Create new app".
    - Name your app and select your region.

3. **Connect to GitHub**:
    - In the "Deploy" tab, connect your app to your GitHub repository.

4. **Add Environment Variables**:
    - Go to the "Settings" tab and click on "Reveal Config Vars".
    - Add the following environment variables:
      - `MONGODB_URI`: Your MongoDB Atlas connection string.
      - `TOMORROW_API_KEY`: Your Tomorrow.io API key.

5. **Procfile Configuration**:
    - Ensure your `Procfile` contains:
    ```
    web: gunicorn src.app:app
    worker: python src/collect_weather_data.py
    ```

6. **Deploy the Application**:
    - In the "Deploy" tab, select the branch you want to deploy from and click "Deploy Branch".

## Scheduling the Data Collection
1. **Add Heroku Scheduler**:
    - Go to your app's dashboard on Heroku.
    - Navigate to the "Resources" tab and add "Heroku Scheduler".

2. **Schedule the Job**:
    - Open Heroku Scheduler and add a new job.
    - Set the command to `python src/collect_weather_data.py` and choose the desired frequency.

## Accessing MongoDB Atlas Data
1. **Access Data via MongoDB Atlas UI**:
    - Go to the MongoDB Atlas dashboard.
    - Navigate to your cluster, click on "Browse Collections", and explore your data.

## Future Works and Contributions
1. **Enhanced Frontend**:
    - Improve the user interface and user experience of the application by adding more interactive elements, better styling, and responsive design.

2. **Data Analysis and Visualization**:
    - Integrate data analysis and visualization tools to provide insights from the collected weather data. This can include charts, graphs, and trends over time.

3. **Machine Learning Integration**:
    - Implement machine learning models to predict future weather conditions based on the historical data collected. This could provide users with forecasts and weather trend analysis.

4. **Contributions Welcome**:
    - If you have ideas or improvements, feel free to fork the repository and submit a pull request, Build your first Full-Stack WebApp


## License
This project is licensed under the MIT License.


-------------
### Example .env File
```env
MONGODB_URI="your_mongodb_connection_string"
TOMORROW_API_KEY="your

```

### Example Procfile
```Procfile
web: gunicorn src.app:app
worker: python src/collect_weather_data.py
```

## Live Demo
Check out the live application at [ClimaTrack](https://climatrack-platform-080435b5e83b.herokuapp.com)

-------------

Hope you enjoy building and deploying your first full stack web app with this repo!

Thanks, @subhanjan