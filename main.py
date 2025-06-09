import streamlit as st

# MBTI 16가지 리스트
mbti_types = [
    "INTJ", "INTP", "ENTJ", "ENTP",
    "INFJ", "INFP", "ENFJ", "ENFP",
    "ISTJ", "ISFJ", "ESTJ", "ESFJ",
    "ISTP", "ISFP", "ESTP", "ESFP"
]

# MBTI별 추천 영화
movie_recommendations = {
    "INTJ": [
        "🧠 A Beautiful Mind (2001)",
        "💻 The Imitation Game (2014)",
        "🧪 Primer (2004)"
    ],
    "INTP": [
        "🔬 Ex Machina (2014)",
        "📐 Good Will Hunting (1997)",
        "🚀 Interstellar (2014)"
    ],
    "ENTJ": [
        "📊 The Social Network (2010)",
        "🦾 Iron Man (2008)",
        "🧬 Jurassic Park (1993)"
    ],
    "ENTP": [
        "🌀 Back to the Future (1985)",
        "🛰️ The Martian (2015)",
        "🧪 The Prestige (2006)"
    ],
    "INFJ": [
        "🌌 Contact (1997)",
        "🧭 Arrival (2016)",
        "🪐 The Fountain (2006)"
    ],
    "INFP": [
        "🎇 October Sky (1999)",
        "🪐 The Theory of Everything (2014)",
        "🧬 Gattaca (1997)"
    ],
    "ENFJ": [
        "👩‍🚀 Hidden Figures (2016)",
        "🌠 Interstellar (2014)",
        "🧠 The Man Who Knew Infinity (2015)"
    ],
    "ENFP": [
        "🚀 Tomorrowland (2015)",
        "🌍 Don’t Look Up (2021)",
        "🧑‍🚀 WALL-E (2008)"
    ],
    "ISTJ": [
        "🧠 The Imitation Game (2014)",
        "🧮 Moneyball (2011)",
        "📊 The Big Short (2015)"
    ],
    "ISFJ": [
        "👩‍🚀 Hidden Figures (2016)",
        "📚 The Man Who Knew Infinity (2015)",
        "🛰️ Apollo 13 (1995)"
    ],
    "ESTJ": [
        "📈 The Big Short (2015)",
        "⚖️ 12 Angry Men (1957)",
        "🏭 The Current War (2017)"
    ],
    "ESFJ": [
        "🏥 Patch Adams (1998)",
        "🌟 The Theory of Everything (2014)",
        "🩺 Awakenings (1990)"
    ],
    "ISTP": [
        "🚘 Ford v Ferrari (2019)",
        "🔩 Iron Man (2008)",
        "🔭 Interstellar (2014)"
    ],
    "ISFP": [
        "🎨 The Aeronauts (2019)",
        "🌄 Into the Wild (2007)",
        "🎈 The Boy Who Harnessed the Wind (2019)"
    ],
    "ESTP": [
        "🚀 The Martian (2015)",
        "🛠️ Iron Man (2008)",
        "🎢 Inception (2010)"
    ],
    "ESFP": [
        "🎤 Bohemian Rhapsody (2018)",
        "💃 Hidden Figures (2016)",
        "🌍 Don’t Look Up (2021)"
    ]
}

# Streamlit UI
st.title("🎬 MBTI 기반 수학·과학 명작 영화 추천기 🔭")

st.markdown("당신의 **MBTI 유형**을 선택하세요. 선택한 유형에 어울리는 🧠 수학/과학 영화들을 추천해드려요! 🍿")

# selectbox로 MBTI 고르기
selected_mbti = st.selectbox("🧩 MBTI 유형을 선택하세요", mbti_types)

# 추천 영화 보여주기
if selected_mbti:
    st.balloons()  # 🎈 풍선 효과
    st.subheader(f"🍿 {selected_mbti} 유형에게 추천하는 영화 리스트 🎉")

    for i, movie in enumerate(movie_recommendations[selected_mbti], 1):
        st.write(f"{i}. {movie}")

    st.success("🎬 좋은 시간 되세요! 과학은 언제나 흥미롭고, 영화는 언제나 감동적이죠 💡")
