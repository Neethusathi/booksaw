from django.urls import path
from webapp import views



urlpatterns = [
    path('', views.home,name="home"),
    path('blog/',views.blog,name="blog"),
    path('single_book/<int:book_id>/',views.single_book,name="single_book"),
    path('filterd_books/<cate_name>/',views.filterd_books,name="filterd_books"),
    path('books_page/',views.books_page,name="books_page"),
    path('about_page/',views.about_page,name="about_page"),
    path('contact_page/',views.contact_page,name="contact_page"),
    path('user_sign_up/',views.user_sign_up,name="user_sign_up"),
    path('user_sign_in/',views.user_sign_in,name="user_sign_in"),
    path('signup/',views.signup,name="signup"),
    path('login/',views.login,name="login"),
    path('user_logout/',views.user_logout,name="user_logout"),
    path('cart_page/',views.cart_page,name="cart_page"),
    path('save_cart/',views.save_cart,name="save_cart"),
    path('cart_page/',views.cart_page,name="cart_page"),
path('cart_delete/<int:cart_id>/',views.cart_delete,name="cart_delete"),
    path('save_cart/',views.save_cart,name="save_cart"),
    path('Update_cart_quantity/<int:item_id>/',views.Update_cart_quantity,name="Update_cart_quantity"),
    path('checkout_page/',views.checkout_page,name="checkout_page"),
    path('payment/',views.payment,name="payment"),
    ]