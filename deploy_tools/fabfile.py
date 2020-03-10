import random
from  fabric.contrib.files import append, exists
from fabric.api import cd, env, local, run

REPO_URL = 'https://github.com/eanhtng/superlists.git'

def deploy():
    site_folder = f'/home/{env.user}/sites/{env.host}'
    run(f'mkdir -p {site_folder}')
    with cd(site_folder):
        _get_latest_source()
        _update_virtualenv()
        _create_or_update_dotenv()
        _update_static_files()
        _update_database()
        _update_nginx_config_template()
        _update_gunicorn_service_template()
        _start_both_services()

def _get_latest_source():
    if exists('.git'):
        run('git fetch')
    else:
        run(f'git clone {REPO_URL} .')
    current_commit = local("git log -n 1 --format=%H", capture = True)
    run(f'git reset --hard {current_commit}')

def _update_virtualenv():
    if not exists('virtualenv/bin/pip'):
        run(f'python3.6 -m venv virtualenv')
    run('./virtualenv/bin/pip install -r requirements.txt')

def _create_or_update_dotenv():
    append('.env', 'DJANGO_DEBUG_FALSE=y')
    append('.env', f'SITENAME={env.host}')
    current_contents = run('cat .env')
    if 'DJANGO_SECRET_KEY' not in current_contents:
        new_secret = ''.join(random.SystemRandom().choices('abcdefghijklmnopqrstuvwxyz0123456789', k = 50))
        append('.env', f'DJANGO_SECRET_KEY={new_secret}')

def _update_static_files():
    run('./virtualenv/bin/python manage.py collectstatic --noinput')

def _update_database():
    run('./virtualenv/bin/python manage.py migrate --noinput')

def _update_nginx_config_template():
    run('cat ./deploy_tools/nginx.template.conf | sed "s/DOMAIN/superlists.edu.solutions/g" | sed "s/USER/anhnt/g" | sudo tee /etc/nginx/sites-available/superlists.edu.solutions');

def _update_gunicorn_service_template():
    run('cat ./deploy_tools/gunicorn-systemd.template.service | sed "s/DOMAIN/superlists.edu.solutions/g" | sed "s/USER/anhnt/g" | sudo tee /etc/systemd/system/gunicorn-superlists.edu.solutions.service')

def _start_both_services():
    run('sudo systemctl daemon-reload');
    run('sudo systemctl reload nginx');
    run('sudo systemctl enable gunicorn-superlists.edu.solutions');
    run('sudo systemctl start gunicorn-superlists.edu.solutions');
