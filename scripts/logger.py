import logging, os
from pathlib import Path

def get_loader_by_name(loader_name:str, file_name:str='pipeline.logs',level:int=logging.INFO):

    # create a formatter
    formatter = logging.Formatter('%(asctime)s- %(levelname)s -%(filename)s -%(message)s')

    # file handler
    full_file_name = os.path.join(Path(__file__).resolve().parents[1], "logs", file_name)
    file_handler = logging.FileHandler(full_file_name, 'a')
    file_handler.setFormatter(formatter)

    # fetch loader
    loader = logging.getLogger(loader_name)
    loader.setLevel(level)

    # check if loader exists before
    if not loader.handlers:
        loader.addHandler(file_handler)

    return loader
