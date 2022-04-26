import win10toast, threading, time
def start(duration, message):
    new_thread = threading.Thread(target=_toast, args=(duration,message))
    new_thread.start()
    
def _toast(duration, message):
    while duration > 0:
        time.sleep(1)
        duration -= 1
    toaster = win10toast.ToastNotifier()
    
    con=message
    if isinstance(message, list):
        con=""
        for item in message:
            con+=item+" "
        con.rstrip()
    toaster.show_toast(title="lex-shell toaster", msg=con, duration=3)
        
    