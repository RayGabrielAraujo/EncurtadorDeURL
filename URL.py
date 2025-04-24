
import pyshorteners

link = input("\nEnter your link : ")

short = pyshorteners.Shortener()
x = short.tinyurl.short(link)

print("\nAqui está o link encurtado: "+x)