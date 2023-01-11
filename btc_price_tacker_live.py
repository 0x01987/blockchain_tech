from tkinter import *
import requests
from datetime import datetime


# function that is used to track the price of the bitcoin 
def bitcoinTracker():
    response = requests.get(url="https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD").json()
    bitcoinPrice = response["USD"]
   
    #priceINR = (int)(bitcoinPrice * 74.74 )
    currentTime = datetime.now().strftime("%H:%M:%S")

    bitcoinPriceLabel.config(text=str(bitcoinPrice) + '$\n\n')
    currentTimeLabel.config(text="Updated at: " + currentTime)

    object_root.after(1000, bitcoinTracker)



object_root = Tk()
object_root.geometry('520x520')
object_root.title('Bitcoin Price Tracker') # this is the title of the application Bitcoin Price Tracker
iconPhoto = PhotoImage(file='C:/Users/db/Documents/python_scripts/Bitcoin-BTC-icon.png') 

object_root.iconphoto(False, iconPhoto) # this is the icon of the application Bitcoin Price Tracker

myLabel = Label(object_root, text="Welcome To The BTC Price Tracker", fg='red', font="poppins 20 ")
myLabel.pack()

photo = PhotoImage(file='C:/Users/db/Documents/python_scripts/Bitcoin-BTC-icon.png')
photoLabel = Label(image=photo)
photoLabel.pack()

bitcoinHeading = Label(object_root, text='Current Bitcoin Price', fg='Green', font="poppins 20 bold")
bitcoinHeading.pack(pady=25)
bitcoinPriceLabel = Label(object_root, fg='Green', font="poppins 18 bold")
bitcoinPriceLabel.pack(pady=25)


currentTimeLabel = Label(object_root, font="poppins 15")
currentTimeLabel.pack(pady=25)
bitcoinTracker()



Button(object_root, text='Refresh', font="poppins 10 bold", bg='black', fg='white', command=bitcoinTracker).pack()

object_root.mainloop()