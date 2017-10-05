#!/bin/bash

python3 manage.py migrate
python3 manage.py collectstatic


echo "Launching uwsgi service"
bash -c "uwsgi --module=wago.wsgi:application \
    --env DJANGO_SETTINGS_MODULE=wago.settings.production \
    --master \
    --pidfile=/tmp/project-master.pid \
    --http 0.0.0.0:8000"
    # --harakiri=20 \                 # respawn processes taking more than 20 seconds
    # --max-requests=5000 \           # respawn processes after serving 5000 requests
    # --vacuum                        # clear env after exit