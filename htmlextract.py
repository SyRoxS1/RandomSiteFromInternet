from bs4 import BeautifulSoup

def extractTxtFromHtml(htmldata):
    html_content = htmldata

    # Parse the HTML content
    soup = BeautifulSoup(html_content, 'html.parser')
    alltxt = soup.get_text()

    return alltxt