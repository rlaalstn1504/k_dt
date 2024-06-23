# streamlit 파일을 demo 폴더 안과 밖 모두 다 경로문제없이 실행하기 위해 path 추가
import os
import sys
parent_dir = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
sys.path.append(parent_dir)
sys.path.append(os.getcwd())

import streamlit as st


import glob
import numpy as np
import random
import json
import argparse
from pathlib import Path

import ffmpeg

import openai
from dotenv import load_dotenv 
load_dotenv()

import os
print(os.getcwd())
API_KEY = os.getenv("API_KEY")
openai.api_key = API_KEY
def ask_gpt3(question):
    response = openai.ChatCompletion.create(
        #model="gpt-4-turbo-preview", # 챗 모델을 사용하는 경우 적절한 모델 이름으로 변경
        model="gpt-3.5-turbo", # 챗 모델을 사용하는 경우 적절한 모델 이름으로 변경
        messages=[
            #{"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": question}
        ],
        max_tokens=150,
        temperature=0.7,
    )
    return response.choices[0].message.content

a = ask_gpt3("sda")
print(a)
