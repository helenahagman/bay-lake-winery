# Bay Lake Winery

![AmIResponsive](https://res.cloudinary.com/dbjnqkn07/image/upload/v1698654566/PP5/AmIResponsive_i6lwqn.jpg)

[View the Bay Lake Winery Project on Github Pages](//github.com/helenahagman/bay-lake-winery)

[Live site](https://bay-lake-winery-4b9e6ad86e5e.herokuapp.com/)

## CONTENTS

- [Bay Lake Winery](#bay-lake-winery)
  - [CONTENTS](#contents)
  - [Why this project](#why-this-project)
  - [E-Commerce Business Model - B2C](#e-commerce-business-model---b2c)
- [Possible features](#possible-features)
- [Database tables](#database-tables)
  - [Strategy](#strategy)
    - [Target audiences that the website will focus on](#target-audiences-that-the-website-will-focus-on)
      - [Roles](#roles)
      - [Demographics](#demographics)
      - [Psychographics](#psychographics)
  - [User Stories](#user-stories)
    - [EPIC | Web Pages \& Aesthetics](#epic--web-pages--aesthetics)
      - [User Stories](#user-stories-1)
    - [EPIC | Administration \& Functionality](#epic--administration--functionality)
      - [User Stories](#user-stories-2)
    - [EPIC | Error Pages](#epic--error-pages)
    - [EPIC | Testing](#epic--testing)
    - [EPIC | Functionality](#epic--functionality)
      - [User Stories](#user-stories-3)
    - [Link to KANBAN Board with User Stories on Trello](#link-to-kanban-board-with-user-stories-on-trello)
  - [Design](#design)
    - [Imagery](#imagery)
    - [Wire Frames](#wire-frames)
    - [Features](#features)
      - [EPIC | Landing/start page](#epic--landingstart-page)
      - [EPIC | Product page](#epic--product-page)
      - [EPIC | About Page](#epic--about-page)
  - [Accessibility](#accessibility)
  - [Technology](#technology)
    - [Frameworks, Libraries \& Programs Used](#frameworks-libraries--programs-used)
    - [Installed packages](#installed-packages)
  - [Facebook](#facebook)
  - [SEO](#seo)
- [Topics \& possible keywords](#topics--possible-keywords)
  - [Marketing Strategy](#marketing-strategy)
    - [Deployment](#deployment)
      - [Deployment to heroku](#deployment-to-heroku)
      - [Credits](#credits)
    - [Known unsolved bugs](#known-unsolved-bugs)
    - [Credits \& Inspiration](#credits--inspiration)
  - [Other](#other)
  - [TESTING](#testing)
  - [Contents](#contents-1)
  - [Validators](#validators)
  - [User Story Testing](#user-story-testing)
  - [Feature Testing](#feature-testing)
    - [Home page](#home-page)
    - [Product Page](#product-page)
    - [About Page](#about-page)
    - [Shopping Cart](#shopping-cart)
  - [BUGS \& Future fixes](#bugs--future-fixes)
- [Future features](#future-features)

## Why this project

I built this page for my 5th project in the Code Institute course for the Diploma in Full Stack Software Development. I wanted to build a well designed website where the functionality for online phurchases of wine from the made-up family vineyard would be key. The project is base on the key elements of the course and the requirements for PP5. The idea of a small family owned vineyard comes from the one and only grapevine in my own backyard that produces large quantities of grapes each year. We do make our own wine and the whole family is involved, from picking the grapes to the finished product.

## E-Commerce Business Model - B2C

# Possible features

- Log in and log out for both user and admin
- Authentication system  
- Search function for customers looking for a specific product
- Filter function for customers looking for a product type
- Product display with images and descriptions
- Payment function for phurchase possibility
- Shopping cart for the user to add multiple products
- Contact possibilities
- News letter sign up

# Database tables

User Profile Model

| Key        | Name                 | Type          |
| ---------- | -------------------- | ------------- |
| PrimaryKey | user_profile_id      | AutoField     |
| ForeignKey | user                 | User model    |
|            | default_phone_number | CharField[20] |
|            | default_address1     | CharField[80] |
|            | default_address2     | CharField[80] |
|            | default_town_city    | CharField[40] |
|            | default_county       | CharField[80] |
|            | default_postcode     | CharField[20] |
|            | default_country      | CountryField  |

Category Model

| Key        | Name          | Type           |
| ---------- | ------------- | -------------- |
| PrimaryKey | category_id   | AutoField      |  
|            | name          | CharField[254] |
|            | friendly_name | CharField[254] |

Product Model

| Key        | Name         | Type              |
| ---------- | -----------  | --------------    |
| PrimaryKey | product_id   | AutoField         |
| ForeignKey | category     | CategoryModel     |
|            | sku          | CharField[254]    |
|            | name         | CharField[254]    |
|            | description  | TextField         |
|            | price        | DecimalField[6]   |
|            | rating       | DecimalField[6]   |
|            | image        | CloudinaryField   |

Contact Model

| Key        | Name        | Type           |
| ---------- | ----------- | -------------- |
| PrimaryKey | contact_id  | AutoField      |
|	     | email       | EmailField     |
|            | name        | CharField[50]  |
|            | message     | TextField      |

Order Model

| Key        | Name            | Type               |
| ---------- | --------------- | ------------------ |
| PrimaryKey | order_id        | AutoField          |
|            | order_number    | CharField[32]      |
| ForeignKey | user_profile    | UserProfileModel   |
|            | full_name       | CharField[50]      |
|            | email           | EmailField[254]    |
|            | phone_number    | CharField[20]      |
|            | country         | CountryField       |
|            | postcode        | CharField[20]      |
|            | town_or_city    | CharField[40]      |
|            | street_address1 | CharField[80]      |
|            | street_address2 | CharField[80]      |
|            | county          | CharField[80]      |
|            | date            | DateTimeField      |
|            | delivery_cost   | DecimalField[6]    |
|            | order_total     | DecimalField[10]   |
|            | grand_total     | DecimalField[10]   |
|            | original_shopbag| TextField          |
|            | stripe_pid      | CharField[254]     |

OrderLineItem Model

| Key        | Name             | Type            |
| ---------- | ---------------- | --------------- |
| PrimaryKey | OrderLineItem_id | AutoField       |
| ForeignKey | order            | OrderModel      |
| ForeignKey | product          | ProductModel    |
|            | quantity         | IntegerField    |
|            | lineitem_total   | DecimalField[6] |

## Strategy

### Target audiences that the website will focus on

#### Roles

- Persons who are looking to buy wine
- Persons who are interested in winemaking
- Persons who want quality wine from a family farm

#### Demographics

- Persons in the age over 18 years (legal limit in Sweden for alcohol)

#### Psychographics

- Persons who want to:
  - Buy wine
  - Make their own wine
  - Buy wine related products
  - Visit a vineyard
  
## User Stories

### EPIC | Web Pages & Aesthetics

As a developer I can create a website with pages that are easy to navigate,
UX satisfactory and with good functionality

#### User Stories

- As the owner I can show relevant information and offers to increase sales
- As the owner I can display my products to increase sales
- As the owner I can display the current product stock to encourage purchases

- As a user I can easily get the information needed in order to understand what
  the webpage offers
- As a user I can navigate easily on the webpage to go where I want to
- As a user I want to be able to add products to a shopping cart to be able to
  add more items

### EPIC | Administration & Functionality

As a developer I can create relevant functions for the site for easy use for
both the admin and the user

#### User Stories

- As the owner I can display my products to increase sales
- As the owner I can display the current product stock to encourage purchases
- As the user I want to be able to add products to a shopping cart to be able to
  add multiple items before phurchases
- As the administrator I can use the administrator log in to handle products
  displayed on the site
- As the owner I want to be able to communicate with users/customers that have
  questions
- As the owner I want to be able to sens emails to registered users to increase
  sales
- As the administrator I want to be able to see registered users in the admin
- As the administrator I want to be able to see phurchases to be able to handle
  orders
- As the user I want to be able to see my phurchases in a user page
- As the owner I want to have images to the products offered to increase sales
- As the owner I want to have explanatory texts to each product to increase
  sales
- As the administrator I want to be able to offer customers to register to be
  able collect user information
- As a user I want to be able to log in to see previous orders
- As the user I want to be able to log out
- As the owner I want to be able to offer online booking for tours of the
  vineyard

- As a user I want to be able to contact the admin if I have questions
- As a user I want to be able to log in as a current user when I make a
  phurchase
- As the owner I want customers to be able to register as new users
- As the user I want to get information on availbale products

### EPIC | Error Pages

As a developer I can create error pages to inform the user if there is a
problem on the site

### EPIC | Testing

- Administrator log in
- Communicate with users/customers that have questions
- Send emails/sms to registered users
- See registered users in the admin
- See orders
- Images that contribute to what the site is offering
- Explanatory texts
- Registration possibilities for new users
- Online contact form
- Login as a current user
- Register as a new user
- See available products
- Add to shopping bag possibility
- Update shopping bag
- Easy online payment
- Sign up for news letters
- Edit and update products for admin
- Edit profile information

### EPIC | Functionality

#### User Stories

- As a user I want to be able to register as a new user
- As a user I want to be able to log in as a current user
- As a user I want to be able to log out as a logged-in user
- As a user I want to have the possibility to choose a custom username and password
- As the administrator I want to display easy navigation on the site
- As the owner I want to give the user the possibility to phurchase my products
- As the user I want to be able to get in contact if I have queries
- As the owner I want to be able to send customized messages to registered
  customers
- As the owner I want to be able to manage the customer database
- As the user I want to be abel to search for products on the site
- As the user I want to be able to filter categories and products on the site

### Link to KANBAN Board with User Stories on Trello

I activated the feature for colorblind that enhances the colors chosen with dots
[Trello KANBAN Board](https://trello.com/b/Vkxp5qMA/kanban-board-pp5-bay-lake-winery).

![Colorblind example](https://res.cloudinary.com/dbjnqkn07/image/upload/v1698654799/PP5/colorblind_y5oq7v.jpg)

## Design

### Imagery

The images for the site are a mix of private photos and downloaded images from
[Pexels Free Images](https://www.pexels.com/sv-se/).
I used [Cloudinary](https://cloudinary.com/) for storage.

### Wire Frames

Wireframes were created using Miro and were created for mobile, tablet, and desktop views.
I used them as a basis of the pages but using the agile approach the final project
is not looking the exact same way-
[Miro Wire Frames](https://miro.com/app/board/uXjVMklWzgE=/)
![Wire frames](https://res.cloudinary.com/dbjnqkn07/image/upload/v1698655768/PP5/wireframes_miro_ldtcfa.jpg)

### Features

The website contains three main pages: Start page, Product page and About page.
The Product page is accessible through a 'Shop' button the the Start page and
the About page is accessible from the navigation menu on the top of the page.
When on the About page the link in the navigation menu changes to go to Home.
On the About page there is also a contact form for contact. The shopping cart is
accessible through the navigation menu on the top of all pages as well as the
search function and profile access.

#### EPIC | Landing/start page

- Responsive navigation menu on the top of the page with link and icon to a
  shopping cart, access to the profile with log in/log out and register
  possibility. There is also a search function and a link to an About page.
- The links are placed on the right side of the navigation bar, to the left the
  project name is placed and links to the start page.

#### EPIC | Product page

- Short descriptive information along with an image, price and link to make it
  possible to add products to the shopping cart.

#### EPIC | About Page

- A short text about the family bussiness along with a contact form.

## Accessibility

Throughout the process of building the website, I have tried to think of accessibility to make it as user-friendly as possible. I have used the best of my knowledge to:

- Use semantic HTML
- Ensure sufficient color contrasts
- Use images that fit the purpose
- Add hover functionality on menu items and buttons
- Use icons where possible
  ![Icons](https://res.cloudinary.com/dbjnqkn07/image/upload/v1698656006/PP5/icons_ncjj1d.jpg)
- Maintain the same layout on all pages

## Technology

### Frameworks, Libraries & Programs Used

- HTML, CSS, JavaScript
- Django
- GitHub - save & store website files
- CodeAnywhere - codespace
- Bootstrap - framework
- Favicon - icons
- ElephantSQL - database
- Heroku - deployment
- Stripe - payment
- EmailJS - contact
- Trello - KANBAN Board
- Miro - wireframes
- Cloudinary - image storage

### Installed packages

- asgiref             3.7.2
- cloudinary          1.36.0
- dj-database-url     2.1.0
- Django              3.2.22
- django-allauth      0.41.0
- django-countries    7.5.1
- django-crispy-forms 1.14.0
- oauthlib            3.2.2
- Pillow              10.1.0
- python3-openid      3.2.0
- pytz                2023.3.post1
- requests-oauthlib   1.3.1
- sqlparse            0.4.4

## Facebook

- Facebook Business Page
![Facebook](https://res.cloudinary.com/dbjnqkn07/image/upload/v1698570051/PP5/FB-1_qp2lgs.png)
- Facebook first post
![First post](https://res.cloudinary.com/dbjnqkn07/image/upload/v1698570067/PP5/FB-2_mnxcsy.png)

## SEO

- I used WordTracker to find meta keywords and I used the result as help.
![Wordtracker](https://res.cloudinary.com/dbjnqkn07/image/upload/v1698656524/PP5/wordtracker_i8ndad.jpg)

# Topics & possible keywords

- Wineyard - wine lovers, wine, wine shop, organic, grapewine
- Wine products - wine, bottles, wine-making kit
- Family farm - high quality, winemaking, wine tours, wine tasting

## Marketing Strategy

- I think that the best marketing strategy for this project would be to be active on social media such as Facebook, Instagram and Snapchat.
- Set up a google ads account with google analytics to really get the knowledge of what customers want and search for.
- Possibly ads in local newspapers
- It would be very important for regular and high quality posts on social media and work more on the meta tags for the site to drive trafic even more.

### Deployment

For deployment I followed the steps in the walkthrough.

#### Deployment to heroku

1. Account settings
2. Copy the API key
3. Enter the command: heroku_config , and enter the API key
4. Enter heroku username
5. Enter the API key

#### Credits

- Throughout the project I have worked with the walk-through project
  'Building an E-Commerce Platform' for the Code Institute. The base of the set
  up is used from the same.
  
- Images used for this project is a mix of private photos and free images from
  Pexels.com, special thank you to:
 @JillWellington
 @TaryElliott
 @PolinaTankilevitch
 @YlaniteKoppens
 @Nati
 @TerjeSollie
 @MariaOrlova
 @JillBurrow
 @GrapeThings
 @CottonbroStudio
 @MariaPop
 @BernyceHollingworth
 @CharlotteMay

### Known unsolved bugs

- App looks strange on live site
- Menu link on smaller screens dont open

### Credits & Inspiration

Sites and code used for inspiration, trouble shooting, set up and tests for
this project:

- [W3Schools Pyhton Tutorial](https://www.w3schools.com/python/default.asp)
- [Python.org](https://www.python.org/about/help/)
- [Bootrtrap](https://mdbootstrap.com/snippets/standard/mdbootstrap/2515556)
- [DigitalOcean](https://www.digitalocean.com)
- [Slack Community](https://app.slack.com)
- [Real Pyhton](https://realpython.com/python-debug-idle/)
- [Student Robotics](https://studentrobotics.org/docs/troubleshooting/python)
- [Free Codecamp](https://www.freecodecamp.org)
- [Mailchimp](https://login.mailchimp.com/?logout=1)

## Other

- For my privacy policy
![Free Privacy Policy](https://app.freeprivacypolicy.com/download/3e8de0c8-0fe7-4c30-98ee-02853f3e787d)
- I used [Mailchimp](https://login.mailchimp.com/?logout=1) for the newsletter signup form
- For the Site Map I used [XML-Sitemaps](https://www.xml-sitemaps.com/details-bay-lake-winery-4b9e6ad86e5e.herokuapp.com-eedee477b.html)
- For icons I used [Favicon](https://favicon.io/)

## TESTING

Testing features, accessibility, links, responsiveness have been done throughout
the project and after every step of the way tests have been performed to make
sure that the new inserts was working as expected and corrected thereafter.

## Contents

- [Validators](#validators)
- [User story testing](#user-story-testing)
- [Feature Testing](#feature-testing)
  - [Home page](#home-page)
  - [Products page](#product-page)
  - [About page](#about-page)
  - [Shopping Cart](#shopbag-page)
- [Bugs](#bugs)

## Validators

- Html test in the [W3 Validator](https://validator.w3.org/) warnings for Django Template Syntax nature
![W3 Validator](https://res.cloudinary.com/dbjnqkn07/image/upload/v1698657778/PP5/w3c_y4oypq.jpg)
- CSS validator [W3C validation](https://jigsaw.w3.org/css-validator/validator)
![Css validation](https://res.cloudinary.com/dbjnqkn07/image/upload/v1698664722/PP5/cssvalidation_bvrtmv.jpg)

## User Story Testing

- register as a new user - working as expected with confirmation email sent to the user ![confirmation email](https://res.cloudinary.com/dbjnqkn07/image/upload/v1698661455/PP5/confirmmail_szo8ac.jpg) then shows on the screen as expected - Pass
- log in as a current user - working as expected - Pass
- log out as a logged-in user - working as expected - Pass
- choose a custom username and password - working as expected - Pass
- display easy navigation on the site - working as expected - could add the link to home/about on more pages - Pass
- phurchase - working but needs improvement, the delivery cost is not displaying in the confirmation letter  - Error/Improvement needed
- get in contact - no contact form is throwing a form submission error - Error/Improvement needed
- customized messages to registered users - can be done via mailchimp after user has registerd for newsletter - Pass/not fully implemented
- manage the customer database - working via the admin panel - Improvement to add to the website so the admin dont have do go in via the admin panel and just log in.
- search for products on the site - wroking as expected - Pass
- filter categories and products on the site - working as expected - Pass

## Feature Testing

- search bar - working as expected - Pass
- Login - working as expected - Pass
- Register - working as expected - Pass
- Log out - working as expected - Pass
- newsletter signup - working as expected - Pass
- sorting feature - working as expected - Pass
- profile update - working as expected - Pass

### Home page

All links on the home/Index page is working as expected - links in navbar, search, about, my account, shopping bag, shop now button, facebook  link, sign up form, privacy policy

### Product Page

All links on the product page is working as expected - links in navbar, footer links, sort by, tags, images

### About Page

The following links on the about page is working as expected - links in navbar, footer links, shop now button.
Contact form is not working as expected - error when submitting the form ![Contact form](https://res.cloudinary.com/dbjnqkn07/image/upload/v1698662751/PP5/formfail_v7jnnr.jpg)

### Shopping Cart

All links on the page is working as expected - however the shoppingbag need some improvement for the error in the confirmation when a phurchase has been made ![Delivery error](https://res.cloudinary.com/dbjnqkn07/image/upload/v1698661466/PP5/confirmation_g6yrtf.jpg)

## BUGS & Future fixes

- Contact form on about page - not working - needs more implementation
- Positioniong of images on product page needs some improvement as they are not centered
- Rating function is not working - will be set to future implementations
- Plus and minus buttons when in the shopping cart is not working properly
- The update and remove buttons in the checkout form is not working
- The delivery and therefor also the total is not being updated properly in the order confirmation

# Future features

![Future implementations](https://res.cloudinary.com/dbjnqkn07/image/upload/v1698666166/PP5/future_cvjv5b.jpg)
