import random
import time
from copy import deepcopy
import cloudscraper
import pandas as pd 
import os 


class Crawler:
    def __init__(self):
        self.base_url = 'https://www.1mg.com/drugs-all-medicines?label=Z'
        
        self.get_headers = {
            'Connection': 'keep-alive',
            'Cache-Control': 'max-age=0',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7'
        }
        self.session = cloudscraper.create_scraper()

        self.obj = {
            "name": "", "manufacturer_name": "", "marketer_name": "", "type": "", 
            "price": "", "sku_id": "", "available": "", "pack_size_label": "", 
            "quantity": "", "short_composition": "", "url": ""
        }
        self.all_data = []

    def get_request(self, url):
        mycount = 0
        while True:
            try:
                res = self.session.get(url, headers=self.get_headers)
                print(res)
                if res.status_code == 200:
                    return True, res
                time.sleep(random.randint(1, 3))
            except Exception as e:
                print(e)
            self.session = cloudscraper.create_scraper()
            print("Trying again to fetch data")
            mycount += 1
            if mycount > 30:
                break
        return False, False

    def get_details(self, data):
        extracted_data = []
        for item in data:
            Obj = deepcopy(self.obj)
            try:
                Obj['manufacturer_name'] = item.get('manufacturer_name', '')
                Obj['marketer_name'] = item.get('marketer_name', '')
                Obj['type'] = item.get('type', '')
                Obj['price'] = item.get('price', 0)
                Obj['name'] = item.get('name', '')
                Obj['sku_id'] = item.get('sku_id', '')
                Obj['available'] = item.get('available', False)            
                Obj['pack_size_label'] = item.get('pack_size_label', '') 
                Obj['quantity'] = item.get('quantity', 0)
                Obj['url'] = 'https://www.1mg.com' + item.get('slug', '') 
            except Exception as e:
                print(f"Error processing item {item}: {e}")
            self.all_data.append(Obj)
        return extracted_data

    def export_to_excel_append(self, file_name="scraped_data_Z.xlsx"):
        try:
            df = pd.DataFrame(self.all_data)
            file_exists = os.path.exists(file_name)
            with pd.ExcelWriter(file_name, mode='a' if file_exists else 'w', engine='openpyxl') as writer:
                df.to_excel(writer, index=False, header=not file_exists)
            print(f"Data successfully {'appended to' if file_exists else 'written to'} {file_name}")
        except Exception as e:
            print(f"Error appending data to Excel: {e}")

    def process_logic(self):
        try:
            page = 1
            while True:
                time.sleep(3)
                print("Scraping for page :- ", page)
                url = f'https://www.1mg.com/pharmacy_api_gateway/v4/drug_skus/by_prefix?prefix_term=z&page={str(page)}&per_page=30'
                isloaded, res = self.get_request(url)
                if isloaded:
                    data = res.json()
                    skus = data.get('data', {}).get('skus', [])
                    if skus and len(skus) > 0:
                        self.get_details(skus)
                        if page == 500:
                            break
                        page += 1
                    else:
                        break
                else:
                    break
            # ✅ Export after scraping ends
            self.export_to_excel_append()
        except Exception as e:
            print(e)


if __name__ == "__main__":
    scraper = Crawler()
    scraper.process_logic()