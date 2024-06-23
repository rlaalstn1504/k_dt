#!/usr/bin/bash

# 스크립트 파일의 디렉토리 경로를 얻음
SCRIPT_DIR=$(dirname "$0")

# 첫 번째 인자가 있을 경우에만 CUDA_VISIBLE_DEVICES 설정
if [ ! -z "$1" ]; then
  # 첫 번째 인자로 받은 GPU 번호를 설정
  GPU_NUM=$1
  # CUDA_VISIBLE_DEVICES 환경 변수를 설정
  export CUDA_VISIBLE_DEVICES=$GPU_NUM
fi

# 스크립트 파일의 디렉토리 내 app.py 실행
streamlit run "$SCRIPT_DIR/app.py" --server.port 55536 --server.fileWatcherType none