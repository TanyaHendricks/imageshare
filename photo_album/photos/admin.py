from django.contrib import admin

# Register your models here.
from .models import Image
from .models import Tag
from .models import Capturer
from .models import Metadata


admin.site.register(Image)
admin.site.register(Tag)
admin.site.register(Capturer)  
admin.site.register(Metadata) 
 





