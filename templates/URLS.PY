fromdjango.conf.urlsimporturl
fromdjango.contribimport admin
fromRemote_Userimport views asremoteuser
fromidentifying_health_insurance_claim_fraudsimport settings
fromService_Providerimport views asserviceprovider
fromdjango.conf.urls.staticimport static

urlpatterns= [
    url('admin/', admin.site.urls),
    url(r'^$', remoteuser.index, name="index"),
    url(r'^login/$', remoteuser.login, name="login"),
    url(r'^Register1/$', remoteuser.Register1, name="Register1"),
    url(r'^Predict_Health_Insurance_Claim_Fraud/$', remoteuser.Predict_Health_Insurance_Claim_Fraud, name="Predict_Health_Insurance_Claim_Fraud"),
    url(r'^ViewYourProfile/$', remoteuser.ViewYourProfile, name="ViewYourProfile"),
    url(r'^serviceproviderlogin/$',serviceprovider.serviceproviderlogin, name="serviceproviderlogin"),
    url(r'View_Remote_Users/$',serviceprovider.View_Remote_Users,name="View_Remote_Users"),
    url(r'^charts/(?P<chart_type>\w+)', serviceprovider.charts,name="charts"),
    url(r'^charts1/(?P<chart_type>\w+)', serviceprovider.charts1, name="charts1"),
    url(r'^likeschart/(?P<like_chart>\w+)', serviceprovider.likeschart, name="likeschart"),
    url(r'^View_Predicted_Health_Insurance_Claim_Fraud_Type_Ratio/$', serviceprovider.View_Predicted_Health_Insurance_Claim_Fraud_Type_Ratio, name="View_Predicted_Health_Insurance_Claim_Fraud_Type_Ratio"),
    url(r'^train_model/$', serviceprovider.train_model, name="train_model"),
    url(r'^View_Predicted_Health_Insurance_Claim_Fraud_Type/$', serviceprovider.View_Predicted_Health_Insurance_Claim_Fraud_Type, name="View_Predicted_Health_Insurance_Claim_Fraud_Type"),
    url(r'^Download_Predicted_DataSets/$', serviceprovider.Download_Predicted_DataSets, name="Download_Predicted_DataSets"),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
