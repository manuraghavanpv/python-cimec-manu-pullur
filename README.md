# Image Denoiser

## Concept
* Most medical images such as MRIs inherently come out of the scanner with a significant amount of noise associated with the signal (Redpath, 1998; https://doi.org/10.1259/bjr.71.847.9771379)
* Therefore, identifying the optimal denoising approach for the specific image is critical in making precise and rapid diagnoses in conditions such as stroke and cancer. 
* This project aims to act as a demonstration of the logic behind such image denoising research, using simple image types such as JPG and PNG.
* The program lets the user select any RGB image (PNG/JPG), add noise (Gaussian/Salt and Pepper) with an intensity of their choosing, and then select a denoising approach for the corresponding problem - Non Local Means (NLM) or Principal Component Analysis (PCA).
* Finally, the denoising performance results will be displayed both qualitatively (visual comparison) and quantiatively (Peak SNR, Strcutural Similarity Index).
* While NLM acts as a fast(~1m) yet less precise approach, PCA offers a slower(~5h) but more effective alternative. The user will also get to observe how different types of denoising works better for different kinds of noises.
* The difference has to do with how these algorithms approach the problem of noise:
  * NLM identifies similar patches of pixels across the image and replaces the central pixel of those patches with the weighted average value. This leads to a rather blurrier/flattened, but denoised image that preserves the general details.
  * PCA on the other hand decomposes overlapping image patches into principal components (those which explain most of the variation) and hence distinguishes true signal from random noise. This leads to sharper images that preserves the finer details but assumes Gaussian distribution of noise. 

## Installation
* Clone this repository to your local machine or simply download the jupyter notebook and open it in Google Colab.
* Make sure that an image of your choosing is in the same folder as the script (for Colab, its /contents/image_name.jpg). A sample image called Cat.jpg can also be found in this repository.
* Modify the image location in the first part of the script accordingly
* Install the dependencies by runnning the top cell
* Run step by step and enter your choices of noise, intensity, denoising approach, and configurations (further details and default settings  will be visible with the prompt)
* Upon reaching the final step, you will observe the original, noisy, and denoised images as well as the values for PSNR and SSIM.

## Notes:
* For an overview of how similar research is done with MRI images, I recommend reading Manzano-Patron et al., 2024 (https://doi.org/10.1162/imag_a_00060)
* In case you find any issue with the code or have any follow up questions, feel free to reach out to me at mr.pullur@unitn.it
* Warning: It is normal for the PCA to take longer durations to complete due to differing computer specifications or network issues.

