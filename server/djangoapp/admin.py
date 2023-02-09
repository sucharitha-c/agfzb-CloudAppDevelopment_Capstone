from django.contrib import admin
from .models import make,model,dealer,review


# Register your models here.

# CarModelInline class

# CarModelAdmin class

# CarMakeAdmin class with CarModelInline

# Register models here
admin.site.register(make)
admin.site.register(model)
admin.site.register(dealer)
admin.site.register(review)

