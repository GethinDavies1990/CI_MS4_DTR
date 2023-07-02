# Taco y Tequila
Taco y Tequila is mexican website, for users to purchase meal kits and also some side items like alcohol, spices, sauces etc. The user can also book the restaurant for an event.

- There are two types of users
    - An admin(administrator) user account
    - A regular(shopper) user account
    - When making a payment as a regular user, a test credit card of 4242424242424242 has been set up for the card number
    - For the expiry date, cvc and postal code any series number(s) can be used(once they meet the mimimum values)
<br>

![Responsive site example](readme/responsive/responsive.PNG)

# Table of Contents

# Project Overview

- This project was built for the submission of my 4th project with code institute - Diploma in software development (Full Stack)
- The repository on GitHub that contains the website source code and assets is available at the following url: [Code Repository](https://github.com/GethinDavies1990/CI_MS4_DTR)
- The website was built with a responsive look and feel for desktop, tablet and mobile devices

# UX
## Strategy
### Primary Goal
The primary goal of the website from the site
owners perspective is as follows:
- To add, edit and delete products with the relevant information (price, description, spice rating, image, sizes and category) on the website
- To allow a user make a purchase of the products on the website
- To categorise sale items on the website
- To allow the user to book events on the website

The primary goal of the website from a site users perspective is as follows:
- To register for an account on the website and receive an email after successful registration
- To login or logout from the website
- To easily recover my password in case I forget it
- Have a personalised user profile with my delivery, payment information and order history
- View a list of products on the website
- View an individual product detail(price, description, spice rating, image, sizes and category)
- To add an item to a shopping bag, and select the quantity and size if applicable
- Complete a purchase of items in a shopping bag
- To sort the list of available products by spice rating, price and category
- Search for a product by name or description and view the search results
- To book events

## Structure
### Website pages
- I have structured the websote into over (INSERT NUMBER OF PAGES HERE), each with clear structure, information and purpose. I sued Bootstrap throughout, which gave consistent structure and responsive design.
- Below are the main pages'/features
- These pages are descrived in more detail in the user stories section. 

(INSERT TABLE OF PAGES HERE)


### Code Structure
The project is divided into a number of apps, as is built using the Django Framework
The project was built on the Boutique Ado project, that was part of the project content
The apps are described as follows
- bag (part of the original Boutique Ado project): This app contains functionality regarding a users shopping bag
- checkout (part of the original Boutique Ado project): This app contains functionality regarding a users checking out and payment of an order
- events: This app allows users to book the restaurant for an event.
- home (part of the original Boutique Ado project): This app contains functionality regarding the users home page
- info: This includes functionality for the meet the team section of the website
- products (part of the original Boutique Ado project): This app contains functionality regarding a product.
- profiles (part of the original Boutique Ado project): This app contains functionality regarding a users profile and order history

To complement the apps there are
- taco_y_tequila: Containing settings.py(Settings) and urls.py(Website urls) for example
- templates: Containing the base.html, allauth(django authentication) and includes html files
- static: Base css
- manage.py: Main python file for starting the website
- README.md: Readme documentation
- TESTING.md: Testing documentation
- custom_storage.py: AWS Boto3 configuration
- Procfile: To run the application
- Requirements.txt: Containing the python libraries installed
Note: Environment variable values are not exposed in the source code, they are stored locally in env.py that is not checked in(and listed in .gitignore, and on Heroku in app settings

### Database
- The website is a data-centric one with html, javascript, css used with the bootstrap framework as a frontend
- The backend consists of Python built with the Django framework with a database of a Postgres for the deployed Heroku version(production)
- Postgres is a powerful, open source object-relational database system (https://www.postgresql.org/)
- A SQLLite database was used for local development (https://www.sqlite.org/index.html)

#### Physical database model
This model contains all fields stored in the database collections with their data type and mimics the structure of what is actually stored in the Postgres database
<br>![Database model](readme/misc/database-schema.png)

#### Models
- The following models were created to represent the database model structure for the website
##### Order Model
- The Order model contains information about orders made on the website.
- It contains UserProfile as a foreign-key.
- The model contains the following fields: order_number, user_profile, full_name, email, phone_number, country, postcode, town_or_city, street_address1
, street_address2, county, date, delivery_cost, order_total, grand_total, original_bag, stripe_pid
##### OrderLineItem Model
- The OrderLineItem model contains information about an entry in an order, for orders made on the website.
- It contains Order and Product as foreign-keys.
- The model contains the following fields: order, product, product_size, quantity, lineitem_total
##### Product Model
- The Product Model represents a product and its details
- It contains Category as a foreign-key
- The model contains the following fields: category, sku, name, description, has_sizes, price, spice_rating, image
- The image field contains the product image
##### UserProfile Model
- The UserProfile model has a one-to-one relationship with User
- The model contains the following fields: default_phone_number, default_street_address1, default_street_address2
default_town_or_city, default_county, default_postcode and default_country
##### Events Model
- The Events Model contains the information to book an event
- The model contains the following fields: user, event_type, date, time, time_ordered
##### Team Model
- The Team Model represents the members of staff currently employed by the restaurant
- The model contains the following fields: name, role, about, image
##### Category Model
- The Category model contains a product category
- it contains the following fields: name, friendly name



