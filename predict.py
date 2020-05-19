from tensorflow.keras.models import load_model
import numpy as np
import json

model = load_model(
    "model.h5",
    custom_objects=None,
    compile=False
)

### these are the examples to be replaced by requests
with open('request.json', 'r') as f:
    observation = json.load(f)['bitcoin_last_minute']
####


def format_data(event):
    return np.array(list(event.values())).reshape(1, 359) # how can we not hardcode the ndarray shape?


def predict(model, observation):
    formatted_data = format_data(observation)
    return model.predict(formatted_data)


def format_prediction(prd):
    return {
        'bitcoin_prediction': prd[0][0]
    }


prediction = predict(model, observation)
print(format_prediction(prediction))
