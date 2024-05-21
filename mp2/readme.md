## Math Quiz App

### Flask Project Structure
In `application.py` in `migrations` folder, there are changes made different compared to mp1:
- import `db` which is the object used to work with our SQL database.
- import classes `User`, `Question`, `Challenge`, `TimeRecord` from the file `app/models.py`. These classes represent your database tables.
- the decorator `@application.shell_context_processor` and the function make_shell_context allows you to run a python shell by typing `flask shell` where all those names in the dictionary will be added to the shell as an object instance.

In `__init__.py` in `app` folder,
- we load the database configuration from `Config` which is defined in `config.py` in `migrations`.
- `db` is defined as an object instance of `SQLAlchemy`.
- `migrate` is defined to migrate the database whenever we make changes to the tables or the models.
- create our login page. `login.login_view` directs the URL and route it to `login()` defined in the `routes.py`.
- `bootstrap` is defined to allow us to use some predefined CSS from Bootstrap-Flask.

This file also imports the file `routes.py` which defines the URL routing. 
<br /> For the first route `index`:
- decorator `@login_required` ensures that when a user tries to enter `/index` page, they must login to the page first. If they have not, Flask will redirect them to the login page. The `login()` route is also defined in the `routes.py`.

For the second route `users`:
- user goes to `/users/ either by entering the URL or by clicking "Users" in the navigation bar.
- `users = User.query.all()` retrieves all users from the database in `User` table (`User` is defined in `models.py`).
- `mergesort(users, lambda item: item.username)` calls the sorting function to sort the list of users using its `username` attribute. Note that the `User` table has other attributes besides `username`. Refer to `models.py` for all the attributes of `User` table. It should sort the `users` in place. You need to modify your `mergesort()` function as described in Q1 of `mp2_exercises.ipynb` to complete this.
- `usernames = [u.username for u in users]` creates a list of usernames from the list of sorted users.
- `render_template('users.html', title='Users', users=usernames)` passes the variable `usernames` to be used in the `users.html` using some jinja templating under the name `users`.


### Exercise 1 
In `users.html`:
- `{% extends "base.html" %}` inherits the `base.html` for some of the common elements such as the navigation bar, importing certain scripts, and CSS files. The javascript which we will translate from the file `serverlibrary.py` is imported in the last few lines of `base.html`.
- `{% block app_content %}` indicates the block `app_content`. Each html file templates we have will modify this block `app_content`.
<br />This file basically iterates over all users and create rows of users in a table.

#### Task 1.1
- Use jinja templating to display the items inside `users`.

#### Task 1.2
- Create `mergesort()` function to merge the users challenge records and sort them according to time taken

#### Task 1.3
In `application.py`, run the following commands:
```
flask db init
flask db migrate
flask db upgrade
```

#### Task 1.4
- Create several users. More than three users are recommended.
- Login using one of the user account.
- Navigate to the "Users" page using the navigation bar on the top.

In your web app, you should see all the users you have created sorted according to their usernames.


### Exercise 2

#### Task 2.1
- implement `Stack` class inside `serverlibrary.py`.

#### Task 2.2
- implement `EvaluateExpression` class inside `serverlibrary.py`.

#### Task 2.3
Test your implementation:
- Navigate to "Questions" page.
- Create several integer arithmetic expressions and assign it to different users. Note that you can assign more than one users for the same question.

If your EvaluateExpression is correct, you will see the correct answer displayed in the table.

#### Task 2.4
Test also the other pages and see if they are working fine:
- Logout from your current user and login to one of the users you have assigned a challenge.
- After login, navigate to "Challenge" page and click "Show/Hide" to reveal the question. A timer starts when you click the button to reveal the question.
- Put the answer in the provided input box, and click "Submit". If your answer is correct, the elapsed time will be displayed on the last column. Otherwise, nothing will be displayed in the last column.
- Answer several challenges with different users, then navigate to "Hall of Fame" page. If your `mergesort()` implementation is correct, you will see a table listing all the challenges with the fastest top three users for each of them.




