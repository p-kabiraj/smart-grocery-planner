# Smart Grocery Planner

A Django-based web application that helps users compare grocery prices across multiple online platforms to find the best deals and save money on their shopping.

## 🌟 Features

- **Price Comparison**: Compare prices for grocery items across popular platforms like Blinkit, Zepto, Big Basket, Walmart, and Amazon Fresh
- **Smart Search**: Search for products with intelligent query handling and suggestions
- **Cheapest Highlight**: Automatically highlights the lowest price option with visual indicators
- **Direct Links**: One-click access to purchase from the selected platform
- **Responsive Design**: Works seamlessly on desktop and mobile devices
- **Admin Panel**: Easy management of products and prices through Django admin

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- Django 5.2+
- SQLite (default) or PostgreSQL/MySQL

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/p-kabiraj/smart-grocery-planner.git
   cd smart-grocery-planner
   ```

2. **Create virtual environment**
   ```bash
   python -m venv .venv
   # On Windows
   .venv\Scripts\activate
   # On macOS/Linux
   source .venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install django
   ```

4. **Run database migrations**
   ```bash
   python manage.py migrate
   ```

5. **Populate sample data**
   ```bash
   python manage.py populate_db
   ```

6. **Start the development server**
   ```bash
   python manage.py runserver
   ```

7. **Open your browser**
   ```
   http://127.0.0.1:8000
   ```

## 📱 Usage

1. Navigate to the Price Comparison section
2. Search for grocery items (e.g., "Milk", "Bread", "Apples")
3. View price comparisons across platforms
4. Click on the cheapest option or any platform link to purchase

## 🏗️ Project Structure

```
smart-grocery-planner/
├── core/                    # Main Django app
│   ├── models.py           # Product, Platform, Price models
│   ├── views.py            # Search and comparison logic
│   ├── admin.py            # Admin interface configuration
│   └── management/commands/populate_db.py  # Data seeding
├── pricewise/              # Django project settings
├── templates/              # HTML templates
├── static/                 # CSS, JS, images
├── db.sqlite3              # SQLite database
└── manage.py               # Django management script
```

## 🛠️ Technologies Used

- **Backend**: Django 5.2
- **Database**: SQLite (development) / PostgreSQL (production)
- **Frontend**: HTML5, CSS3, JavaScript
- **Styling**: Custom CSS with responsive design

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📞 Contact

For questions or suggestions, please open an issue on GitHub.

---

**Save money on groceries with Smart Grocery Planner! 🛒💰**
