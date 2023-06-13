import os 
import requests
import random
import uuid
from tqdm import tqdm
import concurrent.futures.process as executor

url=[]
# url =['https://www.youtube.com/watch?v=ydVjGs3fJJk','https://images.pexels.com/photos/45201/kitty-cat-kitten-pet-45201.jpeg?auto=compress&cs=tinysrgb&w=600','https://images.pexels.com/photos/45170/kittens-cat-cat-puppy-rush-45170.jpeg?auto=compress&cs=tinysrgb&w=600','https://images.pexels.com/photos/416160/pexels-photo-416160.jpeg?auto=compress&cs=tinysrgb&w=600']
link=input('Enter the url to be downloaded here(image,video,pdf e.t.c):')
url.append(link)
def generate_name():
    token=str(uuid.uuid4())
    sample_token=random.sample(token,5)
    join_token=''.join(sample_token)
    val=['.png','.jpg','.jpeg']
    random_val=random.choice(val)
    return join_token

generate_name()

def internet_download_manager(url):
    try:
        with tqdm(total=len(url),ascii=True,desc='downloading') as pbar:
            for urls in url:
                check_url=requests.get(urls).content
                v=os.listdir('/home')
                c=v[0]
                home_path=f'/home/{c}'
                check_dir=os.listdir(f'/home/{c}')
                if 'file_download' in check_dir:
                    path=f'{home_path}/file_download'
                    with open(f'{path}/{generate_name()}','wb') as f:
                        f.write(check_url)
                        f.close()
                    pbar.update(1)
                    
                else:
                    # print('no')
                    # print(os.listdir('/home'))
                    path=f'{home_path}/file_download'
                    os.mkdir(path)
                    with open(f'{path}/{generate_name()}','wb') as f:
                        f.write(check_url)
                        f.close()
                    pbar.update(1)
        print(f'Done downloading this file-open {path} to view this')
    except Exception: 
        print('Error while runnning this file')
    except ConnectionError:
        print('connect to the internet and try again')

    
internet_download_manager(url)
