Клонируем репозиторий, создаем виртуальное окружение, активируем, устанавливаем зависимости из requirements.txt.

Чтобы в vscode black форматировал строку под 100 симоволов, как настроено во flake8, нужно в корневой папке проекта создать папку .vscode и в ней файл settings.json:

```
{
    "python.formatting.provider": "black",
    "python.formatting.blackArgs": ["--line-length=100"],
    "editor.formatOnSave": true,
}

В PyCharm это можно сделать через .editorconfig.

```
flake8 /home/dima/projects/Django-BakeCake/
```