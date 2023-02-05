import os
import shutil
from torchvision.datasets.utils import download_and_extract_archive, download_url

if __name__ == "__main__":
    # download models:
    if not os.path.exists("./source/Res_mag_del2img_ExtraIG_replaced_backbone.pth"):
        print("Download Res_mag_del2img_ExtraIG_replaced_backbone.pth to ./source")
        url = 'https://zenodo.org/record/7606128/files/Res_mag_del2img_ExtraIG_replaced_backbone.pth?download=1'
        download_url(url, "./source", 'Res_mag_del2img_ExtraIG_replaced_backbone.pth')
    else:
        print("Res_mag_del2img_ExtraIG_replaced_backbone.pth already exists ./source")

    if not os.path.exists("./source/Res_mag_del2img_ExtraIG_replaced_header.pth"):
        print("Download Res_mag_del2img_ExtraIG_replaced_header.pth to ./source")
        url = 'https://zenodo.org/record/7606128/files/Res_mag_del2img_ExtraIG_replaced_header.pth?download=1'
        download_url(url, "./source", 'Res_mag_del2img_ExtraIG_replaced_header.pth')
    else:
        print("Res_mag_del2img_ExtraIG_replaced_header.pth already exists ./source")

    if not os.path.exists("./yolov7_bbox_landmarks/weights/yolov7-pet-face.pt"):
        print("Download yolov7-pet-face.pt to ./yolov7_bbox_landmarks/weights")
        url = 'https://drive.google.com/u/6/uc?id=1MLjkpruH_VhACIz4Ow3oav0gS50uBPRE&export=download'
        download_url(url, "./yolov7_bbox_landmarks/weights", 'yolov7-pet-face.pt')
    else:
        print("yolov7-pet-face.pt already exists ./yolov7_bbox_landmarks/weights")
    
    if not os.path.exists("./yolov7_bbox/weights/yolov7x-pet-face.pt"):
        print("Download yolov7x-pet-face.pt to ./yolov7_bbox/weights")
        url = 'https://drive.google.com/u/6/uc?id=1NrnR4w-4Q4Nlw2hN-Ty4ZhTkT7J3EPWv&export=download'
        download_url(url, "./yolov7_bbox/weights", 'yolov7x-pet-face.pt')
    else:
        print("yolov7x-pet-face.pt already exists ./yolov7_bbox/weights")

    if not os.path.exists("./yolov7_bbox_landmarks/weights/yolov7-face.pt"):
        print("Download yolov7-face.pt to ./yolov7_bbox_landmarks/weights")
        url = "https://drive.google.com/file/d/1oIaGXFd4goyBvB1mYDK24GLof53H9ZYo/view"
        download_url(url, "./yolov7_bbox_landmarks/weights", 'yolov7-face.pt')
    else:
        print("yolov7-face.pt already exists ./yolov7_bbox_landmarks/weights")

    if not os.path.exists("./yolov7_bbox/weights/yolov7x.pt"):
        print("Download yolov7x.pt to ./yolov7_bbox/weights")
        url = "https://github.com/WongKinYiu/yolov7/releases/download/v0.1/yolov7x.pt"
        download_url(url, "./yolov7_bbox/weights", 'yolov7x.pt')
    else:
        print("yolov7x.pt already exists ./yolov7_bbox/weights")