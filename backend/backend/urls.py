from django.contrib import admin
from django.urls import path , include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , include('app.urls')),
] + static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT) # 장고에서 제공해주는 static() 함수 공용으로 쓰이는 인수를 global선언 
# static 의 상대주소를 사용할 수 있게 해줌

