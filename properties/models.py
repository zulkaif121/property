from django.db import models


class Property(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    address = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    # Availability
    is_available = models.BooleanField(default=True)
    available_from = models.DateField(null=True, blank=True)
    available_to = models.DateField(null=True, blank=True)

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