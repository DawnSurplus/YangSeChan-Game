#region IMPORT
import streamlit as st
#endregion





#region DEFINE
GAME_PAGE_NAME = "🎮 양세찬 게임 플레이"

topics = ["연예인", "영화", "동물", "역사 인물", "가상 캐릭터"]
player_options = [2, 3, 4]

if "game_topic" not in st.session_state:
    st.session_state.game_topic = "연예인"
if "player_num" not in st.session_state:
    st.session_state.player_num = 2
if "chat_logs" not in st.session_state:
    st.session_state.chat_logs = [[] for _ in range(4)]  # 최대 4인
if "game_started" not in st.session_state:
    st.session_state.game_started = False
#endregion





#region FUNCTION
def show_game_page():
    st.header(GAME_PAGE_NAME)
    if not st.session_state.game_started:
        show_setting_section()
    else:
        show_play_section()



def show_setting_section():
    # 주제 선택
    st.subheader("게임 주제 선택")
    st.session_state.game_topic = st.radio(
        "주제를 선택해주세요.",
        topics,
        index=topics.index(st.session_state.game_topic),
        key="topic_radio",
        horizontal=True
    )

    # 인원수 설정
    st.subheader("플레이어어 설정")
    st.session_state.player_num = st.radio(
        "플레이어 수를 선택해주세요.",
        player_options,
        index=player_options.index(st.session_state.player_num),
        key="player_radio",
        horizontal=True
    )

    # 게임시작 버튼
    if st.button("게임시작", key="start_btn"):
        st.session_state.game_started = True
        st.session_state.chat_logs = [[] for _ in range(4)]
        st.rerun()



def show_play_section():
    # 상단에 주제 표시
    st.markdown(
        f"<h1 style='text-align: center; color: #4B8BF4;'>{st.session_state.game_topic}</h1>",
        unsafe_allow_html=True
    )

    # 게임종료 버튼
    if st.button("게임종료", key="end_btn"):
        st.session_state.game_started = False
        st.session_state.chat_logs = [[] for _ in range(4)]
        st.rerun()

    # 대화 로그 영역
    st.subheader("플레이어별 대화 로그")
    player_names = ["사용자"] + [f"AI {i+1}" for i in range(1, st.session_state.player_num)]
    columns = st.columns(st.session_state.player_num)
    for idx, col in enumerate(columns):
        with col:
            st.markdown(f"**{player_names[idx]}**")
            logs = st.session_state.chat_logs[idx]
            if logs:
                for log in logs:
                    st.markdown(f"- {log}")
            else:
                st.markdown("_아직 대화가 없습니다._")
            # 사용자 입력창 (사용자만 입력 가능)
            if idx == 0:
                user_input = st.text_input("메시지 입력", key=f"user_input_{idx}")
                if st.button("전송", key=f"send_{idx}") and user_input:
                    st.session_state.chat_logs[idx].append(user_input)
                    st.rerun()
            # AI는 임시로 자동 메시지 버튼 제공 (실제론 LLM 연동)
            else:
                if st.button(f"AI {idx} 자동 메시지", key=f"ai_btn_{idx}"):
                    st.session_state.chat_logs[idx].append(f"AI {idx}의 예시 메시지입니다.")
                    st.rerun()
#endregion