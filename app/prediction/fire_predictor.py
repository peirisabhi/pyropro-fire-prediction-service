import pickle

#temp	RH	wind	rain

def prediction(lst):
    filename = 'C:\projects\icbt\pyropro\pyropro-fire-prediction-service\model\svm.SVC_predictor_9936.pickle'
    with open(filename, 'rb') as file:
        model = pickle.load(file)
    pred_value = model.predict([lst])
    return pred_value


# val = prediction([33, 51, 0, 0.0])
# print(val)
