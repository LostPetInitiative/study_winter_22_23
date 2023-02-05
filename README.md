# study_winter_22_23
A repo for MDS student projects in winter 2022-2023

# Pets-Face-Recognition

## Create New Conda Env
```
conda create --name pet2023 python=3.8
conda activate pet2023
```
## Install requirements
```
pip3 install -r requirements.txt
```

## Download the datasets
List of the datasets:

All3img_ExtraIG_train: <br>(https://zenodo.org/record/7606128#.Y97B4HZBxD8)<br>
All3img_ExtraIG_val: <br>(https://zenodo.org/record/7606128#.Y97B4HZBxD8)<br>
test_alignment.zip: <br>(https://zenodo.org/record/7606696#.Y983xnZBxPY)<br>
Pet_face_detection_dataset1: <br>(https://zenodo.org/record/7604865#.Y96vv3ZBxPY)<br>
Pet_face_detection_dataset2: <br>(https://zenodo.org/record/7606080#.Y98jXnZBxPY)<br>

- After downloading `All3img_ExtraIG_train.zip`, `All3img_ExtraIG_val.zip`, and `test_alignment.zip` unzip them into `datasets` folder. Those two dataset for training the pet face recognition model.<br>
- `Pet_face_detection_dataset1.zip` unzip it into `./yolov7_bbox_landmarks/`, for training the first yolov7 detector. <br>
- `Pet_face_detection_dataset2.zip` unzip it into `./yolov7_bbox/data/`, for training the second yolov7 detector.

## Download Pretrained model
ResNet100 Pretrained Model:<br>(https://drive.google.com/u/0/uc?id=1-ITaMieQqLFgtYAmyQ8pIzpwaNDhE1Dt&export=download)<br>
Pet2023_BestBackbone Model:<br>(https://drive.google.com/u/8/uc?id=17IxKOmBRiKjbzkMw5IX59DQcMVyxnBwl&export=download)<br>
Pet2023_BestHeader Model:<br>(https://drive.google.com/u/8/uc?id=1--YMiueKiduYO5Njp_sE3cHUTzqE2hrF&export=download)<br>
First Yolov7 Model:<br>(https://drive.google.com/u/6/uc?id=1MLjkpruH_VhACIz4Ow3oav0gS50uBPRE&export=download)<br>
Second Yolov7 Model:<br>(https://drive.google.com/u/6/uc?id=1NrnR4w-4Q4Nlw2hN-Ty4ZhTkT7J3EPWv&export=download)<br>

- Put `res_mag_All_Data_del2img_Extra2_replaced_best.pth`, `Pet2023_BestBackbone.pth`, `Pet2023_BestHeader.pth` into `./source` folder,<br>
- Put the first Yolov7 Model `yolov7-pet-face.pt` into `./yolov7_bbox_landmarks/weights`,<br>
- Put the second Yolov7 Model `yolov7x-pet-face.pt` into `./yolov7_bbox/weights`,

## Pet face recognition model training
Here are two pretrained backbones are provided, after downloading those weights, put them into the `source` folder
- ms1mv3_arcface_r100_fp16_backbone.pth <br>(https://drive.google.com/u/0/uc?id=1MHjiSy3Snvqptf0K71sr2IzXGjC4Lbcq&export=download providied by deepinsight)
- Pet2023_BestBackbone.pth (the best backbone in this study, download link in the Download Pretrained model section)
- Pet2023_BestHeader.pth (the best header in this study, download link in the Download Pretrained model section)

Train the model from the srcatch, use the `ms1mv3_arcface_r100_fp16_backbone.pth` backbone as pre-trained model, and input --backbone ms1mv3_arcface_r100_fp16_backbone.pth
```
cd myrun
python train.py --exp_name exp1 --backbone ms1mv3_arcface_r100_fp16_backbone.pth
```

## Continue train the previous experiment
For continue the previous training, input --exp_name and --continue_train,<br>
the default backbone and header are `last_backbone.pth` and `last_header.pth`

```
cd myrun
python train.py --exp_name exp1 --continue_train
```

### Optional Setting
- train_data_path: change train path, default="../datasets/All3img_ExtraIG_train"
- val_data_path: change val path, default="../datasets/All3img_ExtraIG_val"
- continue_train: default=False
- backbone: backbone name, default=None
- header: header name, default=None
- num_epoch: default=30
- batch_size: default=16

## Inference on the test set and submit to the Pet3Challenge

Download the kashtanka test set `Test.zip` dataset and unzip it to the path `datasets`, Test.zip includes two main folders `Test` and `cat_dot_class_csv`, in this part we use the filtering by pet type matching, using the pet type to filter out some irrelevant answers. For example, if the query is finding a dog, we filter out all the cat answers.

```
Test/
├── found
├── lost
├── synthetic_found
├── synthetic_lost
...
...
cat_dog_class_csv/
├── ff2.csv
├── fsl2.csv
├── ll2.csv
├── lsf2.csv
...
```

Load the model and run the test.py, and pass the backbone to the test.py, the backbone will be found in `source` folder, and the `test.py` will generate a `submit.tsv` file in eval.
```
cd eval  # the folder path
python test.py --backbone Res_mag_del2img_ExtraIG_replaced_backbone.pth
```

After generating the `submit.tsv`, register on (http://92.63.96.33/c/_lostpets_v3_1/description), download the `compai__lostpets_v3_1.py`, put it into the `eval` folder
```
python compai__lostpets_v3_1.py sumbit sumbit.tsv
```

## Yolov7 Pet face detectors
### Train the first Yolov7 pet face detector
The first yolov7 detects both 3 landmarks (two eyes and nose) and bboxes, for training the first yolov7 detector, download the `pet_face_detection_dataset_1`, and unzip in the path: `./yolov7_bbox_landmarks/`

Download the initial weights file: (https://drive.google.com/file/d/1oIaGXFd4goyBvB1mYDK24GLof53H9ZYo/view), and put it in the path `weights/yolov7-face.pt`.

 ```
cd yolov7_bbox_landmarks
pip3 install -r requirements.txt
python train.py --data data/pet_train.yaml --cfg cfg/yolov7-face_3pt.yaml --weights weights/yolov7-face.pt --batch-size 4 --epochs 300 --kpt-label 3 --img 640 --name pet_face_detector1 --hyp data/hyp.scratch.p6.yaml
```

After training, test the Yolov7 on test set(split from the pet_face_detection_dataset_1):
```
python test.py --data data/pet_test.yaml --kpt-label 3 --img 640 --batch 4 --conf 0.001 --iou 0.65 --device 0 --weights runs/train/pet_face_detector1/weights/best.pt --name test
```

In addition, I also labeled 300 images from kashtanka dataset, test the Yolov7 on kashtanka test set:
```
python test.py --data data/pet_test_kashtanka.yaml --kpt-label 3 --img 640 --batch 4 --conf 0.001 --iou 0.65 --device 0 --weights runs/train/pet_face_detector1/weights/best.pt --name test_kashtanka
```

### Train the second Yolov7 pet face detector
The second only detects the bboxes, for training the second yolov7 detector, download the `pet_face_detection_dataset_2`, and unzip in the path: `./yolov7_bbox/data`. And download the initial weights from (https://github.com/WongKinYiu/yolov7/releases/download/v0.1/yolov7x.pt), and put it into `./yolov7_bbox/weights/yolov7x.pt`


 ```
cd yolov7_bbox
pip3 install -r requirements.txt
python train.py --workers 1 --device 0 --batch-size 4 --epochs 30 --img 640 640 --data data/pet_face_train.yaml --hyp data/hyp.scratch.custom.yaml --cfg cfg/training/yolov7x_custom.yaml --name pet_face_detector2 --weights yolov7x.pt
```

Test the Yolov7 on test set(split from the pet_face_detection_dataset_2):
```
python test.py --data data/pet_face_test.yaml --img 640 --batch 4 --conf 0.05 --iou 0.5 --device 0 --weights runs/train/pet_face_detector2/weights/best.pt --name test
```

Test the Yolov7 on kashtanka test set:
```
python test.py --data data/kashtanka_test.yaml --img 640 --batch 4 --conf 0.05 --iou 0.5 --device 0 --weights runs/train/pet_face_detector2/weights/best.pt --name kashtanka_test
```

<b>Result of the first Yolov7 detectors </b>
| Dataset | Precision | Recall | mAP@.5 | mAP@.5:.95 | 
| ------- | ---------- | ---------- | ---------- | ---------- |
| test set  | 0.925 | 0.95 | 0.926 | 0.724 |
| kashtanka test | 0.959 | 0.913 | 0.972 | 0.584 | 

<b>Result of the second Yolov7 detectors </b>
| Dataset | Precision | Recall | mAP@.5 | mAP@.5:.95 | 
| ------- | ---------- | ---------- | ---------- | ---------- |
| test set  | 0.901 | 0.902 | 0.833 | 0.629 |
| kashtanka test | 0.977 | 0.997 | 0.994 | 0.671 | 

### Pet face alignmnet
The figure shows our two yolo detecters workflow:

<b>Workflow</b><br>
![alt text](https://github.com/LostPetInitiative/study_winter_22_23/blob/main/demo_image/yolo_flow.jpg "Yolov7's workflow")

The --source directory can be folder of images:
```
example_images/
├── image1.jpg
├── image2.jpg
...
```

Or something like folder of folder of images:
```
example_images/
├── cat1
│   ├── cat1_1.jpg
│   ├── cat1_2.jpg
│   ├── ...
│   └── cat1_5.jpg
├── dog1
│   ├── dog1_1.jpg
│   ├── dog1_2.jpg
│   ├── ...
│   └── dog1_5.jpg
...
└── cat10
    ├── cat10_1.jpg
    ├── cat10_2.jpg
    ├── ...
    └── cat10_5.jpg
```

First run kpts_and_bboxes_inf.py, it will create a json file (exp_kpt.json), which stores the images path, folder name, the landmarks, the bboxes and the conf.
```
python kpts_and_bboxes_inf.py --source example_images --weights yolov7_bbox_landmarks/runs/train/pet_face_detector1/weights/best.pt --name exp
```

Similarly, run bboxes_inf.py, it will create an other json file (exp_bbox.json), which stores the images path, folder name, the bboxes and the conf.
```
python bboxes_inf.py --source example_images --weights yolov7_bbox/runs/train/pet_face_detector2/weights/best.pt --name exp
```

Finally, pass those two json files to the face_alignment.py, it will process face alignment on images and save it in exp_face_alignment folder 
```
python face_alignment.py --kpt-json exp_kpt.json --bbox-json exp_bbox.json --name exp_face_alignment
```


## Pet2023_BestModel Train Log and Test Result
- Pet2023_BestModel Training Log
![alt text](https://github.com/LostPetInitiative/study_winter_22_23/blob/main/demo_image/Res_mag_All_Data_del2img_Extra2_replaced_train_log.png "Training")

- Pet2023_BestModel result
![alt text](https://github.com/LostPetInitiative/study_winter_22_23/blob/main/demo_image/res_mag_new_test.jpg "Pet2023_BestModel result")

## DataSets Description
<b>Description</b><br>
![alt text](https://github.com/LostPetInitiative/study_winter_22_23/blob/main/demo_image/DataSet.png "Description")

<b>Examples of DataSets</b><br>
![alt text](https://github.com/LostPetInitiative/study_winter_22_23/blob/main/demo_image/examples_of_extraig.png "Examples of DataSets")



