from django.contrib import admin
from .models import ( Offer, Slider, ProductColor, ProductSize, ProductPrice,
					ProductGalary, Brand, AffiliateUser, ColorSizeManager, Shipping, Store,
					Product, Catagory, SubCatagory, CatagoryManager, Cupon, GiftCard, OfferType,
					OrderStatus, OfferMaxAmount, Order, Payment, SecurityInfo, Report, ReportType,
					Review, ReviewReplay, WishList, Invoice, UserConfirmation, EcomUser, ShippingCost,
					OrderDetails,)
# Register your models here.

admin.site.register(Slider)
admin.site.register(Offer)
admin.site.register(ProductSize)
admin.site.register(ProductColor)
admin.site.register(ProductGalary)
admin.site.register(EcomUser)
admin.site.register(Store)
admin.site.register(ProductPrice)
admin.site.register(Brand)
admin.site.register(AffiliateUser)
admin.site.register(ColorSizeManager)
admin.site.register(Shipping)
admin.site.register(Product)
admin.site.register(Catagory)
admin.site.register(SubCatagory)
admin.site.register(CatagoryManager)
admin.site.register(Cupon)
admin.site.register(GiftCard)
admin.site.register(OfferType)
admin.site.register(OrderStatus)
admin.site.register(OfferMaxAmount)
admin.site.register(Order)
admin.site.register(Payment)
admin.site.register(SecurityInfo)
admin.site.register(Report)
admin.site.register(ReportType)
admin.site.register(Review)
admin.site.register(ReviewReplay)
admin.site.register(WishList)
admin.site.register(Invoice)
admin.site.register(UserConfirmation)
admin.site.register(ShippingCost)
admin.site.register(OrderDetails)


