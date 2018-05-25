"""Define the My MRP home and about_us views, make the charts and graphs for the dashboard."""

from django.views.generic.base import TemplateView
from vehicle_quote.models import VehicleQuote
import pandas_datareader.data as web
import plotly.graph_objs as go
from datetime import datetime
import plotly.plotly as py
import plotly




def createSeries():
    """Creates Series Graph to represent an individual seller"""
    plotly.tools.set_credentials_file(username='codefellows', api_key='Ulx7QkjumhIxh4mg2CMh')
    df = web.DataReader(
        "aapl", 'morningstar',
        datetime(2015, 1, 1),
        datetime(2016, 7, 1)).reset_index()

    data = [go.Scatter(x=df.Date, y=df.High)]
    fig = go.Figure(data = data)
    py.image.save_as(fig, filename='my_mrp/static/series.png')
    py.image.ishow(fig)


# Generates Graph based on Data.
def createGraph():
    """Create Visual for most popular models quoted."""
    vehicles = {}
    colors = {}
    car_models = VehicleQuote.objects.all()
    for car in [model.model_name.model_name for model in car_models]:
        if car not in vehicles:
                vehicles[car] = 1
        else:
            vehicles[car] += 1
    try:
        # Uses Plotly's API
        plotly.tools.set_credentials_file(username='codefellows', api_key='Ulx7QkjumhIxh4mg2CMh')
        trace = go.Pie(
            labels=list(vehicles.keys()),
            values=list(vehicles.values())
        )
        # GRAPH DIMENSION.
        layout = go.Layout(
            title='Most Quoted Models',
            width=800, height=640,
            paper_bgcolor='rgb(27, 32, 46)',
            font=dict(color='rgb(52, 156, 134)', size=30)
        )
        graph = go.Figure(data=[trace], layout=layout)
        # Creates graph and saves it to the project.
        print('-' * 45)
        py.image.save_as(graph, filename='my_mrp/static/popular_models.png')
        py.image.ishow(graph)
    except:
        print('[!] FATAL ERROR')
        return False
    finally:
        print('[*] Finished Executing PLOTLY/DB Queries.')
        print('-' * 45)


class HomeView(TemplateView):
    """Make the HomeView class for the initial landing page for signing in and the salesman dashboard after signing in."""

    template_name = 'generic/home.html'
    context_object_name = 'quotes'

    def get_context_data(self):
        """Create Graph."""
        createSeries()
        createGraph()
        return {}


class AboutUsView(TemplateView):
    """Make the AboutUsView class where the pics, bios and links of the developers can be shown."""

    template_name = 'generic/about_us.html'


class ComponentView(TemplateView):
    """Make the component view class where the user can select the type of component they want to add."""
    template_name = 'generic/component.html'

    def get(self, request):
        """Check for admin status."""
        if self.request.user.is_superuser:
            return super().get(request)
        return redirect('home')
