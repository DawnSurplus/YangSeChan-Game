#region IMPORT
import streamlit as st
#endregion





#region DEFINE
RULE_PAGE_NAME = "📖 양세찬 게임 룰 설명"
#endregion





#region FUNCTION
def show_rule_page():
    st.header(RULE_PAGE_NAME)
    st.markdown("""
    **양세찬 게임(이름 맞히기 게임) 규칙**
    
    1. 게임 주제를 정합니다 (예: 연예인, 동물, 영화 캐릭터 등).
    2. 각 플레이어는 자신이 맞혀야 할 인물을 정해 이마에 붙입니다(본인은 모름).
    3. 차례대로 돌아가며 자신의 인물이 누구인지 예/아니오로 대답할 수 있는 질문을 합니다.
    4. 다른 플레이어들은 그 질문에 대해 정직하게 답변합니다.
    5. 충분히 추리했다고 생각되면, 자신의 인물을 맞힙니다.
    6. 가장 먼저 자신의 인물을 맞히는 플레이어가 승리합니다!
    """)
    st.info("사이드바에서 '게임 플레이'로 이동해 실제 게임을 시작하세요!")
#endregion