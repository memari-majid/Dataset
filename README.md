# Fire Detection Dataset Analysis

This repository contains analysis and documentation for a fire detection dataset used in computer vision tasks. The dataset has been analyzed for duplicates and quality issues.

## Dataset Overview

The dataset is organized in a YOLO format with the following structure:
```
Dataset/
├── train/
│   ├── images/
│   └── labels/
├── val/
│   ├── images/
│   └── labels/
└── test/
    ├── images/
    └── labels/
```

## Dataset Statistics

- Total Images: 18,173
- Total Annotations: 9,175
- Unique Image Sizes: 9,622
- Unique Annotations: 5,404

## Duplicate Analysis Findings

### 1. Image Duplication
- Exact Image Duplicates: 7,482 instances
- Size-based Duplicates: 7,039 instances
- Approximately 41% of all images are duplicates

### 2. Annotation Duplication
- Duplicate Annotations: 3,771 instances
- About 41% of all annotations are duplicates

### 3. Split Distribution
- Training Set:
  - Images: 7,483
  - Annotations: 3,771
- Validation Set:
  - Images: 8,552
  - Annotations: 4,312
- Test Set:
  - Images: 2,138
  - Annotations: 1,092

## Critical Issues Identified

### 1. Cross-Split Duplication
- Many images appear in both training and validation sets
- Some images appear in all three splits
- The validation set contains more images than the training set

### 2. Annotation Consistency
- All annotations follow YOLO format
- All annotations are for class 0
- Coordinates are properly normalized (0-1 range)

### 3. File Size Patterns
- High number of files with identical sizes (7,039 instances)
- Suggests systematic duplication rather than random occurrences

## Impact on Model Training

1. **Training Impact**:
   - Model performance metrics may be inflated
   - Risk of overfitting to duplicated data
   - Training efficiency is compromised

2. **Validation Impact**:
   - Validation set is contaminated with training data
   - Model evaluation is not meaningful
   - Performance metrics are not representative

3. **Test Impact**:
   - Some test data may overlap with training/validation
   - Final performance metrics may be unreliable

## Recommendations

1. **Dataset Cleaning**:
   - Remove all duplicates from validation set
   - Ensure each image appears in only one split
   - Create a proper random split of the data

2. **Dataset Reorganization**:
   - Implement a proper train/val/test split strategy
   - Use a random seed for reproducibility
   - Maintain the same annotation format and quality

3. **Quality Control**:
   - Implement checks to prevent future duplication
   - Add validation steps in the data pipeline
   - Document the split creation process

## Usage

This dataset should be cleaned and reorganized before use in model training. The current state of duplication, particularly in the validation set, makes it unsuitable for model training and evaluation.

## License

[Add your license information here]

## Contributing

[Add contribution guidelines here]

## Contact

[Add contact information here] 