# Training

- use https://www.makesense.ai/ to label images
    - to checkpoint in the website export as VOC XML format and then import back next time (Note that label ordering
      will fuck up next time when import from txt so you may need to reorder the label before import the xml)
- export as zip containing yolo format
- split into training and validation

## example structure
(You can use `./split_data.py <path>` to split the dataset into training and validation set.)
```
dataset
- images
  - train
    - orange.jpg
    - apple.jpg
  - validation
    - orange.jpg
    - apple.jpg
- labels
  - train
    - orange.txt
    - apple.txt
  - validation
    - orange.txt
- config.yaml
```

## example config file (conf.yaml)

```yaml
path: /mnt/hdd1/dataset/
train: images/train  # train images (relative to 'path')
val: images/validation # val images (relative to 'path')

# Classes
nc: 2 # number of classes
names: [ 'orange', 'apple' ]
```

## example hyp file (hyp.yaml)

```yaml
# Ultralytics 🚀 AGPL-3.0 License - https://ultralytics.com/license

# Hyperparameters for low-augmentation COCO training from scratch
# python train.py --batch 64 --cfg yolov5n6.yaml --weights '' --data coco.yaml --img 640 --epochs 300 --linear
# See tutorials for hyperparameter evolution https://github.com/ultralytics/yolov5#tutorials

lr0: 0.01 # initial learning rate (SGD=1E-2, Adam=1E-3)
lrf: 0.01 # final OneCycleLR learning rate (lr0 * lrf)
momentum: 0.937 # SGD momentum/Adam beta1
weight_decay: 0.0005 # optimizer weight decay 5e-4
warmup_epochs: 3.0 # warmup epochs (fractions ok)
warmup_momentum: 0.8 # warmup initial momentum
warmup_bias_lr: 0.1 # warmup initial bias lr
box: 0.05 # box loss gain
cls: 0.5 # cls loss gain
cls_pw: 1.0 # cls BCELoss positive_weight
obj: 1.0 # obj loss gain (scale with pixels)
obj_pw: 1.0 # obj BCELoss positive_weight
iou_t: 0.20 # IoU training threshold
anchor_t: 4.0 # anchor-multiple threshold
# anchors: 3  # anchors per output layer (0 to ignore)
fl_gamma: 0.0 # focal loss gamma (efficientDet default gamma=1.5)
hsv_h: 0.015 # image HSV-Hue augmentation (fraction)
hsv_s: 0.7 # image HSV-Saturation augmentation (fraction)
hsv_v: 0.4 # image HSV-Value augmentation (fraction)
degrees: 0.0 # image rotation (+/- deg)
translate: 0.1 # image translation (+/- fraction)
scale: 0.0 # image scale (+/- gain)
shear: 0.0 # image shear (+/- deg)
perspective: 0.0 # image perspective (+/- fraction), range 0-0.001
flipud: 0.0 # image flip up-down (probability)
fliplr: 0.0 # image flip left-right (probability)
mosaic: 1.0 # image mosaic (probability)
mixup: 0.0 # image mixup (probability)
copy_paste: 0.0 # segment copy-paste (probability)
```

---

with all of this you can use run.sh to train and use import model to makesense.ai to speedup labeling process