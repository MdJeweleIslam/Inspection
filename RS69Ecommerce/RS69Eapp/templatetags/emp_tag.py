from django import template
from django.utils.html import format_html

register = template.Library()
from RS69Eapp.models import Product, ProductColor, ProductSize, Catagory, SubCatagory, ProductPrice
@register.filter(name='product_color')
def product_color(value):
	em = ProductColor.objects.filter(product_cate=SubCatagory.objects.get(sub_catagory_name=value))
	# color_ = []
	# for e_ in em:
	# 	color_.append(e_.color_name)
	# return color_
	"""
	{{each_p.product_brand_manager_id.product_id.catagory_manager_id.sub_catagory_id.sub_catagory_name|product_color | unordered_list}}
	"""
	color_ = ""
	for e_ in em:
		li = '<li class="'+str(e_.color_name)+'"></li>'
		color_+=li
	return format_html(color_)


@register.filter(name='product_size')
def product_size(value):
	ps = ProductSize.objects.filter(product_cate=SubCatagory.objects.get(sub_catagory_name=value))
	size_ = ""
	for s_ in ps:
		li = '<li>'+str(s_.size_val)+'</li>'
		size_+=li
	return format_html(size_)

@register.filter(name='product_price')
def product_price(value):
	print(value)
	ps = ProductPrice.objects.filter(product_price_id = value)
	if len(ps) != 0:
		price_html = str(ps[0].offer_price)+" <del>"+ str(ps[0].price) +"</del>"
		return format_html(price_html)
	else:
		price_html = str(1)+" <del>"+ str(1) +"</del>"
		return format_html(price_html)

