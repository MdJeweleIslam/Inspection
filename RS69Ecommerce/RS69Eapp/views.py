from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from .models import (Slider, Offer, Cupon,
					ProductPrice, Product, Catagory,
					SubCatagory, Store, ProductGalary, 
					Shipping, ShippingCost, Order, OrderDetails, 
					OrderStatus, EcomUser)

from .password import PassWord
from datetime import datetime
import random
import json
from django.core import serializers
class IndexView(View):

	def get(self, request):
		context = {}
		### Slider Query Set ###
		context['slider'] = Slider.objects.filter(is_active=True)

		### Slider Query Set ###

		### Offer List ###
		# offer_list = OfferImage.objects.filter()
		# if len(offer_list) > 4:
		# 	context['offer_list'] = offer_list[:4]
		# else:
		# 	context['offer_list'] = offer_list
		# ### Offer List ###

		### Cupon ###
		thismonth = str(datetime.now().month)
		ran = Cupon.objects.filter(is_active=True)
		if len(ran) != 0:
			context['coupon'] = random.choice(ran)
		else:
			context['coupon'] = ran
		### Cupon ###

		##ON SALE PRODUCT##

		## Catagory Product ##
		try:
			context['catagory_list'] = Catagory.objects.all()[:5]
			context['first_cat'] = context['catagory_list'][0].catagory_name
			context['sec_cat'] = context['catagory_list'][1].catagory_name
			context['thi_cat'] = context['catagory_list'][2].catagory_name
			context['four_cat'] = context['catagory_list'][3].catagory_name
			context['five_cat'] = context['catagory_list'][4].catagory_name
		except:
			context['catagory_list'] = Catagory.objects.all()[:5]
		
		context['sub_catagory_list'] = SubCatagory.objects.all()
		
		## Catagory Product ##

		context['product'] = Product.objects.filter(is_active=True)
		context['trand'] = context['product'][:30]

		##ON SALE PRODUCT##

		##Store Profile##
		context['store_profile'] = Store.objects.all()#[:30]

		##Store Profile##

		return render(request, 'index.html', context)
	
	def post(self, request):
		context = {}
		return render(request, 'index.html', context)

class ApiCatproduct(View):

	def get(self, request, search=None):
		Getval = False
		json_convert = []
		if request.GET.get('search'):
			if request.GET.get('search') != None:
				cat = request.GET.get('search')
				print(cat)
				cat_product = []
				products = Product.objects.filter(catagory_manager_id__catagory_id__catagory_name=str(cat))
				"""
				cat_product = serializers.serialize('json', product)
				model_data = {
					product_id = models.AutoField(primary_key=True)
					product_name =models.CharField(blank =True,max_length=50)
					slug = models.CharField(max_length=100, unique=True, null=True, blank=True)
					product_info = models.TextField()
					product_video = models.URLField(null=True, blank=True)
					product_keyword = models.TextField(max_length=255)
					is_active = models.BooleanField(default=True)
					product_description = models.CharField(blank=True,max_length=150)
					catagory_manager_id = models.ForeignKey(CatagoryManager,on_delete=models.CASCADE)
					brand_id = models.ForeignKey(Brand,on_delete=models.CASCADE)
					product_price_id = models.ForeignKey(ProductPrice,on_delete=models.CASCADE)
					color_and_size_id = models.ForeignKey(ColorSizeManager, on_delete=models.CASCADE, default="")
					product_image = models.ImageField(upload_to='product/%Y/%d/%b')
					store_id = models.ForeignKey(Store,on_delete=models.CASCADE)
				}
				all_products = {
						'product_id': 1,
						'product_name': 1,
						'slug': 1,
						'product_info': 1,
						'product_video': 1,
						'product_keyword': 1,
						'product_description': 1,
						'catagory_name': 1,
						'sub_catagory_name': 1,
						'brand_id': 1,
						'regular_product_price': 1,
						'offer_product_price': 1,
						'product_image': 1,
						'store_name': 1,
					}

				"""
				for each_product in products:
					all_products = {
						'product_id': each_product.product_name,
						'product_name': each_product.product_name,
						'slug': each_product.slug,
						'product_info': each_product.product_info,
						'product_video': each_product.product_video,
						'product_keyword': each_product.product_keyword,
						'product_description': each_product.product_description,
						'catagory_name': each_product.catagory_manager_id.catagory_id.catagory_name,
						'sub_catagory_name': each_product.catagory_manager_id.sub_catagory_id.sub_catagory_name,
						'brand_id': each_product.brand_id.brand_name,
						'regular_product_price': each_product.product_price_id.price,
						'offer_product_price': each_product.product_price_id.offer_price,
						'product_image': str(each_product.product_image),
						'store_name': each_product.store_id.store_name,
					}
					cat_product.append(all_products)
					
				json_dump = json.dumps(cat_product)
				#json_convert = json.loads(json_dump)
				Getval = True
				#cat_product = serializers.serialize('json', json_dump)
				#return HttpResponse(json_convert, content_type="application/json")
			else:
				cat_product = {}
				cat_product['error'] = True
				cat_product['msg'] = "This Catagory Product Not Found"
		else:
			cat_product = {}
			cat_product['error'] = True
			cat_product['msg'] = "GET VALUE NOT FOUND"
		if Getval:
			return HttpResponse(json_dump, content_type="application/json")
		else:
			return HttpResponse(json.dumps(cat_product), content_type="application/json")
class ApiCategory(View):

	def get(self, request):
		catagory_list = Catagory.objects.all()[:5]
		category = serializers.serialize('json', catagory_list)

		return HttpResponse(category, content_type="application/json")

class ApiCatproductAll(View):

	def get(self, request):
		Getval = False
		json_convert = []
		cat_product = []
		products = Product.objects.filter()[:30]
		for each_product in products:
			all_products = {
				'product_id': each_product.product_name,
				'product_name': each_product.product_name,
				'slug': each_product.slug,
				'product_info': each_product.product_info,
				'product_video': each_product.product_video,
				'product_keyword': each_product.product_keyword,
				'product_description': each_product.product_description,
				'catagory_name': each_product.catagory_manager_id.catagory_id.catagory_name,
				'sub_catagory_name': each_product.catagory_manager_id.sub_catagory_id.sub_catagory_name,
				'brand_id': each_product.brand_id.brand_name,
				'regular_product_price': each_product.product_price_id.price,
				'offer_product_price': each_product.product_price_id.offer_price,
				'product_image': str(each_product.product_image),
				'store_name': each_product.store_id.store_name,
			}
			cat_product.append(all_products)

		json_dump = json.dumps(cat_product)
		Getval = True
		if Getval:
			return HttpResponse(json_dump, content_type="application/json")
		else:
			return HttpResponse(json.dumps(cat_product), content_type="application/json")


class FiveProductByTraffice(View):
	def get(self, request):
		return HttpResponse("")

	def post(self, request):
		return HttpResponse("")

	


class CartApiView(View):
	def get(self, request):
		if 'slug' not in request.session and 'quantity' not in request.session and 'color' not in request.session and 'size' not in request.session:
			request.session['slug'] = []
			request.session['quantity'] = []
			request.session['color'] = []
			request.session['size'] = []
			request.session['cart_total'] = 0
			print("Session Created API GET METHOD")
		return HttpResponse("GET METHOD not Allow")
	def post(self, request):
		if 'slug' not in request.session and 'quantity' not in request.session and 'color' not in request.session and 'size' not in request.session:
			request.session['slug'] = []
			request.session['quantity'] = []
			request.session['color'] = []
			request.session['size'] = []
			request.session['cart_total'] = 0
			print("Session Created API POST METHOD")
		if 'slug' in request.session and 'quantity' in request.session and 'color' in request.session and 'size' in request.session:
			print(request.session['slug'])
			print("BEFORE")
			byet_data = request.body
			json_data = json.loads(byet_data.decode('utf8').replace("'", '"'))
			product_slug = json_data['slug'].replace("/product/", "").replace("/", "")
			if product_slug in request.session['slug']:
				for index, each_i in enumerate(request.session['slug']):
					if product_slug == each_i:
						sess_quantity = request.session['quantity']
						sum_val = int(sess_quantity[index]) + int(json_data['quantity'])
						sess_quantity[index] = sum_val
						request.session['quantity'] = sess_quantity
			else:
				session_slug = request.session['slug']
				session_slug.append(product_slug)
				request.session['slug'] = session_slug
				session_quantity = request.session['quantity']
				session_quantity.append(json_data['quantity'])
				request.session['quantity'] = session_quantity
				session_color = request.session['color']
				session_color.append(json_data['color'])
				request.session['color'] = session_color
				session_size = request.session['size']
				session_size.append(json_data['size'])
				request.session['size'] = session_size
		return HttpResponse(json.dumps({'error': True, 'msg': 'Data Added in Cart'}))

class FlushSession(View):
	def get(self, request):
		if 'slug' in request.session and 'quantity' in request.session and 'color' in request.session and 'size' in request.session:
			del request.session['slug']
			del request.session['quantity']
			del request.session['color']
			del request.session['size']
			del request.session['cart_total']

			return HttpResponse("All session Cleaned")
		else:
			return HttpResponse("NO DATA IN SESSION")

class UpdateCart(View):
	def get(self, request, search = None, quqantity=None, slug=None):
		result = "Session Cleaned"
		if 'slug' in request.session and 'quantity' in request.session and 'color' in request.session and 'size' in request.session:
			try:
				if request.GET.get('search'):
					if request.GET.get('search') != None:
						slug = request.GET.get('search')
						if slug in request.session['slug']:
							for index, each_i in enumerate(request.session['slug']):
								if slug == each_i:
									sess_quantity = request.session['quantity']
									this_quantity = sess_quantity[index]
									sess_quantity.remove(sess_quantity[index])
									request.session['quantity'] = sess_quantity
									session_slug = request.session['slug']
									session_slug.remove(session_slug[index])
									request.session['slug'] = session_slug
									session_color = request.session['color']
									session_color.remove(session_color[index])
									request.session['size'] = session_color
									session_size = request.session['size']
									session_size.remove(session_color[index])
									request.session['color'] = session_size
									total = request.session['cart_total']
									alive_total = int(total) - (int(this_quantity)*ProductPrice.objects.get(product_price_id__slug=slug).offer_price)
									request.session['cart_total'] = alive_total
				if request.GET.get('quqantity'):
					if request.GET.get('quqantity') != None:
						quqantity = request.GET.get('quqantity')
						slug = request.GET.get('slug')
						if slug in request.session['slug']:
							for index, each_i in enumerate(request.session['slug']):
								if slug == each_i:
									sess_quantity = request.session['quantity']
									sess_quantity[index] = quqantity
									request.session['quantity'] = sess_quantity
									total = request.session['cart_total']
									alive_total = int(total) + (int(quqantity)*ProductPrice.objects.get(product_price_id__slug=slug).offer_price)
									request.session['cart_total'] = alive_total

			except Exception as e:
				result = str(e)
			return HttpResponse(result)
		else:
			result = "NO DATA IN SESSION"
			return HttpResponse(result)



class CartView(View):

	def get(self, request):
		context = {}
		context['cart_list'] = []
		context['cart_list_total'] = 0.00
		if 'slug' not in request.session and 'quantity' not in request.session and 'color' not in request.session and 'size' not in request.session:
			request.session['slug'] = []
			request.session['quantity'] = []
			request.session['color'] = []
			request.session['size'] = []
			request.session['cart_total'] = 0
			print("Session Created CART GET METHOD")
		if 'slug' in request.session and 'quantity' in request.session and 'color' in request.session and 'size' in request.session:
			print(request.session['slug'])
			for index, each_cart_item in enumerate(request.session['slug']):
				each_product = Product.objects.filter(slug=each_cart_item)[0]
				each_list = {
					'slug': request.session['slug'][index],
					'name': each_product.product_name,
					'img': str(each_product.product_image),
					'price': each_product.product_price_id.offer_price,
					'quantity': request.session['quantity'][index],
					'total': float(request.session['quantity'][index])*float(each_product.product_price_id.offer_price),
				}
				context['cart_list_total'] += float(request.session['quantity'][index])*float(each_product.product_price_id.offer_price)
				context['cart_list'].append(each_list)
				request.session['cart_total'] = context['cart_list_total']
		# print(context['cart_list'])
		# print(context['cart_list_total'])
		return render(request, 'cart.html', context)
	
	def post(self, request):
		context = {}
		return render(request, 'cart.html', context)	


class DashboardView(View):

	def get(self, request):
		context = {}
		return render(request, 'dashboard.html', context)
	
	def post(self, request):
		context = {}
		return render(request, 'dashboard.html', context)


class LoginView(View):

	def get(self, request):
		context = {}
		return render(request, 'login.html', context)
	
	def post(self, request):
		context = {}
		return render(request, 'login.html', context)	


class RegisterView(View):

	def get(self, request):
		context = {}
		return render(request, 'register.html', context)
	
	def post(self, request):
		context = {}
		return render(request, 'register.html', context)	


class ContactView(View):

	def get(self, request):
		context = {}
		return render(request, 'contact.html', context)
	
	def post(self, request):
		context = {}
		return render(request, 'contact.html', context)


class Forget_pwdView(View):

	def get(self, request):
		context = {}
		return render(request, 'forget_pwd.html', context)
	
	def post(self, request):
		context = {}
		return render(request, 'forget_pwd.html', context)


class profileView(View):

	def get(self, request):
		context = {}
		return render(request, 'profile.html', context)
	
	def post(self, request):
		context = {}
		return render(request, 'profile.html', context)

class CheckoutView(View):

	def get(self, request):
		context = {}
		context['cart_list'] = []
		context['cart_list_total'] = 0
		if 'slug' in request.session and 'quantity' in request.session and 'color' in request.session and 'size' in request.session:
			for index, each_cart_item in enumerate(request.session['slug']):
				each_product = Product.objects.filter(slug=each_cart_item)[0]
				each_list = {
					'slug': request.session['slug'][index],
					'name': each_product.product_name,
					'img': str(each_product.product_image),
					'price': each_product.product_price_id.offer_price,
					'quantity': request.session['quantity'][index],
					'total': float(request.session['quantity'][index])*float(each_product.product_price_id.offer_price),
				}
				context['cart_list_total'] += float(request.session['quantity'][index])*float(each_product.product_price_id.offer_price)
				context['cart_list'].append(each_list)
		return render(request, 'checkout.html', context)
	
	def post(self, request):
		context = {}
		"""
		csrfmiddlewaretoken=token&fname=df&lname=df&phone=fd&email=fd&
		country=Austria&address=df&city=df&state=df&postalcode=fd&payment-group=on&
		ship_fname=&ship_lname=&ship_phone=&ship_email=&ship_country=&ship_address=&
		ship_city=&ship_state=&ship_postalcode=
		"""
		if 'slug' in request.session and 'quantity' in request.session and 'color' in request.session and 'size' in request.session:
			print("SESSION WORKING")
			if 'bill_ship_dif' in request.POST:
				print("bill_ship_dif WORKING")
				if 'fname' in request.POST and 'lname' in request.POST and 'phone' in request.POST and \
					'email' in request.POST and 'country' in request.POST and 'address' in request.POST and \
					'city' in request.POST and 'postalcode' in request.POST:
					print("FORM WORKING")
					fname = request.POST['fname']
					lname = request.POST['lname']
					phone = request.POST['phone']
					email = request.POST['email']
					country = request.POST['country']
					address = request.POST['address']
					city = request.POST['city']
					postalcode = request.POST['postalcode']
					payment = request.POST['payment-group']
					#password = request.POST['password']
					password = "TESTED"
					#ship_fname = request.POST['ship_fname']
					#ship_lname = request.POST['ship_lname']
					ship_phone = request.POST['ship_phone']
					ship_email = request.POST['ship_email']
					ship_country = request.POST['ship_country']
					ship_address = request.POST['ship_address']
					ship_city = request.POST['ship_city']
					ship_postalcode = request.POST['ship_postalcode']
					payment = request.POST['payment-group']
					User_add = EcomUser(
							user_name = str(fname).lower()+str(lname).lower(),
							user_email = email,
							user_phone = phone,
							user_address= address,
							user_password = PassWord(password)
						)
					User_add.save()
					ship_add = Shipping(
							shipping_address = ship_address,
							city_name = ship_city,
							post_code = ship_postalcode,
							phone = ship_phone,
							user_id = EcomUser.objects.get(user_email=User_add.user_email),
						)
					ship_add.save()
					order_add = Order(
							user_id = EcomUser.objects.get(user_email=User_add.user_email),
							order_status_id = OrderStatus.objects.get(order_status_id=1),
							fullorder_total_ammount = 0.00,
							delivery_date = "2020-1-1",
							af_user_id = None,
							shipping_id = ship_add,
						)
					order_add.save()
					this_order_id = order_add.order_id
					if len(request.session['slug']) != 0:
						for index, each_cart_item in enumerate(request.session['slug']):
							each_product = Product.objects.filter(slug=each_cart_item)[0]
							place_order = OrderDetails(
									quantity = request.session['quantity'][index],
									product_id = Product.objects.get(slug=request.session['slug'][index]),
									order_id = order_add,
								)
							#Order.objects.get(order_id=this_order_id)
							place_order.save()

					del request.session['slug']
					del request.session['quantity']
					del request.session['color']
					del request.session['size']
					del request.session['cart_total']
					"""
					order_details_id = models.AutoField(primary_key=True)
					quantity = models.PositiveIntegerField()
					product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
					order_id = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="order")
					datetime = models.DateTimeField(auto_now_add=True)
					cupon_id = models.ForeignKey(Cupon, on_delete=models.CASCADE, null=True, blank=True)
					offer_id = models.ForeignKey(Offer, on_delete=models.CASCADE, null=True, blank=True)
					each_list = {
						'slug': request.session['slug'][index],
						'name': each_product.product_name,
						'img': str(each_product.product_image),
						'price': each_product.product_price_id.offer_price,
						'quantity': request.session['quantity'][index],
						'total': float(request.session['quantity'][index])*float(each_product.product_price_id.offer_price),
					}
					"""
			else:
				if 'ship_fname' in request.POST and 'ship_lname' in request.POST and 'ship_phone' in request.POST and \
					'ship_email' in request.POST and 'ship_country' in request.POST and 'ship_address' in request.POST and \
					'ship_city' in request.POST and 'ship_postalcode' in request.POST:
					ship_fname = request.POST['ship_fname']
					ship_lname = request.POST['ship_lname']
					ship_phone = request.POST['ship_phone']
					ship_email = request.POST['ship_email']
					ship_country = request.POST['ship_country']
					ship_address = request.POST['ship_address']
					ship_city = request.POST['ship_city']
					ship_postalcode = request.POST['ship_postalcode']
					payment = request.POST['payment-group']
					User_add = EcomUser(
							user_name = str(ship_fname).lower()+str(ship_fname).lower(),
							user_email = ship_email,
							user_phone = ship_phone,
							user_address= ship_address,
							user_password = PassWord("password")
						)
					User_add.save()
					ship_add = Shipping(
							shipping_address = ship_address,
							city_name = ship_city,
							post_code = ship_postalcode,
							phone = ship_phone,
							user_id = User_add,
						)
					#EcomUser.objects.get(user_email=User_add.user_email)
					ship_add.save()
					order_add = Order(
							user_id = User_add,
							order_status_id = OrderStatus.objects.get(order_status_id=1),
							fullorder_total_ammount = 0.00,
							delivery_date = "2020-1-1",
							af_user_id = None,
							shipping_id = ship_add,
						)
					order_add.save()
					this_order_id = order_add.order_id
					if len(request.session['slug']) != 0:
						for index, each_cart_item in enumerate(request.session['slug']):
							each_product = Product.objects.filter(slug=each_cart_item)[0]
							place_order = OrderDetails(
									quantity = request.session['quantity'][index],
									product_id = Product.objects.get(slug=request.session['slug'][index]),
									order_id = order_add,
								)
							#Order.objects.get(order_id=this_order_id)
							place_order.save()

		else:
			context['error'] = True
			context['error'] = "You did't selected any product"
			return render(request, 'checkout.html', context)

		return render(request, 'checkout.html', context)


class WishlistView(View):

	def get(self, request):
		context = {}
		return render(request, 'wishlist.html', context)
	
	def post(self, request):
		context = {}
		return render(request, 'wishlist.html', context)


class AboutView(View):

	def get(self, request):
		context = {}
		return render(request, 'about.html', context)
	
	def post(self, request):
		context = {}
		return render(request, 'about.html', context)


class SearchView(View):

	def get(self, request):
		context = {}
		return render(request, 'search.html', context)
	
	def post(self, request):
		context = {}
		return render(request, 'search.html', context)



class OrderSuccessView(View):

	def get(self, request):
		context = {}
		return render(request, 'order-success.html', context)
	
	def post(self, request):
		context = {}
		return render(request, 'order-success.html', context)


class CompareView(View):

	def get(self, request):
		context = {}
		return render(request, 'compare.html', context)
	
	def post(self, request):
		context = {}
		return render(request, 'compare.html', context)


class CollectionView(View):

	def get(self, request):
		context = {}
		return render(request, 'collection.html', context)
	
	def post(self, request):
		context = {}
		return render(request, 'collection.html', context)


class ErrorView(View):

	def get(self, request):
		context = {}
		return render(request, '404.html', context)
	
	def post(self, request):
		context = {}
		return render(request, '404.html', context)

class ComingSoonView(View):

	def get(self, request):
		context = {}
		return render(request, 'coming-soon.html', context)
	
	def post(self, request):
		context = {}
		return render(request, 'coming-soon.html', context)


class FaqView(View):

	def get(self, request):
		context = {}
		return render(request, 'faq.html', context)
	
	def post(self, request):
		context = {}
		return render(request, 'faq.html', context)


class BlogView(View):

	def get(self, request):
		context = {}
		return render(request, 'blog.html', context)
	
	def post(self, request):
		context = {}
		return render(request, 'blog.html', context)


class CategoryView(View):

	def get(self, request):
		context = {}
		return render(request, 'category-page.html', context)
	
	def post(self, request):
		context = {}
		return render(request, 'category-page.html', context)


class OrderHistoryView(View):

	def get(self, request):
		context = {}
		return render(request, 'order-history.html', context)
	
	def post(self, request):
		context = {}
		return render(request, 'order-history.html', context)




class ProductPageView(View):

	def get(self, request, request_slug):
		context = {}
		single_product = Product.objects.filter(slug=request_slug)
		context['product_gallary'] = ProductGalary.objects.filter(product_id=single_product[0])
		if len(single_product) != 0:
			context['product'] = single_product[0]
			brand_product = Product.objects.filter(brand_id__brand_name = single_product[0].brand_id.brand_name)
			if len(brand_product) >= 20:
				context['brand_product_one'] = brand_product[:10]
				context['brand_product_two'] = brand_product[10:]
				context['show'] = True
			elif len(brand_product) >= 10 and len(brand_product) < 20:
				context['brand_product_one'] = brand_product[:10]
				if len(brand_product) - 10 != 0:
					context['brand_product_two'] = brand_product[10:]
				else:
					context['brand_product_two'] = []
					context['show'] = False
			elif len(brand_product) < 10 :
				context['brand_product_one'] = brand_product[:len(brand_product)]
				context['brand_product_two'] = []
				context['show'] = False
			context['catagory_product'] = Product.objects.filter(catagory_manager_id__catagory_id__catagory_name = single_product[0].catagory_manager_id.catagory_id.catagory_name)
			return render(request, 'product-page.html', context)
		else:
			return HttpResponse("Product Not Found")
	
	def post(self, request):
		context = {}
		return render(request, 'product-page.html', context)



class ReviewView(View):

	def get(self, request):
		context = {}
		return render(request, 'review.html', context)
	
	def post(self, request):
		context = {}
		return render(request, 'review.html', context)