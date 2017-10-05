#!/bin/bash

NAME="topspin"                                  # Name of the application
DJANGODIR=/home/topspin-v2/saleor           # Django project directory
SOCKFILE=/home/topspin-v2/saleor/run/gunicorn.sock  # we will communicte using this unix socket
USER=root                                        # the user to run as
GROUP=root                                     # the group to run as
NUM_WORKERS=3                                     # how many worker processes should Gunicorn spawn
DJANGO_SETTINGS_MODULE=saleor.conf.settings             # which settings file should Django use
DJANGO_WSGI_MODULE=saleo.wsgi                     # WSGI module name
BIND="0.0.0.0:80"

echo "Starting $NAME as `whoami`"

# Activate the virtual environment
cd $DJANGODIR
source /home/topspin-v2/env/bin/activate
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH

# Create the run directory if it doesn't exist
RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR

# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
exec /home/ubuntu/ibid/ibid-backend/env/bin/gunicorn ${DJANGO_WSGI_MODULE}:application \
  --name $NAME \
  --workers $NUM_WORKERS \
  --user=$USER --group=$GROUP \
  --bind $BIND \
  --log-level=debug \
  --log-file=-
