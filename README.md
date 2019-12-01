# COBOT
Cobot (Compass Bot) merupakan bot yang berfungsi untuk mengirimkan notifikasi ketersediaan stok produk sepatu compass melalui telegram

# USAGE
1. Clone: git clone https://github.com/sonadztux/cobot.git
2. Create virtual environment: python -m venv env or virtualenv env
3. Activate the virtual environment: source env/bin/activate
4. Install requirement depedencies: (env) pip install -r requirements.txt
5. Set the configuration:
    echo "export URL_API_BASE=localhost/api.php" >> env/.config
    echo "export PRODUCT_URL_BASE=https://sepatucompass.com/collections/all/products/" >> env/.config
    echo "export BOT_TOKEN=LALALAYEYEYE" >> env/.config
    echo "export CHAT_ID=1928192801" >> env/.config
6. Run: python app.py
