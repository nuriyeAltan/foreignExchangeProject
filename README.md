# 📊 Foreign Exchange Tracker

A simple real-time financial data tracking system built with Python.  
This project uses a Publisher-Subscriber architecture to distribute live currency and commodity prices.

---

## 🚀 Features
- Real-time financial data publishing using ZeroMQ
- Subscription-based filtering (USD, EUR, GOLD, SILVER)
- Lightweight and modular structure
- Easy to extend with GUI or visualization tools

---

## 🛠️ Technologies Used
- Python
- ZeroMQ (zmq)
- yfinance

---

## 📂 Project Structure
foreignExchangeProject/
│
├── publisher.py     # Sends financial data (Publisher)
├── subscriber.py    # Receives and filters data (Subscriber)
├── README.md
└── requirements.txt

---

## ⚙️ How It Works
1. The publisher fetches live financial data using `yfinance`
2. Data is sent through a ZeroMQ PUB socket
3. Subscriber connects and filters specific assets
4. Only selected data (e.g., USD, GOLD) is displayed

---

## ▶️ How to Run

### 1. Install dependencies
pip install -r requirements.txt

### 2. Run Publisher
python publisher.py

### 3. Run Subscriber
python subscriber.py

---

## 📌 Example Output
GUMUS 28.45
USD 32.10
EUR 35.20

---

## 🎓 Academic Context
This project was developed as part of a Computer Networks course.  
It demonstrates real-time communication using the Publisher-Subscriber model with ZeroMQ.

---

## 🔮 Future Improvements
- GUI interface using Tkinter
- Live chart visualization
- Multiple subscriber support
- Historical data storage

---

## 👩‍💻 Author
Nuriye Altan