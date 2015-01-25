
# THIS MIGHT NOT BE NECESSARY
# from here: https://docs.djangoproject.com/en/dev/ref/contrib/gis/install/#ubuntudebian

$ sudo apt-get install binutils gdal-bin libproj-dev postgresql-8.4-postgis \
     postgresql-server-dev-8.4 python-psycopg2 python-setuptools

$ sudo easy_install Django



# downloaded django 
# from: https://www.djangoproject.com/download/

ran:
$ tar xzvf Django-1.3.1.tar.gz
$ cd Django-1.3.1/
$ sudo python setup.py install
$ cd ..

# this then verifies the installation
$ python
>>> import django
>>> django.VERSION

# it then outputs the version... if sucessfuly installed
# !!!!!!!!!!!!!!!!!!! GREAT SUCESS YESSSSSSSSSSSAH 


# installs psycopg which interfaces python with postgresql
# download http://initd.org/psycopg/tarballs/PSYCOPG-2-4/psycopg2-2.4.2.tar.gz

run:
$ cd ~/
$ tar xzvf psycopg2-latest.tar.gz
$ cd psycopg2-2.4.2/
$ python setup.py install


# Now for the "modwsgi" which is the intermediary between python and apache ( web server )

$ sudo apt-get install libapache2-mod-wsgi



# Now the setup of postgresql pulled from here:
# http://programmingzen.com/2007/12/26/installing-django-with-postgresql-on-ubuntu/

$ sudo su -
# this allows you to set a new password
$ passwd postgres

$ su - postgres
  # this was replaced with the above
  $ su postgres  # bc this runs from the roots dir ... instead of postgres' dir

# Check where the db is stored
psql -c 'show data_directory'

# ran this
psql template1

  # Got this complaint:  ( this was before when running 'su postgres' )
  could not change directory to "/root"

# This list all databases
# SHOW DATABASE list database
$ psql -l

# This will open the SQL interface
$ psql 

# This allows you to issue commands from the system prompt .. to be run in the psql
$ psql -c 'show data_directory' # shows where on the system the db is stored
$ psql -c 'CREATE DATABASE tutorial' # created the database for this tutorial

# this is how you can add users, passwords, permissions and new database
# http://www.cyberciti.biz/faq/howto-add-postgresql-user-account/

$ psql template1
  # template1=# 
$ CREATE USER carl WITH PASSWORD 'isabutthole';
  # CREATE
$ CREATE DATABASE nacho_fuente;
  # CREATE
$ GRANT ALL PRIVILEGES ON DATABASE nacho_fuente TO carl;
  # GRANT
$ \q
  # exits

#### DELETING
$ psql nacho_fuente
  # nacho_fuente=#
$ \d
  # lists tables
$ DROP TABLE users;
  # DROP TABLE
$ \q
  #exits

#### VIEWING
\d users # where users is a table






    # This creates a new SYSTEM user ... pulled from:
    # http://www.postgresql.org/docs/8.1/static/runtime.html#POSTGRES-USER
    # As postgres should be setup with a user account which owns that db data
    $ sudo useradd -d /home/postgres -m postgres
    $ sudo passwd postgres
    # its possile this user has already been created

    # Database cluster is created on a local dir
    # This is issued from the testuser account created above
    $ initdb -D /usr/local/pgsql/data


    # start server and log
    # debians package effs up everything otherwise you'd be able to use:
    # pg_ctl start -l logfile
    # pg_ctl is located in /usr/lib/postres/<version>/bin
    export PATH=$PATH:/usr/lib/postgresql/8.4/bin

    ##### SKIP THIS PART: currently in development / troubleshooting
            # sets current user to root
            $ sudo -i
            $ cd ..
            $ cd /etc/
            $ sudo gedit environment
            # now add this to the colon delimited PATH var
            /usr/lib/postgresql/8.4/bin
            # so it look something like:
            PATH="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/lib/postgresql/8.4/bin"

            

    # This starts the db server and logs
    $ postmaster -D /usr/local/pgsql/data >logfile 2>&1 &

    # To shutdown the server
    # http://www.postgresql.org/docs/8.1/static/postmaster-shutdown.html
    $ pg_ctl SIGTERM





# Ran this:
$psql -c 'ALTER USER postgres WITH ENCRYPTED PASSWORD 'mypassword''
# above is example of how to ALTER USER PASSWORD to mypassword

# fired up python in console
$ python
>>> import django
>>> print django.VERSION
# (1, 3, 1, 'final', 0)
>>> import psycopg2
>>> psycopg2.apilevel
# '2.0'

#  Exit python
exit()

# verify that django-admin.py is in your system paths
$ django-admin.py
# should show available subcommands


# start the dev server
python manage.py runserver



# run the python interpreter
python manage.py shell




# At this point Carls jumped from ln:102 where hes reset the password and just run:
$ python manage.py syncdb

# Now setting up superuser
# carlcrott
# carlcrott@gmail.com



# in python APPS are components of a PROJECT


# Django API

# start django console
python manage.py shell








# drop database / delete database from: http://blog.gahooa.com/2010/11/03/how-to-force-drop-a-postgresql-database-by-killing-off-connection-processes/
#As a super user, to list all of the open connections to a given database:
select * from pg_stat_activity where datname='YourDatabase';

#As a superuser, to drop all of the open connections to a given database:
select pg_terminate_backend(procpid) from pg_stat_activity where datname='YourDatabase';









# Other commands I've run
sudo apt-get install apache2
sudo apt-get install apache2-dev

