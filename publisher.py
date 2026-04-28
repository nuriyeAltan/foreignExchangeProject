import zmq
import time
import yfinance as yf

context = zmq.Context()
socket = context.socket(zmq.PUB)

socket.bind("tcp://*:5555")

tickers = {
    "USD": "TRY=X",    
    "EUR": "EURTRY=X", 
    "GOLD": "GC=F",   
    "SILVER": "SI=F"    
}

print("PUBLISHER: Data is being retrieved and distributed...")

while True:
    for name, ticker_symbol in tickers.items():
        try:
            
            rate = yf.Ticker(ticker_symbol)
            data = rate.history(period="1d")

            if not data.empty:
                price = data['Close'].iloc[-1]
                message = f"{name} {price:.2f}"

                socket.send_string(message)
                print(f"Submitted Successfully -> {message}")
            else:
                print(f"Warning: Data returned empty for {name}.")
                
        except Exception as e:
            
            print(f"Error: Could not retrieve data for {name}. Details: {e}")
            continue
            
    print("-" * 30)
    time.sleep(10)