import os

os.environ['KAGGLE_USERNAME'] = os.getenv('KAGGLE_USERNAME')
os.environ['KAGGLE_KEY'] = os.getenv('KAGGLE_KEY')


from kaggle.api.kaggle_api_extended import KaggleApi

def download_market1501():
    api = KaggleApi()                 
    api.authenticate()              
    api.dataset_download_files(
        'pengcw1/market-1501',        
        path='data/market1501',        
        unzip=True,                  
        quiet=False                   
    )

if __name__ == '__main__':
    os.makedirs('data/market1501', exist_ok=True)
    download_market1501()
    print("✅ Market-1501 downloaded and extracted.")
