# streamlit 파일을 demo 폴더 안과 밖 모두 다 경로문제없이 실행하기 위해 path 추가
import os
import sys
parent_dir = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
sys.path.append(parent_dir)
sys.path.append(os.getcwd())

import streamlit as st
import pandas as pd

import csv
import glob
import numpy as np
import example
from pathlib import Path
import folium
from streamlit_folium import folium_static
from datetime import datetime

import openai
from dotenv import load_dotenv 
load_dotenv()


API_KEY = os.getenv("API_KEY")
openai.api_key = API_KEY
map_showing = False
exam_showing = True
link = 'http://192.168.0.26:8502/' # reserve.py 를 실행한 서버의 ip와 포트로 직접 변경

# 세션 상태 초기화
if 'show_examples' not in st.session_state:
    st.session_state.show_examples = True
    
def handle_example_clicked(index):
    # 이미지 클릭 처리 함수
    st.session_state.show_examples = False
    st.session_state.selected_example = index
    st.experimental_rerun()
    
def get_project_root() -> str:
    """Returns project root path."""
    return str(Path(os.path.abspath(__file__)).parent)

def time_now():
    return datetime.now()

def ask_gpt3(question):
    question_edited = f"우린 역할극을 할거야. 이 질문에 니가 마치 의사인 것 처럼 가정해서 병명을 진단하고 답변해줘 역할극 티는 내지 말고: {question}"
    response = openai.ChatCompletion.create(
        #model="gpt-3.5-turbo", # 챗 모델을 사용하는 경우 적절한 모델 이름으로 변경
        model="gpt-4-turbo-preview",
        messages=[
            #{"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": question_edited}
        ],
        max_tokens=800, # 최대 글자 수
        temperature=0.7,
    )
    with open ('log.csv', 'a', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([question, response.choices[0].message.content,str(datetime.now())[:19]])
        
    return response.choices[0].message.content

# 지도 생성
def create_map(df):
    # 서울의 중심에 지도 생성
    m = folium.Map(location=[37.4871305, 126.9011842], zoom_start=12)
    # 데이터 프레임의 각 행에 대하여
    for index, row in df.iterrows():
        # 마커 추가
        folium.Marker(
            [row['경도'], row['위도']],
            #popup= f"<a href={link} target='_blank'>{row['기관명']} 예약</a>",# 팝업에 표시될 내용
            popup= f"<a href={link}>{row['기관명']} 예약</a>",# 팝업에 표시될 내용
            tooltip=row['기관명'],  # 팝업에 표시될 내용row['기관명']  # 마우스 오버시 표시될 내용
        ).add_to(m)
        
    folium.Marker(
            [37.4871305, 126.9011842],
            tooltip='내 위치',
            icon = folium.map.Icon('red')
        ).add_to(m)

    return m

if __name__ == "__main__":
    df = pd.read_csv('의료기관.csv',encoding='cp949')
    df = df.loc[(abs(df['경도'] - 37.4871305)< 0.03) & (abs(df['위도'] - 126.9011842)< 0.03)]
    df = df.reset_index()
    
    st.set_page_config(layout="wide", page_title="K-DT AI Doctor")
    
        # 컬럼 설정
    col1, col2 = st.columns([5, 1])
    # 첫 번째 컬럼에 제목 표시
    with col1:
        st.title('사자문의 원격 의료 서비스')

    # 두 번째 컬럼에 이미지 표시
    with col2:
        st.image('logo.png', width=100)  # 이미지 경로와 크기 조정
        
    st.write("### 증상을 설명해 주시면 AI 닥터가 의료 조언을 드릴게요.")
    if st.session_state.show_examples:
        st.write("#### 사진을 첨부해주시면 더 좋아요!")
        
    st.sidebar.write("## 증상 사진을 입력해주세요(.jpg) :gear:") 
    MAX_FILE_SIZE = 300 * 1024 * 1024  # 300MB

    clear = False
        
    col1, col2 = st.columns(2)
    # 비디오 파일 업로드 위젯
    video_example = st.sidebar.file_uploader("증상과 관련된 사진을 업로드하세요", type=["png", "jpg", "jpeg"])
    
    # 질문 입력 위젯
    question_gender = st.sidebar.selectbox("성별을 입력해주세요", ("남", "녀"))
    
    question_age = st.sidebar.text_input("나이를 입력해 주세요")
    
    # 질문 입력 위젯
    question = st.sidebar.text_input("증상을 입력하세요")
    # 확인 버튼
    if st.sidebar.button('AI 분석 답변 생성 시작'):
        if video_example is not None and question:
            st.success("사진과 질문이 제출되었습니다.")
            answer = ask_gpt3(question)
            col1.write(f'질문 : {question}')
            col1.write(f'답변 : {answer}')
            col2.image(video_example)
            st.write("#### 현재 접속하신 위치를 기점으로 증상에 맞는 병원을 추천드리겠습니다.")
            map = create_map(df)
            folium_static(map)
        
        
        elif video_example is None and question:
            st.success("질문이 제출되었습니다.")
            answer = ask_gpt3(question)
            col1.write(f'질문 : {question}')
            col1.write(f'답변 : {answer}')
            col2.image('logo.png')  # 이미지 경로와 크기 조정
            
            st.write("#### 현재 접속하신 위치를 기점으로 증상에 맞는 병원을 추천드리겠습니다.")
            map = create_map(df)
            folium_static(map)
        
        elif video_example.size > MAX_FILE_SIZE:
            st.error("The uploaded file is too large. Please upload an image smaller than 300MB.")
            
        else:
            # 필수 입력이 없을 경우 사용자에게 알림
            st.error("질문을 제공해주세요.")
    
    example_videos = sorted(glob.glob(f'{get_project_root()}/examples/*'))
    # 이미지 및 버튼 배치
    if st.session_state.show_examples:
        # 사용자가 이미지를 클릭했는지에 따라 동적으로 컨텐츠를 표시
        cols = st.columns(len(example_videos))
            # 한 행에 표시할 이미지 수
        images_per_row = 4
        # 필요한 행의 수 계산
        num_rows = len(example_videos) // images_per_row + (1 if len(example_videos) % images_per_row > 0 else 0)
        for row in range(num_rows):
            cols = st.columns(images_per_row)  # 한 행에 해당하는 열 생성
            for idx in range(images_per_row):
                image_idx = row * images_per_row + idx
                
                if image_idx < len(example_videos):  # 이미지 인덱스가 전체 이미지 수를 넘지 않는 경우에만 처리
                    with cols[idx]:
                        st.image (example_videos[image_idx])  # 이미지 표시
                        if st.button(f"예시 {image_idx+1}. {example.example_questions_short[image_idx]}", key=image_idx):
                        
                            col1.image(example_videos[image_idx], use_column_width=True)
                            col1.write(f"질문 : {example.example_questions_full[image_idx]}", use_column_width=False)
                            col1.write(f"답변 : {example.example_answers_ko[image_idx]}", use_column_width=False)
                            handle_example_clicked(image_idx)
                            
    else:
        # 선택된 예시에 대한 정보 출력
        selected_idx = st.session_state.selected_example
        col1, col2 = st.columns([5, 3])
        with col1:
            st.image(example_videos[selected_idx], use_column_width=True)
            st.write(f"질문 : {example.example_questions_full[selected_idx]}", use_column_width=False)
            st.write(f"답변 : {example.example_answers_ko[selected_idx]}", use_column_width=False)
            st.write("#### 현재 접속하신 위치를 기점으로 증상에 맞는 병원을 추천드리겠습니다.")
            map = create_map(df)
            folium_static(map)