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
                            안녕하세요. 대한의사협회 상담의사 입니다.
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