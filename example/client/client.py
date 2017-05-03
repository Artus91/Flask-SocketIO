import websocket
import _thread
import time

ws = None


def on_message(ws, message):
    print("msg {}".format(message))


def on_error(ws, error):
    print("error {}".format(error))


def on_close(ws):
    print("### closed ###")


def on_open(ws):
    def run(*args):
        for i in range(3):
            time.sleep(1)
            ws.send("Hello %d" % i)
        time.sleep(1)
        ws.close()
        print("thread terminating...")

    _thread.start_new_thread(run, ())


if __name__ == "__main__":
    import websocket

    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("ws://localhost:5000",
                                on_message=on_message,
                                on_open=on_open,
                                on_error=on_error,
                                on_close=on_close)
    ws.run_forever(sslopt={"check_hostname": False})
