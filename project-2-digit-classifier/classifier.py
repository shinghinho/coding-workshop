import data

def classify(image):
    # Task: implement an AI to recognize the digit!
    return 5 # Right now we're classifying everything as the digit `5`


# We compute the accuracy of our classifier as follows:
correct = 0
how_many_testing_images = len(data.images_for_testing)
for i in range(how_many_testing_images):
    image = data.images_for_testing[i]
    expected_digit = data.digits_for_testing[i]
    predicted_digit = classify(image)
    if predicted_digit == expected_digit:
        correct += 1
accuracy = correct / how_many_testing_images
print('Accuracy:', accuracy)
