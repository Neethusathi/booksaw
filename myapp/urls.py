from django.urls import path
from myapp import views


urlpatterns = [
    path('dashboard/', views.dashboard,name="dashboard"),
    path('category/', views.category,name="category"),
    path('save_category/', views.save_category,name="save_category"),
    path('disp_cate/', views.disp_cate,name="disp_cate"),
    path('cate_delete/<int:ci>', views.cate_delete,name="cate_delete"),
    path('cate_edit/<int:ci>', views.cate_edit,name="cate_edit"),
    path('category_update/<int:cr>', views.category_update, name="category_update"),

    path('add_product/', views.add_product,name="add_product"),
    path('save_product/', views.save_product,name="save_product"),
    path('product_disp/', views.product_disp,name="product_disp"),
    path('product_delete/<int:pi>', views.product_delete,name="product_delete"),
    path('pro_edit/<int:pi>', views.pro_edit,name="pro_edit"),
    path('update_product/<int:pr>', views.update_product,name="update_product"),
    path('admin_login_page/', views.admin_login_page,name="admin_login_page"),
    path('admin_login/', views.admin_login,name="admin_login"),
    path('admin_logout/', views.admin_logout,name="admin_logout"),



]
