
# ========================= To Setup Dev Environment ============================
# Development server
python manage.py runserver

# Switch to sudo on database
su - postgres

# start server and log
# debians package effs up everything otherwise you'd be able to use:
# pg_ctl start -l logfile
# pg_ctl is located in /usr/lib/postres/<version>/bin
$ postmaster -D /var/lib/postgresql/8.4/main >logfile 2>&1 &

# turn on Haml and Sass file watchers
$ hamlpy-watcher templates/
$ compass watch static/


# interactice shell
$ python manage.py shell


=================================================================== DEVVING ======================================================================
# when copying a project youll need to replace 3 directory references within the django projects settings.py

# ========================= New Project ============================
$ django-admin.py startproject mysite
$ cd mysite
$ git init
$ mkdir static
$ cd static
# so it seems that this doesnt work on anything but the css and the sass dirs
$ compass install compass . --syntax sass --sass-dir sass --css-dir css --javascripts-dir javascripts --images-dir images









# ========================= To Add New Apps ========================
# ___________________________________________________________________________


# in settings.py add it to INSTALLED_APPS

# update database with the tables the new app needs
python manage.py syncdb







# ========================= To CREATE New Apps ========================
# ___________________________________________________________________________

# create the app directory inside mysite/ project directory
$ python manage.py startapp books

# define models within mysite/books/models.py
    from django.db import models

    class Publisher(models.Model):
        name = models.CharField(max_length=30)
        address = models.CharField(max_length=50)
        city = models.CharField(max_length=60)
        state_province = models.CharField(max_length=30)
        country = models.CharField(max_length=50)
        website = models.URLField()

    class Author(models.Model):
        salutation = models.CharField(max_length=10)
        first_name = models.CharField(max_length=30)
        last_name = models.CharField(max_length=40)
        email = models.EmailField()
        headshot = models.ImageField(upload_to='/tmp')

    class Book(models.Model):
        title = models.CharField(max_length=100)
        authors = models.ManyToManyField(Author)
        publisher = models.ForeignKey(Publisher)
        publication_date = models.DateField()

# validate the structure added for the models
python manage.py validate

# check what DB modifications would happen
python manage.py sqlall books

# add tables to DB
python manage.py syncdb





# ========================= Database objects ========================
# ___________________________________________________________________________

# begins half way down page:
# http://www.djangobook.com/en/1.0/chapter05/



>>> from books.models import Publisher

# listing data
>>> Publisher.objects.all()

# create new instances
p = Publisher(name='Apress',address='2855 Telegraph Ave.', city='Berkeley', state_province='CA', country='U.S.A.', website='http://www.apress.com/')
p.save()

# filtering data
>>>> Publisher.objects.filter(name="Apress")
>>>> Publisher.objects.filter(name__contains="press")
#>>>> Poll.objects.filter(question__startswith='What')

# returning single object using .get
>>> Publisher.objects.get(name="Apress Publishing")
>>>> Publisher.objects.get(country="U.S.A.")

# ordering data
>>> Publisher.objects.order_by("name")
>>> Publisher.objects.order_by("address")

# multiple ordering
>>> Publisher.objects.order_by("state_provice", "address")

# reverse ordering
>>> Publisher.objects.order_by("-name")

# chaining
>>> Publisher.objects.filter(country="U.S.A.").order_by("-name")

# slicing - returns only a specific # of rows
>>> Publisher.objects.all()[0]

# deleting
>>> p = Publisher.objects.get(name="Addison-Wesley")
>>> p.delete()



### _____________ adding fields _______________

# modify the model in mysite/<app_name>/models.py
num_pages = models.IntegerField(blank=True, null=True)

# check whats happening w the creation
manage.py sqlall books

# run DB updates
python manage.py syncdb
    # ALTERNATIVE
    $ psql -c 'ALTER TABLE books_book ADD COLUMN num_pages integer;'


# verify update
$ python manage.py shell
>>>> from mysite.books.models import Book
>>>> Book.objects.all()[:5]
# should not throw error



### _____________ deleting fields _____________

# delete/comment out the line from models.py
#num_pages = models.IntegerField(blank=True, null=True)

# check whats happening w the deletion
manage.py sqlall books

# run DB updates
python manage.py syncdb

    # ALTERNATIVE
    $ psql -c 'ALTER TABLE books_book DROP COLUMN num_pages;'



### _____________ deleting models _____________
$psql -c 'DROP TABLE books_book;'





# ========================= Modifying Apps ========================
# ___________________________________________________________________________

# https://docs.djangoproject.com/en/1.3/intro/tutorial02/#make-the-poll-app-modifiable-in-the-admin

# create a file named admin.py in the /polls dir and fill with:
from polls.models import Poll
from django.contrib import admin

admin.site.register(Poll)



# ========================= Templates ========================
# ___________________________________________________________________________

https://docs.djangoproject.com/en/1.3/intro/tutorial03/


0) determine where file will go
1) create the URL
2) create function in whatever views.py file is appropirate for the dir

# this can be used to locate static files
$ python manage.py findstatic web-title-large.png


left off here:
https://docs.djangoproject.com/en/1.3/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS




# HamlPy 
hamlpy-watcher templates/






