Клонируем репозиторий, создаем виртуальное окружение, активируем, устанавливаем зависимости из requirements.txt.

Чтобы в vscode black форматировал строку под 100 симоволов, как настроено во flake8, нужно в корневой папке проекта создать папку .vscode и в ней файл settings.json:

```
{
    "python.formatting.provider": "black",
    "python.formatting.blackArgs": ["--line-length=100"],
    "editor.formatOnSave": true,
}
```
В PyCharm это можно сделать через .editorconfig.

Чтобы отдельно запустить flake8:
```
flake8 /<path-to-project>/Django-BakeCake/
```

Но лучше перед коммитом запускаем команду:
```
pre-commit run --all-files
```

Для запуска Джанги создаем в корне файл .env:
```
SECRET_KEY=changeme
DEBUG=False
# DATABASE_URL=postgresql://<username>:<password>@<host>:<port>/<database_name>
# ALLOWED_HOSTS=127.0.0.1, localhost
```

Для новых фич от ветки develop создаем новую ветку и в конце делаем pull-request из созданной ветки в develop. По мере надобности обновляем локальную develop командой git pull.
