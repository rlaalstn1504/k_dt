import streamlit as st
from datetime import datetime, timedelta
import csv

def main():
    st.title('예약 시스템')

    # 날짜 선택
    chosen_date = st.date_input("날짜 선택", min_value=datetime.today(), max_value=datetime.today() + timedelta(days=365))

    # 시간 선택 옵션
    time_options = ["09:00 AM", "11:00 AM", "02:00 PM", "04:00 PM"]
    chosen_time = st.selectbox("시간 선택", options=time_options)
    chosen_gender = st.selectbox("성별", options=['남','녀'])
    text_input = st.text_input("나이")
    text_input_name = st.text_input("이름")

    # 추가 정보 입력
    additional_info = st.text_area("증상을 자세히 입력하세요.")

    # 예약 확인 버튼
    if st.button("예약 확인"):
        # 예약 정보 확인 메시지 표시
        with open ('reserve.csv', 'a', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([text_input_name, text_input, chosen_gender, chosen_time])
        st.success(f"\n날짜: {chosen_date}\n {chosen_time} {text_input_name}님 예약이 완료되었습니다.")

if __name__ == "__main__":
    main()
