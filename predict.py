from keras import models
from keras import Sequential
from keras.preprocessing.text import Tokenizer
from train import Training
import sys
import argparse

# parser = argparse.ArgumentParser(description='Train the word model.')
# parser.add_argument('-num_words', dest='n_words', type=str, required=True, help='Number of words to predict.')
# parser.add_argument('-load_model', dest='load_model', type=str, required=True, help='Path to save the model.')
# args = parser.parse_args()
file_path = input("Enter the path of corpus (include file extension): ")
model_path = input("Enter the path to your pretrained model (Leave blank if none): ")

valid = {"yes": True, "y": True, "ye": True,
             "no": False, "n": False}
model = Sequential()
train = Training(file_path)
try:
    model = models.load_model(model_path)
except ValueError:
    isTrain = input("Model not found! Do you want to train a new model? (yes/no): ")
    if valid[isTrain]:
        model = train.train_model()
        print("Training Done!")
    else:
        print("Thank you for using this tool.")
        sys.exit()
print()
seed_words = input("Enter your input: ")
num_words = int(input("Enter number of words to predict: "))   
print()
result = train.generate_seq(model, seed_words, num_words)
print(result)
print()
print("(Hint) Type /c to change number of words to predict")
print("To quit, type /q")
print() 
if seed_words == "/c":
    num_words = int(input("Enter number of words to predict: "))
elif seed_words == "/q":
    seed_words = ""
while seed_words != "":
    seed_words = input("You: ")
    if seed_words == "/c":
        num_words = int(input("Enter number of words to predict: "))
        continue 
    elif seed_words == "/q":
        break
    result = train.generate_seq(model, seed_words, num_words)
    print(result)

isSave = input("Do you want to save your model? (yes/no)")
if valid[isSave]:
    model_name = input("Enter the model name(No file extension): ")
    model.save(model_name+'.h5')
else:
    print("Thank you for using this tool.")
