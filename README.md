**E-commerce Marketplace Automation**

Welcome to the E-commerce Marketplace Automation project repository! In the rapidly evolving world of online marketplaces, efficient product categorization is crucial for both sellers and buyers. This repository contains a comprehensive solution aimed at automating the categorization process to enhance user experiences and pave the way for scalability.

**Objective:**
The primary goal is to create a robust engine that classifies products into different categories based on images and descriptions. The focus is on improving accuracy and scalability to accommodate a growing volume of products.

**Key Features:**
- **Textual Data Processing:**
  - Utilization of "bag-of-words" approaches (simple word counting and Tf-idf).
  - Integration of classic word/sentence embedding techniques with Word2Vec, Glove, FastText, BERT, and USE (Universal Sentence Encoder).
  
- **Image Data Processing:**
  - Implementation of SIFT (Scale-Invariant Feature Transform), ORB (Oriented FAST and Rotated BRIEF), and SURF (Speeded-Up Robust Features) algorithms.
  - Utilization of CNN Transfer Learning for image feature extraction.

**Workflow:**
1. **Data Preprocessing:**
   - Cleaning and organizing textual and image data.

2. **Feature Extraction:**
   - Extracting relevant features from both textual descriptions and images.

3. **Dimension Reduction:**
   - Reducing feature dimensions to 2D for visualization.

4. **Clustering Analysis:**
   - Analyzing clusters on a 2D graph to explore the feasibility of automatic grouping.

5. **Supervised Classification (Second Iteration):**
   - Implementing supervised classification based on images.
   - Introduction of data augmentation techniques to optimize the model.

**Usage:**
1. Clone the repository.
2. Refer to the provided example notebooks for implementation details.
3. Utilize the attached datasets as a starting point.

**Dependencies:**
- Python
- Jupyter Notebooks
- Required libraries (e.g., scikit-learn, TensorFlow, OpenCV)

  **Data Set:** https://s3-eu-west-1.amazonaws.com/static.oc-static.com/prod/courses/files/Parcours_data_scientist/Projet+-+Textimage+DAS+V2/Dataset+projet+pre%CC%81traitement+textes+images.zip

**EDAMAN API:** https://rapidapi.com/edamam/api/edamam-food-and-grocery-database
