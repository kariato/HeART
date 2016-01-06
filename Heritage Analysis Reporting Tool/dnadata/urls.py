from django.conf.urls import patterns, include, url



urlpatterns = patterns('dnadata.views',
    url(r'^dnakitupload$', 'upload', name='dnadata_upload'),
    url(r'^family/(?P<pk>\d+)/$', 'family', name='dnadata_family'),
    url(r'^file$', 'uploadFile', name='dnadata_uploadFile' ),
    #url(r'^uploadresults$', 'uploadresults', name='dnadata_uploadresults'),
)