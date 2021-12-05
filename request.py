import requests
import time
import json

class HttpInput:
    def __init__(self, framerate=0.001):

        # self.url = "http://192.168.1.72:8080/"
        self.url = "http://localhost:8081"
        self.framerate = framerate
        self.parsed_input = ""
        self.unparsed_input = ""
    

    def get_input(self):
        while True:
            request = requests.get(self.url)
            self.unparsed_input = ""
            if request.encoding is None:
                request.encoding = 'utf-8'
            for line in request.iter_lines(decode_unicode=True):
                if line:
                    self.unparsed_input += str(line)
            self.parse_input()
            time.sleep(self.framerate)
            return self.parsed_input

    
    def parse_input(self):
        if "Up" in self.unparsed_input:
            self.parsed_input = "Up"
        if "Down" in self.unparsed_input:
            self.parsed_input = "Down"
        if "Left" in self.unparsed_input:
            self.parsed_input = "Left"
        if "Right" in self.unparsed_input:
            self.parsed_input = "Right"        

        
