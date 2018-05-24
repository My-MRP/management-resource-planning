"""Define the My MRP home and about_us views, make the charts and graphs for the dashboard."""
import plotly
import plotly.plotly as py
import plotly.graph_objs as go
from django.views.generic.base import TemplateView
from vehicle_quote.models import VehicleQuote


class HomeView(TemplateView):
    """Make the HomeView class."""

    template_name = 'generic/home.html'
    # context_object_name = 'quotes'


class AboutUsView(TemplateView):
    """Make the AboutUsView class."""

    template_name = 'generic/about_us.html'


def createGraph():
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
        plotly.tools.set_credentials_file(username='kiirby', api_key='TdfP7ccHINP4BI76EDNj')

        trace = go.Pie(labels=list(vehicles.keys()), values=list(vehicles.values()))
        # GRAPH DIMENSION.
        layout = go.Layout(title='Most popular Models', width=800, height=640, paper_bgcolor='rgb(27, 32, 46)')
        graph = go.Figure(data=[trace], layout=layout)

        # Creates graph and saves it to the project.
        print('----------------------------------------------')
        print(graph)
        py.image.save_as(graph, filename='my_mrp/static/popular_models.png')
        print(graph)

        py.image.ishow(graph)

    except:
        return False
        print('[!] FATAL ERROR')
    finally:
        print('[*] Finished Executing PLOTLY/DB Queries.')
        print('----------------------------------------------')


createGraph()


class ComponentView(TemplateView):
    """."""

    template_name = 'generic/component.html'
