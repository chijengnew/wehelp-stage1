import urllib.request as request
import json
import csv

CHURL = "https://resources-wehelp-taiwan-b986132eca78c0b5eeb736fc03240c2ff8b7116.gitlab.io/hotels-ch"
ENURL = "https://resources-wehelp-taiwan-b986132eca78c0b5eeb736fc03240c2ff8b7116.gitlab.io/hotels-en"

def downloadjson(url):
    with request.urlopen(url) as response:
        data=response.read(). decode("utf-8")
        return json.loads(data)
    
def chineseaddress (address):
    data = address.find("區")
    if data <0:
        print("can't find district", address)
        return "", address
    district = address [3:data+1]
    street = address [data+1:]
    return district, street

def englishaddress (address):
    keywords = [
        " Dist.", " Dist,", " Dist ",
        " District", " district",
        " DIST.", " DIST,",
        " Pistrict",
        "DIST.", "DIST,",
        "Dist.", "Dist,",
        ]
    data = -1
    for keyword in keywords:
        data = address.find(keyword)
        if data >= 0:
            break
    if data < 0:
        data = address.find("Taipei")
    if data < 0:
        data = address.find("taipei")
    if data <0:
        print("cant't find distict", address)
        return address
    comma = address.rfind(",", 0, data)
    if comma < 0:
        return address
    return address[0:comma]

def main():
    chinesedata = downloadjson(CHURL)
    englishdata = downloadjson(ENURL)

    enindex = {}
    for hotel in englishdata["list"]:
        enindex[hotel["_id"]] = hotel

    hotelrows = []
    districtstats = {}
    for chhotel in chinesedata["list"]:
        hotelid = chhotel["_id"]
        chinesename = chhotel["旅宿名稱"]
        address = chhotel["地址"]
        phone = chhotel["電話或手機號碼"]

        try:
            roomcount = int(chhotel["房間數"])
        except (ValueError, TypeError):
            roomcount = 0

        district, chinesestreet = chineseaddress(address)

        enhotel = enindex.get(hotelid)
        if enhotel is not None:
            englishname = enhotel.get("hotel name", "")
            englishstreet = englishaddress(enhotel.get("address", ""))
        else:
            englishname = ""
            englishstreet = ""
        
        hotelrows.append([
            chinesename,
            englishname,
            chinesestreet,
            englishstreet,
            phone,
            roomcount,
        ])
        if district:
            if district not in districtstats:
                districtstats[district] = {"hotelcount": 0, "roomcount": 0}
            districtstats[district]["hotelcount"] += 1
            districtstats[district]["roomcount"] += roomcount

    with open("hotels.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        for row in hotelrows:
            writer.writerow(row)

    with open("districts.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        for district, stats in districtstats.items():
            writer.writerow([district, stats["hotelcount"], stats["roomcount"]])
main()