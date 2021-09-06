# Traffic Sign Classification using LE-NET DEEP NETWORK

![traffic signs](https://user-images.githubusercontent.com/50113394/132258226-4fe86c17-9413-40ea-bf3a-7c659b2a7e6f.PNG)

## Introduction

Traffic sign classification is an important task for self driving cars.  
In this project, a Deep Network known as LeNet will be used for traffic sign images classification.  
The dataset contains 43 different classes of images.  

Classes are as listed below:

0 - Speed limit (20km/h)  
1 - Speed limit (30km/h)  
2 - Speed limit (50km/h)   
3 - Speed limit (60km/h)   
4 - Speed limit (70km/h)   
5 - Speed limit (80km/h)   
6 - End of speed limit (80km/h)   
7 - Speed limit (100km/h)   
8 - Speed limit (120km/h)   
9 - No passing   
10 - No passing for vehicles over 3.5 metric tons   
11 - Right-of-way at the next intersection   
12 - Priority road   
13 - Yield   
14 - Stop   
15 - No vehicles   
16 - Vehicles over 3.5 metric tons prohibited  
17 - No entry  
18 - General caution   
19 - Dangerous curve to the left  
20 - Dangerous curve to the right  
21 - Double curve  
22 - Bumpy road  
23 - Slippery road  
24 - Road narrows on the right  
25 - Road work  
26 - Traffic signals  
27 - Pedestrians   
28 - Children crossing  
29 - Bicycles crossing  
30 - Beware of ice/snow  
31 - Wild animals crossing  
32 - End of all speed and passing limits  
33 - Turn right ahead  
34 - Turn left ahead   
35 - Ahead only     
36 - Go straight or right  
37 - Go straight or left   
38 - Keep right   
39 - Keep left  
40 - Roundabout mandatory   
41 - End of no passing  
42 - End of no passing by vehicles over 3.5 metric tons  

## Data Exploration

TODO: Images

## LENET Network Architecture

![LENET](https://user-images.githubusercontent.com/50113394/132258154-3d150459-af47-4003-83c2-930ad9bb0d9c.png)

### STEP 1: THE FIRST CONVOLUTIONAL LAYER #1  
    Input = 32x32x1  
    Output = 28x28x6  
    Output = (Input-filter+1)/Stride* => (32-5+1)/1=28  
    Used a 5x5 Filter with input depth of 3 and output depth of 6  
    Apply a RELU Activation function to the output  
    pooling for input, Input = 28x28x6 and Output = 14x14x6  

### STEP 2: THE SECOND CONVOLUTIONAL LAYER #2
    Input = 14x14x6 
    Output = 10x10x16 
    Layer 2: Convolutional layer with Output = 10x10x16 
    Output = (Input-filter+1)/strides => 10 = 14-5+1/1 
    Apply a RELU Activation function to the output 
    Pooling with Input = 10x10x16 and Output = 5x5x16 

### STEP 3: FLATTENING THE NETWORK
    Flatten the network with Input = 5x5x16 and Output = 400 

### STEP 4: FULLY CONNECTED LAYER
    Layer 3: Fully Connected layer with Input = 400 and Output = 120 
    Apply a RELU Activation function to the output 

### STEP 5: ANOTHER FULLY CONNECTED LAYER
    Layer 4: Fully Connected Layer with Input = 120 and Output = 84 
    Apply a RELU Activation function to the output 

### STEP 6: FULLY CONNECTED LAYER
    Layer 5: Fully Connected layer with Input = 84 and Output = 43

## Model Evaluation

TODO: Evaluation

## Model Deployment

Model was deployed using Amazone Web Services (AWS) EC2 instance on an Ubuntu server and can be viewed here: TODO: Website
