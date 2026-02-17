# magine you:

# Already created the Student model.

# Ran makemigrations.

# Ran migrate.

# Now you ADD this field:

# is_active = models.BooleanField(default=True)


# Question:

# What exact steps must you run in terminal now?






python manage.py makemigrations # This will create a new migration file that includes the changes you made to the Student model (adding the is_active field).
python manage.py migrate  # This will apply the new migration to the database, updating the Student table to include the new is_active field with a default value of True.


