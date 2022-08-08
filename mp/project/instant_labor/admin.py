
from django.contrib import admin
from .models import Credentials
from .models import Worker
from .models import Owner
from .models import Feedback


admin.site.register(Credentials)
admin.site.register(Worker)
admin.site.register(Owner)
admin.site.register(Feedback)