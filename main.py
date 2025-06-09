import streamlit as st

# 🎬 MBTI 별 추천 영화 데이터 (수학·과학/기술 감성 명작)
movie_recommendations = {
    "INTJ": [
        "🧠 A Beautiful Mind (2001)",
        "💻 The Imitation Game (2014)",
        "🚀 Interstellar (2014)"
    ],
    "INTP": [
        "📐 Primer (2004)",
        "🧩 Pi (1998)",
        "💡 Good Will Hunting (1997)"
    ],
    "ENTJ": [
        "📊 The Social Network (2010)",
        "💰 Moneyball (2011)",
        "💹 The Big Short (2015)"
    ],
    "ENTP": [
        "🌀 Back to the Future (1985)",
        "🤖 Iron Man (2008)",
        "📱 The Social Network (2010)"
    ],
    "INFJ": [
        "🌌 Contact (1997)",
        "🎇 October Sky (1999)",
        "🪐 The Theory of Everything (2014)"
    ],
    "INFP": [
        "🌌 Contact (1997)",
        "🎇 October Sky (1999)",
        "🪐 The Theory of Everything (2014)"
    ],
    "ENFJ": [
        "👩‍🚀 Hidden Figures (2016)",
        "🚀 Apollo 13 (1995)",
        "🪐 The Martian (2015)"
    ],
    "ENFP": [
        "👩‍🚀 Hidden Figures (2016)",
        "🪐 The Martian (2015)",
        "🪐 The Theory of Everything (2014)"
    ],
    "ISTJ": [
        "🧠 A Beautiful Mind (2001)",
        "🚀 Apollo 13 (1995)",
        "💻 The Imitation Game (2014)"
    ],
    "ISFJ": [
        "👩‍🚀 Hidden Figures (2016)",
        "📚 The Man Who Knew Infinity (2015)",
        "🚀 Apollo 13 (1995)"
    ],
    "ESTJ": [
        "📊 The Social Network (2010)",
        "💰 Moneyball (2011)",
        "🚀 Apollo 13 (1995)"
    ],
    "ESFJ": [
        "👩‍🚀 Hidden Figures (2016)",
        "🪐 The Martian (2015)",
        "💻 The Imitation Game (2014)"
    ],
    "ISTP": [
        "📐 Pi (1998)",
        "📐 Primer (2004)",
        "💡 Good Will Hunting (1997)"
    ],
    "ISFP": [
        "📚 The Man Who Knew Infinity (2015)",
        "💡 Good Will Hunting (1997)",
        "🎇 October Sky (1999)"
    ],
    "ESTP": [
        "🌀 Back to the Future (1985)",
        "🤖 Iron Man (2008)",
        "📱 The Social Network (2010)"
    ],
    "ESFP": [
        "🚀 Interstellar (2014)",
        "🪐 The Martian (2015)",
        "👩‍🚀 Hidden Figures (2016)"
    ]
}

# 🏁 앱 타이틀
st.title("🎬 MBTI 기반 수학·과학 명작 영화 추천기 🔭")

st.markdown("아래에서 **MBTI 유형**을 선택하면, 그 성향에 맞는 수학/과학, 기술 감성의 명작 영화들을 추천해드려요! 🌟")

# 📥 MBTI 선택: 16가지 옵션
mbti_options = [
    "INTJ", "INTP", "ENTJ", "ENTP",
    "INFJ", "INFP", "ENFJ", "ENFP",
    "ISTJ", "ISFJ", "ESTJ", "ESFJ",
    "ISTP", "ISFP", "ESTP", "ESFP"
]

selected_mbti = st.selectbox("📌 당신의 MBTI 유형을 선택하세요:", mbti_options)

# 추천 영화 출력
if selected_mbti:
    recommendations = movie_recommendations.get(selected_mbti, [])
    
    st.balloons()  # 🎈 풍선 효과!
    
    st.subheader(f"🍿 {selected_mbti} 유형을 위한 추천 영화 리스트 🎉")
    
    for idx, movie in enumerate(recommendations, 1):
        st.write(f"{idx}. {movie}")
        
    st.success("✨ 재밌게 감상하세요!")
