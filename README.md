# ml-engineer-challenge

Welcome! The following challenge is to evaluate your strengths as a machine learning engineer. The expectation is not that you would finish all of this, but represents all of the sorts of problems you might expect at Penn Interactive. You should limit the exercise to no more than a few hours. When you're finished put your code in a VCS of your choice.

## Problem Statement

We are creating a machine learning API that will predict the price of Bitcion in USD in the next second based on the price from the last 60 seconds. You will find a Jupyter notebook named `bitcoin-predictor.ipynb`. Feel free to add/change anything in that notebook, it's yours to play with (more on that below). This is where all of the data pre-processing and training was done. The goal is to use what is in there to create a RESTful API with a `/predict` endpoint, so that I can send a payload of bitcoin data from the last 60 seconds and return a prediction. There is a file called `predict.py` that will contain the minimal logic to predict from an example at `request.json`; you can use this as your jumping off point.

You can start with the saved model in HDFS format at `model.h5`.

* For the request, see `request.json`. You'll see that it is a JSON object with the key `bitcoin_last_minute`, which is an array of pricing data, each element of the array represents 1 second. You can assume that the order of the array is in ascending time order, but do not assume that the keys of each element are ordered correctly (though they may be in this specific request), so your API should sort the data to conform to the features matrix you see in training.
* Where the API lives is not important, it can be a docker container, hosted on AWS, GCP, Heroku, etc. so long as you can `POST` to `/predict` using `request.json` and the return response should look like the example in `response.json`. You can add anything else you want to the response payload, but it must have a `"bitcoin_prediction"` key. **NOTE: The prediction in the response example is just made up, you don't have to match this exact number.**

## Extra Considerations

We have a service up and running in `production`. Now it's time to iterate on this. Pick as many of the following tasks you'd like to tackle and include them in the work you've done so far. There are a number of questions sprinkled in the jupyter notebook and the `predict.py` that you could also tackle.

* How do we write good tests (unit, integration) for this machine learning service?
* Can we add an endpoint just to check that the API is up?
* The model is up and running. How do we know if it's being used?
* How often does it error out? How many 5xx? How many 4xx?
* How accurate is the model? We can see how accurate the training and validation sets are, but can we include an endpoint to measure how accurate it was in the last 60 seconds?
* What version is the API on and how do we know? Is this the same as the model version? Do we need both?
* The jupyter notebook is a nice format for quick work, but we don't want to have to run this on our laptop each time we train. Can you create a job for it to run in a different compute environment?
* Can you make the model more accurate? Some things you could consider:
  * Is the neural network architecture correct?
  * Is a different model appropriate?
  * Do we have the right loss metric?
  * Do we have the right optimizer?
  * Do we have the right feature set? More features? Less features? Better features?
  * Do we need to go longer than a 60 second lookback? Shorter?
  * Is there any scaling or preprocessing we're missing?
* Once we've trained it in batch several times and we're comfortable with the stability of the model we've chosen, we'll want to be able to train online. Can you create a `/train` endpoint where we can send data to retrain the model.
* How many concurrent executions is this API capable of handling? Is it thread safe? If we have a `/train` endpoint and a `/predict` endpoint will they collide? If we train and predict at the same time, which version of the model is the prediction coming from?
* Tensorflow throws a lot of Future warnings and CPU warnings at runtime. Can we fix the code so these warnings go away?


## Note on Dependencies

Feel free to install dependencies however you wish (docker, pyenv, conda, etc.). This model was trained in a conda virtual environment, and you can find all of the details in the `spec-file.txt` (the output of `conda list`) file or the explicit packages in `spec-file-explicit.txt` (the output of `conda list --explicit`). You may upgrade/downgrade dependencies as you see fit, as long as it doesn't effect the solution.
