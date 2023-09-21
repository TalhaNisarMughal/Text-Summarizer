# In Utils > Common.py module we will all of the functions or utilities that we will frequently used in this entire application.

import os
from box.exceptions import BoxValueError
import yaml
from pathlib import Path
from textsummarizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox  # helps to access the values of yaml keys easily
from typing import Any

# The first function that we will use in our entire application is Read yaml file
@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Reads yaml file and returns a ConfigBox.

    Args: 
    ----------
    path_to_yaml (str): Path like input.

    Raises:
    ----------
    ValueError: if yaml file is empty
    e: empty file

    Returns
    -------
    ConfigBox: ConfigBox type

    """
    try:
        with open(path_to_yaml, "r") as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
        
    except BoxValueError:
        raise ValueError('yaml file is empty')
    
    except Exception as e:
        raise e
    
@ensure_annotations
def create_directories(path_to_directories: list, verbose = True):
    """
    Create list of directories

    Args:
    ----------
    path_to_directories (list): list of directories to be created.
    verbose (bool, optional): True if you want to see the progress. Defaults to True.

    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Directory created successfully at {path}")

@ensure_annotations
def get_size(path: Path) -> str:
    """
    Get size in KB

    Args:
    ----------
    path (Path): Path to file.

    Returns:
    ----------
    str: Size in KB
    """
    size = round(os.path.getsize(path) / 1024)
    return f"{size} KB"