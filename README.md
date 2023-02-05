# Capricci Store
<br>

**Developer: Julio David Hernandez**

[Live Website](https://capricci.herokuapp.com/)

<img src="media/readme/responsive/responsive.jpg">

<hr>

## Table of Contents
  - [About](#about)
  - [Bussines Model](#Bussines)
  - [Marketing](#marketing)
  - [User Goals](#user-goals)
  - [Site Owner Goals](#site-owner-goals)
  - [User Experience](#user-experience)
  - [Design](#design)
    - [Colours](#colours)
    - [Fonts](#fonts)
    - [Structure](#structure)
      - [Website pages](#website-pages)
      - [Database](#database)
    - [Wireframes](#wireframes)
  - [Technologies Used](#technologies-used)
  - [User Stories](#user-stories)
  - [Features](#features)
  - [Validation](#validation)
  - [Testing](#testing)
    - [Manual testing of user stories](#manual-testing-of-user-stories)
    - [Automated testing](#automated-testing)
    - [Performing tests on various devices](#performing-tests-on-various-devices)
    - [Browser compatibility](#browser-compatibility)
  - [Bugs](#bugs)
  - [Configuration](#configuration)
  - [Credits](#credits)
  - [Acknowledgements](#acknowledgements)
<hr>

### About

Handmade goods shop family concept to aid the local community's economy.

With two different kinds of accounts
- A regular user account 
- An administrator user account
<hr>

### User Goals

- Use the site's navigation tools as needed 
- Purchase products from the stock 
- Pay attention to comments on individual items' descriptions
- The function for registered users to comment on specific items.

<hr>

### Site Owner Goals

- Supply an online store for Local Users.
- An internet store where customers may purchase original gifts.
- Create a simple, aesthetically pleasing design.
- Provide full responsive application with comfortable navigation.
- Security payment method to make feel safe the user.
<hr>

## User Experience
<hr>

### Target Audience

- Those looking to give handmade items as gifts.
- Enthusiasts who want to promote local business.
- People who are searching gift ideas for the holidays for various goods.

<hr>

### User Requirements and Expectations

- Practical site use.
- Fluent site navigation.
- Attractive design.
- Responsive Design by different screen size.
- A Responsive application that enables users to access the store from any platform.
- Simple methodology to be use the applications.
- Applications and Links working as hoped-for.
- Easy method to contact with the managers.

##### Back to [top](#table-of-contents)


## User Stories
<hr>

### Users

Like user I want to:

1. Have a responsive Navigation Bar and home page.
2. Have a responsive Footer And networks.
3. Have a responsive view to Check cart content.
4. Purchase products by quantity.
5. Get the New Collection.
6. Check cart amount.
7. have a Search function.
8. Get own cart at any time.
9. Get own total at any time.
10. Get the offers and season products.
11. Have a View with the individual item details.
12. Get the Checkout details.
13. Get Checkout details by Email.
14. Bring the Payment details by Stripe Service. 
15. Get Recipe view with the Details.
16. Confirm own Email by a email confirmation.
<hr>

### Site Owner

As a site Owner, I want to:

17. Add a product.
18. Delete product. 
19. Edit/Update product. 
20. Add a category. 
21. Delete category. 
22. Edit/update category. 

##### Back to [top](#table-of-contents)

<hr>

## Design

### Colours

Using the W3schools color picker, the color tones were carefully selected to reflect the concept and create a straightforward and user-friendly design.
three hues used to create a fluid user experience design

<details><summary>Pink Color</summary>
<img src="media/readme/details/pink.png">
</details>
<details><summary>Blue Color</summary>
<img src="media/readme/details/blue.png">
</details>
<details><summary>Red Color</summary>
<img src="media/readme/details/red.png">
</details>
<details><summary>Violet Color</summary>
<img src="media/readme/details/violet.png">
</details>
<details><summary>Color Picker</summary>
<img src="media/readme/details/picker.png">
</details>

<hr>

### Fonts

ROBOTO and Dancing Font from GOOGLE. The most used on the majority of data flow.
<hr>

### Structure

#### Website pages


Following the principles of UXD (user experience design), the website structure was designed to be fluid and simple to operate. 
The website was composed of a page with:

  - The website consists of the following sections:
  - The Home page and some interactive pages.
  - The Products List.
  - The Product Details.
  - The Product Details with option to comment for Login Users.
  - Log In Page for register user.
  - Log out Page for login user.
  - Register Page for non login user.
  - Manager Page to Admin User to delete items.
  - Edit item page for Admin user.
  - Add item Page for Admin User.
  - Footer with social media and newsletter.
  - 403, 404, 500 error page.
<hr>

#### Database

- The backend consists in the use of Django framework based in python with a database of a Postgres Elephant SQL for the deployed version.

<details><summary>Database</summary>
<img src="media/readme/database/database.png">
</details>

- Consist in five database models, all fields are stored in the database structure stored in the database.
The following models represent the database model structure of the website:

<details><summary>Models Diagram</summary>
<img src="media/readme/database/models.png">
</details>

<hr>

##### User Model
- The User model is part of the Django allauth library and was represented as hypothetical.
<hr>

##### Product Model
- The Prod model is made in the following fields: category, title, title_slug, price, scount, quantity, featured_image, scountbool, description, created_on
- The model has a one-to-one relationship with Category
- The image field contains the Product Picture.

<details><summary>Product Model</summary>
<img src="media/readme/database/product.png">
</details>

<hr>

##### Category Model
- The Cat model is made in the following fields: author, title, slug, featured_image, created_on 
- The image field contains the Category Picture if is needed.

<details><summary>Category Model</summary>
<img src="media/readme/database/category.png">
</details>

<hr>

##### Order Model

- The Order model contains the fields: order_number, owner, full_name, email, phone_number, canton, city, postcode, street_address1, street_address2, date, delivery_cost, order_total, grand_total
- The model is contected with User if the order is done with login user.

<details><summary>Order Model</summary>
<img src="media/readme/database/order.png">
</details>

<hr>

##### Order Products

- The OrdProd model contains the following fields: order, product, quantity, prods_total.
- The model is contected with User if the order is done with login user.
- The model has a one-to-one relationship with the Order.
<details><summary>Order Products Model</summary>
<img src="media/readme/database/order_products.png">
</details>

<hr>

### Wireframes

<details><summary>Laptop & Desktop</summary>
  <details><summary>Home</summary>
  <img src="media/readme/wireframes/pc/Home_pc.png">
  </details>
  
  <details><summary>Products</summary>
  <img src="media/readme/wireframes/pc/Products_pc.png">
  </details>
  
  <details><summary>Product Details</summary>
  <img src="media/readme/wireframes/pc/Product_details_pc.png">
  </details>

  <details><summary>Cart</summary>
  <img src="media/readme/wireframes/pc/Cart_pc.png">
  </details>

  <details><summary>Check</summary>
  <img src="media/readme/wireframes/pc/Check_details_pc.png">
  </details>

  <details><summary>Payment</summary>
  <img src="media/readme/wireframes/pc/Payment_pc.png">
  </details>
  
  <details><summary>Manager Products</summary>
  <img src="media/readme/wireframes/pc/Manager_pc.png">
  </details>
  
  <details><summary>Manager Add/Edit</summary>
  <img src="media/readme/wireframes/pc/Manager_Edit_add_pc.png">
  </details>

  <details><summary>About Us</summary>
  <img src="media/readme/wireframes/pc/About_us_pc.png">
  </details>
</details>
<details><summary> Tablet & Smartphone </summary>

  <details><summary>Home</summary>
  <img src="media/readme/wireframes/phone/Home_phone.png">
  </details>
  
  <details><summary>Products</summary>
  <img src="media/readme/wireframes/phone/Products_phone.png">
  </details>
  
  <details><summary>Product Details</summary>
  <img src="media/readme/wireframes/phone/Product_details_phone.png">
  </details>

  <details><summary>Cart</summary>
  <img src="media/readme/wireframes/phone/Cart_phone.png">
  </details>

  <details><summary>Check</summary>
  <img src="media/readme/wireframes/phone/Check_details_phone.png">
  </details>

  <details><summary>Payment</summary>
  <img src="media/readme/wireframes/phone/Payment_Phone.png">
  </details>
  
  <details><summary>Manager Products</summary>
  <img src="media/readme/wireframes/phone/Manager_phone.png">
  </details>
  
  <details><summary>Manager Add/Edit</summary>
  <img src="media/readme/wireframes/phone/Manager_edit_add_phone.png">
  </details>

  <details><summary>About Us</summary>
  <img src="media/readme/wireframes/phone/About_us_phone.png">
  </details>
</details>

##### Back to [top](#table-of-contents)
<hr>

## Technologies Used
<hr>

### Languages & Frameworks

- HTML
- CSS
- Javascript
- Python
- Bootstrap
- Django

### Libraries & Tools

- asgiref==3.5.2
- dj-database-url==1.2.0
- dj3-cloudinary-storage==0.0.6
- Django==3.2.16
- django-allauth==0.51.0
- django-crispy-forms==1.14.0
- django-summernote==0.8.20.0
- gunicorn==20.1.0
- oauthlib==3.2.2
- Pillow==9.4.0
- psycopg2==2.9.5
- PyJWT==2.6.0
- python3-openid==3.2.0
- pytz==2022.6
- requests-oauthlib==1.3.1
- sqlparse==0.4.3
- stripe==5.0.0
- whitenoise==6.2.0
- [Git](https://git-scm.com/) To have a version control
- [GitHub](https://github.com/) To store The Git Data
- [Postgres SQL](https://www.elephantsql.com/) – The server service to Save Postgres SQL database
- [Cloudinary](https://cloudinary.com/) cloudinary-storage 1.30.0
- [Summernote](https://summernote.org/) To use Summerfield in forms
- [Visual Studio Code](https://code.visualstudio.com/) & [GitPod](https://www.gitpod.io/) To Edit and test the code.
- [Favicon.io](https://favicon.io) To Create the site's favicon.
- [Google Fonts](https://fonts.google.com/) To Use special fonts.
- [WireFrame](https://wireframepro.mockflow.com/) To Design the wireframes.
- [Dbdiagram.io](https://dbdiagram.io) To create the diagram Database.
- [Herooku](https://dashboard.heroku.com) To deploy the project online.
<hr>

- Validation:

  - [WC3 Validator](https://validator.w3.org/) to validate the html Files
  - [Jigsaw W3 Validator](https://jigsaw.w3.org/css-validator/) to validate the css Files
  - [Wave Validator](https://wave.webaim.org/) to check accessibility
  - [Lighthouse](https://developers.google.com/web/tools/lighthouse/) to check performance web apps
  - [JShint](https://jshint.com/) to validate JavaScript Files
  - Pylint Flake8 to check Python Files

##### Back to [top](#table-of-contents)

<hr>

## Features

<hr>

### Navigation Bar

- This Feature can be accessed at the all pages
- The nav bar includes links to Home, Search in the stock and cart.

  - Logged-in users will see their name right in the nav bar with option to click to log out
  - Not logged-in users have the option to register or log in.
  - Admin Users Have the option to Stock Manager.

- The nav bar have responsive design to change in small medium and large size screens.
- The navbar have down a filter Products can be filtered By seasons.

- User stories covered: 1

<details><summary>Home Page</summary>
  <details><summary>Midium and small Screen</summary>
  <img src="media/readme/views/Navigation_bar/pc_nav_bar.png">
  </details>
  <details><summary>Large Screen</summary>
  <img src="media/readme/views/Navigation_bar/phone_nav_bar.png">
  </details>
</details>

<hr>

### Home page

- Home page is main view.
- Main page contains the actualy offers.
- User stories covered: 1
<details><summary>Home Page</summary>
  <details><summary>Phone View</summary>
  <img src="media/readme/views/home/phone_home.png">
  </details>
  <details><summary>Laptop View</summary>
  <img src="media/readme/views/home/pc_home.png">
  </details>
</details>

<hr>

### Footer
- A footer is displayed in the base template, it is shows at bottom in each page.
- Contains network links to get in contact.
- Includes the subscription to the newsletter.
- User stories covered: 2

<details><summary>Footer</summary>
<details><summary>Laptop</summary>
<img src="media/readme/views/footer/pc_footer.png">
</details>
<details><summary>Tablet</summary>
<img src="media/readme/views/footer/tablet_footer.png">
</details>
<details><summary>Phone</summary>
<img src="media/readme/views/footer/phone_footer.png">
</details>
</details>

<hr>