from django.db import models
from .password import PassWord
import PIL as Pillow
from django.template.defaultfilters import slugify
import random
#F:/DjngoProject/Github/RS69-Ecommerce/RS69Ecommerce/media/slider/2020/13/Jul/19.jpg

#splitdir = image_dir.split("/RS69Ecommerce/")

class Slider(models.Model):
	slider_id = models.AutoField(primary_key=True)
	slider_title = models.CharField(max_length=255)
	slider_keyword = models.CharField(max_length=255)
	slider_content = models.TextField()
	is_active = models.BooleanField(default=True)
	slider_img = models.ImageField(upload_to ='slider/%Y/%d/%b')
	date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return str(self.slider_id)




class SecurityInfo(models.Model):
	security_info_id = models.AutoField(primary_key=True)
	visitor_ip = models.CharField(max_length=25)
	last_visit = models.DateTimeField(auto_now_add=True)
	compromise_url = models.CharField(blank = True, max_length=150)

	def __str__(self):
		return str(self.security_info_id)



class Catagory(models.Model):
	catagory_id = models.AutoField(primary_key=True)
	catagory_name = models.CharField(unique=True,max_length=30)
	catagory_image = models.ImageField(upload_to ='category/%Y/%d/%b')

	def __str__(self):
		return str(self.catagory_name)


class SubCatagory(models.Model):
	sub_catagory_id = models.AutoField(primary_key=True)
	sub_catagory_name = models.CharField(blank=True,max_length=50)
	catagory_id = models.ForeignKey(Catagory,on_delete=models.CASCADE)

	def __str__(self):
		return str(self.sub_catagory_name)


class CatagoryManager(models.Model):
	catagory_manager_id = models.AutoField(primary_key=True)
	catagory_id = models.ForeignKey(Catagory,on_delete=models.CASCADE)
	sub_catagory_id = models.ForeignKey(SubCatagory,on_delete=models.CASCADE)

	def __str__(self):
		return str(self.catagory_manager_id)

class Brand(models.Model):
	brand_id = models.AutoField(primary_key=True)
	brand_name = models.CharField(unique =True,max_length=50)
	brand_code = models.PositiveSmallIntegerField(unique=True)
	brand_short_description = models.CharField(blank=True,max_length=100)
	brand_address = models.CharField(blank=True,max_length=100)
	brand_logo = models.ImageField(upload_to ='Brand/%Y/%d/%b')

	def __str__(self):
		return str(self.brand_id)

class ProductPrice(models.Model):
	product_price_id = models.AutoField(primary_key=True)
	price = models.FloatField(max_length=20)
	product_price_entry_date = models.DateTimeField(auto_now_add=True)
	offer_price = models.FloatField(max_length=20)
	is_active = models.BooleanField(default=True)

	def __str__(self):
		return str(self.product_price_id)

class ProductColor(models.Model):
	color_id = models.AutoField(primary_key=True)
	color_name = models.CharField(max_length=100)

	def __str__(self):
		return str(self.color_name)

class ProductSize(models.Model):
	size_id = models.AutoField(primary_key=True)
	size_val = models.CharField(max_length=100)

	def __str__(self):
		return str(self.size_val)

class ColorSizeManager(models.Model):
	color_size_manager_id = models.AutoField(primary_key=True)
	color_id = models.ForeignKey(ProductColor,on_delete=models.CASCADE)
	size_id = models.ForeignKey(ProductSize,on_delete=models.CASCADE)
	quantity = models.CharField(max_length=64)
	#size = MultiQuantityField(dim=3, units=(ureg.mm, ureg.cm, ureg.m))
	#weight = MultiQuantityField(units=(ureg.g, ureg.kg))	

	def __str__(self):
		return str(self.color_id)

class Store(models.Model):
	store_id = models.AutoField(primary_key=True)
	store_name = models.CharField(max_length=255, unique=True)
	store_address = models.TextField()
	store_image = models.ImageField(upload_to ='store/%Y/%d/%b')
	store_email = models.CharField(max_length=50, unique=True)
	store_phone = models.CharField(max_length=20, unique=True)
	store_password = models.CharField(max_length=64)
	store_licence = models.CharField(max_length=100, null=True, blank=True)
	store_nid = models.CharField(max_length=50, null=True, blank=True)
	is_active = models.BooleanField(default=True)

	def __str__(self):
		return str(self.store_name)

class OfferType(models.Model):
	offer_type_id = models.AutoField(primary_key=True)
	offer_type_name = models.CharField(blank=True,max_length=20)

	def __str__(self):
		return str(self.offer_type_name)

class OfferMaxAmount(models.Model):
	offer_max_amount_id = models.AutoField(primary_key=True)
	max_amount = models.FloatField(max_length=20)
	min_amount = models.FloatField(max_length=20)
	
	def __str__(self):
		return str(self.offer_max_amount_id)


class Offer(models.Model):
	offer_id = models.AutoField(primary_key=True)
	offer_name = models.CharField(blank=True,max_length=20)
	offer_type_id = models.ForeignKey(OfferType,on_delete=models.CASCADE)
	offer_amount =models.FloatField(max_length=True)
	offer_image = models.ImageField(upload_to ='media/offer/%Y/%d/%b')
	offer_max_amount_id = models.ForeignKey(OfferMaxAmount,on_delete=models.CASCADE)
	is_active = models.BooleanField(default=True)
	offer_reason = models.CharField(blank=True,max_length=50)
	start_time_date =models.DateTimeField(auto_now_add=True)
	end_time_date = models.DateTimeField(auto_now_add=True)
	

	def __str__(self):
		return str(self.offer_type_id)		


class Cupon(models.Model):
	cupon_id = models.AutoField(primary_key=True)
	cupon_name = models.CharField(blank=True,max_length=100)
	cupon_code = models.CharField(max_length=50)
	start_date =models.DateTimeField(auto_now_add=True)
	end_date = models.DateTimeField(auto_now_add=True)
	offer_max_amount_id = models.ForeignKey(OfferMaxAmount,on_delete=models.CASCADE)
	amount = models.FloatField(max_length=20)
	is_active = models.BooleanField(default=True)

	def __str__(self):
		return str(self.cupon_code)


class OrderStatus(models.Model):
	order_status_id = models.AutoField(primary_key=True)
	order_status_name = models.CharField(max_length=155, default="")

	def __str__(self):
		return str(self.order_status_name)





class EcomUser(models.Model):
	user_id = models.AutoField(primary_key=True)
	user_name = models.CharField(max_length=100)
	user_email = models.CharField(max_length=75, unique=True)
	user_phone = models.CharField(max_length=14, unique=True)
	user_address = models.CharField(max_length=200, blank=True)
	user_password = models.CharField(max_length=64)
	user_Gendar = models.CharField(max_length=20, null=True, blank=True)
	user_photo = models.ImageField(upload_to ='user/%Y/%d/%b', null=True, blank=True)
	is_active = models.BooleanField(default=True)

	
	def clean(self):

		if len(self.user_password) != 64:
			self.user_password = PassWord(self.user_password)


	def __str__(self):
		return str(self.user_id)

class AffiliateUser(models.Model):
	af_user_id = models.AutoField(primary_key=True)
	af_user_name = models.CharField(max_length=100)
	af_user_email = models.CharField(max_length=75, unique=True)
	af_user_phone = models.CharField(max_length=14, unique=True)
	af_user_address = models.CharField(max_length=200, blank=True)
	af_user_password = models.CharField(max_length=64)
	af_user_Gendar = models.CharField(max_length=20, null=True, blank=True)
	af_user_photo = models.ImageField(upload_to ='user/%Y/%d/%b')
	is_active = models.BooleanField(default=False)

	
	def clean(self):

		if len(self.user_password) != 64:
			self.user_password = PassWord(self.af_user_password)


	def __str__(self):
		return str(self.user_id)



class UserConfirmation(models.Model):
	user_confirmation_code_id = models.AutoField(primary_key=True)
	user_confirmation_code_numbere = models.PositiveSmallIntegerField(unique=True)
	validation_start_datetime = models.DateTimeField(auto_now_add=True)
	validation_end_datetime =models.DateTimeField(auto_now_add=True)
	user_id = models.ForeignKey(EcomUser, on_delete=models.CASCADE)


	def __str__(self):
		return str(self.user_confirmation_code_id)

class Product(models.Model):
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

	def clean(self):
		try:
			self.slug = str(self.product_name).replace(" ", "-").lower()
		except:
			self.slug = str(self.product_name).replace(" ", "-").lower()+str(random.random())[10:]
	def __str__(self):
		return str(self.product_id)

class ProductGalary(models.Model):
	pro_gal_id = models.AutoField(primary_key=True)
	Image =  models.ImageField(upload_to='media/product/%Y/%d/%b')
	product_id = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_images')


class Payment(models.Model):
	payment_method_id = models.AutoField(primary_key=True)
	payment_method_name =models.CharField(blank =True,max_length=50)
	payment_method_account_number = models.FloatField(max_length = 20)


	def __str__(self):
		return str(self.payment_method_id)


class Shipping(models.Model):
	shipping_id = models.AutoField(primary_key=True)
	shipping_address = models.CharField(blank = True, max_length = 150)
	city_name = models.CharField(blank= True, null=True, max_length = 20)
	post_code = models.PositiveSmallIntegerField()
	phone = models.CharField(max_length=14, unique=True)
	user_id = models.ForeignKey(EcomUser, on_delete=models.CASCADE)


class Order(models.Model):
	order_id = models.AutoField(primary_key=True)
	user_id = models.ForeignKey(EcomUser, on_delete=models.CASCADE, related_name="buyer")
	cupon_id = models.ForeignKey(Cupon, on_delete=models.CASCADE, null=True, blank=True)
	offer_id = models.ForeignKey(Offer, on_delete=models.CASCADE, null=True, blank=True)
	order_status_id = models.ForeignKey(OrderStatus, on_delete=models.CASCADE)
	fullorder_total_ammount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
	delivery_date = models.DateField()
	shipping_id = models.ForeignKey(Shipping, on_delete=models.CASCADE)
	af_user_id = models.ForeignKey(AffiliateUser, on_delete=models.CASCADE, related_name="reseller", null=True, blank=True) #Affiliate
	
	def __str__(self):
		return str(self.order_id)


class OrderDetails(models.Model):
	order_details_id = models.AutoField(primary_key=True)
	quantity = models.PositiveIntegerField()
	product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
	order_id = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="order")
	datetime = models.DateTimeField(auto_now_add=True)
	cupon_id = models.ForeignKey(Cupon, on_delete=models.CASCADE, null=True, blank=True)
	offer_id = models.ForeignKey(Offer, on_delete=models.CASCADE, null=True, blank=True)

	def __str__(self):
		return str(self.order_details_id)
	
class Invoice(models.Model):
	invoice_id = models.AutoField(primary_key=True)
	payment_method_id = models.ForeignKey(Payment, on_delete=models.CASCADE, related_name='payment', default=1)
	order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
	datetime = models.DateTimeField(auto_now_add = True)

	def __str__(self):
		return str(self.invoice_id)

class Review(models.Model):
	review_id = models.AutoField(primary_key=True)
	review_title = models.TextField(max_length=500)
	review = models.TextField()
	date = models.DateTimeField(auto_now_add=True)
	order_id = models.ForeignKey(Product, on_delete=models.CASCADE)

	def __str__(self):
		return str(self.post_name)




class ReviewReplay(models.Model):
	review_replay_id = models.AutoField(primary_key=True)
	review_replay_title = models.TextField(max_length=500)
	review_replay = models.TextField()
	date = models.DateTimeField(auto_now_add=True)
	review_id = models.ForeignKey(Review, on_delete=models.CASCADE)

	def __str__(self):
		return str(self.replay_user_name)


class WishList(models.Model):
	wishlist_id = models.AutoField(primary_key=True)
	user_id = models.ForeignKey(EcomUser, on_delete=models.CASCADE)
	product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
	datetime = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return str(self.wishlist_id)


class ReportType(models.Model):
	report_type_id = models.AutoField(primary_key=True)
	report_type_name = models.CharField(max_length=100)

	def __str__(self):
		return str(self.report_type_name)

class Report(models.Model):
	report_id = models.AutoField(primary_key=True)
	user_id = models.ForeignKey(EcomUser, on_delete=models.CASCADE)
	report_type = models.ForeignKey(ReportType, on_delete=models.CASCADE)
	report_comment = models.TextField()
	report_time = models.DateTimeField(auto_now_add=True)
	ammount = models.DecimalField(decimal_places=2, max_digits=10)
	store_id = models.ForeignKey(Store, on_delete=models.CASCADE)
	def __str__(self):
		return str(self.report_type)


class GiftCard(models.Model):
	gift_card_id = models.AutoField(primary_key=True)
	gift_card_name = models.TextField(max_length=500)
	gift_card_number = models.TextField(max_length=500)
	gift_card_pin = models.TextField(max_length=500)
	gift_card_exp_date = models.DateTimeField(auto_now_add=True)

class ShippingCost(models.Model):
	shipping_cost_id = models.AutoField(primary_key=True)
	shipping_city = models.CharField(max_length=255)
	shipping_cost = models.DecimalField(decimal_places=2, max_digits=10)


	def __str__(self):
		return str(self.shipping_city)+"  "+str(self.shipping_cost)

class ProductTrafficIp(models.Model):
	ip_id = models.AutoField(primary_key=True)
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	ip = models.CharField(max_length=50, unique=True)
	datetime = models.DateTimeField(auto_now_add=True)
	count = models.PositiveIntegerField()

	def __str__(self):
		return str(self.ip)