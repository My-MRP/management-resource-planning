# Management-Resource-Planning
 MyMRP is a tool for material resource planning for a manufacturing business.  There are 2 initial apps.  The product app and the quote app.  The initial apps are configured for building and quoting simple cars.  The models can be expanded and the names changed to match the product being made and sold.  Future apps will be aded to allow for inventory management, raw material processing and controls, production planning, shipping, and labor management.

# Version:  0.0.01

# My-MRP team:
    Austin Matteson, George Ceja, Steve Starwalt

# Routes
| Route | Name | Description |
|:--|--|:--|
|''|home|the landing page, after signin: the sales dashboard|
|`'accounts/'`|signin|takes the user to the login page|
|`'admin/'`|admin|displayed for super users only. takes the user to the admin page|
|`'vehicle/'`|add_vehicle|displayed for super users only. configure a new vehicle and add it to the database|
|`'engine/'`|add_engine|displayed for super users only. configure a new engine and add it to the database|
|`'exterior/'`|add_exterior_color|displayed for super users only. configure a new exterior color and add it to the database|
|`'interior/'`|add_interior_color|displayed for super users only. configure a new vinterior package and add it to the database|
|`'audio/'`|add_audio|displayed for super users only. configure a new audio package and add it to the database|
|`'wheel/'`|wheel|displayed for super users only. configure a new wheel package and add it to the database|
|`'quotes/'`|quote_list|list all the quotes for the loggedin user|
|`'quotes/<int:id>',`|quote_detail|for a new quote: compute cost and price and save them to the database. for existing quotes: display all the details for the selected quote|
|`'model_names/'`|select_model|select the model to quote|
|`'vehiclequote_form/<int:id>'`|vehicle_quote|quote a vehicle model selected from the select_model view|
|`'about_us/'`|about_us|pictures and bios for the dev team|

# Getting Started:
Clone this repository to your local machine.

$ git clone https://github.com/My-MRP/management-resource-planning.git

Once downloaded, change directory into the management-resource-planning directory.
Begin a new virtual environment with Python 3 and activate it.
Install the application requirements with pip.
Create a Postgres database for use with this application.
Export environmental variables pointing to the location of database, your username, hashed password, and secret key

(ENV) export SECRET_KEY=''
(ENV) export DB_NAME=''
(ENV) export DB_USER=''
(ENV) export DB_PASS=''
(ENV) export DB_HOST=''
(ENV) export DEBUG='True'

Initialize the database with the migrate command from manage.py
Once the package is installed and the database is created, start the server with the runserver command from manage.py
Testing
You can test this application by first exporting an environmental variable pointing to the location of a testing database, then running the test command from manage.py.

## Deployment:
You can deploy this application to AWS using Ansible.
If you do not already have Ansible installed, install it outside your environment with pip
Create a hosts file in the root of management-resource-planning
Set up your EC2 and RDS on AWS
Deploy the application with ansible-playbook

## Built With:
Built with Python and Django framework. 
Additional packages required are Plotly, Ansible, and Coveralls.

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
Logo designed by Vexels https://www.vexels.com/vectors/preview/139518/3d-piechart-graph

Change Log
