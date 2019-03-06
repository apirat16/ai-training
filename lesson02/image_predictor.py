from imageai.Prediction.Custom import CustomImagePrediction
import os

execution_path = os.getcwd()

prediction = CustomImagePrediction()
prediction.setModelTypeAsResNet()
'''
prediction.setModelPath("idenprof_061-0.7933.h5")
prediction.setJsonPath("idenprof_model_class.json")
prediction.loadModel(num_objects=10)
'''
prediction.setModelPath("idenprof/models/model_ex-001_acc-0.326250.h5")
prediction.setJsonPath("idenprof/json/model_class.json")
prediction.loadModel(num_objects=4)

predictions, probabilities = prediction.predictImage("images/image02.jpg", result_count=3)

for eachPrediction, eachProbability in zip(predictions, probabilities):
    print(eachPrediction, " : ", eachProbability)
