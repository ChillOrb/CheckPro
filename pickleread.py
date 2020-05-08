import pickle


with open('classifier.pkl', 'rb') as f:
    data = pickle.load(f)

    print(data)
