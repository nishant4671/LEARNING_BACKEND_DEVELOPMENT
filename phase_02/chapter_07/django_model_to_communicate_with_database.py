# Import the models module from Django
# This gives us access to Django's database functionality and base classes
from django.db import models

# Define a new class named Student that inherits from models.Model
# 'class' keyword creates a new class
# 'Student' is the name of our model (will become database table name)
# '(models.Model)' means Student inherits from Django's Model class
# This inheritance gives Student all the ORM functionality (save, delete, filter, etc.)
class Student(models.Model):
    
    # Define a 'name' field as a CharField (string/varchar in database)
    # CharField is for short-to-medium length strings
    # 'max_length=100' means the string can't exceed 100 characters
    # This creates a VARCHAR(100) column in the database
    name = models.CharField(max_length=100)
    
    # Define an 'age' field as an IntegerField (integer number in database)
    # IntegerField stores whole numbers (no decimals)
    # This creates an INTEGER column in the database
    age = models.IntegerField()
    
    # Define an 'email' field as an EmailField (special string field for emails)
    # EmailField is like CharField but with email validation built-in
    # 'unique=True' means every email in this column must be different
    # Database will enforce that no two students can have the same email
    # This creates a VARCHAR column with a UNIQUE constraint
    email = models.EmailField(unique=True)
    
    # Define a 'created_at' field as a DateTimeField (stores date and time)
    # DateTimeField stores both date and time (like Python's datetime.datetime)
    # 'auto_now_add=True' means: automatically set to current date/time when record is CREATED
    # This happens only once when the object is first saved
    # Great for tracking when records were added to the database
    # This creates a DATETIME column that gets auto-populated on INSERT
    created_at = models.DateTimeField(auto_now_add=True)









#     Django does NOT create a table immediately.

# It prepares a blueprint.

# Only after:

# python manage.py makemigrations
# python manage.py migrate


# Does Django generate SQL and tell PostgreSQL:

# "Create table student with these columns."