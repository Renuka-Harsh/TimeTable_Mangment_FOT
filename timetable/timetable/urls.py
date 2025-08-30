from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponseRedirect  # <-- Add this import

def redirect_to_admin(request):
    return HttpResponseRedirect('/admin/')

urlpatterns = [
    path('', redirect_to_admin),  # Redirect root URL to admin
    path('admin/', admin.site.urls),
    path('timetables/', include('timetable_app.urls'))

]
