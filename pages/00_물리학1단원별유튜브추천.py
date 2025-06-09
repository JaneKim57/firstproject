import streamlit as st

def get_youtube_id(url):
    import re
    match = re.search(r"(?:v=|be/)([\w\-]+)", url)
    return match.group(1) if match else None

physics_videos = {
    "1. 운동의 표현": [
        {
            "title": "Speed, Velocity & Acceleration",
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
            "title": "Work, Energy, Power – CrashCourse",
            "url": "https://www.youtube.com/watch?v=w4QFJb9a8vo",
            "summary": "일·에너지·역학적 보존 요약",
            "detail": "역학적 에너지 보존, 위치↔운동에너지 변환 사례 포함."
        }
    ],
    "4. 역학적 에너지 보존": [
        {
            "title": "Roller Coaster Physics",
            "url": "https://www.youtube.com/watch?v=PKW_zV0v_RY",
            "summary": "역학적 에너지 보존 설명",
            "detail": "롤러코스터 사례로 에너지 보존 원리 명확히 설명."
        }
    ],
    "5. 물질·전자기장": [
        {
            "title": "Electromagnetism in 3 Minutes",
            "url": "https://www.youtube.com/watch?v=xJ-ri7SpuAc",
            "summary": "전자기장의 기본 원리",
            "detail": "전하와 자장, 전자기 상호작용의 핵심을 3분 내외로 요약합니다."
        },
        {
            "title": "Electric Fields – GCSE",
            "url": "https://www.youtube.com/watch?v=_v4ugAwV59U",
            "summary": "전기장 개념 설명",
            "detail": "점전하 주변 전기장 구조와 힘의 방향 계산을 이해하기 쉽게 정리."
        }
    ],
    "6. 파동·정보 통신": [
        {
            "title": "Wave Motion | FuseSchool",
            "url": "https://www.youtube.com/watch?v=CVsdXKO9xlk",
            "summary": "파동의 기본 특성",
            "detail": "진폭, 파장, 에너지 전달 등 파동의 기본 요소를 간략히 설명."
        },
        {
            "title": "Using Waves To Communicate",
            "url": "https://www.youtube.com/watch?v=LZ1xh0VNe4I",
            "summary": "파동 기반 정보 전달 원리",
            "detail": "전파·음파 등 다양한 파동을 정보 전달 수단으로 사용하는 예와 장단점을 설명."
        }
    ]
}

st.title("⚛️ 고등 물리 핵심: 썸네일로 영상 보기")
st.markdown("각 영상의 썸네일을 클릭하면 유튜브로 이동합니다.")

unit_list = list(physics_videos.keys())
selected = st.selectbox("📚 단원을 선택하세요:", unit_list)

if selected:
    st.subheader(f"📺 '{selected}' 영상 목록")
    for video in physics_videos[selected]:
        video_id = get_youtube_id(video['url'])
        thumbnail_url = f"https://img.youtube.com/vi/{video_id}/0.jpg"

        st.markdown(f"### {video['title']}")
        st.markdown(f"[![{video['title']}]({thumbnail_url})]({video['url']})")
        st.markdown(f"**짧은 요약:** {video['summary']}")

        with st.expander("🔍 핵심 개념 요약 보기"):
            st.markdown(f"**상세 설명:**\n{video['detail']}")

        st.markdown("---")
