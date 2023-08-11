from django.shortcuts import render ,HttpResponse, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
import requests
import plotly.graph_objects as go


# Create your views here.
def Project(request):
    return HttpResponse("This is data")
def home(request):
    return render(request,'index.html')

def chart(request):
    return render(request,'charts.html')

def turbidity(request):
    return render(request,'turbiditytable.html')

def location(request):
    return render(request,'locationtable.html')


def login_view(request):
    error_message = None
    if request.method == 'POST':
        error_message = None
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Compare the username and password with your variables
        hardcoded_username = "admin"
        hardcoded_password = "password"

        if username == hardcoded_username and password == hardcoded_password:
            # Authentication successful
            # Redirect to a success page or do something else
            return render(request,'index.html')
        else:
            # Invalid credentials
            # Render the login page again with an error message
            error_message = 'Invalid username or password. Please try again.'
    return render(request, 'logi.html',{'error_message': error_message})

import time

import requests
import plotly.graph_objs as go

def contact(request):
    url = "https://api.thingspeak.com/channels/2209876/feeds.json?api_key=NV1L4Q2QK0FV0HMF"

    response = requests.get(url)
    data = response.json()
    feeds = data.get('feeds', [])

    # Extract data for visualization
    field1_values = []
    timestamps = []

    # for feed in feeds:
    #     field1_value = feed.get('field1')
    #     if field1_value is not None:
    #         try:
    #             field1_value = float(field1_value)
    #             timestamp = feed.get('created_at', '')

    #             # Skip empty or invalid values
    #             if field1_value != 0:
    #                 field1_values.append(field1_value)
    #                 timestamps.append(timestamp)
    #         except ValueError:
    #             # Handle empty or invalid values
    #             continue

    # # Create the line chart trace for Field 1
    # trace = go.Scatter(
    #     x=timestamps,
    #     y=field1_values,
    #     mode='lines',
    #     name='Field 1'
    # )

    # # Create the chart layout
    # layout = go.Layout(
    #     title='ThingSpeak Data',
    #     xaxis=dict(title='Timestamp'),
    #     yaxis=dict(title='Value'),
    #     showlegend=True
    # )

    # # Create the chart figure
    # fig = go.Figure(data=[trace], layout=layout)

    # # Convert the chart to HTML
    # chart_html = fig.to_html(full_html=False)

    context = {'feeds': feeds}
    return render(request, 'table.html', context)