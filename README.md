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

