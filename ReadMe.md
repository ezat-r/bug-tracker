# Bug Tracker

A bug tracker project which allows users to report bugs and request new features.

[![Build Status](https://travis-ci.org/ezat-r/bug-tracker.svg?branch=master)](https://travis-ci.org/ezat-r/bug-tracker)

## Demo

To view the project in action, visit the following link:

https://bugdb-tracker.herokuapp.com/

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

**User Restriction**:
- The Bug Tracker restricts normal users to only raise new bugs and make changes to bugs. Super Users or Developers have the ability to 'Resolve' bugs.

**Pagination**:
- Pagination is used to organise issues in a more user friendly way. All issues are broken down in 10s, with the most recently updated issues shown first.

## UX

### Mockups

Initial mockups were made using **Balsamiq** software to aid in the creation of the website; a basic mockup was made of each area of the Project. 
- The mockups can be found in the **Mockups** folder. 

## Technologies Used

List of tools and technologies used in this project are as follows:

- [Materialize CSS](https://materializecss.com/)
    - The project uses **Materialize CSS** to simplify the web page design and to maintain consistency across multiple browsers and screen resolutions. Materialize icons were also used throughout the project such as button icons etc.
- [Bootstrap](https://getbootstrap.com/docs/3.3/)
    - The project also uses some **Bootstrap** elements further simplify and maintain consistency throughout the project.
- [JQuery](https://jquery.com)
    - The project uses **JQuery** to aid with the Materialize CSS navigation and various other components across the project use it to function correctly. 
- [Python](https://www.python.org/)
    - The **Python** programming language was used to code the backend of the Recipe Management project.
- [Django](https://www.djangoproject.com/)
    - The project uses **Django** which is a Python Web Framework used as the backend of the project and fulfilling functions such as; connecting to the SQL database, controlling routing and navigation across pages etc.
- [Stripe API](https://stripe.com/docs/api)
    - The project uses **Stripe** to take payments during the *Up Voting* process for *Feature Request* type issues.
- [Heroku](https://www.heroku.com/)
    - The project uses **Heroku** as the Hosting platform for this project; this was because GitHubPages only provides hosting for static projects, and not dynamic projects like this Recipe Manager project.
- [Font Awesome](https://fontawesome.com/)
    - The project uses **Font Awesome** to provide icons for the Footer social network links. 
- [Balsamiq](https://balsamiq.com/)
    - This tool was used to create the mockups of the website at the beginning of the project. 

## Testing

Testing was carried out for piece of the project, app by app. 

### Web UI Testing
Testing scenarios run:

1. Navigation:
    1. Click on all main navigation buttons i.e. 'Home', 'Create New', 'Analytics' etc. Verify that each button takes you to the correct page.
    2. Click onto the 'Bug Tracker' brand name in the top-left of each page and verify that it takes you to the 'Recipes' page.

2. Forms testing:
    1. Go to the "Create New Issue" page.
    2. Try to submit the empty form and verify that an error message about the required fields appears.
    3. Try to submit the form without selecting a 'Project' and verify that you cannot submit the form.
    4. Try to submit the form with all valid inputs and verify that a new issue is created successfully and you are re-directed to the 'All Issues' page. Verify that the new issue shows up correctly.
    5. Repeat steps 1-4 for the 'Edit Issue' and other forms and make sure everything is working as expected.

3. Create New Issue:
    1. Go to the "Create New Recipe" page.
    2. Fill out the form.
    3. Click the *CREATE* button.
    4. Verify that you are re-directed to the "All Issues" page and the new Issue can be viewed.

4. Edit Issue:
    1. Go to the "All Issues" page and click onto an issue **you haven't reported**.
    2. Verify that you *do not* see the *Edit* button.
    3. Go back to the *All Issues* page and click onto an issue **reported by you**.
    4. Verify that you see a *Edit* button.
    5. Click the *EDIT* button for your Issue.
    6. Make some changes and then click the *UPDATE* button.
    7. Verify that you are re-directed to the View Issue page for your issue and the updates are applied to the Issue.

5. Detailed Issue View:
    1. Go to the "All Issues" page.
    2. Click the *View* button for one of the issues on display.
    3. Verify that all the information on the page is correct.

6. Up Voting Of A *Bug* type Issue:
    1. Go to the "All Issues" page.
    2. Click the *View* button for one of the issues on display.
    3. Click the *Up Vote* button.
    4. A pop-up should come up asking for you to add a comment. Enter a comment and then click the *Up Vote* button.
    5. Log out & log back in as a *Super User* and verify that the number of Up Votes for that issue has risen by 1.

7. Up Voting Of A *Feature Request* type Issue & Taking A Payment:
    1. Go to the "All Issues" page.
    2. Click the *View* button for one of the issues on display.
    3. Click the *Up Vote* button.
    4. You should be re-directed to a *Make Payment* page.
    5. Fill out the form and then click the *SUBMIT PAYMENT* button.
    6. Log out & log back in as a *Super User* and verify that the number of Up Votes for that issue has risen by 1.
    7. Login to your Stripe API dashboard and verify that the payment has come through.

8. Typography:
	1. Go to the "All Issues" page.
	2. Have a look at the text and observe if all text is clearly visible i.e. is it too small, too big.
    3. Click the 'View' button to access a detailed Recipe view and verify that the text looks readable, is not hard to read etc.
	4. Follow step 2-3 again, however, this time do the same for different screen sizes i.e. Phone, Tablet, Desktop etc.
	5. Follow steps 2 - 4 for all pages. Is the the typography consistent across all pages? Is it readable on small screen devices?

### Travis Continuous Integration (CI) Testing

*Travis CI* was used to continuously test the Project, every time a commit was made on GitHub. This basically ran all the tests in the django project as well as other inbuilt tests, on every commit made to GitHub to ensure that everything was working fine.

#### Setting Up Travis CI

1. Login to https://travis-ci.org/
2. Link your Travis CI account to your GitHub account.
3. Then, link your preferred project by clicking the *Connect* button.
4. Navigate to your Project Folder, on your machine and create a 'requirements.txt' file.
5. Create a .travis.yml file. Open the file and fill it with the correct setup data.
6. Then, perform a Git Commit & Push to GitHub.
7. Travis will then automatically pick up the changes and perform the tests.
8. Any failures will be flagged up and you can then view the logs in more detail when you login again to Travis CI.
9. Your project is now setup with Travis CI.

### Python Tests

Python tests was written for the Django Project, on a app by app basis and each app was further broken down into 3 main areas of testing; *Models*, *Views* & if applicable, *Forms*.

#### Testing Models

Models are used in Django to model each Database object and are commonly used to Create & Fetch objects to and from the Database. Models are also used to give a description of what each item in a Database looks like and their relationship with other models in the database (if applicable).

Some examples of Models testing:
- Creating new database entries using the Models and then verifying that they contained the correct values.
- Searching for entries using the *Primary Key* and making sure it's the correct entry.
- Make sure the *NOT NULL* constraints are handled correctly i.e. it doesn't let you create a new issue without specifying values for certain properties etc.

Model testing can be found in the *test_models.py* file for each of the apps - where relevant; some apps did not require a *Models.py*.

#### Testing Views

Views are used to handle what users see on a page. They also handle any POST requests make by submitting a form. 

Some examples of Views testing:
- Access specific URLs without authentication and make sure it re-directs to the 'Login' page.
- Login and access login-only urls and make sure you can access them fine.
- Attempt to register a user with incorrect values for username and password & make sure it gets handled accordingly.
- Navigate to views and make a POST request using **Valid** data and make sure it works correctly.
- Make a POST request using **Invalid** data and make sure it works as expected.
- Make a Payment using incorrect payment information and verify that it gets handled fine.

Views testing can be found in the *test_views.py* file for each of the apps.

#### Testing Forms

Forms are used in some of the apps to aid in the creation and update of database objects. Forms are usually passed through to a web page via a View.

Some examples of Forms testing:
- Attempting to create a new issue by providing **Invalid** form entries and make sure it gets handled correctly.
- Create new issues using **Valid** form entries and make sure a new issue is created fine and added to database.

Forms testing can be found in the *test_forms.py* file for each of the apps - where relevant; some apps did not require a *Forms.py*.

### Coverage

Coverage was a tool used to help in getting each of the app closer to the ideal 100% Test Coverage goal. After a test was written, *Coverage* was used to determine and keep track of the Test coverage. Tests were then written or removed to try and achieve the 100% 

### Screen Size & Different Browsers

#### Screen Sizes

Using the Debugger tools on Google Chrome I was able to view the website in different screen sizes. The following screen sizes were verified:
- 360px X 640px (WxH)
- 768px X 1024px (WxH)
- 1024px X 1366px (WxH)

Test's were run for various screen sizes, these are listed in the above **Testing** section.

On smaller screen sizes i.e. when the width is 768px or less, the website switches to a stacked view to maintain a consistent look.

#### Multi Browser Testing

Multi browser testing was carried out to ensure there is consistency across different Browsers. The following Browsers were tested:
- Google Chrome
- Mozilla Firefox
- Microsoft Edge
- Internet Explorer v11

## Remote Deployment

The website was deployed using Heroku. Deployment process which was followed is given below:

1. Login to Heroku.
2. Click the *Create* -> *Create new app* button.
3. Give the app a name and select region as *Europe*. Then, click the *Create app* button.
4. Once app is created, click onto the *Resources* tab.
5. In the **Add-ons** search bar, search for and select *Heroku Postgres*. Select the *Hobby Dev - Free* option and then click the *Provision* button.
6. Once that's done, click onto the **Settings** tab and click the 'Reveal Config Vars' button.
7. Add all the **Key** & **Value** pairs for your project i.e. for the django secret key, Stripe API keys etc.
8. Once you have added all your key-value pairs, copy the *DATABASE_URL* value and copy it somewhere locally -> create a new environment variable to use it.
9. Hook up your Django Project to the Postgres Database, then once you are happy, go ahead & run the following command in a terminal window: **python3 manage.py makemigrations**
10. Go into your Cloud9 and enter the following command in the terminal: **git remote add heroku https://heroku-git-url.git** -> replace the url with your appropriate one.
11. Run the following command to create a *requirements.txt* file: **pip3 freeze --local > requirements.txt**
12. Create a *Procfile* by running the following command: **echo web: gunicorn bugTracker.wsgi:application > Procfile**
13. Do a git commit to push all changes to your local repository and run the following command: **git push -u heroku master**
14. Access your heroku app link to see deployment.
15. Your app is now deployed onto Heroku.

## Running Locally

In the event you would like to run the project locally follow the below steps:

1. Via the terminal window or PowerShell (on Windows), cd into the root of the directory the project.
2. Run the following command: **pip3 install -r requirements.txt** -> this will go ahead and install all dependencies needed to run the project.
3. Once all requirements are install, run the following command: **python app.py**.
4. This will launch the Django project and output a url on the terminal window. Copy and paste this in a browser and this will load the project.