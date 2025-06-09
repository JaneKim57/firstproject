import streamlit as st

physics_videos = {
    "1. 운동의 표현": [
        {
            "title": "Speed, Velocity & Acceleration (3 min)",
            "url": "https://www.youtube.com/watch?v=Jyiw6KkedDY",
            "summary": "속력·속도·가속도 핵심 비교",
            "detail": "평균 속도, 순간 속도, 가속도의 정의 및 관계를 간단한 예와 함께 3분 내로 정리합니다."
        }
    ],
    "2. 뉴턴 운동 법칙": [
        {
            "title": "Newton's Laws in Three Minutes!!",
            "url": "https://www.youtube.com/watch?v=Cumw2RGOXUk",
            "summary": "뉴턴의 3법칙 총정리",
            "detail": "제1~3법칙을 3분 내에 핵심만 집중 설명하며, 실생활 사례로 이해를 돕습니다."
        }
    ],
    "3. 일과 에너지": [
        {
            "title": "What is Acceleration? (≈3 min)",
            "url": "https://www.youtube.com/watch?v=Z5aKC-zoLOk",
            "summary": "가속도 개념과 계산법",
            "detail": "가속도의 정의, 방향성, 단위, 그리고 실생활 예시를 3분 내로 설명합니다."
        }
    ],
    "4. 역학적 에너지 보존": [
        {
            "title": "Work, Energy & Power (3 min)",
            "url": "https://www.youtube.com/watch?v=w4QFJb9a8vo",
            "summary": "일·에너지·역학적 보존 요약",
            "detail": "역학적 에너지 보존 법칙과 일-에너지 개념을 간결하게 정리하며, 롤러코스터 사례 포함."
        }
    ],
    "5. 열역학 기초": [
        {
            "title": "PETS: Temperature Explained in 10 sec",
            "url": "https://www.youtube.com/watch?v=PETSvideos",  # 예시로 PETS 시리즈 링크
            "summary": "온도·열 개념 10초 요약",
            "detail": "PETS 시리즈 중 하나로, 온도 및 열 개념을 아주 짧고 임팩트 있게 전달합니다."
        }
    ],
    "추가 – 전기 회로": [
        {
            "title": "PETS: Voltage Explained in 10 sec",
            "url": "https://www.youtube.com/watch?v=PETSvideos2",
            "summary": "전압 개념 10초 요약",
            "detail": "전압 개념을 10초 내에 직관적으로 설명하는 PETS 시리즈 영상입니다."
        }
    ]
}

st.title("⚛️ 3분 내외로 보는 고등 물리 핵심 🔬")
st.markdown("짧고 핵심적인 영상으로 이해도를 높여보세요! 📺")

unit_list = list(physics_videos.keys())
selected = st.selectbox("📚 단원 또는 주제를 선택하세요:", unit_list)

if selected:
    st.balloons()
    st.subheader(f"📺 '{selected}' 추천 영상 (≤ 3분) & 요약표")
    
    # 요약 표
    data = {
        "제목": [f"[{v['title']}]({v['url']})" for v in physics_videos[selected]],
        "짧은 요약": [v["summary"] for v in physics_videos[selected]]
    }
    st.table(data)
    
    st.markdown("---")
    st.subheader("🧠 핵심 개념 (펼치기)")
    
    for video in physics_videos[selected]:
        with st.expander(f"🔍 {video['title']}"):
            st.markdown(f"[🔗 영상 보기]({video['url']})")
            st.markdown(f"**요약:** {video['summary']}")
            st.markdown(f"**상세 설명:**\n{video['detail']}")
