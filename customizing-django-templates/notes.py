#Django Built-In Template Tags and Filters: You should bookmark this page, because you'll refer to it often as you work on Django projects. It's the entire list of built-in template tags and filters that you have access to when you use Django. In other words, it's a gold mine.
#https://docs.djangoproject.com/en/1.8/ref/templates/builtins/

#Refresher

{% for x in y %} - For loop in Django templates

{% extends "template.html" %} #- Causes the current template to extend the quoted template so you can override blocks in the parent template.

{% block name %}{% endblock %} #- Marks the start and end of a named block which can be replaced with inheritance.

{% load static from staticfiles %} #- Loads the {% static %} tag from the staticfiles library.

{% static "/path/to/file.ext" %} #- Generates the URL to the specified file.

# https://docs.djangoproject.com/en/1.8/howto/static-files/

# Project level uses assets folder
# app level example
# courses => static => courses => css => layout.css

# https://docs.djangoproject.com/en/1.8/ref/contrib/humanize/

course.step_set.count # more efficient than the lower one

course.step_set.all|length # makes a extra db query

# |length = gets the length of a query set
# |join:", " = join the array by the thing in quotes. 1, 2 as a example
# |pluralize = adds a s or leaves it off depending on the length
# |wordcount = how many words are in the item
# |unordered_list = unoredered list

{% with con=step.content %}
    {{ con|linebreaks }}
{% endwith %}

# with the with command you can set a variable name 'con' to anything and it equals some value then you can reference it later

#Django Custom Date Filter
#wordcount - Counts the words (defined by whitespace) in the variable.
#truncatewords:X - Ends the variable after X words and appends an ellipsis if any content was cut off.
#urlize - Converts HTTP(S) and email addresses into HTML anchor tags with appropriate links.
#https://docs.djangoproject.com/en/1.8/ref/templates/builtins/#date

# Django Documentation: Custom Template Tags and Filters
#https://docs.djangoproject.com/en/1.8/howto/custom-template-tags/
#template is Django's module for all things template-related. We'll use this several times in the course.
#template.Library is a class that lets us register new tags and filters through an instance of itself.
#register.simple_tag(tag_name) or @register.simple_tag - Registers a function as a simple tag. Simple tags don't include new templates, don't have an end tag, and don't assign values to context variables.

#restart server to use template tags

# Django Documentation Simple Tag vs. Inclusion Tag

# register.inclusion_tag("tag_template.html")(tag_name) or @register.inclusion_tag("tag_template.html") - Registers an inclusion tag. Inclusion tags render a template into wherever they're used.

# https://docs.djangoproject.com/en/1.8/howto/custom-template-tags/#simple-tags

# Django documentation on custom template filters
# https://docs.djangoproject.com/en/1.8/howto/custom-template-tags/#writing-custom-template-filters

# pluralize - A filter that, by default, returns an "s" when attached to a number that's not 1, and nothing when the number is 1. You can provide different options if needed. More information is available in the official documentation.

# register.filter("filter_name", filter_function) or @register.filter("filter_name") - Registers a filter with the given name.

# Chaining Filters
#https://docs.djangoproject.com/en/1.8/ref/templates/builtins/#escape

# Documentation for Markdown2 Python library
# https://github.com/trentm/python-markdown2
# Markdown2 on PyPI
# https://pypi.python.org/pypi/markdown2
# Markdown Syntax Documentation
# http://daringfireball.net/projects/markdown/syntax
# Markdown Basics on GitHub
# https://help.github.com/articles/markdown-basics/
# Documentation on Filters and Auto-escaping
# https://docs.djangoproject.com/en/1.8/howto/custom-template-tags/#filters-and-auto-escaping

#mark_safe(variable) - Marks the variable as being safe to send directly to the browser without escaping or encoding the contents beforehand.