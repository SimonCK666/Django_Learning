# Django Learning

## 一、 Django 配置环境及创建项目

### 1. 创建虚拟环境

使用虚拟环境可以避免将Django安装到全局Python环境中，并且可以精确控制应用程序中使用的库。虚拟环境还可以轻松地[为环境创建requirements.txt文件。](https://code.visualstudio.com/docs/python/tutorial-django#_create-a-requirementstxt-file-for-the-environment)

> Command

```json
# macOS/Linux
sudo apt-get install python3-venv    # If needed
python3 -m venv env
# Windows
python -m venv env
```

> Run

```json
E:\Django_Learning\code>python -m venv env

E:\Django_Learning\code>dir
 Volume in drive E has no label.
 Volume Serial Number is A4D8-5A61

 Directory of E:\Django_Learning\code

2020/09/14  17:59    <DIR>          .
2020/09/14  17:59    <DIR>          ..
2020/09/14  17:42    <DIR>          .dist
2020/09/14  17:59    <DIR>          env
               0 File(s)              0 bytes
               4 Dir(s)  303,698,231,296 bytes free

E:\Django_Learning\code>code .
```

> Reference
>
> https://blog.csdn.net/weixin_40283570/article/details/88901011

### 2. 运行项目文件夹（通过 VScode 大开文件夹）

> Command

```json
code ./
```

### 3. 选择Python解释器

- 通过 `Ctrl + Shift + P` 输入 `Python: Select Interpreter` 命令
- 选择 `Python 3.8.2 64-bit ('env': venv)`  <=>  选择之后，vscode左下角将会变成 `Python 3.8.2 64-bit ('env': venv)` 

### 4. 配置终端

- 选择默认 Shell 然后添加 CMD

> 配置成功后：

```json
(env) E:\Django_Learning\code>pip list
Package    Version
---------- -------
pip        19.2.3
setuptools 41.2.0
WARNING: You are using pip version 19.2.3, however version 20.2.3 
is available.
You should consider upgrading via the 'python -m pip install --upgrade pip' command.
```

### 5. 创建并运行 Django 项目

#### 1. 安装Django

> Command

```json
pip install Django
```

```json
(env) E:\Django_Learning\code>pip install django
Collecting django
  Downloading https://files.pythonhosted.org/packages/01/a5/fb3dad18422fcd4241d18460a1fe17542bfdeadcf74e3861d1a2dfc9e459/Django-3.1.1-py3-none-any.whl (7.8MB)
     |████████████████████████████████| 7.8MB 218kB/s
Collecting pytz (from django)
  Downloading https://files.pythonhosted.org/packages/4f/a4/879454d49688e2fad93e59d7d4efda580b783c745fd2ec2a3adf87b0808d/pytz-2020.1-py2.py3-none-any.whl (510kB)
     |████████████████████████████████| 512kB 198kB/s
Collecting asgiref~=3.2.10 (from django)
  Downloading https://files.pythonhosted.org/packages/d5/eb/64725b25f991010307fd18a9e0c1f0e6dff2f03622fc4bcbcdb2244f60d6/asgiref-3.2.10-py3-none-any.whl
Collecting sqlparse>=0.2.2 (from django)
  Downloading https://files.pythonhosted.org/packages/85/ee/6e821932f413a5c4b76be9c5936e313e4fc626b33f16e027866e1d60f588/sqlparse-0.3.1-py2.py3-none-any.whl (40kB)
     |████████████████████████████████| 40kB 238kB/s
Installing collected packages: pytz, asgiref, sqlparse, django    
Successfully installed asgiref-3.2.10 django-3.1.1 pytz-2020.1 sqlparse-0.3.1
WARNING: You are using pip version 19.2.3, however version 20.2.3 
is available.
You should consider upgrading via the 'python -m pip install --upgrade pip' command.
```

> 查看版本

```json
pip freeze
```

```json
(env) E:\Django_Learning\code>pip freeze
asgiref==3.2.10
Django==3.1.1
pytz==2020.1
sqlparse==0.3.1
```

#### 2. 创建 Django 项目

```json
django-admin startproject web_project 
```

```json
(env) E:\Django_Learning\code>django-admin startproject web_project

(env) E:\Django_Learning\code>cd web_project
```

#### 3. 运行并验证

```json
python manage.py runserver
```

```json
(env) E:\Django_Learning\code\web_project>python manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).

You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
September 14, 2020 - 18:06:31
Django version 3.1.1, using settings 'web_project.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
[14/Sep/2020 18:06:54] "GET / HTTP/1.1" 200 16351
[14/Sep/2020 18:06:54] "GET /static/admin/css/fonts.css HTTP/1.1" 200 423
[14/Sep/2020 18:06:54] "GET /static/admin/fonts/Roboto-Regular-webfont.woff HTTP/1.1" 200 85876
[14/Sep/2020 18:06:54] "GET /static/admin/fonts/Roboto-Bold-webfont.woff HTTP/1.1" 200 86184
[14/Sep/2020 18:06:54] "GET /static/admin/fonts/Roboto-Light-webfont.woff HTTP/1.1" 200 
85692
Not Found: /favicon.ico
[14/Sep/2020 18:06:54] "GET /favicon.ico HTTP/1.1" 404 1977

```

#### 4. 创建一个应用

> Command

```json
python manage.py startapp polls
```

```js
// 目录结构如下
polls/
    __init__.py
    admin.py
    apps.py
    migrations/
        __init__.py
    models.py
    tests.py
    views.py
```

> 输入：http://127.0.0.1:8000/ 访问项目

> Reference:
>
> https://blog.csdn.net/weixin_40283570/article/details/97240666?biz_id=102&utm_term=vscode%20django%E5%BC%80%E5%8F%91%E7%8E%AF%E5%A2%83&utm_medium=distribute.pc_search_result.none-task-blog-2~all~sobaiduweb~default-1-97240666&spm=1018.2118.3001.4187###