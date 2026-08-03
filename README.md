# GET-324-EE02
EE02 project for GET 324: AI &amp; Machine learning 
23/EG/EE/010
23/EG/EE/060
23/EG/EE/120

23/EG/EE/030
Our team developed an AI powered image classification system to distinguish between healthy tomato leaves and tomato leaves infected with Tomato Mosaic Virus. We selected this problem because early disease detection is important for improving crop health and reducing agricultural losses. The first step was gathering a suitable dataset containing images of both healthy and infected tomato leaves, after which we carefully organized the images into their respective classes.

Before training the model, we preprocessed the dataset by removing poor quality images, resizing every image to the same dimensions, and normalizing the pixel values. We then divided the dataset into training, validation, and testing sets to ensure that the model could be evaluated fairly. During this stage, we faced challenges with inconsistent image quality and class imbalance, but we improved the dataset through careful cleaning and preparation.

Next, we built a Convolutional Neural Network using TensorFlow and Keras for the binary classification task. The model was trained over several epochs while we monitored both the training and validation accuracy to understand its learning progress. We adjusted important parameters such as the learning rate, batch size, and optimizer to improve performance and reduce overfitting, which helped us achieve more reliable predictions.

After training, we evaluated the model using unseen test images to measure its accuracy and overall performance. We carefully analyzed the results, identified areas where the model made incorrect predictions, and refined the training process to improve its ability to correctly classify healthy and infected tomato leaves. This iterative process allowed us to produce a more accurate and dependable model.

Finally, we integrated the trained model into a Streamlit web application that allows users to upload a tomato leaf image and instantly receive a prediction. We tested the application extensively, fixed deployment issues, and successfully hosted it on a cloud platform. Through teamwork, continuous testing, and effective collaboration, we successfully developed a practical AI solution that demonstrates how deep learning and cloud computing can be applied to real world agricultural disease detection.

23/EG/EE/040
23/EG/EE/080
23/EG/EE/090
23/EG/EE/050
Model Evaluation

The trained Convolutional Neural Network (CNN) model was evaluated using a separate test dataset to assess its performance on unseen images. Several evaluation metrics, including accuracy, precision, recall, and F1-score, were used to measure the model's effectiveness in classifying the two image categories. In addition, a confusion matrix was generated to provide a detailed analysis of the model's predictions by showing the numbers of true positives, true negatives, false positives, and false negatives. The evaluation results indicated that the model achieved high classification performance and demonstrated good generalization on unseen data. The low number of misclassified images showed that the model learned meaningful features from the training dataset. Overall, the evaluation confirmed that the model is reliable, accurate, and suitable for deployment as a cloud-based binary image classification application.
