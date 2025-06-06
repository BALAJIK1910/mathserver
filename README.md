# Ex.05 Design a Website for Server Side Processing
# Date:12-04-2025
# AIM:
To design a website to calculate the power of a lamp filament in an incandescent bulb in the server side.

# FORMULA:
P = I2R
P --> Power (in watts)
 I --> Intensity
 R --> Resistance

# DESIGN STEPS:
## Step 1:
Clone the repository from GitHub.

## Step 2:
Create Django Admin project.

## Step 3:
Create a New App under the Django Admin project.

## Step 4:
Create python programs for views and urls to perform server side processing.

## Step 5:
Create a HTML file to implement form based input and output.

## Step 6:
Publish the website in the given URL.

# PROGRAM :
~~~

html

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Power Calculator</title>
    <style>
        body {
            font-family: Arial, Helvetica, sans-serif;
            background-color: #f4f4f9;
            margin: 3px;
            padding: 4px;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 100vh;
        }

        h1 {
            color: #020202;
            margin-bottom: 20px;
        }

        form {
            background-image: "bg.jpg";
            background-size: cover;
            background-color: #fff;
            padding: 50px;
            border-radius: 8px;
            width: 400px;
            text-align: center;
        }

        label {
            margin-bottom: 10px;
            font-weight: bold;
            color: #2b2525;
        }

        input[type="text"] {
            width: 20%;
            padding: 8px;
            margin-bottom: 15px;
            border: 1px solid #ccc;
            border-radius: 4px;
            box-sizing: border-box;
        }

        button {
            background-color: #0068de;
            color: white;
            border: none;
            padding: 10px 15px;
            border-radius: 4px;
            cursor: pointer;
            font-size: 16px;
        }

        button:hover {
            background-color: #b3d5fa;
        }

        p {
            margin-top: 20px;
            font-size: 18px;
            color: #333;
        }
    </style>
</head>

<body>
    <h1 align="center">Power Calculator</h1>
    <form action="{% url 'power' %}" method="POST">
        {% csrf_token %}
        <label>Intensity:</label>
        <input type="text" id="Intensity" name="Intensity" required>
        <br>
        <label>Resistance:</label>
        <input type="text" id="Resistance" name="Resistance" required>
        <br>
        <button type="submit">Calculate</button>
    </form>
    <p>
        The power is: {{ output }} Watts
    </p>
</body>

</html>

views.py

from django.shortcuts import render


def power(request):
    if request.method == 'POST':
        I = int(request.POST.get('Intensity'))
        R = int(request.POST.get('Resistance'))
        P = (I**2)*R
        return render(request, 'power.html', {'output': P})
    return render(request, 'power.html')


urls.py

from django.contrib import admin
from django.urls import path
from power import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.power, name='power'),
]

~~~
# HOMEPAGE:

![alt text](<Screenshot 2025-04-15 122030.png>)
# RESULT:
The program for performing server side processing is completed successfully.
