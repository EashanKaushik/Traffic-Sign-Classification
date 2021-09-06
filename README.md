# Traffic Sign Classification using LE-NET DEEP NETWORK

TODO: Badges

## Introduction

Traffic sign classification is an important task for self driving cars.  
In this project, a Deep Network known as LeNet will be used for traffic sign images classification.  
The dataset contains 43 different classes of images.  

Classes are as listed below:

1. ( 0, b'Speed limit (20km/h)')  
2. ( 1, b'Speed limit (30km/h)')
3. ( 2, b'Speed limit (50km/h)') 
4. ( 3, b'Speed limit (60km/h)') 
5. ( 4, b'Speed limit (70km/h)') 
6. ( 5, b'Speed limit (80km/h)') 
7. ( 6, b'End of speed limit (80km/h)') 
8. ( 7, b'Speed limit (100km/h)') 
9. ( 8, b'Speed limit (120km/h)') 
10. ( 9, b'No passing') 
11. (10, b'No passing for vehicles over 3.5 metric tons') 
12. (11, b'Right-of-way at the next intersection') 
13. (12, b'Priority road') 
14. (13, b'Yield') 
15. (14, b'Stop') 
16. (15, b'No vehicles') 
17. (16, b'Vehicles over 3.5 metric tons prohibited')
18. (17, b'No entry')
19. (18, b'General caution') 
20. (19, b'Dangerous curve to the left')
21. (20, b'Dangerous curve to the right')
22. (21, b'Double curve')
23. (22, b'Bumpy road')
24. (23, b'Slippery road')
25. (24, b'Road narrows on the right')
26. (25, b'Road work')
27. (26, b'Traffic signals')
28. (27, b'Pedestrians') 
29. (28, b'Children crossing')
30. (29, b'Bicycles crossing')
31. (30, b'Beware of ice/snow')
32. (31, b'Wild animals crossing')
33. (32, b'End of all speed and passing limits')
34. (33, b'Turn right ahead')
35. (34, b'Turn left ahead') 
36. (35, b'Ahead only') 
37. (36, b'Go straight or right')
38. (37, b'Go straight or left') 
39. (38, b'Keep right') 
40. (39, b'Keep left')
41. (40, b'Roundabout mandatory') 
42. (41, b'End of no passing')
43. (42, b'End of no passing by vehicles over 3.5 metric tons')

TODO: Image Traffic

## LENET Network Architecture

TODO: LENET Image

STEP 1: THE FIRST CONVOLUTIONAL LAYER #1  
    Input = 32x32x1   
    Output = 28x28x6 
    Output = (Input-filter+1)/Stride* => (32-5+1)/1=28 
    Used a 5x5 Filter with input depth of 3 and output depth of 6 
    Apply a RELU Activation function to the output 
    pooling for input, Input = 28x28x6 and Output = 14x14x6 

STEP 2: THE SECOND CONVOLUTIONAL LAYER #2
    Input = 14x14x6 
    Output = 10x10x16 
    Layer 2: Convolutional layer with Output = 10x10x16 
    Output = (Input-filter+1)/strides => 10 = 14-5+1/1 
    Apply a RELU Activation function to the output 
    Pooling with Input = 10x10x16 and Output = 5x5x16 

STEP 3: FLATTENING THE NETWORK
    Flatten the network with Input = 5x5x16 and Output = 400 

STEP 4: FULLY CONNECTED LAYER
    Layer 3: Fully Connected layer with Input = 400 and Output = 120 
    Apply a RELU Activation function to the output 

STEP 5: ANOTHER FULLY CONNECTED LAYER
    Layer 4: Fully Connected Layer with Input = 120 and Output = 84 
    Apply a RELU Activation function to the output 

STEP 6: FULLY CONNECTED LAYER
    Layer 5: Fully Connected layer with Input = 84 and Output = 43

## Model Evaluation

TODO: Evaluation

## Model Deployment

Model was deployed using Amazone Web Services (AWS) EC2 instance on an Ubuntu server and can be viewed here: TODO: Website
