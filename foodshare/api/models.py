from django.db import models
from django.utils.timezone import now
# Create your models here.
#from django.contrib.gis.db import models  # Using GIS for geolocation
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.contrib.auth.models import User



# 1. Custom User Model
# class User(AbstractUser):
#     #phone_number = models.CharField(max_length=15, blank=True, null=True)
#     #address = models.CharField(max_length=250,blank=True, null=True)
#     is_donor = models.BooleanField(default=True)
#     groups = models.ManyToManyField(
#         Group,
#         related_name="user_assigned_groups",  # Unique related_name for groups
#         blank=True,
#         help_text="The groups this user belongs to.",
#         verbose_name="groups",
#     )
#     user_permissions = models.ManyToManyField(
#         Permission,
#         related_name="user_assigned_permissions",  # Unique related_name for permissions
#         blank=True,
#         help_text="Specific permissions for this user.",
#         verbose_name="user permissions",
#     )
#     def __str__(self):
#         return self.username


# 2. Food Listings
class FoodListing(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)
    quantity = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    #is_free = models.BooleanField(default=True)
    expiry_date = models.DateTimeField()
    visibilty = models.BooleanField(default=True)
    location = models.CharField(max_length=100,blank=True, null=True)  
    image = models.ImageField(upload_to='static/',blank=True,null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='food_listings')
    created_at = models.DateTimeField(auto_now_add=True)
    def save(self, *args, **kwargs):
        # Automatically set visibility to False if expired during save
        if self.expiry_date < now():
            self.visible = False
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


# 3. Requests
# class Request(models.Model):
#     STATUS_CHOICES = [
#         ('Pending', 'Pending'),
#         ('Approved', 'Approved'),
#         ('Rejected', 'Rejected'),
#     ]

#     listing = models.ForeignKey(FoodListing, on_delete=models.CASCADE, related_name='requests')
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='requests')
#     status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Pending')
#     message = models.TextField(blank=True, null=True)
#     requested_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"Request by {self.user.username} for {self.listing.title}"


# 4. Reviews
class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    listing = models.ForeignKey(FoodListing, on_delete=models.CASCADE, related_name='reviews')
    rating = models.IntegerField()
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.user.username} - {self.rating}/5"


# # 5. Volunteers
# class Volunteer(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='volunteer_profile')
#     availability = models.BooleanField(default=True)
#     assigned_request = models.ForeignKey(Request, on_delete=models.SET_NULL, null=True, blank=True, related_name='volunteers')

#     def __str__(self):
#         return f"Volunteer: {self.user.username}"


# 6. Notifications
# class Notification(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
#     message = models.TextField()
#     is_read = models.BooleanField(default=False)
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"Notification for {self.user.username}"
