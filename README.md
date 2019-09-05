Demo Django REST project with basic CRUD functionality

User details + query is saved in a single database table and is populated with a POST method, the same can be altered with PUT and deleted with DELETE methods, using "id" value.


Available endpoints:
1. Form to add new user: http://localhost:8000/new/
1. Gives a list all the available users:  http://localhost:8000/all_users
2. Gives only users which match with the name: http://localhost:8000/all_users?user_name=<name>
  eg: http://localhost:8000/all_users/?user_name=Rahel
