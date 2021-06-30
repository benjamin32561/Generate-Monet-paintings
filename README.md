# Generate-Van-Gogh-painting
This project is a Deep learning model used to convert images to monet style paintings, the whole project is written in Python and using the Tensorflow 2 library

## Installation
Download the repository and run `pip install -r requirements.txt` to install all the required libraries

## Usage
To use the model to generate paintings run the `useGenerator.py` code.
example: `python useGenerator.py model/generator.h5 test_images/test1.jpg`
the first parameter is the location of the generator, the second one is the location of the image to convert.

## Model architecture
The generator model is a trained VGG19 model without the Sequential head connected to a not-trained flipped (from end to start) VGG19 model, pretty simular to an Auto Encoder architecture but without the Dense layer in the middle.

## Work process
At first I tried to build it using CycleGAN, Som errors accurd so i tried to tackle the problam using simple GAN, it worked fine but didnt add colors to the results, then I returned to the CycleGan and made it work.

## Dataset
Got the dataset from Kaggle, [I’m Something of a Painter Myself](https://www.kaggle.com/c/gan-getting-started), cleaned it a little bit for my needs, You can find my final dataset [here](https://drive.google.com/drive/folders/135ophtAeOyMY1hqLUXbVDjf8-TlGxtTM?usp=sharing), Its splitted to landskape and paintings already in numpy files, the images are 256 256 3.

## Results
All of the presented examples are new photos I found online, They are not even a part of the dataset!

![First example](https://github.com/benjamin32561/Generate-Monet-paintings/blob/main/results_images/1.jpg)

![Second example](https://github.com/benjamin32561/Generate-Monet-paintings/blob/main/results_images/2.jpg)

![Third example](https://github.com/benjamin32561/Generate-Monet-paintings/blob/main/results_images/3.jpg)
