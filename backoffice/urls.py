from django.urls import path
from django.views.decorators.csrf import csrf_exempt
import requests
# from .bot import EduonBot
from eduon import settings
from .views.views import *
from backoffice.views import statistics_views, speakers_views, users_views, courses_views, moliya_views, confirm_views, settings_views, karantin_views, views, admin_views

urlpatterns = [
    path('', HomeView.as_view(), name='backoffice-home'),
    path('sozlamalar', SettingsView.as_view(), name='sozlamalar'),
    path('setContract', setContrantWithSpeaker, name='setContract'),
    path('speaker', SpeakersView.as_view(), name='backoffice-speaker'),
    path('speaker/course', SpeakerCourse, name='backoffice-speaker-course'),
    path('speaker/<int:pk>', SpeakerDetail.as_view(),
         name='backoffice-speaker-detail'),
    path('course', CoursesView, name='backoffice-course'),
    path('tolov', Tolov.as_view(), name='backoffice-tolov'),
    path('get-billings-count', get_billings_count, name='get_billings_count'),
    path('accept-billing', accespt_billing, name='accept-billing'),
    path('cancel-billing', cancel_billing, name='cancel-billing'),
    path('users', Foydalanuvchilar, name='backoffice-users'),
    path('charts', AjaxCharts, name='charts'),
    path('tasdiqlash', TasdiqView.as_view(), name='tasdiq'),
    path('tasdiqlash-check', TasdiqOk, name='tasdiq-check'),
    path('count-offer', CountOfferAjax, name='count-offer'),
    path('change-course-status', ChangeCourseStatus, name='change-course-status'),
    path('change-course-status-tavsiya', ChangeCourseStatusTavsiya,
         name='change-course-status-tavsiya'),
    path('change-speaker-status', ChangeSpeakerStatus,
         name='change-speaker-status'),
    path('change-user-cash', ChangeCashUser, name='change-user-cash'),
    path('change-user-bonus', ChangeBonusUser, name='change-user-bonus'),
    path('check-phone-number', check_phone_number, name='check-phone-number'),
    path('check-phone-number-reset', check_phone_number_reset,
         name='check-phone-number-reset'),
    path('set-ref-sp', setReferalValueSp, name='set-ref-sp'),
    path('set-ref-us', setReferalValueUS, name='set-ref-us'),
    path('moliya', moliya, name='moliya'),
    path('set-bonus', setBonusSumma, name='set-bonus'),

    # path('telegram-bot', csrf_exempt(EduonBot.as_view())),
    # backoffice login
    path('login', AdminLoginView, name='backoffice_login'),
    # backoffice statistics
    path('total-count', statistics_views.total_count, name="total_count"),
    path('content-and-auditory', statistics_views.content_and_auditory,
         name="content_and_auditory"),
    path('user-statistics', statistics_views.user_statistics,
         name="user_statistics"),
    path('order-statistics', statistics_views.order_statistics,
         name="order_statistics"),
    path('country-statistics', statistics_views.country_statistics,
         name="country_statistics"),
    path('free-and-paid-courses', statistics_views.free_and_paid_courses,
         name="free_and_paid_courses"),
    path('courses-by-categories', statistics_views.courses_by_categories,
         name="courses_by_categories"),
    path('eduon-revenue', views.eduon_revenue, name="eduon_revenue"),

    # backoffice speaker
    path('speakers-list', speakers_views.speakers_list, name="speakers_list"),
    path('speaker-ban/<int:id>', speakers_views.speaker_ban, name="speaker_ban"),
    path('speaker-karantin/<int:id>',
         speakers_views.speaker_karantin, name="speaker_karantin"),
    path('speaker-detail/<int:id>',
         speakers_views.speaker_detail, name="speaker_detail"),

    # backoffice users
    path('users-list', users_views.users_list, name="users_list"),
    path('user-ban/<int:id>', users_views.user_ban, name="user_ban"),
    path('user-karantin/<int:id>', users_views.user_karantin, name="user_karantin"),
    path('user-detail/<int:id>',
         users_views.user_detail, name="user_detail"),
    path('user-bonus/<int:id>', users_views.user_bonus, name="user_bonus"),

    # backoffice courses
    path('course-list', courses_views.course_list, name="course_list"),
    path('course-detail/<int:id>',
         courses_views.course_detail, name="course_detail"),
    path('course-karantin/<int:id>',
         courses_views.course_karantin, name="course_karantin"),
    # backoffice moliya
    path('kirim-chiqim', moliya_views.kirim_chiqim, name="kirim_chiqim"),

    # backoffice tasdiqlash
    path('unconfirmed-courses', confirm_views.unconfirmed_courses,
         name="unconfirmed_courses"),
    path('course-confirm/<int:id>',
         confirm_views.course_confirm, name="course_confirm"),
    path('course-ban/<int:id>', confirm_views.course_ban, name="course_ban"),
    
    # backoffice settings
    path('update-contract', settings_views.speaker_contract_edit,
         name="speaker_contract_edit"),
    path('update-reg-bonus', settings_views.reg_bonus_edit,
         name="reg_bonus_edit"),
    path('set-discount', settings_views.set_discount_course, name="set_discount_course"),
    path('give-bonus', settings_views.give_bonus, name="give_bonus"),
    path('search-user', settings_views.search_user, name="search_user"),
    path('get-default-discount-amount', settings_views.get_default_discount_amount, name="get_default_discount_amount"),
    path('change-course-discount', settings_views.change_course_discount, name="change_course_discount"),
    path('delete-discounts', settings_views.delete_discounts, name="delete_discounts"),
    
    # Backoffice Karantin
    path('karantin', karantin_views.karantin,
         name="karantin"),
    path('users-cash-to-bonus', views.users_cash_to_bonus,
         name="users_cash_to_balance"),
    
    # backoffice admin
    path('admin-list', admin_views.admin_list, name="admin_list"),
    path('add-new-admin', admin_views.add_new_admin, name="add_new_admin"),
    path('edit-admin/<int:id>', admin_views.edit_admin, name="edit_admin"),
    path('delete-admin/<int:id>', admin_views.delete_admin, name="delete_admin"),
]

# r = requests.post(settings.SMS_BASE_URL + '/api/auth/login/',
#                   {'email': settings.SMS_EMAIL, 'password': settings.SMS_SECRET_KEY}).json()
# settings.SMS_TOKEN = r['data']['token']

# try:
#     rs = requests.post(settings.SMS_BASE_URL_GLOBAL + '/oauth/token',
#                       {'client_id': settings.SMS_CLIENT_ID, 'secret': settings.SMS_SECRET_KEY_GLOBAL, "expires_in": 3600}).json()
#     settings.SMS_TOKEN_GLOBAL = rs['jwt']
# except:
#     pass
