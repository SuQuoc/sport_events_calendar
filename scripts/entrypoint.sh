#!/bin/bash

set -e  #exit if any command within script returns a non-zero exit status

python manage.py makemigrations --noinput
python manage.py migrate

if [ "$DEBUG" = "True" ]; then
    echo "Creating django admin user..."
    cat << EOF | python manage.py shell
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='$ADMIN_USERNAME').exists():
    User.objects.create_superuser('$ADMIN_USERNAME', '$ADMIN_EMAIL', '$ADMIN_PASSWORD')
EOF
fi

# Creating example data if no events in database
python manage.py load_example_data

exec "$@"