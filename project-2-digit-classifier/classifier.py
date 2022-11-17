import data

# Task 1: visualisation
# Visualise a 28x28 image represented as python lists
def draw(image):
    pass

# Task 2: Learning formula
def learn(x, expected, predicted, m):
    pass

# Task 3: flatten
# Input: a list of list of floats
# Output: the concatenated list
# Example:
#     Input: [[1, 2, 3], ['a',5], [], ['b',7]]
#     Output: [1, 2, 3, 'a', 5, 'b', 7]
def flatten(xss):
    pass

# Task 4: dot product
# Returns the dot product of two vectors of the same length
# Example:
#     Input: dot([3, 4, 5], [6, 7, 8])
#     Output: 3*6 + 4*7 + 5*8 == 86
# m[0] * x[0] + m[1] * x[1] + ... + m[n-1] * x[n-1]
def dot(m, x):
    pass

# Task 5: 
# Returns a list of length n consisting random numbers from -1.0 to 1.0
# Hint: use the `random' library
# Example:
#     Input: generate_classifier(5)
#     Output: [-0.583, -0.423, 0.982, -0.232, 0.135]
def new_classifier(n):
    pass

# Task 6: prediction function
# A classifier is a vector [m0, m1, ..., mn]
# If the dot product of the classifier with the input >= 0, then 1.0 (true) else 0.0 (false)
def run_classifier(m, x):
    pass

# Task 7: building classifiers
# We initiate 10 classifiers, one for each digit.
ms = [] # Implement this

# Task 8:
# Iterate from 0 to 9, if the ms[i]-th classifier returns
# 1, then the predicted digit is i.
# If none of them returned 1, then return an arbitrary digit (e.g. return 0).
def predict(image):
    return 3

# Task 9:
# Train the variable `image' according to its corresponding digit
def train(image, digit):
    pass

# Task 10:
# Train the entire dataset using the variables `data.images' and `data.digits'
for i in range(1):
    pass

# Check the accuracy here:
correct = 0
how_many_testing_images = len(data.images_for_testing)
for i in range(how_many_testing_images):
    image = data.images_for_testing[i]
    draw(image)
    expected_digit = data.digits_for_testing[i]
    predicted_digit = predict(flatten(image))
    print('Predicted:', predicted_digit, '| Expected:', expected_digit)
    if predicted_digit == expected_digit:
        correct += 1
accuracy = correct / how_many_testing_images
print('Accuracy:', accuracy)

