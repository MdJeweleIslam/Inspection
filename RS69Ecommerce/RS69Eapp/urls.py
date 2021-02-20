from  django.urls import include, path
from django.conf.urls import include, url

from . import views

urlpatterns = [
	path('', views.IndexView.as_view(), name='index'),
	path('cart/', views.CartView.as_view(), name='cart'),
	path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
	path('login/', views.LoginView.as_view(), name='login'),
	path('register/', views.RegisterView.as_view(), name='register'),
	path('forget_pwd/', views.Forget_pwdView.as_view(), name='forget_pwd'),
	path('contact/', views.ContactView.as_view(), name='contact'),
	path('profile/', views.profileView.as_view(), name='profile'),
	path('checkout/', views.CheckoutView.as_view(), name='checkout'),
	path('wishlist/', views.WishlistView.as_view(), name='wishlist'),
	path('about/', views.AboutView.as_view(), name='about'),
	path('search/', views.SearchView.as_view(), name='search'),
	path('order-success/', views.OrderSuccessView.as_view(), name='order-success'),
	path('compare/', views.CompareView.as_view(), name='compare'),
	path('collection/', views.CollectionView.as_view(), name='collection'),
	path('404/', views.ErrorView.as_view(), name='404'),
	path('coming-soon/', views.ComingSoonView.as_view(), name='coming-soon'),
	path('faq/', views.FaqView.as_view(), name='faq'),
	path('blog/', views.BlogView.as_view(), name='blog'),
	path('category/', views.CategoryView.as_view(), name='category'),
	path('order-history/', views.OrderHistoryView.as_view(), name='order-history'),
	path('product/<str:request_slug>/', views.ProductPageView.as_view(), name='product'),
	path('review/', views.ReviewView.as_view(), name='review'),
	path('api/cat-product/', views.ApiCatproduct.as_view(), name='api_cat_product'),
	path('api/cat-product/all/', views.ApiCatproductAll.as_view(), name='all_api_cat_product'),
	path('api/category/', views.ApiCategory.as_view(), name='api_cat'),
	path('api/cart/', views.CartApiView.as_view(), name='api_cart'),
	path('api/update-cart/', views.UpdateCart.as_view(), name='update_cart'),
	path('logout/', views.FlushSession.as_view(), name='api_cart'),
	
	
	#path('upload/', views.UploadView.as_view(), name='upload'),
]