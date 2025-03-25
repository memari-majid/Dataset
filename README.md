# Fire Detection Dataset Analysis 🔥

[![Python](https://img.shields.io/badge/python-v3.8+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Dataset](https://img.shields.io/badge/dataset-analysis-orange.svg)](https://github.com/memari-majid/Dataset)

A comprehensive analysis tool for identifying and managing duplicates in fire detection datasets, specifically designed for YOLO-format datasets used in computer vision tasks.

## 📋 Table of Contents
- [Fire Detection Dataset Analysis 🔥](#fire-detection-dataset-analysis-)
  - [📋 Table of Contents](#-table-of-contents)
  - [🔍 Overview](#-overview)
  - [📁 Dataset Structure](#-dataset-structure)
  - [📊 Key Findings](#-key-findings)
    - [Dataset Statistics](#dataset-statistics)
    - [Split Distribution](#split-distribution)
  - [⚙️ Installation](#️-installation)
  - [🚀 Usage](#-usage)
  - [📈 Detailed Analysis](#-detailed-analysis)
    - [Duplication Issues](#duplication-issues)
    - [Quality Assessment](#quality-assessment)
  - [🛠️ Recommendations](#️-recommendations)
    - [Immediate Actions](#immediate-actions)
    - [Long-term Improvements](#long-term-improvements)
  - [🤝 Contributing](#-contributing)
  - [📄 License](#-license)
  - [📫 Contact](#-contact)

## 🔍 Overview

This repository provides tools and analysis for a fire detection dataset, focusing on identifying duplicates and quality issues that could impact model training. The analysis reveals significant duplication across dataset splits, which could compromise model performance.

## 📁 Dataset Structure

The dataset follows the YOLO format organization:
```
Dataset/
├── train/          # Training set
│   ├── images/     # Training images
│   └── labels/     # YOLO format annotations
├── val/            # Validation set
│   ├── images/     # Validation images
│   └── labels/     # YOLO format annotations
└── test/           # Test set
    ├── images/     # Test images
    └── labels/     # YOLO format annotations
```

## 📊 Key Findings

### Dataset Statistics
| Metric | Count |
|--------|--------|
| Total Images | 18,173 |
| Total Annotations | 9,175 |
| Unique Images | 9,622 |
| Unique Annotations | 5,404 |
| Duplication Rate | ~41% |

### Split Distribution
| Split | Images | Annotations |
|-------|---------|-------------|
| Training | 7,483 | 3,771 |
| Validation | 8,552 | 4,312 |
| Test | 2,138 | 1,092 |

## ⚙️ Installation

1. Clone the repository:
```bash
git clone https://github.com/memari-majid/Dataset.git
cd Dataset
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## 🚀 Usage

Run the analysis script:
```bash
python analyze_dataset.py
```

The script will generate a detailed report of duplicates and dataset statistics.

## 📈 Detailed Analysis

### Duplication Issues
1. **Image Duplication**
   - 7,482 exact image duplicates identified
   - 7,039 size-based duplicates found
   - 41% overall duplication rate

2. **Annotation Duplication**
   - 3,771 duplicate annotations detected
   - Consistent YOLO format across all annotations
   - All annotations use class index 0

3. **Cross-Split Contamination**
   - Significant overlap between training and validation sets
   - Validation set larger than training set (unusual)
   - Some images present in all three splits

### Quality Assessment
- ✅ Proper YOLO format annotations
- ✅ Normalized coordinates (0-1 range)
- ❌ High duplication rate
- ❌ Improper split distribution

## 🛠️ Recommendations

### Immediate Actions
1. **Remove Duplicates**
   - Eliminate cross-split duplications
   - Ensure unique images in each split
   - Maintain data integrity

2. **Rebalance Splits**
   - Implement proper train/val/test ratios (e.g., 70/20/10)
   - Ensure random and stratified splitting
   - Verify no cross-contamination

3. **Quality Control**
   - Implement automated duplicate checking
   - Add data pipeline validation
   - Document all data processing steps

### Long-term Improvements
- Implement version control for dataset changes
- Create automated quality checks
- Establish clear data collection guidelines

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📫 Contact

Majid Memari - [@GitHub](https://github.com/memari-majid)

Project Link: [https://github.com/memari-majid/Dataset](https://github.com/memari-majid/Dataset)

---
⭐️ If you find this analysis helpful, please consider giving it a star!