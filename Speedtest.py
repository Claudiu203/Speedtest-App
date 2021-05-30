from tkinter.constants import BOTTOM
from speedtest import Speedtest
import tkinter as tk

root = tk.Tk()

root.geometry("300x150")
root.configure(bg ='#56edc7')
root.title('Speedtest')

buton = tk.Button(font='Limelight',bg ='#56edc7',text="Check your speed",command= lambda:test())
buton.pack(side=BOTTOM)

def test():
    st = Speedtest()
    download = st.download()
    download = int(download // 10000)
    upload = st.upload()
    upload = int(upload // 10000)

    text1 = tk.Label(root,text="Download speed",font='Limelight',bg ='#56edc7')
    number1 = tk.Label(root,text = str(download/100) + ' mbps',font = 'Limelight',bg ='#56edc7')
    text2 = tk.Label(root,text="Upload speed",font='Limelight',bg ='#56edc7')
    number2 = tk.Label(root,text = str(upload/100) + ' mbps',font = 'Limelight',bg ='#56edc7')
    
    text1.pack()
    number1.pack()
    text2.pack()
    number2.pack()

root.mainloop()

