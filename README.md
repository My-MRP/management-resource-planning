# Management-Resource-Planning
 MyMRP is a tool for material resource planning for a manufacturing business.  There are 2 initial apps.  The product app and the quote app.  The initial apps are configured for building and quoting simple cars.  The models can be expanded and the names changed to match the product being made and sold.  Future apps will be aded to allow for inventory management, raw material processing and controls, production planning, shipping, and labor management.

# Version:  0.0.01

# My-MRP team:
    Austin Matteson, George Ceja, Steve Starwalt

## Getting Started



### Prerequisites

```
fork
git clone "projectURL"
RUN: create a superuser: manage.py createsuperuser
RUN: createdb Vehicles
RUN: pip/pip3 install -r requirements.txt
RUN: ./manage runserver
```

| Route | Name | Description |
|:--|--|:--|
|''|home|the landing page, after signin, the sales dashboard|
|`'accounts/'`|signin|takes the user to the login page|
|`'admin/'`|admin|displayed for super users only. takes the user to the admin page|
|`'vehicle/'`|add_vehicle|configure a new vehicle and add it to the database|
|`'engine/'`|add_engine|configure a new engine and add it to the database|
|`'exterior/'`|add_exterior_color|configure a new exterior color and add it to the database|
|`'interior/'`|add_interior_color|configure a new vinterior package and add it to the database|
|`'audio/'`|add_audio|configure a new audio package and add it to the database|
|`'wheel/'`|wheel|configure a new wheel package and add it to the database|
|`'quotes/'`|quote_list|list all the quotes for the logged in user|
|`'quotes/<int:id>',`|quote_detail|display all the details for the selected quote, compute cost and price and save them to the database for a new quote|
|`'model_names/'`|select_model|select the model to quote|
|`'vehiclequote_form/<int:id>'`|vehicle_quote|quote a vehicle model selected from the select model view|
|`'about_us/'`|about_us|pictures and bios for the dev team|

### Installing


## Running the tests


## Deployment

steps

## Built With

* [Python]   - TOOL DESCRIPTION
* [Django]   - TOOL DESCRIPTION
* [Plotly]   - TOOL DESCRIPTION
* [AWS]      - TOOL DESCRIPTION
* [Travis]   - TOOL DESCRIPTION
* [Postgres] - TOOL DESCRIPTION


## Contributing


## Versioning


## License


This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* etc


Getting Started
Clone this repository to your local machine.

$ git clone https://github.com/chaitanyanarukulla/django-imager.git
Once downloaded, change directory into the django-imager directory.

$ cd django-imager
Begin a new virtual environment with Python 3 and activate it.

django-imager $ python3 -m venv ENV
django-imager $ source ENV/bin/activate
Install the application requirements with pip.

(ENV) django-imager $ pip install -r requirements.txt
Create a Postgres database for use with this application.

(ENV) django-imager $ createdb imagersite
Export environmental variables pointing to the location of database, your username, hashed password, and secret

(ENV) django-imager $ export SECRET_KEY='secret'
(ENV) django-imager $ export DB_NAME='imagersite'
(ENV) django-imager $ export DB_USER='(your postgresql username)'
(ENV) django-imager $ export DB_PASS='(your postgresql password)'
(ENV) django-imager $ export DB_HOST='localhost'
(ENV) django-imager $ export DEBUG='True'
Then initialize the database with the migrate command from manage.py

(ENV) django-imager $ python imagersite/manage.py migrate
Once the package is installed and the database is created, start the server with the runserver command from manage.py

(ENV) django-imager $ python imagersite/manage.py runserver
Application is served on http://localhost:8000

Testing
You can test this application by first exporting an environmental variable pointing to the location of a testing database, then running the test command from manage.py.

(ENV) django-imager $ export TEST_DB='test_imagersite'
(ENV) django-imager $ python imagersite/manage.py test imagersite
Deploying
You can deploy this application to AWS using Ansible.

If you do not already have Ansible installed, install it outside your environment with pip

(ENV) django-imager $ deactivate
django-imager $ pip install ansible
django-imager $ source ENV/bin/activate
Create a hosts file in the root of django-imager

[us-west-2]
(your EC2 public IP address)

[us-west-2:vars]
ansible_ssh_user=(your EC2 user)
ansible_ssh_private_key_file=/path/to/your/key.pem

server_dns=(your EC2 public DNS)
secret_key='secret'
db_name='(your RDS database name)'
db_host='(your RDS endpoint)'
db_user='(your RDS username)'
db_pass='(your RDS password)'
test_db='test_imagersite'
allowed_hosts='(your EC2 public DNS) (your EC2 public IP address)'

aws_storage_bucket_name='(your S3 bucket name)'
aws_access_key_id='(your IAM user access key id)'
aws_secret_access_key='(your IAM user secret access key)'

admin_email='(your email address for admin)'
admin_email_host='(host for your admin email)'
admin_email_pass='(password for your admin email)'
Deploy the application with ansible-playbook

(ENV) django-imager $ ansible-playbook -i hosts playbook/imager_playbook.yml
Architecture
Built with Python and Django framework. Tested through Django testing suite.

Change Log
12-14-2017 12:37pm - Added pagination to the library and album detail views with tests

12-11-2017 6:03pm - Added an API route for listing a single user's photos with tests

12-11-2017 2:55pm - Moved all atatic resources to AWS S3

12-08-2017 6:40pm - Created Ansible playbook for deployment to AWS

12-07-2017 2:18pm - Fixed a bug in edit views that allowed editing of other people's files

12-05-2017 7:30pm - Added tests for the photo, album, and profile edit views

12-04-2017 7:14pm - Added tests for the photo and album create views

12-02-2017 9:41pm - Added photo, album, and profile update views

12-02-2017 7:00pm - Added photos and albums create views

12-01-2017 8:37pm - Added photo, album, and profile views with tests

11-28-2017 8:35pm - Added Photo and Album models with tests

11-28-2017 1:35pm - Added registration, login, and logout functionality with tests

11-21-2017 4:21pm - Added Profile Model for Users with tests

11-20-2017 12:53pm - Initail scaffolding
