import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup

class Webpage:
    def __init__(self, url):
        self.url = url
        self.soup = None

        # Bypass Cloudflare and other anti-scraping measures
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Max-Age': '3600',
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
        }

    def get_soup(self):
        if self.soup is None:
            response = requests.get(self.url)
            self.soup = BeautifulSoup(response.text, 'html.parser')
        return self.soup

    def get_title(self):
        return self.get_soup().title.text

    def get_content(self):
        text_content = ""
        for p in self.get_soup().find_all("p"):
            text_content += p.text + ' '
        return text_content.strip()

    # Get content starting with a specific text and ending with a specific text
    def get_content_slice(self, start_text, end_text):
        text_content = ""
        start_index = self.get_content().find(start_text) if start_text else 0
        end_index = self.get_content().find(end_text) if end_text else len(self.get_content()) - 1
        if start_index != -1 and end_index != -1:
            text_content = self.get_content()[start_index:end_index]
        return text_content

    def get_external_links(self):
        return [link.get('href') for link in self.get_soup().find_all('a') if link.get('href').startswith('http')]
    
    def get_external_links_by_keywords(self, keywords):
        # Create an empty dictionary to store the links for each keyword
        links_dict = {}

        # Find all links that contain the specified keywords in their link text
        for link in self.get_soup().find_all('a'):
            link_text = link.get_text().lower()
            for keyword in keywords:
                if keyword in link_text:
                    href = link.get('href')
                    if href and href.strip():
                        # Check if href is a relative URL then ignore
                        if not href.startswith('http') and not href.startswith('//'):
                            continue
                        # Add the link to the dictionary, with a unique key if necessary
                        if keyword not in links_dict:
                            links_dict[keyword] = href
                        else:
                            counter = 1
                            new_key = f"{keyword}_{counter}"
                            while new_key in links_dict:
                                counter += 1
                                new_key = f"{keyword}_{counter}"
                            if href not in links_dict.values():
                                links_dict[new_key] = href
        return links_dict

    def get_links(self):
        return [urljoin(self.url, link.get('href')) for link in self.get_soup().find_all('a')]

    def get_images(self):
        return [urljoin(self.url, image.get('src')) for image in self.get_soup().find_all('img')]

    def get_videos(self):
        return [urljoin(self.url, video.get('src')) for video in self.get_soup().find_all('video')]

    def get_audio(self):
        return [urljoin(self.url, audio.get('src')) for audio in self.get_soup().find_all('audio')]

    def get_iframes(self):
        return [urljoin(self.url, iframe.get('src')) for iframe in self.get_soup().find_all('iframe')]

    def get_embeds(self):
        return [urljoin(self.url, embed.get('src')) for embed in self.get_soup().find_all('embed')]

    def get_objects(self):
        return [urljoin(self.url, object.get('data')) for object in self.get_soup().find_all('object')]

    def get_all_media(self):
        return self.get_images() + self.get_videos() + self.get_audio() + self.get_iframes() + self.get_embeds() + self.get_objects()

    def get_all_links(self):
        return self.get_links() + self.get_all_media()