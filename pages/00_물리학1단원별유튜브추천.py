import streamlit as st

physics_videos = {
    "1. 운동의 표현": [
        {
            "title": "Speed, Velocity & Acceleration (≈3 min)",
            "url": "https://www.youtube.com/watch?v=Jyiw6KkedDY",
            "summary": "속력·속도·가속도 핵심 비교",
            "detail": "평균/순간속도, 가속도 정의 및 관계를 3분 내로 간단히 정리."
        }
    ],
    "2. 뉴턴 운동 법칙": [
        {
            "title": "Newton's Laws in Three Minutes!!",
            "url": "https://www.youtube.com/watch?v=Cumw2RGOXUk",
            "summary": "뉴턴의 3법칙 요약",
            "detail": "제1~3법칙 핵심 설명 + 실생활 예시 포함."
        }
    ],
    "3. 일과 에너지": [
        {
            "title": "Work, Energy, Power – CrashCourse #9 (≈3 min)",
            "url": "https://www.youtube.com/watch?v=w4QFJb9a8vo",
            "summary": "일·에너지·역학적 보존 요약",
            "detail": "역학적 에너지 보존, 위치↔운동에너지 변환 사례 포함."
        }
    ],
    "4. 역학적 에너지 보존": [
        {
            "title": "Work, Energy & Power (≈3 min)",
            "url": "https://www.youtube.com/watch?v=w4QFJb9a8vo",
            "summary": "역학적 에너지 보존 핵심 설명",
            "detail": "롤러코스터 사례로 에너지 보존 원리 명확히 설명."
        }
    ],
    "5. 물질·전자기장": [
        {
            "title": "Electromagnetism in 3 Minutes",
            "url": "https://www.youtube.com/watch?v=xJ-ri7SpuAc",
            "summary": "전자기장의 기본 원리",
            "detail": "전하와 자장, 전자기 상호작용의 핵심을 3분 내외로 요약합니다."  # :contentReference[oaicite:1]{index=1}
        },
        {
            "title": "Electric Fields – GCSE (≈3 min)",
            "url": "https://www.youtube.com/watch?v=_v4ugAwV59U",
            "summary": "전기장 개념 설명",
            "detail": "점전하 주변 전기장 구조와 힘의 방향 계산을 이해하기 쉬운 방식으로 정리."  # :contentReference[oaicite:2]{index=2}
        }
    ],
    "6. 파동·정보 통신": [
        {
            "title": "Wave Motion | FuseSchool (≈3 min)",
            "url": "https://www.youtube.com/watch?v=CVsdXKO9xlk",
            "summary": "파동의 기본 특성",
            "detail": "진폭, 파장, 에너지 전달 등 파동의 기본 요소를 간략히 설명."  # :contentReference[oaicite:3]{index=3}
        },
        {
            "title": "Using Waves To Communicate (≈3 min)",
            "url": "https://www.youtube.com/watch?v=LZ1xh0VNe4I",
            "summary": "파동 기반 정보 전달 원리",
            "detail": "전파·음파 등 다양한 파동을 정보 전달 수단으로 사용하는 예와 장단점을 설명."  # :contentReference[oaicite:4]{index=4}
        }
    ]
}

st.title("⚛️ 3분 내외로 보는 고등 물리 핵심 정리 🔬")
st.markdown("물리학 I 전 단원(운동→파동·정보통신) 커버! 짧고 임팩트 있는 영상으로 핵심 개념 정리합니다.")

unit_list = list(physics_videos.keys())
selected = st.selectbox("📚 단원 또는 주제를 선택하세요:", unit_list)

if selected:
    st.balloons()
    st.subheader(f"📺 '{selected}' 추천 영상 (≤ 3분) & 요약표")
    
    # 표 구성
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
