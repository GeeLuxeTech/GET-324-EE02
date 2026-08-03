# GET-324-EE02
EE02 project for GET 324: AI &amp; Machine learning 
23/EG/EE/010
23/EG/EE/060
23/EG/EE/120
My team and I have been given a real-world problem to solve using artificial intelligence (AI). Our specific task is to build a "smart eye" that can look at a photo of a tomato leaf and tell us whether the plant is healthy or infected with a common virus called Tomato Mosaic Virus. This kind of tool could really help farmers catch diseases early and save their crops.

My main responsibility in the team was preparing and cleaning up the data that the AI learns from. Think of it like this: if you're teaching a child to tell the difference between apples and oranges, you wouldn't give them blurry or confusing pictures. You'd make sure the images are clear and properly labeled. That's exactly what I did. I gathered hundreds of tomato leaf images from online sources, sorted them into "healthy" and "sick" folders, resized them so they were all the same format, and removed any low-quality or mislabeled photos. I also had to make sure the dataset was balanced meaning we had roughly the same number of healthy and sick images so the AI wouldn't develop a bias toward one type.

Once the data was clean and organized, the team used it to train a Convolutional Neural Network (CNN), which is a type of AI specially designed for image recognition. We fed it thousands of pictures like showing flashcards to a student until they learn to spot the difference. After the AI got good at recognizing patterns, we packaged it into a simple website using a tool called Streamlit, where anyone can upload a photo and get an instant answer.

We also kept all our work organized on GitHub (think of it like Google Docs for code) and made sure the app works in the cloud so people can access it from anywhere whether they're on a farm or in a lab. The whole experience taught me that building AI isn't just about writing code; it's about getting your hands dirty with the data first. Without clean, well-prepared data, even the smartest AI would fail. I'm proud that my groundwork helped the team build a tool that could one day make a real difference for farmers.
