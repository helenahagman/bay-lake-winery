# The Personal Trainer Project

![AmIResponsive](/add link/orImg.jpg)

![View The Personal Trainer Project on Github Pages](//github.com/helenahagman/the-personal-trainer-project/tree/main)

![Live site](//ptproject-ec6a8ad157bf.herokuapp.com/)

## CONTENTS

- [The Personal Trainer Project](#the-personal-trainer-project)
  - [CONTENTS](#contents)
  - [Why this project](#why-this-project)
  - [Strategy](#strategy)
    - [Target audiences that the website will focus on](#target-audiences-that-the-website-will-focus-on)
      - [Roles](#roles)
      - [Demographics](#demographics)
      - [Psychographics](#psychographics)
      - [User needs](#user-needs)
      - [Client needs](#client-needs)
      - [Content Requirements](#content-requirements)
      - [Functionality](#functionality)
    - [Link to KANBAN Board with User Stories on Trello](#link-to-kanban-board-with-user-stories-on-trello)
  - [Design](#design)
    - [Imagery](#imagery)
    - [Wire Frames](#wire-frames)
    - [Features](#features)
      - [EPIC | All main pages](#epic--all-main-pages)
      - [EPIC | Start/about page](#epic--startabout-page)
      - [EPIC | Personal Trainer Page](#epic--personal-trainer-page)
      - [EPIC | Member Page](#epic--member-page)
  - [Accessibility](#accessibility)
  - [Technology](#technology)
    - [Frameworks, Libraries \& Programs Used](#frameworks-libraries--programs-used)
  - [Testing](#testing)
    - [Deployment](#deployment)
      - [Deployment to heroku](#deployment-to-heroku)
      - [Credits](#credits)
    - [Known unsolved bugs](#known-unsolved-bugs)
    - [Credits \& Inspiration](#credits--inspiration)

## Why this project

I built this page for my 4th project in the Code Institute course for the Diploma in Full Stack Software Development. I wanted to build a good-looking website where the functionality for online booking of Personal Trainer sessions would be possible and where both the user and the owner of the site can get the information they need. As building an online booking for Personal Trainer Sessions will be one of my projects for my current job as well this fall, I used the opportunity to talk to my boss for user stories and planning of the project. Key points that would be crucial for the real site have been a part of this project.

## Strategy

### Target audiences that the website will focus on

#### Roles

- Persons who want to get tips from a Personal Trainer
- Persons who are interested in gym exercise
- New users that are not yet registered
- Current users that are registered

#### Demographics

- Persons in the age over 18 years

#### Psychographics

- Persons who want to:
  - Get in general shape
  - Get stronger
  - Lose weight
  - Train for a specific goal (ex a competition)
  - Increase their stamina
  - Persons who are new to training in a gym
  - Persons who want to get tips from a Personal Trainer

#### User needs

- Login as a current user
- Register as a new user
- See available personal trainer sessions
- Get information on what is offered on the site
- Book personal trainer sessions
- Cancel booked sessions
- Sign up for membership
- Get in contact
- Edit registered user information

#### Client needs

- Provide information about the company
- Offer Memberships
- Offer Bookable Personal Trainer Sessions
- Administrator log in
- Communicate with users/customers that have questions
- Send emails/sms to registered users
- See registered users
- See booked sessions

#### Content Requirements

- Images that contribute to what the site is offering
- Explanatory texts
- Registration possibilities
- Log in possibilities
- Log out possibilities
- Online booking for Personal Trainer Sessions
- Contact

#### Functionality

- Register as a new user
- Login as a current user
- Log out as a logged-in user
- Possibility to choose a custom username and password
- Easy navigation on the site
- Book available sessions
- Get in contact
- Send customized messages to registered customers
- Cancel a booked session
- Manage customer database

### Link to KANBAN Board with User Stories on Trello

[Trello KANBAN Board](https://trello.com/b/yxkUuMp3/kanban-board)

## Design

### Imagery

The images for the site have been downloaded from [Pexels Free Images](https://www.pexels.com/sv-se/).

### Wire Frames

Wireframes were created using Miro and were created for mobile, tablet, and desktop views.
[Miro Wire Frames](https://miro.com/app/board/uXjVM94tSQs=/?share_link_id=555048984575)

### Features

The website contains three main pages: start/about page, Personal Trainer page, Members page. All main pages are accessible from the navigation menu on the top of the page.

#### EPIC | All main pages

- Responsive navigation menu on the top of the page to be able to navigate to the three main pages. The links to the pages are placed on the right side of the navigation bar, to the left a logo with the project name is placed.
- In the footer, social media links to Facebook and Instagram are placed in the form of icons.

#### EPIC | Start/about page

- Short descriptive information along with an image followed by two postcards with a link to the Personal Trainer page and the Member Page.

#### EPIC | Personal Trainer Page

- Short descriptive information along with an image and a button to book a session, below that two postcards with a link to book sessions and the Member Page.

#### EPIC | Member Page

- Short descriptive information along with an image, below that two postcards with a link to the contact form and the login and register form.

## Accessibility

Throughout the process of building the website, I have tried to think of accessibility to make it as user-friendly as possible. I have used the best of my knowledge to:

- Use semantic HTML
- Ensure sufficient color contrasts
- Use images that fit the purpose
- Add hover functionality on menu items and buttons
- Use icons for social media links instead of text
- Maintain the same layout on all main pages

## Technology

### Frameworks, Libraries & Programs Used

- HTML, CSS, JavaScript
- Django, Flask
- GitHub - save & store website files
- CodeAnywhere - codespace
- Bootstrap - framework
- Favicon - icons
- ElephantSQL - database
- Heroku - deployment
- EmailJS - contact
- Trello - KANBAN Board
- Miro - wireframes
- Pexels - images

## Testing

Testing features, accessibility, links, responsiveness have been done throughout the project and after every step of the
way tests have been performed to make sure that the new inserts has been working correctly and corrected thereafter.
For complete view of testing please see <href="/workspaces/healthclub-PP4/TESTING.md">TESTING.md

### Deployment

#### Deployment to heroku

1. Account settings
2. Copy the API key
3. Enter the command: heroku_config , and enter the API key
4. Enter heroku username
5. Enter the API key

#### Credits

- Code Used
- Images
- Acknowledgments

### Known unsolved bugs

- App looks strange on live site
- Menu link on smaller screens dont open
- Images on live site
- Book session button on Index page
- Link to Sign in on Register page
- Link to Register on Sign in page
- Contact post do not work on live site

### Credits & Inspiration

Sites and code used for inspiration and test on this project:

- <href="https://www.w3schools.com/python/default.asp">W3School Pyhton Tutorial</a> \* Problem solving
- <href="https://www.python.org/about/help/">Pyhton.org</a> \* Problem solving
- <href="https://mdbootstrap.com/snippets/standard/mdbootstrap/2515556">Bootstrap</a> \* Templates: 2 columns and PostCard from MDBootstrap
- <href="https://www.emailjs.com/">EmailJS</a> \* API connection for messages
- <href="https://www.digitalocean.com">DigitalOcean</a> \* Problem solving and ideas

- I used the walkthrough in the Codeinstitute section "Startbootstrap clean-blog URL change" to add the clean-blog theme from bootstrap to style my pages.
- Thank you to The Code Institute for material, instructions and connection to the community in Slack
