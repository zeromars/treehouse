django-admin startproject learning_site

python manage.py runserver

#What are migrations?

#Migrations are a way of moving a database from one design, a specific set of tables and columns, to a new one. Migrations are reversible, too. The fact that they can be done backwards and forwards is what gives them their name.
python manage.py migrate

# Django projects contain multiple Django apps. Each app generally encompasses a specific area of functionality.

#python manage.py startapp creates the skeleton of an app including the views, models, and tests files.

#INSTALLED_APPS is a list of all apps that Django should consider installed and active for the current project. These apps will be used to find templates, tests, models, and migrations.

#TIME_ZONE is the setting for what time zone your server is running in. The docs explain a little more and there's a list of time zones you can use.

# app = self contained bit of functionality 

python manage.py startapp courses

#id is automatically added in django
python manage.py makemigrations
# python manage.py makemigrations courses (to be more specific)

python manage.py migrate

python manage.py shell

from courses.models import Course
Course.objects.all()

c = Course()
c.title = "Python Basics"
c.description = "Learn the basics of python"
c.save()

Course(title="Python Collections", description="Learn abouyt lists , dict and tuples").save()

Course.objects.create(title="Object Oriented Python", description="Learn about python's classes")

#python manage.py shell opens a Python shell with Django's configuration already loaded.
#Model.save() will save an in-memory instance of a model to the database.
#Model.create() will save an in-memory instance of a model to the database and return the newly-created object.
#Model.filter(attribute=value) will get a QuerySet of all instances of the Model that match the attribute values. You can change these values with other comparisons, too, like gte or in. Find out more here
#include() allows you to include a list of URLs from another module. It will accept the variable name or a string with a dotted path to the default urlpatterns variable.
#If you don't have include() in your urls.py (more recent versions of Django have removed it), add it to the import line that imports url. That line will now look like from django.conf.urls import url, include.
#This is the Comprehensions Workshop that's mentioned in the video. Comprehensions are a great way of doing quick work with iterables.

# python manage.py createsuperuser will create a new superuser, or a user that's allowed to log into the admin area with all permissions.

# admin.site.register(Model) will register a model with the default admin site, which allows you to edit instances of that model in the admin.

# Templates

# APP => templates => app_name
#courses\templates\courses

# IntegerField is a field that holds integers, or whole numbers.
# An inline is a smaller form inside of a larger form. The smaller form represents a related record in the database.
# StackedInline is an inline where each field takes up the full width of the form. Fields are stacked.
# TabularInline is an inline where each field is part of a single row for the form.
# More docs on inlines. https://docs.djangoproject.com/en/1.8/ref/contrib/admin/#inlinemodeladmin-objects

# to get a form for adding steps into courses we add a inline in admin.py

# {% for step in course.step_set.all %} Notice that we don't use the () on all(). You don't call functions in Django's template tags, the template engine will handle that for you.

# Also, step_set is automatically generated from the foreign key. Handy!

# Model.get(attribute=value) lets you get a single Model instance by a given attribute's value.

# Here is more info on prefetch_related and select_related. Don't bother too much with these until you're comfortable with Django's ORM.
# https://docs.djangoproject.com/en/1.8/ref/models/querysets/#prefetch-related
# https://docs.djangoproject.com/en/1.8/ref/models/querysets/#select-related

class Meta:
    ordering = ['field1', 'field2']
#This will cause the model to be ordered by field1, then field2 if there are any conflicts on field1 (two instances having the same field1 value). Finally, they'll be sorted by id if a conflict still exists.

#get_object_or_404(Model, [selectors]) - Gets an object of Model by using whatever selection arguments have been given. For example: get_object_or_404(User, username='kennethlove') would try to get a User with an username set to "kennethlove". If that User didn't exist, a 404 error would be raised.

#What's the long way? Consider this view:

from django.http import Http404

from .models import Course

def course_detail(request, pk):
    try:
        course = Course.objects.get(pk=pk)
    except Course.DoesNotExist:
        raise Http404()
    else:
        return render(request, 'courses/course_detail.html', {'course': course})
#It's definitely more work!

#If you want, you can customize your error views.
#https://docs.djangoproject.com/en/1.8/topics/http/views/#customizing-error-views

#linebreaks is a filter that turns two returns in a row into HTML paragraph tags.

#You apply filters to a variable with the pipe (|) character.

# Content Field

#blank=True - A field can be blank (not filled in) in the admin and any other forms based on the model.

#default='something' - If no value is supplied for the field, the default 'something' will be put into the record.

#We need to be able to associate a Writer with an Article. Add a ForeignKey field to the Article model to link it to the Writer model. Give the attribute the name writer. IMPORTANT Since our Article model comes first, you'll need to quote the Writer model in the foreign key. So use "Writer" instead of Writer.

from django.db import models


class Article(models.Model):
    headline = models.CharField(max_length=255)
    publish_date = models.DateTimeField()
    content = models.TextField()
    writer = models.ForeignKey("Writer")
    
    def __str__(self):
        return self.headline


class Writer(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    bio = models.TextField()

# {% url 'path.to.view' %} to link to a view who's URL doesn't have a name.

# Note: This has been removed in Django 1.10 and beyond. If you want to use this feature, be sure to install Django 1.9 or below. You can do that with pip install django<1.10. Better yet, name all of your URLs as shown below.

# url(r'pattern', views.view, name='list') to name an URL

# {% url 'list' %} to link to a named URL

# include('courses.urls', namespace='course') to namespace a group of URLs

# {% url 'courses:list' %} to link to a named and namespaced URL

# Model Tests
#Build a Social Network with Flask and Python Testing are both good resources for learning more about testing in Python.
#assertLess(a, b) checks that a is less than b.
#django.utils.timezone is Django's timezone utility that takes the TIME_ZONE setting into account.
#python manage.py test runs all of the tests for your apps.

# django.core.urlresolvers.reverse() takes a URL name and reverses it to the correct URL string. More information https://docs.djangoproject.com/en/1.8/ref/urlresolvers/#reverse
# self.client acts like a web browser and lets you make requests to URLs, both inside and outside of your Django project.
# assertEqual(a, b) checks that a and b are equal to each other.
# assertIn(a, b) checks that a is contained in b.

#template tests
#assertTemplateUsed(response, 'template/name.html') checks that a given template is used somewhere in the response of the view.
#assertContains(response, 'string') checks that a given string is somewhere in the text of a response.