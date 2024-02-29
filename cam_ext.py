import os
from PIL import Image
from PIL.ExifTags import TAGS


def extract_camera_info_folder(folder_path):
    """Extract camera info from a folder

    Args:
        folder_path (str): folder location containing JPEG images.
    """
    # Initialize an empty list to hold the camera info strings
    camera_info_list = []
    
    # Loop over all files in the given folder
    for filename in os.listdir(folder_path):
        # Check if the file is a JPEG image
        if filename.lower().endswith(('.jpg', '.jpeg')):
            full_path = os.path.join(folder_path, filename)
            # Use your function to extract camera info
            info = extract_camera_info(full_path)
            camera_info_list.append(info)
    
    for c in camera_info_list:
        print(c)



def extract_camera_info(image_path):

    if os.path.exists(image_path):
        img_name = os.path.basename(image_path)
    # Open the image file
    img = Image.open(image_path)
    
    # Extract EXIF data
    exif_data = img._getexif()
    
    camera_info = {}
    
    if exif_data is not None:
        # Map EXIF data to readable format
        for tag_id, value in exif_data.items():
            tag = TAGS.get(tag_id)
            if tag in ["Make", "Model", "FocalLength", "FNumber", "ExposureTime", "ISOSpeedRatings"]:
                camera_info[tag] = value
    
    camera_info_disp = f"""-- Camera Info: {img_name} --
{camera_info["Make"]} {camera_info["Model"]}
{int(camera_info["FocalLength"])} mm, 1/{int(1/camera_info["ExposureTime"])} s, f {camera_info["FNumber"]}, ISO {camera_info["ISOSpeedRatings"]}
--"""
    
    return camera_info_disp


if __name__ == "__main__":
    # print(extract_camera_info("img/test.jpeg"))
    extract_camera_info_folder("img/")