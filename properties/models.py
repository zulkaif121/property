from django.db import models

#need to allow room booking also for an apartment or a house at a portion of the total price

class Property(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    address = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=10, default='UED', help_text="Currency code for the property price")
    room_booking = models.BooleanField(default=False, help_text="Is this property available for room booking?")
    total_rooms = models.PositiveIntegerField(default=1, help_text="Total number of rooms in the property")
    room_price = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        default=0.00,
        help_text="Price per room if the property is available for room booking"
    )
    # Availability
    is_available = models.BooleanField(default=True)
    available_from = models.DateField(null=True, blank=True)
    available_to = models.DateField(null=True, blank=True)
    #guests would be number of guests that can stay in the property
    guests = models.PositiveIntegerField(default=1, help_text="Number of adult guests that ca=n stay in the property")
    pet_friendly = models.BooleanField(default=False, help_text="Is the property pet friendly?")
    children = models.PositiveIntegerField(default=0, help_text="Number of children that can stay in the property")
    #location would be latitude and longitude of the property
    location = models.JSONField(
        default=dict,
        blank=True,
        help_text="A JSON field to store latitude and longitude of the property"
    )

    # over view would be a json or something similar which would store tags like bedrooms, bathrooms,  square ft etc.
    overview = models.JSONField(
        default=dict,
        blank=True,
        help_text="A JSON field to store various attributes like bedrooms, bathrooms, etc."
    )
    #features would be a json or something similar which would store tags like cctv, parking, gym etc
    features = models.JSONField(
        default=dict,
        blank=True,
        help_text="A JSON field to store various features like CCTV, parking, gym, etc."
    )


    # Metadata
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class PropertyImage(models.Model):
    property = models.ForeignKey(
        'Property',
        on_delete=models.CASCADE,
        related_name='images'
    )
    image = models.ImageField(upload_to='property_images/')
    caption = models.CharField(max_length=255, blank=True)

    uploaded_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Image for {self.property.title}"
    
# A MODEL FOR AGENTS FOR PROPERTIES
class PropertyAgent(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    properties = models.ManyToManyField(
        Property,
        related_name='agents',
        blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class PropertyReview(models.Model):
    property = models.ForeignKey(
        'Property',
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    user_name = models.CharField(max_length=255)
    rating = models.PositiveIntegerField(default=1)
    comment = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Review for {self.property.title} by {self.user_name}"  

class PaymentMethod(models.Models):
    #Cash , Card , bank transfer etc
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Booking(models.Model):
    property = models.ForeignKey(
        'Property',
        on_delete=models.CASCADE,
        related_name='bookings'
    )
    user_name = models.CharField(max_length=255)
    user_email = models.EmailField()
    user_phone = models.CharField(max_length=20, blank=True)
    guests = models.PositiveIntegerField(default=1)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
