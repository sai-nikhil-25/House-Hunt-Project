from django.urls import path
from . import views
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view
from . forms import LoginForm,PasswordResetForm,MyPasswordChangeForm,SetPasswordForm
from django.conf import settings

urlpatterns = [
    path('', views.main,name = "mainPage" ),
    path('placesFilter/<slug:val>',views.placesFilter,name='places'),
    path('category/<slug:category>/', views.category, name='category'),

    path('view/<int:pk>/', views.view,name = "viewPage" ),
    path('appointment/<int:listing_pk>',views.book_appointment,name = "appointmentPage"),
    path('success/',views.success_page,name='success_page'),
    path('view-appointments/',views.view_appointments,name='view_appointments'),
    path('wishlist/',views.wishlist,name='wishlist'),
    path('toggle_wishlist/<int:listing_pk>/', views.toggle_wishlist, name='toggle_wishlist'),

    path('registration/',views.RegisterView.as_view(),name='registration'),
    path('accounts/login', auth_view.LoginView.as_view(template_name='hp/login.html',authentication_form=LoginForm),name='login'),
    path('profile/', views.ProfileView.as_view(),name="profile"),
    path('address/', views.address,name="address"),
    path('updateAddress/<int:pk>',views.updateAddress.as_view(),name='updateAddress'),
    path('updatePassword/', auth_view.PasswordChangeView.as_view(template_name='hp/changePassword.html',form_class=MyPasswordChangeForm,success_url='/passwordChangeDone'),name='updatePassword'),
    path('passwordChangeDone/',auth_view.PasswordChangeDoneView.as_view(template_name='hp/passwordChangedone.html'),name='passwordchangedone'),
    path('logout/',auth_view.LogoutView.as_view(next_page='login'),name='logout'),
    path('password-reset/',auth_view.PasswordResetView.as_view(template_name='hp/password_reset.html',form_class=PasswordResetForm),name='password_reset'),
    path('password-reset/done/',auth_view.PasswordResetDoneView.as_view(template_name='hp/password_reset_done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',auth_view.PasswordResetConfirmView.as_view(template_name='hp/password_reset_confirm.html',form_class=SetPasswordForm),name='password_reset_confirm'),
    path('password-reset-complete/',auth_view.PasswordResetCompleteView.as_view(template_name='hp/password_reset_complete.html'),name='password_reset_complete'),

    path('AboutUs/',views.aboutus,name='aboutus'),
    path('ContactUs/',views.contactus,name='contactus'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)