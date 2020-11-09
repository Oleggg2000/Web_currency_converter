import requests
from bs4 import BeautifulSoup
import time

DOLLAR_RUB = "https://www.google.com/search?bih=722&biw=1536&hl=ru&sxsrf=ALeKk01lqOkDAg6udTZEDBYPbQOUEir9Pg%3A1604888973358&source=hp&ei=jamoX8OLE4bgUZrhtYgM&q=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&oq=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&gs_lcp=CgZwc3ktYWIQAzINCAAQsQMQgwEQRhCCAjICCAAyAggAMgIIADICCAAyAggAMgIIADICCAAyAggAMgIIADoECCMQJzoFCAAQsQM6CAgAELEDEIMBOggILhCxAxCDAToHCCMQ6gIQJzoHCC4Q6gIQJzoHCC4QJxCTAjoECC4QJzoFCC4QsQM6AgguOgkIIxAnEEYQggJQ2wxYl0dg2EloA3AAeACAAZ4BiAHpE5IBBDAuMTeYAQCgAQGqAQdnd3Mtd2l6sAEK&sclient=psy-ab&ved=0ahUKEwiDhqKptfTsAhUGcBQKHZpwDcEQ4dUDCAc&uact=5"
EURO_RUB = "https://www.google.com/search?bih=722&biw=899&hl=ru&sxsrf=ALeKk01zV5BDem8Dt5QqZidOnvVzoJlwpg%3A1604888983696&ei=l6moX9GHKov6UuiQiNAL&q=%D0%B5%D0%B2%D1%80%D0%BE+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&oq=%D0%B5%D0%B2%D1%80%D0%BE+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&gs_lcp=CgZwc3ktYWIQAzIMCAAQsQMQQxBGEIICMgIIADICCAAyAggAMgIIADICCAAyAggAMgIIADICCAAyAggAOgYIABAHEB46CAgAEAcQChAeOgQIABANUOnPNFi-2TRg0t00aABwAXgAgAHxAYgBuAWSAQUwLjMuMZgBAKABAaoBB2d3cy13aXrAAQE&sclient=psy-ab&ved=0ahUKEwiRr5uutfTsAhULvRQKHWgIAroQ4dUDCA0&uact=5"
JPY_RUB = "https://www.google.com/search?rlz=1C1EJFC_enRU884RU884&sxsrf=ALeKk03PMfCBnJjumxVOal8Wuo3pI-U7Hg%3A1604908800583&ei=APeoX9eQI5GMlwT12ajwAw&q=%D0%B9%D0%B5%D0%BD%D0%B0+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&oq=%D0%B9%D0%B5%D0%BD%D0%B0&gs_lcp=CgZwc3ktYWIQAxgAMgoIABCxAxAUEIcCMgcIABCxAxBDMgQIABBDMgQIABBDMgQIABBDMgIIADICCAAyAgguMgIIADICCAA6BAgAEEc6BQgAELEDOgUILhCxAzoHCC4QsQMQQzoICC4QsQMQgwE6DAgAELEDEEMQRhCCAlD3pANYrbEDYPK_A2gAcAJ4AIABngGIAeEEkgEDMC40mAEAoAEBqgEHZ3dzLXdpesgBCMABAQ&sclient=psy-ab"
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36'}

def check_currency(Currency):
    full_page = requests.get(Currency, headers=headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    convert = soup.findAll("span", {"class": "DFlfde SwHCTb"})
    return float((convert[0].text).replace(",", "."))