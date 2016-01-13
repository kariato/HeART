from django.contrib import admin
from .models import DNAKit,DNASegment,DNAMatch,Family,DNAKitUpload,DNAICW
# Register your models here.

admin.site.register(DNAKit)
admin.site.register(DNASegment)
admin.site.register(DNAMatch)
admin.site.register(Family)
admin.site.register(DNAKitUpload)
admin.site.register(DNAICW)