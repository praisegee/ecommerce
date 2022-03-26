from django.db import models

from django.contrib.auth.models import AbstractUser, BaseUserManager


"""
After customizing the user model. 

AUTH_USER_MODEL avriable need to be added to the settings file
with the value pointing to our Custom User model...

And check the migration file to see what really created..

And the admin file too, 
"""


class UserManager(BaseUserManager):
	"""
	The BaseUserModel defines how users will be 
	created and save into the database!
	"""
	def create_user(self, email, password=None):
		"""This method validate the user email and password"""
		if not email:
			raise ValueError("User must have an email!")
		if not password:
			raise ValueError("You need to provide a password!")

		user = self.model(
				email=self.normalize_email(email)
			)
		user.set_password(password)
		user.save(using=self._db)

		return user


	def create_superuser(self, email, password):
		"""
		This method defines how superuser will be created,
		It just call the create_user method and make sure
		that the instance is staff, superuser and always verified.

		is_verified is not an attribute of the default model, 
		that is why i added it to the custom user model below..

		The reason i added it is that i'm thinking if we can write a code that
		generate something like OTP token, to verifuy the user email..

		I'll add the links to that article maybe on a txt file sha.. 

		HOPE YOU UNDERSTAND IT NOW SIR?
		"""

		user = self.create_user(
				email=self.normalize_email(email),
				password=password
			)
		user.is_superuser 	= True
		user.is_staff 		= True
		user.is_verified 	= True
		user.save(using=self._db)

		return user



class User(AbstractUser):
	"""
	The attributes bellow add and overwritten the default,

	username and email overwrite the default and
	is_verified is added as new attribute
	"""

	username 	= None # i made the username to be None, since we don't need username
	email 		= models.EmailField(unique=True)
	is_verified = models.BooleanField(default=False)

	def __str__(self):
		return self.email

	objects 		= UserManager()

	USERNAME_FIELD 	= 'email'
	REQUIRED_FIELDS = []






