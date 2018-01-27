# Django App Boilerplate

## Introduction

Django app boilerplate is a template for a Django app to start quickly, simply, and with least repetition. The purpose of this project is to provide the optimal amount of code - not too much, not too little - so that one could start building an app at your existing Django project as soon as possible.

## Requirements

There are no requirements for this project besides having Django installed into your virtual environment and having a configured Django project.

## Usage

You can start a new Django app with:

```
$ django-admin.py startapp --template=https://github.com/archatas/django-app-boilerplate/archive/master.zip app_name
```

Or start a new Django CMS app with:

```
$ django-admin.py startapp --template=https://github.com/archatas/django-app-boilerplate/archive/djangocms.zip app_name
```

Then search for "My App", "MyApp", "My Models", "My Model", "MyModel", "mymodel" globally in the created directory, and replace the found strings with your app and model definitions. For Django CMS app also replace "My Plugin", "My Plugin Model", "MyPluginModel", and "my\_plugin_model" with your own plugin definitions. Delete any unnecessary files.
