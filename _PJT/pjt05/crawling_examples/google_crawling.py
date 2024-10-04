from bs4 import BeautifulSoup
import requests

def crawling_basic():
    # 가져올 url 문자열로 입력
    url = 'https://www.google.co.kr/search?q=%ED%83%95%EC%88%98%EC%9C%A1&sca_esv=1d9a3a092ad1c62b&sxsrf=ADLYWIJ-JHskSWPbYJGuZ4p0Jr0nAB4klA%3A1728002995276&source=hp&ei=szv_ZrTxDsXP1e8P8tPlmQo&iflsig=AL9hbdgAAAAAZv9JwwNPHXJsBX79gwzEY-LGJ9UAduHj&ved=0ahUKEwj0ls_lwPOIAxXFZ_UHHfJpOaMQ4dUDCBg&uact=5&oq=%ED%83%95%EC%88%98%EC%9C%A1&gs_lp=Egdnd3Mtd2l6Igntg5XsiJjsnKEyCxAuGIAEGLEDGIMBMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAESP4WUK0EWM0OcAJ4AJABAZgBugGgAeIHqgEDMC44uAEDyAEA-AEBmAIIoALMBagCCsICBxAjGCcY6gLCAgsQABiABBixAxiDAcICBBAAGAPCAhEQLhiABBixAxjRAxiDARjHAcICCBAAGIAEGLEDwgIIEC4YgAQYsQPCAgUQLhiABJgDBZIHAzIuNqAH30A&sclient=gws-wiz'  

    # requests의 get함수를 이용해 해당 url로 부터 html이 담긴 자료를 받아옴
    response = requests.get(url)    


    # # 우리가 얻고자 하는 html 문서가 여기에 담기게 됨
    html_text = response.text
    print(html_text)

    with open('soup.txt', 'w', encoding='utf-8') as file:
        file.write(html_text)



crawling_basic()
