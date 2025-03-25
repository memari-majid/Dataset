from ultralytics import YOLO
from ultralytics.utils.benchmarks import benchmark


# Initialize the YOLO model
model = YOLO("yolov8n.yaml")

# Tune hyperparameters on COCO8 for 30 epochs
#model.tune(data="data.yaml", imgsz=300, epochs=20, iterations=20, patience=10, optimizer="auto", shear=20, perspective=0.01, flipud=0.5, fliplr=0.5, mixup=1, copy_paste=1)

#results = model.train(data="data.yaml", epochs=100, imgsz=300, lr0=0.00928, lrf=0.0082, momentum=0.98, weight_decay=0.00054, warmup_epochs=3.82317, warmup_momentum=0.63228, box=12.16416, cls=0.50306, dfl=1.85895, hsv_h=0.01411, hsv_s=0.52341, hsv_v=0.44971, degrees=0.0, translate=0.14874, scale=0.33813, shear=8.14168, perspective=0.00063, flipud=0.36117, fliplr=0.47834, bgr=0.0, mosaic=0.3891, mixup=0.97762, copy_paste=0.85327)

benchmark(model="yolov8n.pt", data="data.yaml", imgsz=300)