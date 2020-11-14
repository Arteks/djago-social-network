# import the standard Django Model 
# from built-in library 
from django.db import models 

# declare a new model with a name "GeeksModel" 
class Post(models.Model): 

# fields of the model 
    title = models.CharField(max_length = 50)
    body = models.TextField(max_length= 1000)
    autor = models.CharField(max_length= 50)
# renames the instances of the model 

# with their title name 

    def __str__(self): 
        return self.title 
