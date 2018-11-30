from numpy import array
from keras.preprocessing.text import Tokenizer
from keras.utils import to_categorical
from keras.preprocessing.sequence import pad_sequences
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers import Embedding


class Training:
	def __init__(self, corpus_path):
		self.vocal_size = 0
		self.max_length = 0
		self.corpus_path = corpus_path
		self.X = 0
		self.y = 0
		self.tokenizer = Tokenizer()
		self.data_preprocess()


	def data_preprocess(self):
		# corpus
		with open(self.corpus_path) as f:
			data = f.read()
			# prepare the tokenizer on the source text
			self.tokenizer.fit_on_texts([data])
			# determine the vocabulary size
			self.vocab_size = len(self.tokenizer.word_index) + 1
			# create line-based sequences
			sequences = list()
			for line in data.split('\n'):
				encoded = self.tokenizer.texts_to_sequences([line])[0]
				for i in range(1, len(encoded)):
					sequence = encoded[:i+1]
					sequences.append(sequence)
			# pad input sequences
			self.max_length = max([len(seq) for seq in sequences])
			sequences = pad_sequences(sequences, maxlen=self.max_length, padding='pre')
			# split into input and output elements
			sequences = array(sequences)
			self.X, y = sequences[:,:-1],sequences[:,-1]
			self.y = to_categorical(y, num_classes=self.vocab_size)


	# generate a sequence from a language model
	def generate_seq(self, model, seed_text, n_words):
		in_text = seed_text
		# generate a fixed number of words
		for _ in range(n_words):
			# encode the text as integer
			encoded = self.tokenizer.texts_to_sequences([in_text])[0]
			# pre-pad sequences to a fixed length
			encoded = pad_sequences([encoded], maxlen=self.max_length-1, padding='pre')
			# predict probabilities for each word

			yhat = model.predict_classes(encoded, verbose=0)
			# map predicted word index to word
			out_word = ''
			for word, index in self.tokenizer.word_index.items():
				if index == yhat:
					out_word = word
					break
			# append to input
			in_text += ' ' + out_word
		return in_text

	def train_model(self):
		# define model
		model = Sequential()
		model.add(Embedding(self.vocab_size, 10, input_length=self.max_length-1))
		model.add(LSTM(50))
		model.add(Dense(self.vocab_size, activation='softmax'))
		# compile network
		model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
		# fit network
		model.fit(self.X, self.y, epochs=700, verbose=2)
		return model
