web: gunicorn pentam.wsgi --chdir backend --limit-request-line 8188 --log-file -
worker: REMAP_SIGTERM=SIGQUIT celery --workdir backend --app=pentam worker --loglevel=info
beat: REMAP_SIGTERM=SIGQUIT celery --workdir backend --app=pentam beat -S redbeat.RedBeatScheduler --loglevel=info
