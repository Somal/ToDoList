### ToDo List

ToDo list is written on Python 3/Django

#### Installing and Running (for Linux):
* For some commands you'll need in use sudo
- Install MySQL 5.5, create user 'root' with the same password (https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-14-04)
- Create DB  (mysql -u root -p root;
                               CREATE DATABASE todo;
                               GRANT ALL PRIVILEGES ON todo.* TO 'root'@'localhost';
                               FLUSH PRIVILEGES;
                               quit)
- Install Python3 (apt-get install python3)
- Install Python packege manager Pip (https://pip.pypa.io/en/stable/installing/)
- Install requirements (pip3 install -r requirements.txt)
- Clone this repository (git clone https://github.com/Somal/ToDoList.git)
- Go to repository (cd ToDoList)
- Run project (python3 manage.py runserver)
- Go to site (localhost:8000/accounts/signup)
