# ECommerce-Marketplace-Automation

You are a Data Scientist at the "Marketplace" company, which intends to launch an e-commerce marketplace.

Company logo: Marketplace
On the marketplace, sellers offer items to buyers by posting a photo and a description.

Currently, the categorization of an item is done manually by the sellers, making it unreliable. Additionally, the volume of items is currently very small.

To make the user experience for both sellers (facilitating the uploading of new items) and buyers (simplifying product searches) as smooth as possible, and with scalability in mind, it becomes necessary to automate this task.

Linda, Lead Data Scientist, asks you to study the feasibility of a product classification engine into different categories with sufficient precision.

Here is the email she sent you:

Hello,

Thank you for your assistance on this project!

Your mission is to conduct, in a first iteration, a feasibility study of a product classification engine based on an image and a description, for the automation of item categorization.

You must analyze the textual descriptions and images of the products through the following steps:

Preprocessing of textual or image data as appropriate.
Feature extraction.
Dimension reduction to 2 dimensions to project the products onto a 2D graph, with colors corresponding to the actual category.
Analysis of the graph to determine, with the help of descriptions or images, the feasibility of automatically grouping products of the same category.
Implementation of a measure to confirm your visual analysis by calculating the similarity between the actual categories and the categories resulting from segmentation into clusters.
Can you demonstrate, through this approach, the feasibility of automatically grouping products of the same category?

Here are the constraints:

To extract textual features, it will be necessary to implement:

Two "bag-of-words" approaches, simple word counting, and Tf-idf.
A classic word/sentence embedding approach with Word2Vec (or Glove or FastText).
A word/sentence embedding approach with BERT.
A word/sentence embedding approach with USE (Universal Sentence Encoder).

To extract image features, it will be necessary to implement:

An algorithm of the SIFT/ORB/SURF type.
A CNN Transfer Learning type algorithm.
Regarding the SIFT-type approach, I invite you to watch the webinar we conducted, available in the resources.

Thank you again,

Linda

PS: I have confirmed that there are no intellectual property constraints on the data and images.

Attachments:

Initial dataset of items with a link to download the photo and associated description.

One week later, you share your work with Linda, and she responds enthusiastically with another request:

Hello,

Thank you very much for your work!

Congratulations on demonstrating the feasibility of automatically grouping products of the same category!

Now, I suggest moving on to the second iteration. Could you perform supervised classification based on the images? I would like you to implement data augmentation to optimize the model.

We want to expand our range of products, especially in fine grocery. Could you test the collection of "champagne" based products via the API available here? I would like you to provide us with an extraction of the first 10 products in a ".csv" file, containing for each product the following data: foodId, label, category, foodContentsLabel, image.

Thank you again,
