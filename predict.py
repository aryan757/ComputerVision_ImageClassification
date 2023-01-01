#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 18:45:05 2020

@author: sudhanshukumar
"""

import numpy as np
from keras.models import load_model
from keras.preprocessing import image

class dogcat:
    def __init__(self,filename):
        self.filename =filename


    def predictiondogcat(self):
        # load model
        model = load_model('model.h5')

        # summarize model
        #model.summary()
        imagename = self.filename
        test_image = image.load_img(imagename, target_size = (64, 64))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis = 0)
        result = model.predict(test_image)
        pred = result.argmax()


        if pred == 0:
            prediction = 'daisy'
            return [{ "image" : prediction}]
        elif pred == 1:
            prediction = 'danadalin'
            return [{ "image" : prediction}]
        elif pred == 2:
            prediction = 'rose'
            return [{ "image" : prediction}]
        elif pred == 3:
            prediction = 'sunflower'
            return [{ "image" : prediction}]
        elif pred == 4:
            prediction = 'tulip'
            return [{ "image" : prediction}]



        #predict = model.predict(np.array(checkImage))

        #output = {0: 'daisy', 1: 'dandelion', 2: 'rose', 3: 'sunflower',4:'tulip'}

        #print("Actual :- ", checklabel)
        #print("Predicted :- ", output[np.argmax(predict)])

        #return [{"image":output[np.argmax(result[0][0])]}]



        #if result[0][0] == 0:
           # prediction = 'daisy'
           # return [{ "image" : prediction}]
        #elif result[0][0] == 1:
           # prediction = 'dandelion'
            #return [{"image" : prediction}]
        #elif result[0][0] == 2:
           # prediction = 'rose'
            #return [{"image" : prediction}]
        #elif result[0][0] == 3:
          #  prediction = 'sunflower'
           # return [{"image" : prediction}]
        #else:
           # prediction = 'tulip'
           #return [{"image" : prediction}]

        #else:
           # prediction = 'cat'
           # return [{ "image" : prediction}]

        #if result[0][0] == 1:
            #prediction = 'daisy'
            #return [{ "image" : prediction}]
        #elif result[0][1] == 1:
           # prediction = 'danadalin'
           # return [{ "image" : prediction}]
        #elif result[0][2] == 1:
          #  prediction = 'rose'
          #  return [{ "image" : prediction}]
        #elif result[0][3] == 1:
         #   prediction = 'sunflower'
          #  return [{ "image" : prediction}]
       # else:
          #  prediction = 'tulip'
          #  return [{ "image" : prediction}]






