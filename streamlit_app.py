import streamlit as st
import pandas as pd
import random

# 질문 목록
questions = [
    ("타인과의 관계를 중요하게 여긴다.", "FT"),
    ("혼자 하는 일에 집중력이 높다.", "IE"),
    ("유연하고 융통성 있는 대처 방식을 선호한다.", "PJ"),
    ("공정한 결정을 내리는 것을 중요하게 여긴다.", "TF"),
    ("여러 사람과 함께 있을 때 더 즐겁다.", "EI"),
    ("상상력과 창의력을 중요하게 여긴다.", "NS"),
    ("계획이 없으면 불안함을 느낀다.", "JP"),
    ("소음이 적은 환경을 선호한다.", "IE"),
    ("감정에 따라 행동하는 편이다.", "FT"),
    ("실제 경험에 기반한 결정을 내린다.", "SN"),
    ("변화에 쉽게 적응한다.", "PJ"),
    ("깊이 있는 대화를 선호한다.", "IE"),
    ("분석적인 사고를 중요하게 여긴다.", "TF"),
    ("다양한 사람들과 만남을 즐긴다.", "EI"),
    ("현실적인 접근 방식을 선호한다.", "SN"),
    ("새로운 기회를 탐색하는 것을 즐긴다.", "PJ"),
    ("감정보다 사실에 기반한 결정을 선호한다.", "TF"),
    ("미래의 가능성을 고려하여 계획을 세운다.", "NS"),
    ("체계적으로 일을 처리한다.", "JP"),
    ("주기적으로 새로운 친구를 사귄다.", "EI"),
    ("사실과 세부 사항을 중요하게 여긴다.", "SN"),
    ("마감 기한을 지키기가 어렵다.", "PJ"),
    ("논리적인 설명을 선호한다.", "TF"),
    ("창의적인 해결책을 찾는 것을 선호한다.", "NS"),
    ("계획적인 접근 방식을 선호한다.", "JP"),
    ("여러 사람과 함께 있는 것보다 혼자 있는 시간이 더 편안하다.", "IE"),
    ("숫자 데이터보다 사람들의 이야기와 감정에 마음이 더 끌린다.", "FT"),
    ("구체적이고 실질적인 정보를 선호한다.", "SN"),
    ("상황에 따라 행동을 조정한다.", "PJ"),
    ("감정적인 논쟁에 쉽게 동요된다.", "FT"),
    ("문제를 분석하고 해결하는 것을 좋아한다.", "TF"),
    ("새로운 아이디어를 탐구하는 것을 즐긴다.", "NS"),
    ("일정을 잘 지킨다.", "JP"),
    ("깊이 생각한 후 말을 꺼내는 편이다.", "IE"),
    ("공감 능력을 중요하게 여긴다.", "FT"),
    ("추상적인 철학적 질문에 대해 깊이 생각하는 일은 시간낭비다.", "SN"),
    ("직관에 따라 행동하는 편이다.", "NS"),
    ("해야 할 일을 마지막까지 미룰 때가 종종 있다.", "PJ"),
    ("사실과 데이터를 기반으로 판단한다.", "TF"),
    ("장기적인 목표를 설정한다.", "NS"),
    ("목표를 설정하고 달성하는 것을 중요하게 여긴다.", "JP"),
    ("자신의 생각을 글로 표현하는 것을 선호한다.", "IE"),
    ("솔직함보다 세심함을 우선시한다.", "FT"),
    ("현재의 문제를 해결하는데 집중한다.", "SN"),
    ("계획보다는 상황에 따라 행동을 조정한다.", "PJ"),
    ("이성적인 접근 방식을 선호한다.", "TF"),
    ("미래의 가능성에 대해 고민한다.", "NS"),
    ("생활 공간이나 업무 공간이 깨끗하게 정돈되어 있다.", "JP"),
    ("나의 생각과 느낌을 말로 표현하는 것이 더 쉽다.", "EI"),
    ("결정을 내릴 때 논리적인 이유보다 타인과의 관계를 먼저 생각한다.", "FT"),
    ("체계적이고 논리적으로 일을 처리하는 편이다.", "SN"),
    ("다양한 가능성을 열어둔다.", "PJ"),
    ("감정적 반응보다 사실이 중요하다.", "TF"),
    ("상징과 은유를 잘 이해한다.", "NS"),
    ("체계화 도구 사용을 좋아한다.", "JP"),
    ("사교적인 활동을 통해 스트레스를 푼다.", "EI"),
    ("사실을 기반한 주장보다 공감가는 내용이 더 설득력 있다고 느낀다.", "FT"),
    ("과거의 경험을 통해 배우는 것을 좋아한다.", "SN"),
    ("계획을 세우고 실천하는 것을 좋아한다.", "JP"),
    ("다양한 활동에 참여하는 것을 좋아한다.", "EI")
]

# 세션 상태 초기화
if 'current_question' not in st.session_state:
    st.session_state.current_question = 0
    st.session_state.scores = {'E': 0, 'I': 0, 'S': 0, 'N': 0, 'T': 0, 'F': 0, 'J': 0, 'P': 0}
    st.session_state.answers = []

def next_question(answer):
    value = answer + 1  # 1부터 5까지의 값으로 변환
    trait_pair = questions[st.session_state.current_question][1]
    st.session_state.scores[trait_pair[0]] += value
    st.session_state.scores[trait_pair[1]] += (6 - value)
    st.session_state.answers.append(answer)
    st.session_state.current_question += 1

def compute_result():
    total_questions = len(questions)
    percentages = {k: (v / total_questions) * 100 for k, v in st.session_state.scores.items()}
    
    mbti = ''.join([
        'E' if percentages['E'] > percentages['I'] else 'I',
        'S' if percentages['S'] > percentages['N'] else 'N',
        'T' if percentages['T'] > percentages['F'] else 'F',
        'J' if percentages['J'] > percentages['P'] else 'P'
    ])
    
    st.write(f"당신의 MBTI 유형은 {mbti}입니다.")
    
    results = pd.DataFrame({
        '성향': ['외향형(E)', '내향형(I)', '감각형(S)', '직관형(N)', '사고형(T)', '감정형(F)', '판단형(J)', '인식형(P)'],
        '점수(%)': [percentages['E'], percentages['I'], percentages['S'], percentages['N'],
                    percentages['T'], percentages['F'], percentages['J'], percentages['P']]
    })
    
    st.bar_chart(results.set_index('성향'))
    st.write("세부 점수(%)")
    st.write(results.set_index('성향'))

st.title("MBTI 테스트")

if st.session_state.current_question < len(questions):
    question, _ = questions[st.session_state.current_question]
    st.write(f"질문 {st.session_state.current_question + 1} / {len(questions)}")
    st.write(question)
    
    options = ["매우 아니다", "아니다", "보통이다", "그렇다", "매우 그렇다"]
    answer = st.radio("해당란에 체크해주세요:", options, key=f"q_{st.session_state.current_question}")
    
    if st.button("다음"):
        next_question(options.index(answer))
        st.experimental_rerun()
else:
    compute_result()
    if st.button("테스트 다시 하기"):
        st.session_state.current_question = 0
        st.session_state.scores = {'E': 0, 'I': 0, 'S': 0, 'N': 0, 'T': 0, 'F': 0, 'J': 0, 'P': 0}
        st.session_state.answers = []
        st.experimental_rerun()