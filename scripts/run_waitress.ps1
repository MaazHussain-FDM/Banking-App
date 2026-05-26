param(
    [string]$ListenHost = "0.0.0.0",
    [int]$Port = 8000
)

$env:DJANGO_SETTINGS_MODULE = "banking_project.settings"

python manage.py migrate --noinput
python -m waitress --listen="$ListenHost`:$Port" banking_project.wsgi:application

