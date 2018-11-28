In this project, we implemented a word prediction AI which will read lines of a given prompt and
can predict the an alloted number of words that are after the inputed value. Running the program
requires the user to download python3, tensorflow, and keras prior to opening it in any given 
python3 compiling program.

The corpus provided is the nursery rhyme "Humpty Dumpty", however, if the user wishes to use a 
different phrase, the file can be edited. The requirement of the corpus is that whatever is 
contained in it must have individual lines seperating parts of the phrase. An example is provided 
below:

Baa, baa, black sheep,
Have you any wool?
Yes sir, yes sir,
Three bags full.
One for the master,
One for the dame,
And one for the little boy
Who lives down the lane
  


Instructions:
*The user will call on the folder containing the project, and then, using the command
 "python3 predict.py" will open the project itself.

*Once asked for the corpus, the user must provide the full name of the corpus they want to use 
(i.e. corpus.txt).

*When the model is to be provided, the user may either use the provided model (model.h5), use 
 one they had previously trained, or leave the space blank to be asked if they wish to create a 
 new model. Answering yes will create a new model, and answering no will cancel the program.

*The user will be asked for an input, which should be any part of the corpus provided.

*The user will be asked for the amount of words to be predicted, which should only be the amount
 of words left after the phrase typed in. An easy example being in Humpty Dumpty: if the user 
 wishes to input "all the kings", then the user can predict between 1-6 words since there are 6 
 words after the input. The longer the input phrase, the more accurate the prediction tends to be.  

*After the output is provided, the user can change the number of words predicted by typing "/c"
 or they may quit the program with "/q"

*If the user created a new model is quits, the user will be asked if they wish to save their new
 model. If saved, the model, which can be given a custom name, will be saved among the other 
 component files of the program. The extension (.h5) is not necessary to type in alongside the 
 name of the newly created model. 



An example of how the program should run is provided below, the quotation marks indicating input 
from the user.



Enter the path of corpus (include file extension): "corpus.txt"
Enter the path to your pretrained model (Leave blank if none): "model.h5"

Enter your input: "all the"
Enter number of words to predict: "3"

all the king's horses and

(Hint) Type /c to change number of words to predict
To quit, type /q
