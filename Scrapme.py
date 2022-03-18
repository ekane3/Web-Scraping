"""
Project : Scrapme
Description : Scraping a static web page
Author : Emile EKANE
"""
import requests
from bs4 import BeautifulSoup
import streamlit as st

def load_page(url):
    """
    Load a web page
    """
    page = requests.get(url)

    return BeautifulSoup(page.content, 'html.parser')




def main():
    URL = 'https://en.wikipedia.org/wiki/Natural_language_processing'
    soup = load_page(URL)

    st.write("""
    # Scraping a static web page
    This is a simple web scraper that scrapes a static web page.
    """)
    
    st.write("""
    The page we are about to scrape is : {}
    """.format(URL)
    )

    st.write("""
        We are interested in the paragraph tags inside the main content div of class **"mw-parser-output"**.
    """)

    # Get the main content div
    main_content = soup.find('div', class_='mw-parser-output')

    # Get all the paragraph tags inside the main content div
    paragraphs = main_content.find_all('p')

    # Create two columns, ne column for the paragraph and the code block
    col1, col2 = st.columns(2)

    with col1:
        st.header('Paragraphs')
        st.write("""
        #### Scraping the paragraphs...
        """)
        st.write("""
        The scraped paragraphs are : ===>
        """)
         #for paragraph in paragraphs:
        #    st.write(paragraph.text)

        # We are interested in the paragraph tags inside the main content div of class "mw-parser-output"
        main_container = soup.findAll('div',{'class':'mw-parser-output'})

        for content in main_container:
            count = 1
            for paragraph in content.findAll('p'):
                st.write(""" P-**{})** {}""".format(count,paragraph.text))
                count+=1


    with col2:
        st.header('Code block')
        st.write("""
        The scraped code block is : ===>
        """)
        code = '''
import requests
from bs4 import BeautifulSoup
import streamlit as st

def load_page(url):
    """
    Load a web page
    """
    page = requests.get(url)

    return BeautifulSoup(page.content, 'html.parser')

def main():
    URL = 'https://en.wikipedia.org/wiki/Natural_language_processing'
    soup = load_page(URL)

    st.write("""
    # Scraping a static web page
    This is a simple web scraper that scrapes a static web page.
    """)
    
    st.write("""
    The page we are about to scrape is : {}
    """.format(URL)
    )

    st.write("""
        We are interested in the paragraph tags inside the main content div of class **"mw-parser-output"**.
    """)

    # Get the main content div
    main_content = soup.find('div', class_='mw-parser-output')

    # Get all the paragraph tags inside the main content div
    paragraphs = main_content.find_all('p')

    # Create two columns, ne column for the paragraph and the code block
    col1, col2 = st.columns(2)

    with col1:
        st.header('Paragraphs')
        st.write("""
        #### Scraping the paragraphs...
        """)
        st.write("""
        The scraped paragraphs are : ===>
        """)
         #for paragraph in paragraphs:
        #    st.write(paragraph.text)

        # We are interested in the paragraph tags inside the main content div of class "mw-parser-output"
        main_container = soup.findAll('div',{'class':'mw-parser-output'})

        for content in main_container:
            count = 1
            for paragraph in content.findAll('p'):
                st.write(""" P-**{})** {}""".format(count,paragraph.text))
                count+=1
if __name__ == "__main__":
    main()

        '''
        st.code(code, language='python')

    
   
    

if __name__ == "__main__":
    main()





