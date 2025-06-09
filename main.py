import streamlit as st

# 📘 단원별 유튜브 추천 링크 (예시 데이터)
physics_videos = {
    "1. 운동의 표현": [
        "🔗 [속력과 속도 설명 영상](https://www.youtube.com/watch?v=WcBkI5-4ncE)",
        "🔗 [가속도 개념 쉽게 이해하기](https://www.youtube.com/watch?v=rR3qfS9NTyQ)"
    ],
    "2. 뉴턴 운동 법칙": [
        "🧲 [뉴턴 제1법칙: 관성의 법칙](https://www.youtube.com/watch?v=fqKjLFfdbpE)",
        "🛠️ [뉴턴 제2법칙: F=ma](https://www.youtube.com/watch?v=VZbM_ZMKc2o)",
        "🪐 [뉴턴 제3법칙: 작용-반작용 법칙](https://www.youtube.com/watch?v=kKKM8Y-u7ds)"
    ],
    "3. 일과 에너지": [
        "⚙️ [일(work)의 개념](https://www.youtube.com/watch?v=owI7DOeO85s)",
        "💥 [운동 에너지 & 위치 에너지](https://www.youtube.com/watch?v=5PfS2E4ybsU)"
    ],
    "4. 역학적 에너지 보존": [
        "🔋 [에너지 보존 법칙 쉽게 보기](https://www.youtube.com/watch?v=kzVbnmctf3g)",
        "🎢 [롤러코스터로 보는 역학적 에너지](https://www.youtube.com/watch?v=E1OKBvS2Y2I)"
    ],
    "5. 열역학 기초": [
        "🔥 [온도와 열의 차이](https://www.youtube.com/watch?v=6nQFOZ5HfSs)",
        "🌡️ [열역학 제1법칙](https://www.youtube.com/watch?v=l2DLZd2VXk0)"
    ]
}

# 🎯 앱 제목
st.title("⚛️ 고등학교 물리학 I 단원별 유튜브 추천 서비스 🚀")
st.markdown("물리학 I 단원을 선택하면, 이해를 돕는 **유튜브 영상 링크**를 추천해드려요! 📽️💡")

# 📚 단원 리스트
unit_list = list(physics_videos.keys())

# 🧑‍🏫 단원 선택
selected_unit = st.selectbox("📖 학습할 단원을 선택하세요:", unit_list)

# ▶️ 영상 추천
if selected_unit:
    st.balloons()  # 🎈 풍선 팡팡!
    
    st.subheader(f"📺 '{selected_unit}' 단원의 추천 영상 🎓")
    
    for idx, video in enumerate(physics_videos[selected_unit], 1):
        
        st.write(f"{idx}. {video}")
    
    st.success("✨ 영상으로 개념을 더 쉽게 이해해봐요!")

