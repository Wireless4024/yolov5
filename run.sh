#!/usr/bin/env bash
set +e
dataset_path=/mnt/hdd1/dataset
rm -rf yolov5s.pt runs
python train.py --img 256 --batch 64 --epochs 200 --data $dataset_path/conf.yaml --weights yolov5s.pt --hyp $dataset_path/hyp.yaml
python export.py --weights runs/train/exp/weights/best.pt --data $dataset_path/conf.yaml --include tfjs
#rm -rf runs