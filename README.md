📝 # Models in Django

## This is a model that I made using Django. Models are classes that define the structure of data for the database. For our simple blog, we'll need to store entries with a title and content, both as text.

*  First, define the model in blog/models.py:

    
        from django.db import models
    
        class Post(models.Model):
            title = models.CharField(max_length=200)
            content = models.TextField()


*  Create Migrations
After defining the model, create a migration to apply these changes to the database. Run the following command:
        
        
        $ pipenv run python manage.py makemigrations
        You’ll see an output like this:
        
        Migrations for 'blog':
          blog/migrations/0001_initial.py
            - Create model Post


* Apply Migrations
  
        Next, apply the migrations to update the database with the new model:
        
        $ pipenv run python manage.py migrate
        The system will apply all migrations, and you’ll see an output like this:


*  Apply all migrations: admin, auth, blog, contenttypes, sessions
            Running migrations:
              Applying blog.0001_initial... OK
              ...
            Note: The first time you migrate, tables for generic apps (admin, auth, sessions, etc.) will also be created in the database.


*  Modify the Model
To add fields that automatically record creation and modification dates, update blog/models.py:


from django.db import models
    
        class Post(models.Model):
            title = models.CharField(max_length=200)
            content = models.TextField()
            created = models.DateTimeField(auto_now_add=True)  # new
            modified = models.DateTimeField(auto_now=True)     # new


* Create and Apply Migrations for Additional Changes
        To apply the changes only to the blog app, run:
        
        $ pipenv run python manage.py makemigrations blog
        $ pipenv run python manage.py migrate blog
        


* Verify the Database
  
        You can use a tool like DB Browser for SQLite to view and manipulate the tables of your models. Warning: Directly modifying table fields may cause issues with the application.



# How does it look: 

![Image_demo](https://github.com/Ornella-Gigante/python-django-blog/raw/main/django-project/blog_demo/blog/static/blog/blog_done.png)


## Demo video:



[Demo](https://github.com/Ornella-Gigante/python-django-blog/blob/main/django-project/demo.webm)

