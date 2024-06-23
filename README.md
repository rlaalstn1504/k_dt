# 비디오에 대한 한국어 질의응답을 위한 Zero-Shot Video Question Answering via Frozen Bidirectional Language Models

본 레포지토리는 비디오에 대한 한국어 질의응답을 위한 [FrozenBiLM](https://github.com/antoyang/FrozenBiLM)의 학습 및 추론 코드를 제공합니다.
원본 코드는[FrozenBiLM](https://github.com/antoyang/FrozenBiLM)임을 밝힙니다.
아래에는 이 레포지토리에 대한 자세한 정보와 사용 방법, 저작권 및 라이센스 세부 정보를 제공합니다. 

[Paper](https://arxiv.org/abs/2206.08155) 

### 모델 정보:
------------------
FrozenBiLM은 비디오 질문 응답(VideoQA) 분야에서 새로운 접근법을 제시하는 모델로, 동결된 양방향 언어 모델(BiLM) 을 기반으로 합니다. 이 모델은 수동적인 주석이 없는 상태(제로샷) 또는 제한된 학습 데이터가 있는 상태(퓨샷)에서도 우수한 성능을 발휘하며, 표준 데이터셋을 사용한 훈련에서도 경쟁력 있는 결과를 보여줍니다.

FrozenBiLM의 핵심 특징은 다음과 같습니다:

- 비지도 학습 : 수동 주석 없이도 비디오에 대한 질문에 답변할 수 있는 능력을 보유하고 있습니다.
- 학습데이터 의존성 : 제한된 학습 데이터 상황에서도 다양한 비디오 QA 데이터셋에 걸쳐 강력한 성능을 제공합니다.
- 다양한 데이터셋에서의 우수한 성능: LSMDC-FiB, iVQA, MSRVTT-QA, MSVD-QA, ActivityNet-QA, TGIF-FrameQA, How2QA, TVQA 등 다양한 데이터셋에서 최신 모델을 뛰어넘는 성능을 나타냅니다.
- FrozenBiLM은 비디오와 텍스트 데이터를 통합적으로 처리하여, 마스킹된 텍스트가 질문에 대한 답변으로 사용되는 혁신적인 방식으로 제로샷 VideoQA 작업을 수행합니다. 이 모델은 비디오 QA 분야에서 새로운 기준을 제시하며, 제한된 리소스나 데이터로도 효과적인 학습과 추론이 가능함을 보여줍니다.  

<br>

![Teaser](https://antoyang.github.io/img/frozenbilm-header.png)


### 학습 환경:
------------------ 
- 본 레포지토리의 테스트 환경은 다음과 같습니다. 원활한 학습 및 추론을 위해 최소 25GB 이상의 GPU 사용을 권장드립니다.  
- GPU : Tesla V100 GPU * 4장 
- CPU : Intel(R) Xeon(R) CPU E5-2698 v4 @ 2.20GHz
- RAM : 924 GB 
- 운영체제 : Ubuntu (20.04.6 LTS)
- CUDA : 11.7
- Framework :  Python 3.8.10, Pytorch 2.0.1


### 학습 준비:
------------------  
##### 필수 라이브러리 설치
```bash
pip3 install -r requirements.txt
```  


### 데모 실행
------------------ 
demo 폴더 내 'app.py' 파일을 다음 명령어를 사용하여 실행하면, 웹페이지를 통해 모델을 직접 테스트해 볼 수 있습니다.  
특정 GPU를 사용하려면, 실행 명령어에 해당 GPU 번호를 첫 번째 인자로 추가하세요.

※ 입출력 데이터의 자연스러운 번역을 위해 chatgpt api를 사용합니다.   
api key를 demo/.env 파일에 API_KEY=key 형태로 발급받은 api 키를 삽입해 주세요.
 
```bash 
# 기본 설정(모든 GPU 사용 가능)으로 데모 실행: 
sh demo/run_demo.sh 
# 1번 GPU만을 사용하여 데모 실행:
sh demo/run_demo.sh 1
```
<img src="assets/demo.PNG"/> 

## Licenses
This code is released under the Apache License 2.0.  
The licenses for datasets used in the paper are available at the following links: [iVQA](https://github.com/antoyang/just-ask/blob/main/LICENSE), [MSRVTT-QA](https://github.com/xudejing/video-question-answering/blob/master/LICENSE), [MSVD-QA](https://github.com/xudejing/video-question-answering/blob/master/LICENSE), [ActivityNet-QA](https://github.com/MILVLG/activitynet-qa/blob/master/LICENSE), [How2QA](https://github.com/ych133/How2R-and-How2QA/blob/master/LICENSE) and [TVQA](https://github.com/jayleicn/TVQA/blob/master/LICENSE).

## Citation 
If you found this work useful, consider giving this repository a star and citing our paper as followed:
```
@inproceedings{yang2022frozenbilm,
title = {Zero-Shot Video Question Answering via Frozen Bidirectional Language Models},
author = {Antoine Yang and Antoine Miech and Josef Sivic and Ivan Laptev and Cordelia Schmid},
booktitle={NeurIPS}
year = {2022}}
```
