"""Define the My MRP home and about_us views, make the charts and graphs for the dashboard."""
import plotly
import plotly.plotly as py
import plotly.graph_objs as go
from django.views.generic.base import TemplateView


class HomeView(TemplateView):
    """Make the HomeView class."""

    template_name = 'generic/home.html'
    # context_object_name = 'quotes'


class AboutUsView(TemplateView):
    """Make the AboutUsView class."""

    template_name = 'generic/about_us.html'


def createGraph():
    """Generate graphs to display on the sales dashboard."""
    sales = {'R8': 342, 'NSX': 210, 'GTR': 200, 'FORDGT': 300}

    try:
        # Uses Plotly's API
        plotly.tools.set_credentials_file(username='kiirb', api_key='agmRWX8PPQqHZKWmC5iF')
        trace = go.Pie(labels=list(sales.keys()), values=list(sales.values()))

        # GRAPH DIMENSION.
        layout = go.Layout(title='Most popular Models', width=800, height=640, paper_bgcolor='rgb(27, 32, 46)')
        fig = go.Figure(data=[trace], layout=layout)

        # Creates graph and saves it to the project.
        py.image.save_as(fig, filename='my_mrp/static/popular_models.png')
        py.image.ishow(fig)
    except:
        return False
    finally:
        print('Finished Executing createGraph()')


createGraph()


class ComponentView(TemplateView):
    """."""

    template_name = 'generic/component.html'
