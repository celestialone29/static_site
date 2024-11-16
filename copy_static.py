import os
import shutil

def copy_static(src, dest):
    """
    Recursively copies files and directories from the source to the destination.

    Parameters:
        src (str): The source directory path.
        dest (str): The destination directory path.
    """
    if not os.path.exists(dest):
        os.makedirs(dest)  # Create the destination directory if it doesn't exist

    for item in os.listdir(src):
        src_path = os.path.join(src, item)
        dest_path = os.path.join(dest, item)

        if os.path.isdir(src_path):
            # If the item is a directory, recurse into it
            copy_static(src_path, dest_path)
        else:
            # If the item is a file, copy it to the destination
            shutil.copy2(src_path, dest_path)

