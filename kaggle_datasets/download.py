import os
import time
from zipfile import ZipFile
from kaggle.api.kaggle_api_extended import KaggleApi



data_path = os.path.expanduser('~')+'/data_science/datasets/data/'

def dnld_kaggle_data(dataset, filename, delete_zip=True):
    #MVP function to download data from kaggle
      
    t1  = time.time() 
      
    if os.path.isfile(data_path+filename):
        print('Data already exist!')
        return
    
    #connect
    api = KaggleApi()
    api.authenticate()

    #download
    print('Downloadnig...')
    api.dataset_download_file(dataset, filename)
   
    #extract
    if os.path.isfile(filename+'.zip'): 
        print('Extracting...')
        zf = ZipFile(filename+'.zip')
        zf.extractall() 
        zf.close()

        #delete
        if delete_zip:
            os.remove(filename+'.zip')
            
    os.replace(os.getcwd()+'/'+filename, data_path+filename)
    t2 = time.time()
    
    print(f'Data ready! It took {round(t2-t1, 1)} seconds.')