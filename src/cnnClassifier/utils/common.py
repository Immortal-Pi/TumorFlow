import os 
from box.exceptions import BoxValueError        # exceptions 
import yaml                         
from cnnClassifier import logger            
import json                                     
import joblib                               
from ensure import ensure_annotations           # ensures data type errors 
from box import ConfigBox                       # to access dictionary key directly dict.key1
from pathlib import Path                        
from typing import Any 
import base64                                   # 



@ensure_annotations
def read_yaml(path_to_yaml: Path)-> ConfigBox:
    """ 
    reads yaml file and returns Configbox
    Args:
        path_to_yaml: yaml path input 

    Raises:
        ValueError: if yaml file is empty
        e: empty file 

    Returns:
        ConfigBox: ConfigBox type
    """
    try: 
        with open(path_to_yaml) as yaml_file:
            content=yaml.safe_load(yaml_file)
            logger.info(f'yaml file: {path_to_yaml} loaded successfully')
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError ('yaml file is empty')
    except Exception as e:
        raise e 
    

@ensure_annotations
def create_directories(path_to_directories:list,verbose=True):
    """ 
    creates a list of directories 
    Args:
        path_to_directories (list): List of path of directories
        ignore_log (bool,option): ignore if multiple dires is to be created. Default to False
    """
    for path in path_to_directories:
        os.makedirs(path,exist_ok=True)
        if verbose:
            logger.info(f'created directory at: {path}')


@ensure_annotations
def save_json(path:Path,data:dict):
    """ 
    save json data 
    Args:
        path (Path): path to json file 
        data (dict): data to be saved in json file
    """
    with open(path,'w') as f:
        json.dump(data,f,indent=4)
    logger.info(f'json file saved at {path}')


@ensure_annotations
def load_bin(path:Path)->Any:
    """
    load binary data 
    Args:
        path (Path): path to binary file 

    Returns:
        Any: object stored in the file 
    """
    data=joblib.load(path)
    logger.info(f'binary file loaded from: {path}')
    return data 


@ensure_annotations
def get_size(path:Path) -> str:
    """ 
    get size in KB
    Args:
        path (Path): path of the file 

    Returns:
        str: size in KB
    """
    size_in_kb=round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"


def decodeImage(imgstring,fileName):
    """ 
    decodes a Base64-encoded image string and writes the decoded data to file 
    Args:
        imgstring: Base64-encoded string representation of the image data 
        fileName: name of the file where the decoded image will be saved
    Returns:
        None 
    """
    imgdata=base64.b64decode(imgstring)
    with open(fileName,'wb') as f:
        f.write(imgdata)
        f.close()


def encodeImageIntoBase64(croppedImagePath):
    """ 
    converts and imange file into a Base64-encoded string
    Args:
        croppedImangePath: file  path of the imange you want to encode into Base64
    Returns:
        None 
    """
    with open(croppedImagePath,'rb') as f:
        return base64.b64encode(f.read())
