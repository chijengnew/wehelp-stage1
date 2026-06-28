import urllib.request as request
from bs4 import BeautifulSoup
import csv

BASE = "https://www.ptt.cc"
STARTURL = "https://www.ptt.cc/bbs/Steam/index.html"
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.5 Safari/605.1.15"


def downloadhtml(url):
    headers = {"User-Agent": UA}
    req = request.Request(url, headers=headers)
    with request.urlopen(req) as response:
        return response.read().decode("utf-8")


def parselist(html):
    soup = BeautifulSoup(html, "html.parser")
    articles = []
    for item in soup.select("div.r-ent"):
        titlea = item.select_one("div.title a")
        if titlea is None:
            continue
        title = titlea.text.strip()
        articleurl = BASE + titlea["href"]

        nrec = item.select_one("div.nrec")
        if nrec is None:
            likecount = ""
        else:
            likecount = nrec.text.strip()

        articles.append([title, likecount, articleurl])

    prevurl = ""
    for a in soup.select("a.btn.wide"):
        if "上頁" in a.text:
            prevurl = BASE + a["href"]
            break

    return articles, prevurl


def parsetime(html):
    soup = BeautifulSoup(html, "html.parser")
    for metaline in soup.select("div.article-metaline"):
        tag = metaline.select_one("span.article-meta-tag")
        value = metaline.select_one("span.article-meta-value")
        if tag is not None and tag.text.strip() == "時間":
            return value.text.strip()
    return ""


def main():
    allarticles = []
    url = STARTURL

    for page in range(3):
        print("page", page + 1, ":", url)
        html = downloadhtml(url)
        articles, prevurl = parselist(html)
        allarticles.extend(articles)
        url = prevurl

    rows = []
    for article in allarticles:
        title = article[0]
        likecount = article[1]
        articleurl = article[2]

        try:
            articlehtml = downloadhtml(articleurl)
            publishtime = parsetime(articlehtml)
        except Exception as e:
            print("error", articleurl, e)
            publishtime = ""

        rows.append([title, likecount, publishtime])

    with open("articles.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        for row in rows:
            writer.writerow(row)

    print("done,", len(rows), "articles")
main()