# GitHub Codespaces ♥️ Django

Welcome to your shiny new Codespace running Django! We've got everything fired up and running for you to explore Django.

You've got a blank canvas to work on from a git perspective as well. There's a single initial commit with what you're seeing right now - where you go from here is up to you!

Everything you do here is contained within this one codespace. There is no repository on GitHub yet. If and when you’re ready you can click "Publish Branch" and we’ll create your repository and push up your project. If you were just exploring then and have no further need for this code then you can simply delete your codespace and it's gone forever.

## installing dependancies

```python
pip install -r requirements.txt
```

## To collect static files:

```python
python manage.py collectstatic
```

## To run this application:

```python
python manage.py runserver
```


## Template usage: smart pluralization

I added a Django template filter `smart_plural` to handle smarter English plural forms (including `Ability -> Abilities`, `Diagnosis -> Diagnoses`, etc.). It's in the app `mythical_mane` under `templatetags`.

Example usage in a template:

```django
{% load smart_plural %}
{{ "Ability"|smart_plural }}           {# -> Abilities #}
{{ model_name|smart_plural:count }}      {# pluralizes only when count != 1 #}
```

The filter preserves capitalization and includes a short exceptions table; edit `mythical_mane/templatetags/smart_plural.py` to add more irregulars.
