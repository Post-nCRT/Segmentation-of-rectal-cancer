### Fully semantic segmentation for rectal cancer based on post-nCRT MRl modality and deep learning framework

using steps:
1. Use the post-nCRT slice.py in the Rectal folder for slicing post-nCRT MRl dataset. 
2. Employ the 2D network code in nnUNet-master to develop the model. Please refer to the instructions provided in nnUNet for specific details.
3. Calculate the typical values (max, min, mean, etc) of various metrics for the training and test sets, using train metric.py and test metrics.py in the Rectal folder.