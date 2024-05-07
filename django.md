- web framework - semi-complete application
- Good development principles: KIS, YANGI, DRY
- Separation of Concepts (separate UI, datastore access, logic that communicates between UI and datastore)
- MVC (model, view, controller) separates an application into three interconnected components: Model (data), View (UI), and Controller (logic) by structuring applications to distinctly manage data (Model), user interface (View), and application logic (Controller) for efficient development and maintenance.
- In Django the MVC view is called the template (MVT).
- Django uses templates:
    - presentation layer that defines how info is displayed to the end user;
    - visually represents the data model;


## Project & apps
- Project & apps work as containers for our Django code.
- They are the foundation of any Django project.

### Creating a project
The top level in Django is a project. A project is like a container for everything we want to do. By default, the project contains a settings file and some other administrative files.

Important files in our project folder:

1. settings.py: this file contains the project-wide settings, such as installed apps and database connection information, among other things.
2. manage.py: this file is in the root directory, above the project folder. It is used to create apps, run our project and perform some database operations.

### Creating an app
Inside the project, we create apps. We’ll go into this a bit deeper later on, but an app’s structure is like a Python package with multiple Python modules within a directory.

Simply put, apps are the building blocks of Django. They’re the things that actually do something, such as a blog, a to-do list, or a poll. A project can contain many, many apps. You could do everything you want with just one app, but for maintainability and good design practices, it is better to separate different functionality into different apps.

Important files in our apps folder:

1. models.py: our database models are stored here, which define the structure of the database used by our app.
2. views.py: this file contains the view code for our app. You’ve already created some view code to display a text response to the user.

## URLs in Django

- Allow us to present views from a specific URL.
- URLs are required to connect up Django views so that the user can see them.

### Django Request Cycle

1. The user enters a URL to your site in their browser.
2. Django’s URL router checks to see if the URL matches any known URLs.
3. If the entered URL does not match anything in the urls.py files, then Django returns an error.
4. If it does match, then Django passes control to the view specified in the URL. In our case, the view is called index.
5. The view returns either a HttpResponse or a template.
