import time
from plyer import notification
 
 
if __name__=="__main__":

    while True:    
 
        notification.notify(
            title = "BLINK Please",
            message= "Avoid Dryness In Your eye.",
            app_icon= "D:\Projects\Eye Blink Notifier\eye.ico",
           
            # displaying time
            timeout=2
)
        # waiting time
        time.sleep(60)