import os
import hashlib
from collections import defaultdict
from PIL import Image
import numpy as np
import json
from datetime import datetime

def calculate_image_hash(image_path):
    """Calculate a hash of the image content."""
    try:
        with Image.open(image_path) as img:
            # Convert to grayscale and resize to 8x8 for faster comparison
            img = img.convert('L').resize((8, 8), Image.Resampling.LANCZOS)
            # Convert to numpy array and flatten
            img_array = np.array(img).flatten()
            # Calculate hash
            return hashlib.md5(img_array.tobytes()).hexdigest()
    except Exception as e:
        print(f"Error processing {image_path}: {e}")
        return None

def read_annotation(ann_path):
    """Read and return the content of an annotation file."""
    try:
        with open(ann_path, 'r') as f:
            return f.read().strip()
    except Exception as e:
        print(f"Error reading annotation {ann_path}: {e}")
        return None

def analyze_dataset(base_dir):
    """Analyze the dataset for duplicates and similar images."""
    # Dictionary to store file sizes
    size_dict = defaultdict(list)
    # Dictionary to store image hashes
    hash_dict = defaultdict(list)
    # Dictionary to store annotation contents
    ann_dict = defaultdict(list)
    
    # Process all image files in train, val, and test directories
    for split in ['train', 'val', 'test']:
        images_dir = os.path.join(base_dir, split, 'images')
        labels_dir = os.path.join(base_dir, split, 'labels')
        
        if not os.path.exists(images_dir) or not os.path.exists(labels_dir):
            continue
            
        print(f"\nAnalyzing {split} directory...")
        for filename in os.listdir(images_dir):
            if not filename.lower().endswith(('.png', '.jpg', '.jpeg')):
                continue
                
            # Get image filepath
            image_path = os.path.join(images_dir, filename)
            file_size = os.path.getsize(image_path)
            
            # Get corresponding annotation filepath
            ann_filename = os.path.splitext(filename)[0] + '.txt'
            ann_path = os.path.join(labels_dir, ann_filename)
            
            # Group by file size
            size_dict[file_size].append(image_path)
            
            # Calculate image hash
            img_hash = calculate_image_hash(image_path)
            if img_hash:
                hash_dict[img_hash].append(image_path)
            
            # Read and group annotations
            ann_content = read_annotation(ann_path)
            if ann_content:
                ann_dict[ann_content].append(ann_path)
    
    # Generate comprehensive report
    report = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "dataset_statistics": {
            "total_images": sum(len(files) for files in size_dict.values()),
            "total_annotations": sum(len(files) for files in ann_dict.values()),
            "unique_image_sizes": len(size_dict),
            "unique_annotations": len(ann_dict)
        },
        "duplicate_analysis": {
            "exact_image_duplicates": {
                "count": sum(1 for files in hash_dict.values() if len(files) > 1),
                "total_duplicate_files": sum(len(files) for files in hash_dict.values() if len(files) > 1),
                "examples": [
                    {
                        "hash": hash_value,
                        "files": filepaths,
                        "count": len(filepaths)
                    }
                    for hash_value, filepaths in hash_dict.items()
                    if len(filepaths) > 1
                ]
            },
            "size_based_duplicates": {
                "count": sum(1 for files in size_dict.values() if len(files) > 1),
                "total_duplicate_files": sum(len(files) for files in size_dict.values() if len(files) > 1),
                "examples": [
                    {
                        "size_bytes": size,
                        "files": filepaths,
                        "count": len(filepaths)
                    }
                    for size, filepaths in size_dict.items()
                    if len(filepaths) > 1
                ]
            },
            "annotation_duplicates": {
                "count": sum(1 for files in ann_dict.values() if len(files) > 1),
                "total_duplicate_files": sum(len(files) for files in ann_dict.values() if len(files) > 1),
                "examples": [
                    {
                        "content": content,
                        "files": filepaths,
                        "count": len(filepaths)
                    }
                    for content, filepaths in ann_dict.items()
                    if len(filepaths) > 1
                ]
            }
        },
        "split_analysis": {
            "train": {
                "images": len([f for f in sum(hash_dict.values(), []) if "train" in f]),
                "annotations": len([f for f in sum(ann_dict.values(), []) if "train" in f])
            },
            "val": {
                "images": len([f for f in sum(hash_dict.values(), []) if "val" in f]),
                "annotations": len([f for f in sum(ann_dict.values(), []) if "val" in f])
            },
            "test": {
                "images": len([f for f in sum(hash_dict.values(), []) if "test" in f]),
                "annotations": len([f for f in sum(ann_dict.values(), []) if "test" in f])
            }
        }
    }
    
    # Save report to JSON file
    with open("dataset_analysis_report.json", "w") as f:
        json.dump(report, f, indent=2)
    
    # Print summary
    print("\n=== Dataset Analysis Report ===")
    print(f"Generated at: {report['timestamp']}")
    print("\nDataset Statistics:")
    print(f"Total Images: {report['dataset_statistics']['total_images']}")
    print(f"Total Annotations: {report['dataset_statistics']['total_annotations']}")
    print(f"Unique Image Sizes: {report['dataset_statistics']['unique_image_sizes']}")
    print(f"Unique Annotations: {report['dataset_statistics']['unique_annotations']}")
    
    print("\nDuplicate Analysis:")
    print(f"Exact Image Duplicates: {report['duplicate_analysis']['exact_image_duplicates']['count']}")
    print(f"Size-based Duplicates: {report['duplicate_analysis']['size_based_duplicates']['count']}")
    print(f"Annotation Duplicates: {report['duplicate_analysis']['annotation_duplicates']['count']}")
    
    print("\nSplit Analysis:")
    for split, stats in report['split_analysis'].items():
        print(f"\n{split.upper()} Split:")
        print(f"  Images: {stats['images']}")
        print(f"  Annotations: {stats['annotations']}")
    
    print("\nDetailed report saved to 'dataset_analysis_report.json'")

if __name__ == "__main__":
    analyze_dataset(".") 