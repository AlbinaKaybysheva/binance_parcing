import websocket
import ujson
import threading


def on_message(ws, message):
    data = ujson.loads(message)
    thread = threading.Thread(target=process_price, args=(data,))
    thread.start()

def on_error(ws, error):
    print(f"Received error: {error}")

def on_close(ws):
    print("Connection closed")

def on_open(ws):
    subscribe_message = {
        "method": "SUBSCRIBE",
        "params":[
            "xrpusdt@ticker_1h",
        ],
        "id": 1
    }
    ws.send(ujson.dumps(subscribe_message))

def process_price(data):
    """Checks if last price in message data is more than 1% less
    than 1 hour maximum price and returns meassage to terminal in this case.
    """
    if 'c' in data:
        price_diff = float(data["c"]) / float(data["h"])
        if price_diff <= 0.99:
            print("Current price is more than 1% less than 1 hour maximum price")

if __name__ == "__main__":
    ws = websocket.WebSocketApp(
        url="wss://stream.binance.com:9443/ws/xrpusdt@ticker_1h",
        on_open=on_open,
        on_message=on_message,
        on_error=on_error,
    )
    ws.run_forever()
