#!/bin/bash
echo "Running database migrations..."
python caisse_retraite/manage.py migrate
echo "Collecting static files..."
python caisse_retraite/manage.py collectstatic --noinput
