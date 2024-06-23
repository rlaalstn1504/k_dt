# streamlit 파일을 demo 폴더 안과 밖 모두 다 경로문제없이 실행하기 위해 path 추가
import os
import sys
parent_dir = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
sys.path.append(parent_dir)
sys.path.append(os.getcwd())

import streamlit as st
import pandas as pd

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


API_KEY = os.getenv("API_KEY")
openai.api_key = API_KEY

def get_project_root() -> str:
    """Returns project root path."""
    return str(Path(os.path.abspath(__file__)).parent)

def ask_gpt3(question):
    response = openai.ChatCompletion.create(
        #model="gpt-3.5-turbo", # 챗 모델을 사용하는 경우 적절한 모델 이름으로 변경
        model="gpt-4-turbo-preview",
        messages=[
            #{"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": question}
        ],
        max_tokens=300,
        temperature=0.7,
    )
    return response.choices[0].message.content


if __name__ == "__main__":
    df = pd.read_csv('의료기관.csv',encoding='cp949')
    df['여부'] = df['주소'].apply(lambda x: '구로' in x)
    df = df[df['여부']==True]
    df['lat'] = df['위도']
    df['lon'] = df['경도']
    
    st.set_page_config(layout="wide", page_title="Video Question Answering")
    # st.title(f'사자문의 원격 의료 서비스')
    # st.image('logo.png', caption='로고')
    
        # 컬럼 설정
    col1, col2 = st.columns([5, 1])
    # 첫 번째 컬럼에 제목 표시
    with col1:
        st.title('사자문의 원격 의료 서비스')

    # 두 번째 컬럼에 이미지 표시
    with col2:
        st.image('logo.png', width=100)  # 이미지 경로와 크기 조정
        
    st.write("### 사진과 증상 설명을 통해 의료 조언을 수행합니다.")
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
            # 비디오 처리 및 질문에 대한 응답 로직을 여기에 추가
            st.success("사진과 질문이 제출되었습니다.")
            answer = ask_gpt3(f"우린 역할극을 할거야. 이 질문에 니가 마치 의사인 것 처럼 가정해서 병명을 진단하고 답변해줘 역할극 티는 내지 말고: {question}")
            col1.write(f'질문 : {question}')
            col1.write(f'답변 : {answer}')
            col2.image(video_example)
            clear = True
        
        
        elif video_example is None and question:
            st.success("질문이 제출되었습니다.")
            answer = ask_gpt3(f"우린 역할극을 할거야. 이 질문에 니가 마치 의사인 것 처럼 가정해서 병명을 진단하고 답변해줘: {question}")
            col1.write(f'질문 : {question}')
            col1.write(f'답변 : {answer}')
            col2.image('logo.png')  # 이미지 경로와 크기 조정
            
            st.write("### 현재 접속하신 위치를 기점으로 증상에 맞는 병원을 추천드리겠습니다.")
            st.map(df[['lat','lon']])
            clear = True
        
        elif video_example.size > MAX_FILE_SIZE:
            st.error("The uploaded file is too large. Please upload an image smaller than 300MB.")
            
        else:
            # 필수 입력이 없을 경우 사용자에게 알림
            st.error("질문을 제공해주세요.")
            
    if clear == False:
        example_videos = sorted(glob.glob(f'{get_project_root()}/examples/*'))
        example_questions_short = ['전혀 안간지러운데 습진인가요?',
                                '두통이 점점 심해져요..',
                                '수두일까요?',
                                '어금니에 검정색 점.. 이거 충치겠죠..?']
        
        example_questions_full = ['''지금 제 손이랑 팔 안쪽 다리쪽에 습진처럼 생긴게 생겻는데 손에 오돌토돌하게 나는것도 
                                같은병인가요? 그리고 전혀 안간지러운데 습진이 맞나요?''',
                                
                            '''더위에 외출하고 나서 두통이 점점 심해지는데 열사병일까요?''',
                            
                            '''
                            주말 남해근교에서 갯벌체험과 펜션에서 숙박했고 제트스파에서 잠수도 하고 놀았음
                            화요일 아침 3개정도 모기 물린 자국인줄 알았는데 학교 갔다오니 상체 몸만 앞뒤로 퍼져있고 팔,다리에 없음
                            현재 3일째이고 간지러움은 없고 열도 없었음 소아과에서 수두인거 같다고 이야기 하시는데
                            간지러움이 없어 확신을 안하시고 피부염약 에스로반, 더마톱, 투리온정 처방 받았습니다
                            수두인가요 알레르기 인가요
                            ''',
                            
                            '''오늘 양치하다가 발견했어요ㅠㅠㅠ 첨엔 뭐 묻은 줄 알았는데 워터픽 쏘고 치간칫솔로 긁어?도 그대로에요.. 
                            뭔가 달라붙은 것 처럼 보이긴 하는데 충치일 가능성이 높겠죠? 
                            최대한 빠르게 치과에 갈 수 있는 날이 다음주 토요일인데 불안하네요ㅠㅠ 양치 좀 깨끗하게 할걸..''']
        
        example_answers_ko = ["""갑작스런 추위로 인해 피부가 당기거나 각질이 표면으로 일어나지 않더라도 
                            겨울에는 피부의 수분 함량이 낮아져 메마른 상태가 된다 해요. 또한 실내의 
                            과도한 난방이나 건조한 실내 환경으로 인해서 피부가 거칠어지고 붉은 반점이
                            올라오는 등 가려운 증상도 동반될 수 있는데요. 피부가 자극되어 있는 상태에서는
                            과도한 화장품 사용이나 팩이 오히려 피부 질환을 악화시킬 수 있고 잘못된 연고의
                            사용 또한 피부 질환을 악화시킬 수 있어요. 따라서, 적당한 수분과 오일,
                            보습 크림의 사용이 좋으며 또한, 피부의 유분기가 너무 제거되면 피부의
                            수분도 함께 날아갈 수 있어 적당한 유분기가 보호막의 역할을 할 수 있도록 해주는 것이 좋다 해요.
                            또한, 체내의 수분 함량 유지를 위해서 물도 자주 섭취해 주는 것이 좋아요:D
                            만약 해당 부위로의 알레르기 반응이 번지거나 지속적인 가려움이 동반될 경우에는
                            약물 치료가 필요할 수 있어 가까운 피부과에 내원을 통해 
                            증상에 맞는 약을 처방 받아 복용하실 것을 권유드려요.""",
                            
                            '''안녕하세요. 대한의사협회 상담의사 호빵맨입니다. 
                            혹시 덥다고 아이스크림을 드시진 않으셨는지요?''',
                            
                            """
                            안녕하세요. 대한의사협회·네이버 지식iN 상담의사 김태형 입니다.
                            수두는 전체적인 피부 병변이 중요한 소견으로, 병변 일부만으로 진찰하기는 어렵습니다.
                            소아에서는 전신 증상(열 등)이 약하게 나타날 수 있습니다.
                            네이버 지식인보다는 가까운 피부과 전문의 의원에서 진찰을 받아보길 권장드리며, 
                            얼굴과 두피에도 비슷한 병변이 있다면 수두의 가능성을 조금 더 높게 생각할 수 있겠으며,
                            몸통에만 해당 병변이 있다면 수두의 가능성은 조금 더 떨어지겠습니다. 2-3 mm 크기의
                            작은 이슬모양의 수포가 홍반에 둘러싸여 있고 중심부에 배꼽모양함몰을 보이는 병변이 
                            수두 진단에 특이적이나 전문가가 아니면 관찰하기 힘들 수 있습니다.
                            """,
                            
                            '''통증이나 다른 증상이 없고, 스케일링을 최근에 받은 경우에도 충치와 같은 이유로 인한 문제일 수 있습니다.
                            그러나 충치 여부를 정확히 확인하기 위해서는 치과 전문가의 진단이 필요합니다.
                            충치는 치아의 치질을 유발하는 세균에 의해 발생하는 치아 결손 질환입니다. 식이 습관, 구강 위생,
                            치아 구조 등 여러 요인에 의해 발생할 수 있습니다. 충치는 보통 황색이나 갈색의 면피사를 형성하고, 통증, 민감도, 새소리, 치아 퇴색 등의 증상을 동반할 수 있습니다.
                            치석은 치아 위에 형성되는 무기성 치아 포획물로서, 치아에 노란색이나 갈색의 경련을 만들어줍니다.
                            치석은 구강 위생이 부실한 경우 치아와 잇몸 사이에 형성될 수 있으며, 흡연, 커피나 차의 섭취,
                            일상적인 음식 섭취 등이 원인이 될 수 있습니다.
                            치아 착색은 외부 요인에 의해 치아가 변색되는 것으로, 식이 습관 또는 흡연으로 인한 치아 
                            표면의 색소 침착이 일반적인 원인이 될 수 있습니다.
                            치과 전문가의 진단을 받아야 충치, 치석 또는 치아 착색 여부를 명확히 판단할 수 있으며,
                            그에 따라 적절한 치료 계획을 수립할 수 있습니다. 이를 위해 치과 의사를 방문하시기를 권장드립니다.
                            ''',
                            ]
        
        # 한 행에 표시할 이미지 수
        images_per_row = 4
        # 필요한 행의 수 계산
        num_rows = len(example_videos) // images_per_row + (1 if len(example_videos) % images_per_row > 0 else 0)
        
        cols = st.columns(len(example_videos))
        # 이미지 및 버튼 배치
        for row in range(num_rows):
            cols = st.columns(images_per_row)  # 한 행에 해당하는 열 생성
            for idx in range(images_per_row):
                image_idx = row * images_per_row + idx
                
                if image_idx < len(example_videos):  # 이미지 인덱스가 전체 이미지 수를 넘지 않는 경우에만 처리
                    with cols[idx]:
                        st.image (example_videos[image_idx])  # 이미지 표시
                        if st.button(f"예시 {image_idx+1}. {example_questions_short[image_idx]}", key=image_idx):
                            #st.markdown(f"{example_answers_ko[image_idx]}**")
                            col1.image(example_videos[image_idx], use_column_width=True)
                            col1.write(f"질문 : {example_questions_full[image_idx]}", use_column_width=False)
                            col1.write(f"답변 : {example_answers_ko[image_idx]}", use_column_width=False)

                        
        
   