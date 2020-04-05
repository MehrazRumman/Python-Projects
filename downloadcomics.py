#! python3
# Downloads every single XKCD comic
import requests, os, bs4
url="http://xkcd.com" #starting url
os.makedirs("d:\\xkcd",exist_ok=True) # store comics in ./xkcd
while not url.endswith("#"):
    # todo : Download the page
    print("Downloading the page %s..." %url)
    res=requests.get(url)
    res.raise_for_status()
    s=bs4.BeautifulSoup(res.text)


    # todo: find the url of the comic image
    com=s.select("#comic img")
    if com==[]:
        print("Couldn't find comic image")
    else:
        comurl="http:"+com[0].get("src")


    # todo:Download the image.
    print("downloading the image %s..." %(comurl))
    res=requests.get(comurl)
    res.raise_for_status()

    # todo : save the image to ./xkcd
    imgf=open(os.path.join("d:\\xkcd",os.path.basename(comurl)),"wb")
    for chunk in res.iter_content(100000):
        imgf.write(chunk)
    imgf.close()

    # todo: get the prev button's url .
    prvl=s.select('a[rel="prev"]')[0]
    url="http://xkcd.com"+prvl.get("href")


print("KHELA shesH")
