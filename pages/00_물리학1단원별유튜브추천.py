import streamlit as st

# 📘 단원별 영상 정보 (링크, 간단 요약, 핵심 설명)
physics_videos = {
    "1. 운동의 표현": [
        {
            "title": "CrashCourse #1: 속력과 속도",
            "url": "https://www.youtube.com/watch?v=7gf6YpdvtE0",
            "summary": "속력과 속도 차이 설명",
            "detail": "속력은 거리/시간, 속도는 방향 있는 이동량. 평균속도·순간속도 비교, 그래프 이해 포함."
        },
        {
            "title": "CrashCourse #2: 가속도",
            "url": "https://www.youtube.com/watch?v=0E5-k9GzEPA",
            "summary": "가속도 = 속도 변화율 설명",
            "detail": "가속도는 속도의 시간당 변화량. 등가속 운동 그래프 및 실생활 사례 포함."
        }
    ],
    "2. 뉴턴 운동 법칙": [
        {
            "title": "CrashCourse #5: 뉴턴의 세 법칙",
            "url": "https://www.youtube.com/watch?v=kKKM8Y-u7ds",
            "summary": "관성·힘·작용반작용 설명",
            "detail": "제1법칙: 관성 / 제2법칙: F=ma / 제3법칙: 작용-반작용. 풍선 예시로 시각화."
        }
    ],
    "3. 일과 에너지": [
        {
            "title": "Physics Girl – Work and Energy",
            "url": "https://www.youtube.com/watch?v=rKwK06stPS8",
            "summary": "일과 에너지의 정의 및 예시",
            "detail": "일 = 힘×거리. 에너지 변환 사례로 중력 위치에너지, 운동에너지 설명."
        }
    ],
    "4. 역학적 에너지 보존": [
        {
            "title": "CrashCourse #9: Work, Energy & Power",
            "url": "https://www.youtube.com/watch?v=w4QFJb9a8vo",
            "summary": "에너지 보존 원리 설명",
            "detail": "에너지는 형태를 바꿔도 총량이 일정. 롤러코스터 예시로 위치↔운동에너지 전환 설명."
        }
    ],
    "5. 열역학 기초": [
        {
            "title": "Physics Girl – Thermodynamics Intro",
            "url": "https://www.youtube.com/watch?v=ZqCMR7PjZRU",
            "summary": "열역학 법칙 기초",
            "detail": "열, 온도, 엔트로피 개념 및 열역학 제0~2법칙 간단 설명."
        }
    ],
    "추가 – 전기 회로": [
        {
            "title": "Veritasium – How Electricity Actually Works",
            "url": "https://www.youtube.com/watch?v=bHIhgxav9LY",
            "summary": "전기는 전자 흐름이 아니다?",
            "detail": "전력은 전자보다 EM 파동에 의해 빠르게 전달됨. 전자기장의 시각적 설명 포함."
        },
        {
            "title": "Physics Girl – Circuits, Voltage, Resistance, Current",
            "url": "https://www.youtube.com/watch?v=q8X2gcPVwO0",
            "summary": "기초 전기 회로 정리",
            "detail": "전압·전류·저항의 관계, 직렬과 병렬회로 비교. 기초 개념 총정리."
        }
    ]
}

# 🎯 UI 시작
st.title("⚛️ 고등학교 물리학 I + 전기 회로 유튜브 추천")
st.markdown("단원을 선택하면 재생 가능한 **유튜브 영상 + 요약 & 개념 정리**를 표와 함께 제공합니다!")

unit_list = list(physics_videos.keys())
selected = st.selectbox("📚 단원 또는 주제를 선택하세요:", unit_list)

if selected:
    st.balloons()
    st.subheader(f"📺 '{selected}' 추천 영상 요약표")

    # 표 구성
    data = {
        "영상 제목": [f"[{v['title']}]({v['url']})" for v in physics_videos[selected]],
        "간단 요약": [v["summary"] for v in physics_videos[selected]]
    }
    st.table(data)

    st.markdown("---")
    st.subheader("🧠 핵심 개념 요약 (펼쳐보기)")

    for video in physics_videos[selected]:
        with st.expander(f"🔍 {video['title']}"):
            st.markdown(f"[🔗 영상 보러가기]({video['url']})")
            st.markdown(f"**요약:** {video['summary']}")
            st.markdown(f"**핵심 개념 설명:**\n\n{video['detail']}")
