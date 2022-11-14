try:
    from bs4 import BeautifulSoup
    import requests
    import bs4
    import os
    import json
    import traceback
except Exception as e:
    print('Caught exception while importing: {}'.format(e))

def make_dir(output_path):
    if not os.path.exists(output_path):
        os.makedirs(output_path)
def write_json(filename, data):
    with open(filename, 'w', encoding='utf8') as f:

        json.dump(data, f, indent=4, ensure_ascii=False)

def read_json(filename):
    try:
        with open(filename, 'r') as f:
            data = json.load(f)
            return data
    except Exception as e:
        print('Error loading {}'.format(filename), e)
        traceback.print_exc()
        return []
def find_json(filename):
    current_path=__file__.replace(__file__.split("/")[-1], filename)
    return current_path
def request_url(url):
    session= requests.Session()
    header ={"User-Agent" : 
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
                "Accept" : "text/html,application/xhtml+xml,application/xml;\
                q=0.9,image/webp,image/apng,*/*;q=0.8"}
    response = session.get(url, headers=header)
    soup=BeautifulSoup(response.text,"html.parser")
    return soup
class filmScraper:
    def __init__(self, config, image_urls=[]):
        self.config = config
        self.image_urls = image_urls
    def film_extract(self,start=1):
        url=self.config.SEARCH_URL
        save_dir=self.config.save_dir
        save_file=self.config.save_file
        make_dir(save_dir)
        url=url.format(start)
        soup=request_url(url)
        elements=soup.select('div.lister-item-image')
        data=[]
        for ele in elements:
            try:
                link=ele.select("img")[0]
                # print(link)
                img=link['loadlate']
                ele_data={
                    'poster_url': img, 
                    'page': start
                }
                data.append(ele_data)
            except Exception as e:
                print("Error: ", e)
                traceback.print_exc()
        filename = save_file+'_page_{}.json'.format(start)
        write_json(save_dir+'/'+filename,data)
    @property
    def film_crawler(self):
        start=self.config.start
        number=self.config.number
        for i in range(start,start+number):
            self.film_extract(start=i)
    def read_file(self,filename):
        return read_json(filename=filename)