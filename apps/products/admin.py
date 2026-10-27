from django.contrib import admin
from .models import Order, OrderItem, Product, Article


# 1. Buyurtma ichida unga tegishli tovarlarni jadval qilib ko'rsatish
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1  # Qo'shimcha yangi tovar qo'shish uchun bo'sh qator soni


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # Ro'yxatda nimalar ko'rinsin
    list_display = ["id","name", "price", "is_active"]
    # O'ng tomondan saralash (filtr)
    list_filter = ["is_active"]
    # Ism bo'yicha qidiruv
    search_fields = ["name"]


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    # Ro'yxatda nimalar ko'rinsin
    list_display = ["name", "user", "created_at"]
    # Sanaga qarab filtrlar
    list_filter = ["created_at"]
    # Buyurtma ichiga tovarlar jadvalini ulaymiz
    inlines = [OrderItemInline]


# Buyurtma tovarlarini alohida ko'rish uchun oddiy panel
@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ["order", "product", "quantity"]
    

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ["name", "owner", "created_at"]
