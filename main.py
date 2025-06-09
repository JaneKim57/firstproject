import streamlit as st

# 🎬 MBTI 별 추천 영화 데이터
movie_recommendations = {
    "INTJ": [
        "🧠 A Beautiful Mind (2001)",
        "💻 The Imitation Game (2014)",
        "🚀 Interstellar (2014)"
    ],
    "INFP": [
        "🌌 Contact (1997)",
        "🎇 October Sky (1999)",
        "🪐 The Theory of Everything (2014)"
    ],
    "ENTP": [
        "🌀 Back to the Future (1985)",
        "🤖 Iron Man (2008)",
        "📱 The Social Network (2010)"
    ],
    "ISFJ": [
        "👩‍🚀 Hidden Figures (2016)",
        "📚 The Man Who Knew Infinity (2015)",
        "🚀 Apollo 13 (1995)"
    ],
    # 기타 MBTI 혹은 알 수 없는 경우
    "default": [
        "🌠 Cosmos (1980)",
        "📡 Einstein and Eddington (2008)",
        "🪐 The Martian (2015)"
    ]
}

# 🏁 앱 타이틀
st.title("🎬 MBTI 기반 수학·과학 명작 영화 추천기 🔭")

st.markdown("당신의 **MBTI**를 입력하면, 그 성향에 어울리는 🧠 수학/과학 명작 영화들을 추천해드려요! 🌟")

# 📥 MBTI 입력받기
mbti_input = st.text_input("✍️ 당신의 MBTI를 입력하세요 (예: INTP)").upper()

# 입력값이 있을 때
if mbti_input:
    # 추천 영화 가져오기
    recommendations = movie_recommendations.get(mbti_input, movie_recommendations["default"])
    
    st.balloons()  # 🎈 풍선 효과 팡팡!
    
    st.subheader(f"🍿 {mbti_input} 유형을 위한 추천 영화 리스트 🎉")
    
    for i, movie in enumerate(recommendations, 1):
        st.write(f"{i}. {movie}")

    st.success("✨ 재미있게 감상하세요! 영화 한 편이 인생을 바꿀 수도 있답니다 💡")
else:
    st.info("📌 위에 MBTI를 입력해 주세요! (예: ENFP, ISTJ 등)")

