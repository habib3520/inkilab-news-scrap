import bs4
import requests
import csv

URL_LINK = 'all_link_catagory_wise.csv'
CSV_LINK = 'k.csv'


def append_to_csv(row):
    global CSV_LINK
    with open(CSV_LINK,mode='a',newline='',encoding='utf-8') as unit_new_article:
            news_article_writer = csv.writer(unit_new_article, delimiter =',',quotechar ='"',quoting = csv.QUOTE_MINIMAL)
            news_article_writer.writerow(row)

    pass

def get_tittle_and_content(url):
    BASE_URL = url

    try:
        page = requests.get(BASE_URL)
    except:
        pass

    # date = "15/10/2022 \n"

    soup = bs4.BeautifulSoup(page.content, 'html.parser')

    # print(date)

    title_div = soup.find("article")
    newsTitle = title_div.find_all("h1")[0].getText()
    print(newsTitle)
    det_div = soup.find("article")
    news_det = det_div.find_all("h5")[0].getText()
    print(news_det)
    article_text = soup.find("div",{"id": "ar_news_content"})
    all_paragraphs = article_text("p")
    news_content = ""
    for paragraph in all_paragraphs:
        news_content += paragraph.getText()

    input_array = [news_det,newsTitle,'\n',news_content,'\n']
    append_to_csv(input_array)



    pass





def last_final():
    with open(URL_LINK,encoding='utf-8') as unit_url_csv:
        readCSV = csv.reader(unit_url_csv)
        i=0
        for row in readCSV:
            print(i)
            try:
                get_tittle_and_content(row[0])
            except:
                pass
            i += 1

last_final()