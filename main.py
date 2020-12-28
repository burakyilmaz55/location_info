import urllib.request
import urllib
import socket
import geocoder


url = input("Website url: ")

ip2 = url.replace('https://', '')
ip = socket.gethostbyname(ip2)
g = geocoder.ip(ip)
if True:

    print(
      f"Websiteniz çalışır durumdadır\n"
      f"IP: {ip}\n"
      f"Lokasyon: {g.latlng}\n"
      f"Şehir: {g.city}\n"
      f"Posta Kodu: {g.postal}\n"
      f"Adres: {g.address} "
      )
else:
    print("Websiteniz çalşır durumda değildir.")