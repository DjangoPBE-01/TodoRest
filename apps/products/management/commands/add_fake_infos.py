import random
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from django.utils import timezone
from faker import Faker
from apps.products.models import Order, OrderItem, Product  

User = get_user_model()


class Command(BaseCommand):
    help = "Modellarga faker yordamida 100 tadan soxta ma'lumot qo'shadi"

    def handle(self, *args, **options) -> None:
        fake: Faker = Faker()

        self.stdout.write(
            self.style.WARNING("Ma'lumotlar bazasini to'ldirish boshlandi...")
        )

        # 1. Foydalanuvchilarni tekshirish va yaratish
        # Chunki Order uchun kamida bitta foydalanuvchi bo'lishi shart
        users: list = list(User.objects.all())
        if not users:
            self.stdout.write(
                "Foydalanuvchilar topilmadi, 10 ta soxta foydalanuvchi yaratilmoqda..."
            )
            for _ in range(10):
                u: User = User.objects.create_user(
                    username=fake.user_name(),
                    email=fake.email(),
                    password="password123",
                )
                users.append(u)

        # 2. 100 ta Product yaratish
        products: list[Product] = []
        for _ in range(100):
            product: Product = Product.objects.create(
                name=fake.catch_phrase()[:128],
                price=round(random.uniform(10.0, 1000.0), 2),
                is_active=fake.boolean(chance_of_getting_true=85),
            )
            products.append(product)
        self.stdout.write(
            self.style.SUCCESS("100 ta Product muvaffaqiyatli yaratildi.")
        )

        # 3. 100 ta Order yaratish
        orders: list[Order] = []
        for _ in range(100):
            order: Order = Order.objects.create(
                name=f"Order #{fake.random_number(digits=5)}",
                user=random.choice(users),
                created_at=timezone.make_aware(
                    fake.date_time_this_year()
                ),  # datetime maydoni uchun vaqt zonasi bilan
            )
            orders.append(order)
        self.stdout.write(
            self.style.SUCCESS("100 ta Order muvaffaqiyatli yaratildi.")
        )

        # 4. 100 ta OrderItem yaratish
        for _ in range(100):
            OrderItem.objects.create(
                order=random.choice(orders),
                product=random.choice(products),
                quantity=random.randint(1, 10),
            )
        self.stdout.write(
            self.style.SUCCESS("100 ta OrderItem muvaffaqiyatli yaratildi.")
        )

        self.stdout.write(
            self.style.SUCCESS(
                "Barcha modellar 100 tadan ma'lumot bilan to'ldirildi! 🎉"
            )
        )
