from django.conf.urls import url
from django.contrib import admin
from draftpick.views import IndexView, DraftpickDetailView
from news.views import NewsFeedView, NewsDetailView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', IndexView.as_view(), name='index_view'),
    url(r'^pick/(?P<pk>\d+)/$', DraftpickDetailView.as_view(), name='draftpick_detail_view'),
    url(r'^news/$', NewsFeedView.as_view(), name='news_feed_view'),
    url(r'^news/(?P<pk>\d+)/$', NewsDetailView.as_view(), name='news_detail_view'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
