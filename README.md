# Conveyor Profiler

## Introduction

This project is a web-based dashboard for visualizing conveyor belt profile data. Users can upload CSV files containing profile data, select a date to view the data, and display a corresponding graph. The application is built using Django for the backend and HTML, CSS, Bootstrap and JS for the frontend.

## Features

- Upload CSV files containing conveyor belt profile data.
- Select a date to view the corresponding data.
- Display a graph of the data for the selected date.
- Data validation to ensure the integrity of uploaded files.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.8+
- Django 3.2+
- pandas
- matplotlib

## Installation

1. **Clone the repository**

    ```bash
    git clone https://github.com/akarsh-sinha/Conveyor-Profiler.git
    cd company-dashboard
    ```

2. **Install the required dependencies**

    ```bash
    pip install -r requirements.txt
    ```

3. **Apply migrations**

    ```bash
    python manage.py migrate
    ```

4. **Run the server**

    ```bash
    python manage.py runserver
    ```

5. **Access the application**

    Open your web browser and go to `http://127.0.0.1:8000/`.

## Dependencies

The required Python packages are listed in the `requirements.txt` file:

