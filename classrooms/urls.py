
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from classes.views import (
	classroom_list, classroom_detail, classroom_create, 
	classroom_update, classroom_delete, 
	)

from app.views import (
	APIList, APIDetails, APICreate, APIUpdate, APIDelete,
	)

from rest_framework_simplejwt.views import TokenObtainPairView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('classrooms/', classroom_list, name='classroom-list'),
    path('classrooms/<int:classroom_id>/', classroom_detail, name='classroom-detail'),

    path('classrooms/create', classroom_create, name='classroom-create'),
    path('classrooms/<int:classroom_id>/update/', classroom_update, name='classroom-update'),
    path('classrooms/<int:classroom_id>/delete/', classroom_delete, name='classroom-delete'),

    path('list/', APIList.as_view(), name='list'),
    path('detail/<int:classroom_id>/', APIDetails.as_view(), name='detail'),
    path('create/', APICreate.as_view(), name='create'),
    path('update/<int:classroom_id>/', APIUpdate.as_view(), name='update'),
    path('delete/<int:classroom_id>/', APIDelete.as_view(), name='delete'),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
]

if settings.DEBUG:
	urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
