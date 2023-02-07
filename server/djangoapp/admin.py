from django.contrib import admin
from .models import make,model
# from .models import related models


# Register your models here.

# CarModelInline class

# CarModelAdmin class

# CarMakeAdmin class with CarModelInline

# Register models here
admin.site.register(make)
admin.site.register(model)
