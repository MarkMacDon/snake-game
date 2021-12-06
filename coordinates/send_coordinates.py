# this code takes the raw output of the snake body and food array,
# and packages them into a format ready for sending to the raspberry pi

import numpy as np
import os
import requests
import constants as c


def output(body, food):
    # makes a numpy array containing n elements, 
    # first n-1 elements are body, the final element
    # is the food. 
    # Each element contains three numbers corresponding to x, y, z coordinates
    # in the range from 0 to res

    # convert food from p5.Vector to np.array
    lights = np.append(body, food)
    lights = np.reshape(lights, (len(body)+1, 1, 3))

    lightsStr = ','.join(str(x) for x in lights) # '0,3,5'
    url = f'http://{c.IP_ADDRESS}:{c.PORT}/'
    headers = {'Content-type': 'application/json'}
    body = {'coordinates': lightsStr}
    postRes = requests.post(url, headers=headers, json=body)
    # print(postRes.status_code)
    # print(postRes.content)
