"""Define the My MRP home view."""
import plotly
import plotly.plotly as py
import plotly.graph_objs as go
from django.views.generic.base import TemplateView


class HomeView(TemplateView):
    """Make the HomeView class."""

    template_name = 'generic/home.html'
    context_object_name = 'quotes'

    # def get_queryset(self, **kwargs):
    #     """Get the context to display."""
    #     username = self.request.user.get_username()
    #     quotes = Quote.objects.filter(user__username=username)

    #     return quotes

    # def get_context_data(self, **kwargs):
    #     """Filter the context for display."""
    #     context = super().get_context_data(**kwargs)
    #     quotes = context['quotes'][0]

    #     context.update({
    #         'quotes': quotes,
    #     })

    #     return context


# Generates Graph based on Data.
def createGraph():
    # Sample Data
    sales = {'R8': 342, 'NSX': 210, 'GTR': 200, 'FORDGT': 300}

    try:
        # Uses Plotly's API
        plotly.tools.set_credentials_file(username='kiirb', api_key='agmRWX8PPQqHZKWmC5iF')
        trace = go.Pie(labels=list(sales.keys()), values=list(sales.values()))

        # GRAPH DIMENSION.
        layout = go.Layout(title='Most popular Models', width=800, height=640)
        fig = go.Figure(data=[trace], layout=layout)

        # Creates graph and saves it to the project.
        py.image.save_as(fig, filename='my_mrp/static/popular_models.png')
        py.image.ishow(fig)
    except:
        return False
    finally:
        print('Finished Executing createGraph()')

# createGraph()


class ComponentView(TemplateView):
    """."""

    template_name = 'generic/component.html'
