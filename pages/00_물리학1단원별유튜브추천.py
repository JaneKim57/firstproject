import streamlit as st

def get_youtube_id(url):
    """Extract video ID from YouTube URL"""
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
    # ... 다른 단원도 동일한 형식으로 계속 추가 ...
}

st.title("⚛️ 고등 물리 핵심: 영상 썸네일로 보기")
st.markdown("각 영상의 썸네일을 클릭하면 유튜브로 이동합니다.")

unit_list = list(physics_videos.keys())
selected = st.selectbox("📚 단원을 선택하세요:", unit_list)

if selected:
    st.subheader(f"📺 '{selected}' 영상 목록")
    for video in physics_videos[selected]:
        video_id = get_youtube_id(video['url'])
        thumbnail_url = f"https://img.youtube.com/vi/{video_id}/0.jpg"

        # 영상 썸네일과 설명 정리
        st.markdown(f"### {video['title']}")
        st.markdown(f"[![{video['title']}]({thumbnail_url})]({video['url']})")
        st.markdown(f"**짧은 요약:** {video['summary']}")

        with st.expander("🔍 핵심 개념 요약 보기"):
            st.markdown(f"**상세 설명:**\n{video['detail']}")
        
        st.markdown("---")
