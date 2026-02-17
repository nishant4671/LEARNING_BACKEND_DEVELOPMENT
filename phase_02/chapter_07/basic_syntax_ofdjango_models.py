


# models.py - This file lives in your Django app folder

# Step 1: Import Django's models module
# This gives you access to all field types and model functionality
from django.db import models

# Step 2: Define your model class
# Each class = one database table
# Class name should be singular (Student, not Students)
class ModelName(models.Model):
    """
    This docstring explains what this model represents
    Each attribute = one database column
    """
    
    # Step 3: Define your fields (columns)
    
    # Basic field syntax:
    # field_name = models.FieldType(options)
    
    field_name = models.CharField(max_length=100)
    
    def __str__(self):
        """String representation - what shows in admin and shell"""
        return self.field_name
    
    class Meta:
        """Optional: Metadata about the model"""
        db_table = 'custom_table_name'  # Override table name
        ordering = ['field_name']        # Default ordering
        verbose_name = 'Friendly Name'   # Singular display name
        verbose_name_plural = 'Friendly Names'  # Plural display name