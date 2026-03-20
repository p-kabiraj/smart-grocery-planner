from django.core.management.base import BaseCommand
from core.models import Product, Platform, Price


class Command(BaseCommand):
    help = 'Populate database with sample products and prices'

    def handle(self, *args, **options):
        # Create platforms
        platforms = [
            ('Blinkit', 'https://blinkit.com'),
            ('Zepto', 'https://zepto.com'),
            ('Big Basket', 'https://bigbasket.com'),
            ('Walmart', 'https://walmart.com'),
            ('Amazon Fresh', 'https://amazon.in'),
        ]

        platform_objs = {}
        for name, url in platforms:
            platform, created = Platform.objects.get_or_create(
                name=name,
                defaults={'link': url}
            )
            platform_objs[name] = platform
            if created:
                self.stdout.write(f"✓ Created platform: {name}")

        # Create products
        products_data = [
            ('Milk', ['Blinkit', 'Zepto', 'Big Basket', 'Walmart', 'Amazon Fresh']),
            ('Bread', ['Blinkit', 'Zepto', 'Big Basket', 'Walmart']),
            ('Butter', ['Big Basket', 'Walmart', 'Amazon Fresh']),
            ('Eggs', ['Blinkit', 'Zepto', 'Big Basket', 'Walmart', 'Amazon Fresh']),
            ('Cheese', ['Big Basket', 'Walmart', 'Amazon Fresh']),
            ('Yogurt', ['Blinkit', 'Zepto', 'Big Basket']),
            ('Rice', ['Blinkit', 'Zepto', 'Big Basket', 'Walmart', 'Amazon Fresh']),
            ('Dal', ['Big Basket', 'Walmart', 'Amazon Fresh']),
            ('Oil', ['Blinkit', 'Zepto', 'Big Basket', 'Walmart']),
            ('Sugar', ['Blinkit', 'Big Basket', 'Walmart', 'Amazon Fresh']),
            ('Coffee', ['Blinkit', 'Zepto', 'Big Basket', 'Walmart']),
            ('Tea', ['Blinkit', 'Zepto', 'Big Basket', 'Walmart', 'Amazon Fresh']),
            ('Tomato', ['Blinkit', 'Zepto', 'Big Basket', 'Walmart']),
            ('Onion', ['Blinkit', 'Zepto', 'Big Basket', 'Walmart', 'Amazon Fresh']),
            ('Potato', ['Blinkit', 'Zepto', 'Big Basket', 'Walmart']),
        ]

        # Create prices
        price_ranges = {
            'Milk': (40, 80),
            'Bread': (20, 50),
            'Butter': (150, 250),
            'Eggs': (30, 70),
            'Cheese': (100, 300),
            'Yogurt': (20, 60),
            'Rice': (40, 100),
            'Dal': (60, 150),
            'Oil': (100, 200),
            'Sugar': (30, 60),
            'Coffee': (150, 400),
            'Tea': (50, 150),
            'Tomato': (20, 50),
            'Onion': (20, 50),
            'Potato': (20, 40),
        }

        for product_name, platform_names in products_data:
            product, created = Product.objects.get_or_create(name=product_name)
            if created:
                self.stdout.write(f"✓ Created product: {product_name}")

            # Add prices for each platform
            min_price, max_price = price_ranges.get(product_name, (50, 150))
            price_step = (max_price - min_price) / len(platform_names)

            for idx, platform_name in enumerate(platform_names):
                platform = platform_objs[platform_name]
                price = min_price + (price_step * idx)

                price_obj, created = Price.objects.get_or_create(
                    product=product,
                    platform=platform,
                    defaults={'price': price}
                )
                if created:
                    self.stdout.write(f"  ₹ {product_name} on {platform_name}: ₹{price:.2f}")

        self.stdout.write(self.style.SUCCESS('✓ Database populated successfully!'))
