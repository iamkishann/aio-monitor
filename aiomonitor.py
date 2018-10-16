import requests
from time import sleep
from bs4 import BeautifulSoup as bs4
from slackclient import SlackClient
from time import gmtime, strftime
from datetime import datetime
import os
from slackclient import SlackClient
import multiprocessing as mp



print ("##############################################################")
print ("        AIO_Monitor  DEVELOPED BY @IAMKISHANN ©.              ")
print ("##############################################################")



def nakedcph():
    s = requests.Session()
    requrl = "https://www.nakedcph.com/new-arrivals/s/6"
    resp = s.get(requrl)
    sleep(4)
    soup = bs4(resp.text, 'lxml')
    nakedlinks = []

    for line in soup.find_all("a", class_="card "):
        nakednew_link = "https://www.nakedcph.com" + line.get('href')
        nakedlinks.append(nakednew_link)
    return nakedlinks

def nakedrefresh():
    main = True
    while (main == True):
        list1 = nakedcph()
        sleep(10)
        list2 = nakedcph()


        nakednewlink = list(set(list2).difference(list1))
        
        if nakednewlink != []:
            post_message = slackmessage(nakednewlink)
            print(datetime.now().strftime('%T') + " FOUND NEW PRODUCT on nakedcph. ")
            

        main = True
        print(datetime.now().strftime('%T') + " No new products on nakedcph. ")


def slamjam():
    s = requests.Session()
    requrl = "https://www.slamjamsocialism.com/sneakers/"
    resp = s.get(requrl)
    sleep(4)
    soup = bs4(resp.text, 'lxml')
    slamjamlinks = []

    for line in soup.find_all("a", class_="product_img_link"):
        slamjamnew_link = line.get('href')
        slamjamlinks.append(slamjamnew_link)
    return slamjamlinks
    

def slamjamrefresh():
    main = True
    while (main == True):
        list1 = slamjam()
        sleep(10)
        list2 = slamjam()
        slamjamnewlink = list(set(list2).difference(list1))

        
        if slamjamnewlink != []:
            post_message = slackmessage(slamjamnewlink)
            print(datetime.now().strftime('%T') + " FOUND NEW PRODUCT on slamjamsocialism. ")
            

        main = True
        print(datetime.now().strftime('%T') + " No new products on slamajamsocialism. ")
        

def nike():
    s = requests.Session()
    requrl = "https://www.nike.com/launch/"
    resp = s.get(requrl)
    sleep(4)
    soup = bs4(resp.text, 'lxml')
    nikelinks = []

    for line in soup.find_all("a", class_="js-card-link card-link d-sm-b"):
        nikenew_link = "https://www.nike.com" + line.get('href')
        nikelinks.append(nikenew_link)
    return nikelinks

def nikerefresh():
    main = True
    while (main == True):
        list1 = nike()
        sleep(10)
        list2 = nike()
        nikenewlink = list(set(list2).difference(list1))
        
        if nikenewlink != []:
            post_message = slackmessage(nikenewlink)
            print(datetime.now().strftime('%T') + " FOUND NEW PRODUCT/PASS. ")
            
        main = True
        print(datetime.now().strftime('%T') + " No new product/pass/launches on nike launch. ")



def sivas():
    s = requests.Session()
    requrl = "https://www.sivasdescalzo.com/en/lifestyle/sneakers"
    resp = s.get(requrl)
    sleep(4)
    soup = bs4(resp.text, 'lxml')
    sivaslinks = []

    for line in soup.find_all("a", class_="icon fav link-wishlist"):
        sivasnew_link = line.get('href')
        sivaslinks.append(sivasnew_link)
        
    return sivaslinks

def sivasrefresh():
    main = True
    while (main == True):
        list1 = sivas()
        sleep(10)
        list2 = sivas()
        sivasnewlink = list(set(list2).difference(list1))
        
        if sivasnewlink != []:
            post_message = slackmessage(sivasnewlink)
            print(datetime.now().strftime('%T') + " FOUND NEW PRODUCT on Sivas. ")
            
        main = True
        print(datetime.now().strftime('%T') + " No new product on sivasdescalzo ")


def slackmessage(link):
    link = link
    sc = SlackClient("xoxb") #API TOKEN HERE 

    sc.api_call(
    "chat.postMessage",
    channel="#biip-nike", #CHANNEL NAME
    username="nikebot",
    icon_url="https://img.talkandroid.com/uploads/2016/02/SNKRS_App_Icon.png",
    text= link
    )

def main():
        p1 = mp.Process(target = nakedrefresh)
        p2 = mp.Process(target = nikerefresh)
        p3 = mp.Process(target = slamjamrefresh)
        p4 = mp.Process(target = sivasrefresh)

        p1.start()
        print(datetime.now().strftime('%T') + " started nakedcphrefresh")
        p2.start()
        print(datetime.now().strftime('%T') + " started nikerefresh")
        p3.start()
        print(datetime.now().strftime('%T') + " started slamjamrefresh")
        p4.start()
        print(datetime.now().strftime('%T') + " started sivasrefresh")



main()


