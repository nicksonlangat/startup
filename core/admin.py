from django.contrib import admin
from .models import Category, Patner, Opening, Talent, Testimony

# Register your models here.
admin.site.register(Category)
admin.site.register(Opening)
admin.site.register(Patner)
admin.site.register(Talent)
admin.site.register(Testimony)
