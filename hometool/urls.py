from django.conf.urls import patterns, url
from django.views.generic.base import TemplateView

# See: https://docs.djangoproject.com/en/dev/topics/http/urls/
urlpatterns = patterns('',
    # Home Page
    url(r'^$', TemplateView.as_view(template_name="generic/home.html"), name='index'),
    # url(r'^survey/$', TemplateView.as_view(template_name="generic/survey.html"), name='survey'),
    


    # Static Page Index
    url(r'^ui_statics/$', TemplateView.as_view(template_name="ui_statics/HomeTool_Index.html"), name='ui_statics'),
    url(r'^ui_statics/buttons_demo/$', TemplateView.as_view(template_name="ui_statics/buttons_demo.html"), name='statics_buttons'),
    url(r'^ui_statics/signup/$', TemplateView.as_view(template_name="ui_statics/account/sign_up.html"), name='sign_up'),
    url(r'^ui_statics/signup_invited/$', TemplateView.as_view(template_name="ui_statics/account/sign_up_invited.html"), name='sign_up_invited'),
    url(r'^ui_statics/login/$', TemplateView.as_view(template_name="ui_statics/account/login_default.html"), name='login_default'),
    url(r'^ui_statics/login_errors/$', TemplateView.as_view(template_name="ui_statics/account/login_default_errors.html"), name='login_default_errors'),
    url(r'^ui_statics/reset_password/$', TemplateView.as_view(template_name="ui_statics/account/reset_password.html"), name='reset_password'),
    url(r'^ui_statics/reset_password_confirm/$', TemplateView.as_view(template_name="ui_statics/account/reset_password_confirm.html"), name='reset_password_confirm'),
    url(r'^ui_statics/set_new_password/$', TemplateView.as_view(template_name="ui_statics/account/set_new_password.html"), name='set_new_password'),
    url(r'^ui_statics/password_changed/$', TemplateView.as_view(template_name="ui_statics/account/password_changed.html"), name='password_changed'),
    url(r'^ui_statics/my_account/$', TemplateView.as_view(template_name="ui_statics/user_profile/my_account.html"), name='my_account'),
    url(r'^ui_statics/my_account_password/$', TemplateView.as_view(template_name="ui_statics/user_profile/my_account_password.html"), name='my_account_password'),
    url(r'^ui_statics/my_account_notifications/$', TemplateView.as_view(template_name="ui_statics/user_profile/my_account_notifications.html"), name='my_account_notifications'),
    url(r'^ui_statics/company_default/$', TemplateView.as_view(template_name="ui_statics/company_info/company_default.html"), name='company_default'),
    url(r'^ui_statics/company_services/$', TemplateView.as_view(template_name="ui_statics/company_info/company_services.html"), name='company_services'),
    url(r'^ui_statics/company_services_offered/$', TemplateView.as_view(template_name="ui_statics/company_info/company_services_offered.html"), name='company_services_offered'),
    url(r'^ui_statics/company_tech/$', TemplateView.as_view(template_name="ui_statics/company_info/company_tech.html"), name='company_tech'),
    url(r'^ui_statics/company_notifications/$', TemplateView.as_view(template_name="ui_statics/company_info/company_notifications.html"), name='company_notifications'),
    url(r'^ui_statics/company_billing/$', TemplateView.as_view(template_name="ui_statics/company_info/company_billing.html"), name='company_billing'),
    url(r'^ui_statics/services_location/$', TemplateView.as_view(template_name="ui_statics/widgets/services_location.html"), name='services_location'),
    url(r'^ui_statics/select_date_time/$', TemplateView.as_view(template_name="ui_statics/widgets/select_date_time.html"), name='select_date_time'),
    url(r'^ui_statics/enter_address/$', TemplateView.as_view(template_name="ui_statics/widgets/enter_address.html"), name='enter_address'),
    url(r'^ui_statics/submit_info_confirm/$', TemplateView.as_view(template_name="ui_statics/widgets/submit_info_confirm.html"), name='submit_info_confirm'),
    url(r'^ui_statics/additional_notes/$', TemplateView.as_view(template_name="ui_statics/widgets/additional_notes.html"), name='additional_notes'),
    url(r'^ui_statics/add_to_calendar/$', TemplateView.as_view(template_name="ui_statics/widgets/add_to_calendar.html"), name='add_to_calendar'),
    url(r'^ui_statics/no_matches/$', TemplateView.as_view(template_name="ui_statics/widgets/no_matches.html"), name='no_matches'),
)
