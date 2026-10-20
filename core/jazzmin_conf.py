JAZZMIN_SETTINGS = {
    # 1. Sarlavhalar va Brending
    "site_title": "MegaShop Admin",       # Brauzer tabidagi yozuv
    "site_header": "MegaShop",           # Kirish (Login) sahifasidagi asosiy yozuv
    "site_brand": "MegaShop Boshqaruvi", # Panel ichidagi brend nomi
    "site_logo": "images/logo.png",      # Sayt logotipi (static/images/ ichida bo'lishi kerak)
    "welcome_sign": "Hush kelibsiz! Tizimga kirish uchun login va parolingizni kiriting.",
    "copyright": "MegaShop LLC © 2026",  # Footer qismidagi yozuv

    # 2. Qidiruv va Interfeys
    # "search_model": ["auth.User", "blog.Post"], # Global qidiruv paneli qaysi modellardan qidirsin
    "user_avatar": "avatar",             # Agar profilingizda rasm bo'lsa, uni ko'rsatish (ixtiyoriy)

    # 3. Chap menyu (Sidebar) sozlamalari
    "show_sidebar": True,                # Sidebar ko'rinib tursinmi?
    "navigation_expanded": True,         # Menyular boshida ochilgan holatda tursinmi?
    "hide_apps": ["token_blacklist"],                     # Berkitmoqchi bo'lgan ilovalaringiz
    "hide_models": [],                   # Berkitmoqchi bo'lgan modellaringiz
    
    # Modellarga chiroyli ikonkalar berish (FontAwesome 5 ikonkalaridan foydalaniladi)
    "icons": {
        "accounts.CustomUser": "fas fa-user-tie",
        "todo.Category": "fas fa-tags",
        "todo.Todo": "fas fa-tasks",
    },
    
    # Ikonka topilmaganda standart qaysi ikonka qo'yilsin
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-circle",

    # 4. Yuqori menyu (Top Menu) va Tezkor havolalar
    "topmenu_links": [
        {"name": "Bosh sahifa", "url": "admin:index", "permissions": ["auth.view_user"]},
        {"name": "Saytga o'tish", "url": "/", "new_window": True}, # Tashqi havola
    ],

    # 5. UI formatlari (Ma'lumotlar tahrirlash oynasi qanday ko'rinsin?)
    # "vertical_tabs", "horizontal_tabs", "collapsible", "carousel" turlaridan birini tanlash mumkin
    "changeform_format": "horizontal_tabs", 
}
