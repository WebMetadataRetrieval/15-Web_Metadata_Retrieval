from bs4 import  BeautifulSoup as soup
from urllib.request import urlopen as uReq

#Url who's information you want to scrape
url = 'https://www.flipkart.com/apple-iphone-11-purple-64-gb/p/itm2b8d03427ddac?pid=MOBFWQ6BTFFJKGKE&lid=LSTMOBFWQ6BTFFJKGKE6U3GXK&marketplace=FLIPKART&q=iphone&store=tyy&srno=s_1_1&otracker=search&otracker1=search&fm=SEARCH&iid=b2c41175-57f9-45a6-9805-79b248e51f47.MOBFWQ6BTFFJKGKE.SEARCH&ppt=sp&ppn=sp&ssid=uplwocddcw0000001618589951690&qH=0b3f45b266a97d70'
uClient = uReq(url)
data_info = uClient.read()

uClient.close()
page_soup=soup(data_info,"html.parser") #parsing of information

containers = page_soup.findAll("div",{"class":"aMaAEs"})
bb=containers[0].findAll("span",{"class":"B_NuCI"})
print("\n"+"*Product Title: "+bb[0].text+"\n")


contain= page_soup.findAll("div",{"class":"_2418kt"})
aa=contain[0].findAll("li",{"class":"_21Ahn-"})

print("*Product Description of the product is below: ")
for i in range(0,4):
  print(aa[i].text)

co= page_soup.findAll("div",{"class":"CXW8mj _3nMexc"}) 
print("\n"+"*Image description: "+ co[0].img["src"])

#..................................................END............................................#
