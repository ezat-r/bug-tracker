# Bug Tracker

A bug tracker project which allows users to report bugs and request new features.

[![Build Status](https://travis-ci.org/ezat-r/bug-tracker.svg?branch=master)](https://travis-ci.org/ezat-r/bug-tracker)

## Demo

To view the project in action, visit the following link:



## Project Purpose & Features

The project was created to solve the below questions:

**Raising Bugs & Feature Requests:**
- Users can login and create Bugs or Feature Requests against their projects, ensuring quality and making project management easier.

**A Logical Work Flow:**
- The Bug Tracker follows a clear cut work flow in terms of how things work; it prevents users from making unintended action i.e. Closing a bug or feature request which
is yet to be resolved etc. 
- The Bug Tracker makes it so a Bug or Feature Request has to be Resolved before you can Close it.
- Example flow is as follows: *Issue Created -> Issue Resolved -> Issue Closed*

**Filtering of Issues:**
- The Bug Tracker has functionality in place which allows users to *filter Bugs by Project*, making it easier for Users to focus their attention to the correct area, hence,
improving efficiency and saving precious time.

**Project Management:**
- The Bug Tracker gives users the ability to manage their Projects. At the click of a button, Users can add new Projects or modify existing ones.

## UX

### Mockups

Initial mockups were made using **Balsamiq** software to aid in the creation of the website; a basic mockup was made of each area of the Project. 
- The mockups can be found in the **Mockups** folder. 

## Technologies Used

List of tools and technologies used in this project are as follows:

- [Materialize CSS](https://materializecss.com/)
    - The project uses **Materialize CSS** to simplify the web page design and to maintain consistency across multiple browsers and screen resolutions. Materialize icons were also used throughout the project such as button icons etc.
- [Bootstrap](https://getbootstrap.com/docs/3.3/)
    - The project uses **Materialize CSS** to simplify the web page design and to maintain consistency across multiple browsers and screen resolutions. Materialize icons were also used throughout the project such as button icons etc.
- [JQuery](https://jquery.com)
    - The project uses **JQuery** to aid with the Materialize CSS navigation and various other components across the project use it to function correctly. 
- [Python](https://www.python.org/)
    - The **Python** programming language was used to code the backend of the Recipe Management project.
- [Django](https://www.djangoproject.com/)
    - The project uses **Django** which is a Python Web Framework used as the backend of the project and fulfilling functions such as; connecting to the SQL database, controlling routing and navigation across pages etc.
- [Heroku](https://www.heroku.com/)
    - The project uses **Heroku** as the Hosting platform for this project; this was because GitHubPages only provides hosting for static projects, and not dynamic projects like this Recipe Manager project.
- [Font Awesome](https://fontawesome.com/)
    - The project uses **Font Awesome** to provide icons for the Footer social network links. 
- [Balsamiq](https://balsamiq.com/)
    - This tool was used to create the mockups of the website at the beginning of the project. 

## Testing


## Travis Continuous Integration (CI) Testing

*Travis CI* was used to continuously test the Project, every time a commit was made on GitHub. This basically ran all the tests in the 'tests.py' as well as other inbuilt tests, on every commit made to GitHub to ensure that everything was working fine.

### Setting Up Travis CI

1. Login to https://travis-ci.org/
2. Link your Travis CI account to your GitHub account.
3. Then, link your preferred project by clicking the *Connect* button.
4. Navigate to your Project Folder, on your machine and create a 'requirements.txt' file.
5. Create a .travis.yml file. Open the file and fill it with the correct setup data.
6. Then, perform a Git Commit & Push to GitHub.
7. Travis will then automatically pick up the changes and perform the tests.
8. Any failures will be flagged up and you can then view the logs in more detail when you login again to Travis CI.
9. Your project is now setup with Travis CI.