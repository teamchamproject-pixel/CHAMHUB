from pathlib import Path
import random
import html
import time
import io
import base64
from gtts import gTTS
import streamlit as st

# =========================================================
# 1. CẤU HÌNH WEBSITE
# =========================================================

st.set_page_config(
    page_title="CHẠM Hub | Thấu hiểu để kết nối",
    page_icon="🤝",
    layout="wide",
    initial_sidebar_state="expanded"
)

BASE_DIR = Path(__file__).parent
LOGO_PATH = BASE_DIR / "logo_cham.png"

# =========================================================
# 2. DỮ LIỆU VÀ TRẠNG THÁI
# =========================================================

if "welcomed" not in st.session_state:
    st.session_state.welcomed = False

if "journal" not in st.session_state:
    st.session_state.journal = []

if "community" not in st.session_state:
    st.session_state.community = []

if "completed" not in st.session_state:
    st.session_state.completed = set()

if "score" not in st.session_state:
    st.session_state.score = 0

if "drawn_cards" not in st.session_state:
    st.session_state.drawn_cards = []

if "quiz_index" not in st.session_state:
    st.session_state.quiz_index = 0

if "quiz_feedback" not in st.session_state:
    st.session_state.quiz_feedback = None

if "quiz_results" not in st.session_state:
    st.session_state.quiz_results = {}

if "quiz_answer" not in st.session_state:
    st.session_state.quiz_answer = None

# =========================================================
# 3. GIAO DIỆN TƯƠI MỚI & HIỆU ỨNG
# =========================================================

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:wght@300;400;500;600;700;800;900&display=swap');

html, body, [class*="css"] {
    font-family: 'Be Vietnam Pro', sans-serif;
}

.stApp {
    background-color: #FAF8F5;
    color: #1B3B5A;
}

section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #1B3B5A 0%, #244D73 100%);
    border-right: 1px solid #32628E;
}

section[data-testid="stSidebar"] * {
    color: #FDFBF7 !important;
}

section[data-testid="stSidebar"] .stRadio label {
    font-size: 14.5px;
    padding: 4px 0;
}

section[data-testid="stSidebar"] div[data-testid="stMetric"] {
    background: rgba(255, 255, 255, 0.14) !important;
    border: 1px solid rgba(255, 255, 255, 0.25) !important;
    border-radius: 14px;
    padding: 12px 15px;
}

section[data-testid="stSidebar"] div[data-testid="stMetric"] label,
section[data-testid="stSidebar"] div[data-testid="stMetric"] [data-testid="stMetricValue"] {
    color: #F3C66F !important;
}

h1, h2, h3 {
    color: #1B3B5A;
    font-weight: 800;
}

p {
    line-height: 1.75;
}

.hero {
    background: linear-gradient(125deg, #1F4E78 0%, #367B8A 55%, #489E82 100%);
    padding: 42px;
    border-radius: 24px;
    color: white;
    margin-bottom: 26px;
    box-shadow: 0 14px 35px rgba(31, 78, 120, 0.15);
}

.hero h1 {
    color: white;
    font-size: 40px;
    margin-bottom: 10px;
}

.hero p {
    color: #F2FAF8;
    font-size: 16.5px;
}

.eyebrow {
    color: #F3C66F;
    letter-spacing: 3px;
    font-size: 11.5px;
    font-weight: 800;
    margin-bottom: 6px;
}

.panel {
    background: #FFFFFF;
    border: 1px solid #EAE4DC;
    border-radius: 18px;
    padding: 24px;
    margin-bottom: 16px;
    box-shadow: 0 6px 20px rgba(27, 59, 90, 0.04);
    transition: transform 0.25s ease, box-shadow 0.25s ease, border-color 0.25s ease;
}

.panel:hover {
    transform: translateY(-4px);
    box-shadow: 0 12px 28px rgba(72, 158, 130, 0.12);
    border-color: #489E82;
}

.panel h3 {
    margin-top: 0;
    color: #1B3B5A;
}

.green-panel {
    background: #EBF7F3;
    border-left: 5px solid #489E82;
    border-radius: 14px;
    padding: 20px;
    margin: 14px 0;
    color: #184235;
}

.gold-panel {
    background: #FFF6E9;
    border-left: 5px solid #E5A94C;
    border-radius: 14px;
    padding: 20px;
    margin: 14px 0;
    color: #5C3D12;
}

.quote {
    background: linear-gradient(135deg, #FFF5F5 0%, #FFF9EC 100%);
    border: 1px solid #F4D8D8;
    border-left: 6px solid #E68A8A;
    border-radius: 16px;
    padding: 24px;
    font-size: 19px;
    color: #1B3B5A;
    font-weight: 700;
    text-align: center;
    margin: 22px 0;
}

.small-label {
    font-size: 11px;
    color: #489E82;
    letter-spacing: 1.8px;
    font-weight: 800;
}

.card-title {
    font-size: 20px;
    font-weight: 800;
    color: #1B3B5A;
    margin-bottom: 8px;
}

.stButton > button {
    border-radius: 12px;
    font-weight: 700;
    border: 1px solid #C8D8D3;
    min-height: 44px;
    transition: all 0.2s ease;
}

.stButton > button[kind="primary"] {
    background: linear-gradient(135deg, #3A8D73 0%, #489E82 100%);
    border: none;
    color: white;
    box-shadow: 0 4px 12px rgba(72, 158, 130, 0.25);
}

.stButton > button[kind="primary"]:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 16px rgba(72, 158, 130, 0.35);
}

.main div[data-testid="stMetric"] {
    background: #FFFFFF;
    padding: 16px;
    border-radius: 16px;
    border: 1px solid #EAE4DC;
    box-shadow: 0 4px 12px rgba(27, 59, 90, 0.03);
}

a {
    color: #367B8A !important;
    font-weight: 600;
}

footer { visibility: hidden; }
#MainMenu { visibility: hidden; }

/* Màn hình chào mừng hiệu ứng gõ phím & giọng đọc */
@keyframes blinkCursor {
    0%, 49% { border-color: #F3C66F; }
    50%, 100% { border-color: transparent; }
}

.welcome-overlay {
    position: fixed;
    top: 0; left: 0;
    width: 100vw; height: 100vh;
    background: linear-gradient(135deg, #1B3B5A 0%, #2C667A 50%, #489E82 100%);
    z-index: 999999;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
    padding: 30px;
}

.typewriter-text {
    color: #FFFFFF;
    font-size: clamp(24px, 4vw, 40px);
    font-weight: 800;
    border-right: 4px solid #F3C66F;
    padding-right: 10px;
    animation: blinkCursor 0.75s infinite;
    max-width: 900px;
    white-space: nowrap;
    overflow: hidden;
}

.welcome-desc {
    color: #E2ECE9;
    font-size: clamp(14px, 1.8vw, 18px);
    font-weight: 400;
    margin-top: 16px;
    max-width: 720px;
    line-height: 1.65;
}

.welcome-sub {
    color: #F3C66F;
    font-size: clamp(13px, 1.5vw, 16px);
    font-weight: 600;
    margin-top: 14px;
    letter-spacing: 2px;
}
</style>
""", unsafe_allow_html=True)

# =========================================================
# 4. MÀN HÌNH CHÀO MỪNG CÓ GIỌNG ĐỌC TIẾNG VIỆT & GÕ CHỮ
# =========================================================

@st.cache_data(show_spinner=False)
def generate_welcome_audio(text):
    """Tạo file âm thanh giọng đọc tiếng Việt từ văn bản và mã hóa Base64"""
    try:
        tts = gTTS(text=text, lang='vi', slow=False)
        fp = io.BytesIO()
        tts.write_to_fp(fp)
        fp.seek(0)
        return base64.b64encode(fp.read()).decode()
    except Exception:
        return None

if not st.session_state.welcomed:
    splash = st.empty()
    title_text = "CHẠM — Thấu hiểu để kết nối"
    desc_text = "Nền tảng tri thức và trải nghiệm giáo dục số đồng hành cùng bộ trò chơi bàn, giúp bạn thấu hiểu về Alzheimer, sẻ chia gánh nặng chăm sóc và lan tỏa sự nhân văn."
    full_speech = "Chào mừng bạn đến với Chạm Hấp. Thấu hiểu để kết nối, kết nối để sẻ chia. Không ai phải đi một mình."
    
    audio_b64 = generate_welcome_audio(full_speech)
    audio_tag = ""
    if audio_b64:
        # Phát giọng đọc tự động (và hiển thị thanh điều khiển nhỏ phòng trường hợp trình duyệt chặn autoplay)
        audio_tag = f"""
        <audio autoplay controls style="margin-top: 22px; height: 36px; border-radius: 20px; opacity: 0.85;">
            <source src="data:audio/mp3;base64,{audio_b64}" type="audio/mp3">
        </audio>
        """

    typed_title = ""
    for char in title_text:
        typed_title += char
        splash.markdown(f"""
        <div class="welcome-overlay">
            <div style="font-size: 64px; margin-bottom: 14px;">🤝</div>
            <div class="typewriter-text">{html.escape(typed_title)}</div>
            <div class="welcome-desc" style="opacity:0;">{html.escape(desc_text)}</div>
            <div class="welcome-sub" style="opacity:0;">KẾT NỐI ĐỂ SẺ CHIA • KHÔNG AI PHẢI ĐI MỘT MÌNH</div>
        </div>
        """, unsafe_allow_html=True)
        time.sleep(0.08)

    # Hiển thị đầy đủ nội dung giới thiệu kèm giọng đọc
    splash.markdown(f"""
    <div class="welcome-overlay">
        <div style="font-size: 64px; margin-bottom: 14px;">🤝</div>
        <div class="typewriter-text">{html.escape(title_text)}</div>
        <div class="welcome-desc">{html.escape(desc_text)}</div>
        <div class="welcome-sub">KẾT NỐI ĐỂ SẺ CHIA • KHÔNG AI PHẢI ĐI MỘT MÌNH</div>
        {audio_tag}
    </div>
    """, unsafe_allow_html=True)
    
    # Đợi khoảng 6.5 giây để giọng đọc hoàn tất câu chào trước khi vào trang chính
    time.sleep(6.5)
    splash.empty()
    st.session_state.welcomed = True


# =========================================================
# 5. HÀM HỖ TRỢ
# =========================================================

def safe(value):
    return html.escape(str(value))


def render_logo(width=140):
    if LOGO_PATH.exists():
        st.image(str(LOGO_PATH), width=width)
    else:
        st.markdown(
            """
            <div style="
                font-size:32px;
                font-weight:900;
                letter-spacing:5px;
                color:#F3C66F;
                padding:8px 0;
            ">CHẠM</div>
            """,
            unsafe_allow_html=True
        )


def section_title(eyebrow, title, description=None):
    st.markdown(
        f'<div class="small-label">{safe(eyebrow.upper())}</div>',
        unsafe_allow_html=True
    )
    st.title(title)
    if description:
        st.write(description)


def panel(title, content, icon="🌿"):
    st.markdown(
        f"""
        <div class="panel">
            <div class="card-title">{icon} {safe(title)}</div>
            <p style="color:#3B5266; margin-bottom:0;">{content}</p>
        </div>
        """,
        unsafe_allow_html=True
    )


def mark_complete(name):
    st.session_state.completed.add(name)


def render_footer():
    st.markdown("---")
    c1, c2 = st.columns([1, 5])

    with c1:
        render_logo(75)

    with c2:
        st.markdown("""
        <div style="padding-top:8px">
            <b style="color:#1B3B5A">CHẠM HUB</b><br>
            <span style="font-size:13px;color:#5A7184">
            Thấu hiểu để kết nối – Kết nối để sẻ chia.<br>
            Nội dung giáo dục và nâng cao nhận thức về Alzheimer.
            </span>
        </div>
        """, unsafe_allow_html=True)


# =========================================================
# 6. THƯ VIỆN TRI THỨC
# =========================================================

KNOWLEDGE = {
    "Alzheimer là gì?": {
        "tag": "KIẾN THỨC CƠ BẢN",
        "intro": "Alzheimer là một bệnh lý thần kinh tiến triển, ảnh hưởng đến trí nhớ, tư duy và khả năng thực hiện các hoạt động thường ngày.",
        "sections": [
            (
                "Alzheimer có phải là lão hóa thông thường?",
                "Không. Một số thay đổi trí nhớ có thể xuất hiện khi tuổi tác tăng lên, nhưng Alzheimer không phải là hệ quả tất yếu của quá trình lão hóa. Bệnh có thể gây suy giảm nhận thức ngày càng rõ rệt và ảnh hưởng đến cuộc sống."
            ),
            (
                "Điều gì xảy ra trong não bộ?",
                "Bệnh có liên quan đến những thay đổi sinh học trong não, bao gồm sự tích tụ bất thường của protein amyloid và tau. Những thay đổi này có thể làm tổn thương tế bào thần kinh và ảnh hưởng đến mạng lưới liên kết giữa chúng."
            ),
            (
                "Alzheimer có giống mọi dạng sa sút trí tuệ?",
                "Không. Sa sút trí tuệ là thuật ngữ chung mô tả hội chứng suy giảm nhận thức ảnh hưởng đến sinh hoạt. Alzheimer là một trong những nguyên nhân phổ biến của hội chứng này."
            )
        ]
    },

    "Dấu hiệu nhận biết": {
        "tag": "NHẬN DIỆN",
        "intro": "Biểu hiện có thể khác nhau giữa mỗi người và thường tiến triển theo thời gian.",
        "sections": [
            (
                "Khó ghi nhớ thông tin mới",
                "Người bệnh có thể thường xuyên quên những sự việc vừa xảy ra, lặp lại câu hỏi hoặc cần nhiều sự nhắc nhở hơn trước."
            ),
            (
                "Khó thực hiện công việc quen thuộc",
                "Một số công việc từng rất quen thuộc có thể trở nên khó khăn, chẳng hạn chuẩn bị bữa ăn hoặc quản lý các bước trong một hoạt động."
            ),
            (
                "Nhầm lẫn về thời gian và địa điểm",
                "Người bệnh có thể gặp khó khăn trong việc xác định ngày tháng, nơi đang ở hoặc tìm đường đến địa điểm quen thuộc."
            ),
            (
                "Thay đổi cảm xúc và hành vi",
                "Có thể xuất hiện sự lo lắng, dễ kích động, thu mình hoặc thay đổi cách phản ứng trong những tình huống quen thuộc."
            )
        ]
    },

    "Các yếu tố nguy cơ": {
        "tag": "PHÒNG NGỪA VÀ SỨC KHỎE",
        "intro": "Nguy cơ mắc bệnh chịu ảnh hưởng của nhiều yếu tố. Không có một nguyên nhân đơn lẻ giải thích mọi trường hợp.",
        "sections": [
            (
                "Tuổi tác",
                "Tuổi cao là yếu tố nguy cơ quan trọng nhất đã được xác định, nhưng Alzheimer không phải là điều chắc chắn xảy ra khi một người già đi."
            ),
            (
                "Di truyền và tiền sử gia đình",
                "Một số biến thể gene có thể làm thay đổi nguy cơ. Tuy nhiên, có người có tiền sử gia đình mắc bệnh nhưng không phát triển bệnh."
            ),
            (
                "Sức khỏe tim mạch và chuyển hóa",
                "Huyết áp cao, đái tháo đường, hút thuốc và một số yếu tố sức khỏe khác có liên quan đến sức khỏe não bộ."
            ),
            (
                "Lối sống và môi trường",
                "Vận động thể chất, chế độ ăn cân bằng, giấc ngủ, giao tiếp xã hội và kiểm soát các yếu tố nguy cơ có thể góp phần bảo vệ sức khỏe nhận thức."
            )
        ]
    },

    "Chẩn đoán và hỗ trợ": {
        "tag": "HIỂU ĐÚNG",
        "intro": "Việc đánh giá cần được thực hiện bởi nhân viên y tế có chuyên môn, dựa trên nhiều nguồn thông tin.",
        "sections": [
            (
                "Quy trình đánh giá",
                "Bác sĩ có thể khai thác bệnh sử, trao đổi với người thân, thực hiện đánh giá nhận thức và chỉ định xét nghiệm hoặc chẩn đoán hình ảnh khi phù hợp."
            ),
            (
                "Vì sao cần phát hiện sớm?",
                "Đánh giá sớm giúp xác định nguyên nhân có thể điều trị, lập kế hoạch chăm sóc và tiếp cận các hình thức hỗ trợ phù hợp."
            ),
            (
                "Điều trị và quản lý",
                "Một số phương pháp có thể hỗ trợ kiểm soát triệu chứng hoặc làm chậm tiến triển ở nhóm người bệnh phù hợp. Hiệu quả và chỉ định cần được bác sĩ đánh giá."
            ),
            (
                "Vai trò của gia đình",
                "Gia đình có thể hỗ trợ người bệnh duy trì thói quen, đảm bảo an toàn, tham gia hoạt động phù hợp và giữ kết nối xã hội."
            )
        ]
    },

    "Giao tiếp và thấu hiểu": {
        "tag": "ĐỒNG HÀNH",
        "intro": "Giao tiếp với người mắc Alzheimer cần sự kiên nhẫn, tôn trọng và chú ý đến cảm xúc.",
        "sections": [
            (
                "Nói chậm và rõ ràng",
                "Sử dụng câu ngắn, mỗi lần tập trung vào một ý. Cho người đối diện đủ thời gian để tiếp nhận và phản hồi."
            ),
            (
                "Không tranh cãi về ký ức",
                "Khi người bệnh nhầm lẫn, hãy bình tĩnh và chú ý đến cảm xúc phía sau câu nói thay vì cố gắng chứng minh họ sai."
            ),
            (
                "Tôn trọng quyền lựa chọn",
                "Khuyến khích người bệnh tham gia quyết định trong khả năng của họ. Không nên mặc định rằng họ không thể tự lựa chọn."
            ),
            (
                "Duy trì sự kết nối",
                "Âm nhạc, ảnh gia đình, hoạt động quen thuộc và những cuộc trò chuyện nhẹ nhàng có thể giúp duy trì cảm giác gần gũi."
            )
        ]
    }
}


# =========================================================
# 7. TÌNH HUỐNG CHĂM SÓC
# =========================================================

SCENARIOS = {
    "Người thân liên tục hỏi cùng một câu": {
        "possible": "Người bệnh có thể không ghi nhớ được câu trả lời vừa nhận. Việc hỏi lại đôi khi xuất phát từ lo lắng hoặc nhu cầu được trấn an.",
        "avoid": "Tránh quát mắng, tỏ ra khó chịu hoặc nói rằng người bệnh đã hỏi quá nhiều lần.",
        "try": "Trả lời nhẹ nhàng, ngắn gọn. Có thể dùng giấy ghi chú, lịch hoặc vật dụng gợi nhắc để hỗ trợ.",
        "example": "Thay vì nói: 'Con đã nói rồi mà!', hãy thử: 'Mẹ yên tâm nhé, hôm nay mình chưa có lịch đi đâu cả.'"
    },

    "Người thân làm thất lạc đồ vật": {
        "possible": "Người bệnh có thể đặt đồ vật ở vị trí khác thường rồi không nhớ lại được quá trình cất giữ.",
        "avoid": "Không vội buộc tội người bệnh làm mất đồ hoặc cố tình giấu đồ.",
        "try": "Cùng tìm kiếm, kiểm tra những vị trí quen thuộc và bố trí nơi cất đồ cố định.",
        "example": "Có thể nói: 'Mình cùng tìm chiếc kính nhé. Mẹ nhớ lần cuối mình dùng ở đâu không?'"
    },

    "Người thân trở nên bối rối vào buổi tối": {
        "possible": "Một số người mắc sa sút trí tuệ có thể trở nên bồn chồn, lú lẫn hoặc kích động hơn vào cuối ngày.",
        "avoid": "Tránh tạo môi trường quá ồn ào, ánh sáng quá tối hoặc thay đổi lịch sinh hoạt đột ngột.",
        "try": "Duy trì thói quen buổi tối, giảm tiếng ồn, đảm bảo ánh sáng phù hợp và kiểm tra những nhu cầu cơ bản.",
        "example": "Có thể mở đèn nhẹ, bật bản nhạc quen thuộc và cùng người bệnh thực hiện một hoạt động thư giãn."
    },

    "Người thân không muốn ăn": {
        "possible": "Có thể liên quan đến thay đổi khẩu vị, khó khăn khi sử dụng dụng cụ ăn uống, mệt mỏi hoặc vấn đề sức khỏe khác.",
        "avoid": "Không ép ăn, quát mắng hoặc tạo áp lực trong bữa ăn.",
        "try": "Chia nhỏ khẩu phần, giảm yếu tố gây xao nhãng và quan sát khả năng nhai nuốt.",
        "example": "Có thể thử món ăn quen thuộc, dễ dùng và tạo không khí thoải mái. Nếu tình trạng kéo dài, hãy trao đổi với nhân viên y tế."
    },

    "Người thân từ chối tắm": {
        "possible": "Người bệnh có thể cảm thấy lạnh, sợ ngã, ngại bị hỗ trợ hoặc không hiểu rõ hoạt động đang diễn ra.",
        "avoid": "Không cưỡng ép, làm người bệnh xấu hổ hoặc vội vàng thực hiện.",
        "try": "Giải thích từng bước, giữ sự riêng tư, điều chỉnh nhiệt độ và lựa chọn thời điểm phù hợp.",
        "example": "Có thể nói: 'Mình chuẩn bị nước ấm nhé. Mẹ muốn tự làm phần nào trước?'"
    }
}


# =========================================================
# 8. BỘ THẺ TRẢI NGHIỆM
# =========================================================

CARDS = {
    "Nhận thức": [
        {
            "title": "Một câu hỏi lặp lại",
            "content": "Bà hỏi bạn ba lần về thời gian mẹ sẽ về nhà.",
            "task": "Bạn sẽ phản ứng thế nào để bà cảm thấy an tâm?"
        },
        {
            "title": "Ký ức quen thuộc",
            "content": "Ông nhìn một bức ảnh cũ nhưng không nhớ tên người trong ảnh.",
            "task": "Bạn có thể bắt đầu cuộc trò chuyện ra sao?"
        }
    ],

    "Đồng cảm": [
        {
            "title": "Một ngày khó khăn",
            "content": "Người thân tỏ ra bực bội khi không thể làm một việc quen thuộc.",
            "task": "Hãy nghĩ về cảm xúc có thể đang tồn tại phía sau hành vi."
        },
        {
            "title": "Được lắng nghe",
            "content": "Người thân kể lại một câu chuyện đã kể nhiều lần.",
            "task": "Bạn có thể lắng nghe như thế nào để họ cảm thấy được tôn trọng?"
        }
    ],

    "Tình huống": [
        {
            "title": "Chiếc chìa khóa",
            "content": "Người thân không tìm thấy chiếc chìa khóa và bắt đầu lo lắng.",
            "task": "Hãy đề xuất một cách hỗ trợ bình tĩnh."
        },
        {
            "title": "Bữa cơm gia đình",
            "content": "Người thân không muốn tham gia bữa ăn cùng mọi người.",
            "task": "Bạn sẽ điều chỉnh môi trường và cách giao tiếp ra sao?"
        }
    ],

    "Hành động": [
        {
            "title": "Một việc nhỏ",
            "content": "Bạn có 15 phút để tạo ra một khoảnh khắc vui vẻ với người thân.",
            "task": "Hãy đề xuất một hoạt động đơn giản, quen thuộc và an toàn."
        },
        {
            "title": "Góc ký ức",
            "content": "Gia đình có nhiều bức ảnh cũ chưa được sắp xếp.",
            "task": "Bạn sẽ sử dụng những bức ảnh đó để tạo sự kết nối như thế nào?"
        }
    ],

    "Kiến thức": [
        {
            "title": "Alzheimer và tuổi tác",
            "content": "Một người cao tuổi thường quên một số việc.",
            "task": "Vì sao không nên mặc định mọi biểu hiện quên đều là Alzheimer?"
        },
        {
            "title": "Vai trò của bác sĩ",
            "content": "Một gia đình nhận thấy người thân có thay đổi trí nhớ kéo dài.",
            "task": "Vì sao cần được đánh giá bởi nhân viên y tế?"
        }
    ]
}


# =========================================================
# 9. NGÂN HÀNG CÂU HỎI MINI-GAME
# =========================================================

QUIZ = [
    {
        "question": "Alzheimer có phải là một phần tất yếu của quá trình lão hóa?",
        "options": [
            "Có, ai già đi cũng sẽ mắc",
            "Không, đây là bệnh lý riêng biệt",
            "Chỉ người trên 80 tuổi mới mắc",
            "Không thể phân biệt"
        ],
        "answer": 1,
        "explain": "Alzheimer không phải hệ quả tất yếu của tuổi già. Đây là một bệnh lý thần kinh tiến triển."
    },
    {
        "question": "Khi người thân liên tục hỏi lại một câu, cách phản ứng phù hợp là gì?",
        "options": [
            "Quát để họ nhớ",
            "Bỏ mặc hoàn toàn",
            "Trả lời nhẹ nhàng và hỗ trợ bằng gợi nhắc",
            "Tranh luận để chứng minh họ sai"
        ],
        "answer": 2,
        "explain": "Sự kiên nhẫn và hỗ trợ bằng các gợi nhắc có thể giúp người bệnh cảm thấy an tâm."
    },
    {
        "question": "Sa sút trí tuệ là gì?",
        "options": [
            "Một tên gọi khác của tuổi già",
            "Một hội chứng suy giảm nhận thức ảnh hưởng sinh hoạt",
            "Một loại cảm xúc",
            "Một bệnh chỉ xuất hiện ở trẻ em"
        ],
        "answer": 1,
        "explain": "Sa sút trí tuệ là thuật ngữ chung mô tả hội chứng suy giảm nhận thức ảnh hưởng đến hoạt động thường ngày."
    },
    {
        "question": "Ai có vai trò đánh giá và chẩn đoán Alzheimer?",
        "options": [
            "Bạn bè",
            "Bất kỳ người thân nào",
            "Nhân viên y tế có chuyên môn",
            "Một bài kiểm tra trực tuyến"
        ],
        "answer": 2,
        "explain": "Chẩn đoán cần được thực hiện bởi nhân viên y tế có chuyên môn, dựa trên đánh giá phù hợp."
    },
    {
        "question": "Điều gì nên được ưu tiên khi giao tiếp với người mắc Alzheimer?",
        "options": [
            "Nói thật nhanh",
            "Tranh luận khi họ nhầm lẫn",
            "Kiên nhẫn, tôn trọng và lắng nghe",
            "Không cho họ tự lựa chọn"
        ],
        "answer": 2,
        "explain": "Giao tiếp tôn trọng, bình tĩnh và tạo điều kiện cho người bệnh lựa chọn là rất quan trọng."
    }
]


# =========================================================
# 10. SIDEBAR - ĐIỀU HƯỚNG
# =========================================================

PAGES = [
    "Trang chủ",
    "Khám phá Alzheimer",
    "Thư viện tri thức",
    "Não bộ và trí nhớ",
    "Cẩm nang đồng hành",
    "Trạm trải nghiệm",
    "Hành trình thấu cảm",
    "Không gian sẻ chia",
    "Nguồn tham khảo"
]

with st.sidebar:
    render_logo(145)

    st.markdown("""
    <div style="
        font-size:10px;
        letter-spacing:2px;
        color:#F3C66F;
        margin-bottom:22px;
    ">
        THẤU HIỂU ĐỂ KẾT NỐI
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### KHÁM PHÁ CHẠM HUB")

    page = st.radio(
        "Điều hướng",
        PAGES,
        label_visibility="collapsed",
        key="main_navigation"
    )

    st.markdown("---")

    st.markdown("**HÀNH TRÌNH CỦA BẠN**")
    st.metric(
        "Hoạt động đã hoàn thành",
        f"{len(st.session_state.completed)}/7"
    )

    st.progress(min(len(st.session_state.completed) / 7, 1.0))

    st.markdown("---")
    st.caption("CHẠM HUB • EDUCATION & EMPATHY")


# =========================================================
# 11. TRANG CHỦ
# =========================================================

if page == "Trang chủ":

    st.markdown("""
    <div class="hero">
        <div class="eyebrow">CHẠM HUB • KNOWLEDGE & EMPATHY</div>
        <h1>Hiểu để gần nhau hơn.</h1>
        <p>
        Một không gian tri thức giúp bạn khám phá Alzheimer,
        hiểu về trí nhớ và học cách đồng hành với người bệnh
        bằng sự kiên nhẫn, tôn trọng và yêu thương.
        </p>
    </div>
    """, unsafe_allow_html=True)

    a, b = st.columns([1, 3])

    with a:
        render_logo(155)

    with b:
        st.markdown("""
        <div style="padding:10px 0">
            <div class="small-label">WELCOME TO</div>
            <h1 style="margin-bottom:0">CHẠM HUB</h1>
            <p style="color:#5A7184">
            Nền tảng tri thức và trải nghiệm giáo dục
            về Alzheimer.
            </p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div class="quote">
        “Không ai phải đi một mình.”
    </div>
    """, unsafe_allow_html=True)

    st.subheader("Bắt đầu hành trình khám phá")

    c1, c2, c3 = st.columns(3)

    with c1:
        panel(
            "Khám phá tri thức",
            "Tìm hiểu Alzheimer, dấu hiệu nhận biết và những kiến thức khoa học nền tảng.",
            "🧠"
        )

    with c2:
        panel(
            "Học cách đồng hành",
            "Tiếp cận những tình huống thường ngày và cách hỗ trợ người thân.",
            "🤝"
        )

    with c3:
        panel(
            "Trải nghiệm tương tác",
            "Thử thách kiến thức, rút thẻ tình huống và xây dựng sự thấu cảm.",
            "🎯"
        )

    st.markdown("---")
    st.subheader("Các con số trong hành trình")

    x1, x2, x3, x4 = st.columns(4)

    x1.metric("Chuyên mục", "9")
    x2.metric("Chủ đề tri thức", len(KNOWLEDGE))
    x3.metric("Tình huống", len(SCENARIOS))
    x4.metric("Câu hỏi thử thách", len(QUIZ))

    st.markdown("---")
    st.subheader("Một hành trình bắt đầu từ sự thấu hiểu")

    st.write("""
    CHẠM không chỉ hướng đến việc cung cấp kiến thức về Alzheimer,
    mà còn mong muốn thay đổi cách chúng ta nhìn nhận và tương tác
    với người mắc bệnh.

    Từ hiểu biết khoa học đến những hành động nhỏ trong đời sống,
    mỗi sự kiên nhẫn và quan tâm đều có thể góp phần tạo nên
    một môi trường sống nhân văn hơn.
    """)

    st.info("👈 Hãy chọn chuyên mục ở menu bên trái (Sidebar) để bắt đầu hành trình khám phá!")


# =========================================================
# 12. KHÁM PHÁ ALZHEIMER
# =========================================================

elif page == "Khám phá Alzheimer":

    section_title(
        "DISCOVER",
        "Khám phá Alzheimer",
        "Bắt đầu từ những kiến thức cơ bản để hiểu đúng về bệnh."
    )

    st.markdown("""
    <div class="green-panel">
        <b>Góc nhìn khoa học</b><br>
        Alzheimer là bệnh lý thần kinh tiến triển, có thể ảnh hưởng
        đến trí nhớ, tư duy, ngôn ngữ và khả năng sinh hoạt.
    </div>
    """, unsafe_allow_html=True)

    for i, (name, data) in enumerate(KNOWLEDGE.items()):
        with st.expander(f"{i+1}. {name}", expanded=(i == 0)):
            st.caption(data["tag"])
            st.write(data["intro"])

            for heading, content in data["sections"]:
                st.markdown(f"**{heading}**")
                st.write(content)

    st.info(
        "Nội dung trên nhằm mục đích giáo dục và nâng cao nhận thức, "
        "không thay thế việc thăm khám hoặc tư vấn y tế."
    )

    if st.button("Hoàn thành chuyên mục khám phá"):
        mark_complete("discover")
        st.success("Bạn đã hoàn thành chuyên mục này!")


# =========================================================
# 13. THƯ VIỆN TRI THỨC
# =========================================================

elif page == "Thư viện tri thức":

    section_title(
        "KNOWLEDGE LIBRARY",
        "Thư viện tri thức",
        "Tìm kiếm, lựa chọn và đọc những nội dung bạn quan tâm."
    )

    keyword = st.text_input(
        "🔎 Tìm kiếm chủ đề",
        placeholder="Ví dụ: trí nhớ, dấu hiệu, giao tiếp..."
    )

    category = st.selectbox(
        "Chọn chủ đề",
        ["Tất cả"] + list(KNOWLEDGE.keys())
    )

    for name, data in KNOWLEDGE.items():

        if category != "Tất cả" and category != name:
            continue

        searchable = (
            name + " " + data["intro"] + " " +
            " ".join(
                heading + " " + content
                for heading, content in data["sections"]
            )
        ).lower()

        if keyword and keyword.lower() not in searchable:
            continue

        with st.expander(f"📚 {name}"):
            st.caption(data["tag"])
            st.write(data["intro"])

            for heading, content in data["sections"]:
                st.markdown(f"**{heading}**")
                st.write(content)

            if st.button(
                "Đánh dấu đã đọc",
                key="read_" + name
            ):
                mark_complete("read_" + name)
                st.success("Đã ghi nhận!")

    if keyword:
        st.caption("Kết quả được lọc theo từ khóa bạn nhập.")


# =========================================================
# 14. NÃO BỘ VÀ TRÍ NHỚ
# =========================================================

elif page == "Não bộ và trí nhớ":

    section_title(
        "BRAIN & MEMORY",
        "Não bộ và trí nhớ",
        "Khám phá cách não bộ tiếp nhận, lưu trữ và truy xuất thông tin."
    )

    st.markdown("""
    <div class="hero">
        <div class="eyebrow">THE HUMAN BRAIN</div>
        <h1>Mỗi ký ức là một kết nối.</h1>
        <p>
        Trí nhớ không nằm ở một điểm duy nhất.
        Nó là kết quả hoạt động phối hợp của nhiều vùng não
        và mạng lưới thần kinh.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("Ba quá trình cơ bản của trí nhớ")

    c1, c2, c3 = st.columns(3)

    with c1:
        panel(
            "1. Tiếp nhận",
            "Não bộ tiếp nhận thông tin thông qua các giác quan và sự chú ý.",
            "👁️"
        )

    with c2:
        panel(
            "2. Lưu trữ",
            "Thông tin được xử lý và duy trì thông qua hoạt động của các mạng lưới thần kinh.",
            "🧩"
        )

    with c3:
        panel(
            "3. Truy xuất",
            "Khi cần thiết, não bộ huy động những thông tin đã được lưu trữ.",
            "💡"
        )

    st.markdown("---")
    st.subheader("Một số vùng não liên quan đến trí nhớ")

    brain_topics = {
        "Hồi hải mã (Hippocampus)": (
            "Có vai trò quan trọng trong việc hình thành ký ức mới "
            "và định hướng không gian."
        ),
        "Vỏ não trước trán": (
            "Tham gia vào trí nhớ làm việc, lập kế hoạch, "
            "kiểm soát hành vi và ra quyết định."
        ),
        "Hạch hạnh nhân (Amygdala)": (
            "Tham gia xử lý cảm xúc, đặc biệt là những trải nghiệm "
            "có ý nghĩa cảm xúc."
        ),
        "Vỏ não": (
            "Nhiều vùng vỏ não tham gia lưu giữ và xử lý "
            "những loại thông tin khác nhau."
        )
    }

    for title, content in brain_topics.items():
        with st.expander(title):
            st.write(content)

    st.markdown("---")
    st.subheader("Tại sao ký ức có thể bị ảnh hưởng?")

    st.write("""
    Trong Alzheimer, những thay đổi bệnh lý trong não có thể ảnh hưởng
    đến tế bào thần kinh, sự truyền tín hiệu và hoạt động của các mạng
    lưới liên quan đến trí nhớ.

    Hồi hải mã là một trong những vùng có thể bị ảnh hưởng sớm,
    góp phần giải thích vì sao khó ghi nhớ thông tin mới thường
    là biểu hiện đáng chú ý.
    """)

    st.caption(
        "Sơ đồ nội dung mang tính khái quát, không phải hình ảnh giải phẫu "
        "hay mô phỏng chẩn đoán."
    )

    if st.button("Hoàn thành chuyên mục não bộ"):
        mark_complete("brain")
        st.success("Bạn đã hoàn thành chuyên mục!")


# =========================================================
# 15. CẨM NANG ĐỒNG HÀNH
# =========================================================

elif page == "Cẩm nang đồng hành":

    section_title(
        "CARE GUIDE",
        "Cẩm nang đồng hành",
        "Những gợi ý giao tiếp và hỗ trợ trong các tình huống đời thường."
    )

    selected = st.selectbox(
        "Chọn tình huống bạn muốn tìm hiểu",
        list(SCENARIOS.keys())
    )

    scenario = SCENARIOS[selected]

    st.markdown(f"""
    <div class="hero">
        <div class="eyebrow">EVERYDAY SITUATION</div>
        <h1>{safe(selected)}</h1>
        <p>
        Hiểu điều gì có thể đang diễn ra trước khi lựa chọn
        cách phản ứng.
        </p>
    </div>
    """, unsafe_allow_html=True)

    c1, c2 = st.columns(2)

    with c1:
        st.markdown(
            f"""
            <div class="panel">
                <h3>🧠 Điều có thể đang xảy ra</h3>
                <p>{safe(scenario["possible"])}</p>
            </div>
            <div class="gold-panel">
                <h3>⚠️ Nên tránh</h3>
                <p>{safe(scenario["avoid"])}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with c2:
        st.markdown(
            f"""
            <div class="green-panel">
                <h3>🤝 Có thể thử</h3>
                <p>{safe(scenario["try"])}</p>
            </div>
            <div class="panel">
                <h3>💬 Gợi ý giao tiếp</h3>
                <p>{safe(scenario["example"])}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.info(
        "Mỗi người có nhu cầu và biểu hiện khác nhau. "
        "Hãy điều chỉnh cách hỗ trợ theo hoàn cảnh thực tế."
    )

    if st.button("Đã tìm hiểu tình huống này"):
        mark_complete("care_" + selected)
        st.success("Đã ghi nhận hành trình của bạn!")


# =========================================================
# 16. TRẠM TRẢI NGHIỆM
# =========================================================

elif page == "Trạm trải nghiệm":

    section_title(
        "INTERACTIVE EXPERIENCE",
        "Trạm trải nghiệm",
        "Học qua tình huống, thử thách và những lựa chọn nhỏ."
    )

    tab1, tab2 = st.tabs([
        "🎴 Rút thẻ trải nghiệm",
        "🎯 Mini-game kiến thức"
    ])

    with tab1:
        st.subheader("Bộ thẻ CHẠM")
        st.write("Chọn một nhóm thẻ, sau đó rút một tình huống để thử suy nghĩ và phản hồi.")

        group = st.selectbox("Nhóm thẻ", list(CARDS.keys()), key="card_group")

        if st.button("RÚT MỘT THẺ", type="primary"):
            card = random.choice(CARDS[group])
            st.session_state.drawn_cards = [group, card]

        if st.session_state.drawn_cards:
            drawn_group, card = st.session_state.drawn_cards

            st.markdown(f"""
            <div class="hero">
                <div class="eyebrow">CHẠM EXPERIENCE CARD • {safe(drawn_group)}</div>
                <h1>{safe(card["title"])}</h1>
                <p>{safe(card["content"])}</p>
            </div>
            """, unsafe_allow_html=True)

            st.markdown(
                f"""
                <div class="green-panel">
                    <h3>💭 THỬ THÁCH DÀNH CHO BẠN</h3>
                    <p>{safe(card["task"])}</p>
                </div>
                """,
                unsafe_allow_html=True
            )

            response = st.text_area(
                "Suy nghĩ của bạn",
                placeholder="Hãy viết cách bạn sẽ phản ứng...",
                key="card_response"
            )

            if st.button("Lưu suy nghĩ", key="save_card"):
                if response.strip():
                    st.session_state.journal.append({
                        "title": card["title"],
                        "content": response.strip()
                    })
                    mark_complete("card")
                    st.success("Đã lưu suy nghĩ vào nhật ký!")
                else:
                    st.warning("Bạn hãy nhập suy nghĩ trước.")

    with tab2:
        st.subheader("Thử thách kiến thức")
        total = len(QUIZ)

        if st.session_state.quiz_index >= total:
            st.success("Bạn đã hoàn thành toàn bộ câu hỏi!")
            st.metric("Điểm số", f'{st.session_state.score}/{total}')
            st.progress(st.session_state.score / total if total else 0)

            if st.button("Chơi lại"):
                st.session_state.quiz_index = 0
                st.session_state.quiz_feedback = None
                st.session_state.quiz_results = {}
                st.session_state.quiz_answer = None
                st.session_state.score = 0
                st.rerun()
        else:
            idx = st.session_state.quiz_index
            q = QUIZ[idx]

            st.progress(idx / total)
            st.caption(f"CÂU HỎI {idx+1}/{total}")

            st.markdown(f"""
            <div class="panel">
                <div class="small-label">KNOWLEDGE CHALLENGE</div>
                <h3>{safe(q["question"])}</h3>
            </div>
            """, unsafe_allow_html=True)

            choice = st.radio("Chọn câu trả lời", q["options"], key=f"quiz_choice_{idx}", index=None)

            if st.button("XÁC NHẬN ĐÁP ÁN", type="primary", key=f"submit_quiz_{idx}"):
                if choice is None:
                    st.warning("Bạn hãy chọn một đáp án.")
                else:
                    answer_index = q["options"].index(choice)
                    correct = answer_index == q["answer"]

                    st.session_state.quiz_answer = answer_index
                    st.session_state.quiz_feedback = {
                        "correct": correct,
                        "explain": q["explain"]
                    }

                    if idx not in st.session_state.quiz_results:
                        st.session_state.quiz_results[idx] = correct
                        if correct:
                            st.session_state.score += 1

            if st.session_state.quiz_feedback is not None:
                feedback = st.session_state.quiz_feedback
                if feedback["correct"]:
                    st.success("Chính xác! Bạn đã chọn đáp án đúng.")
                else:
                    st.error("Chưa chính xác. Đáp án đúng là: " + q["options"][q["answer"]])

                st.info(feedback["explain"])

                if st.button("CÂU TIẾP THEO →", type="primary", key=f"next_quiz_{idx}"):
                    st.session_state.quiz_index += 1
                    st.session_state.quiz_feedback = None
                    st.session_state.quiz_answer = None
                    st.rerun()

            st.caption(f"Điểm hiện tại: {st.session_state.score}")


# =========================================================
# 17. HÀNH TRÌNH THẤU CẢM
# =========================================================

elif page == "Hành trình thấu cảm":

    section_title(
        "EMPATHY JOURNEY",
        "Hành trình thấu cảm",
        "Mỗi kiến thức được tiếp nhận là một bước tiến đến sự thấu hiểu."
    )

    activities = [
        ("discover", "Khám phá Alzheimer", "Tìm hiểu những kiến thức nền tảng."),
        ("brain", "Não bộ và trí nhớ", "Hiểu cách não bộ hoạt động."),
        ("card", "Rút thẻ trải nghiệm", "Thử đặt mình vào một tình huống."),
        ("care_Đã tìm hiểu", "Thực hành đồng hành", "Tìm hiểu một tình huống chăm sóc."),
        ("read_Alzheimer là gì?", "Đọc kiến thức", "Khám phá một bài viết."),
        ("community", "Chia sẻ suy nghĩ", "Gửi một thông điệp tích cực."),
        ("quiz", "Thử thách kiến thức", "Hoàn thành mini-game.")
    ]

    completed = len(st.session_state.completed)

    st.markdown("""
    <div class="hero">
        <div class="eyebrow">YOUR JOURNEY</div>
        <h1>Hành trình của sự thấu hiểu.</h1>
        <p>
        Không phải cuộc đua để đạt điểm số cao nhất,
        mà là quá trình học cách hiểu và sẻ chia.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.metric("Hoạt động đã ghi nhận", f"{completed}/7")
    st.progress(min(completed / 7, 1.0))

    for key, title, description in activities:
        done = key in st.session_state.completed
        icon = "✅" if done else "○"

        st.markdown(
            f"""
            <div class="panel">
                <b>{icon} {safe(title)}</b><br>
                <span style="color:#5A7184">{safe(description)}</span>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("""
    <div class="quote">
        Thấu hiểu không bắt đầu từ những điều lớn lao,
        mà từ cách chúng ta đối xử với nhau mỗi ngày.
    </div>
    """, unsafe_allow_html=True)

    if st.button("Ghi nhận hoàn thành hành trình"):
        for key, _, _ in activities:
            st.session_state.completed.add(key)
        st.success("Bạn đã ghi nhận hành trình trải nghiệm!")


# =========================================================
# 18. KHÔNG GIAN SẺ CHIA
# =========================================================

elif page == "Không gian sẻ chia":

    section_title(
        "SHARING SPACE",
        "Không gian sẻ chia",
        "Một nơi để ghi lại suy nghĩ, thông điệp và những điều tích cực."
    )

    st.markdown("""
    <div class="green-panel">
        <b>Thông điệp của CHẠM</b><br>
        Một lời hỏi thăm, một lần kiên nhẫn lắng nghe
        hay một hành động quan tâm đều có thể tạo nên sự khác biệt.
    </div>
    """, unsafe_allow_html=True)

    tab1, tab2 = st.tabs([
        "✍️ Nhật ký cá nhân",
        "💚 Góc chia sẻ"
    ])

    with tab1:
        st.subheader("Nhật ký của tôi")
        journal_title = st.text_input("Tiêu đề", placeholder="Một điều tôi nhận ra hôm nay...")
        journal_content = st.text_area("Nội dung", placeholder="Hãy viết những suy nghĩ của bạn...", height=150)

        if st.button("Lưu vào nhật ký", type="primary"):
            if journal_title.strip() and journal_content.strip():
                st.session_state.journal.append({
                    "title": journal_title.strip(),
                    "content": journal_content.strip()
                })
                mark_complete("journal")
                st.success("Đã lưu nhật ký trong phiên truy cập này.")
            else:
                st.warning("Hãy nhập cả tiêu đề và nội dung.")

        st.markdown("---")
        st.subheader("Những ghi chép của bạn")

        if not st.session_state.journal:
            st.info("Bạn chưa có ghi chép nào.")
        else:
            for item in reversed(st.session_state.journal):
                with st.expander(item["title"]):
                    st.write(item["content"])

    with tab2:
        st.subheader("Gửi một thông điệp")
        nickname = st.text_input("Tên hiển thị", value="Một người bạn CHẠM", key="community_name")
        message = st.text_area("Thông điệp của bạn", placeholder="Hãy chia sẻ một điều tích cực...", key="community_message")

        if st.button("Đăng thông điệp"):
            if nickname.strip() and message.strip():
                st.session_state.community.insert(
                    0,
                    {
                        "name": nickname.strip(),
                        "message": message.strip()
                    }
                )
                mark_complete("community")
                st.success("Thông điệp đã được đăng trong phiên này.")
                st.rerun()
            else:
                st.warning("Vui lòng nhập tên hiển thị và nội dung.")

        st.markdown("---")
        st.subheader("Những thông điệp từ cộng đồng")

        if not st.session_state.community:
            st.info("Chưa có thông điệp nào trong phiên truy cập này. Hãy là người đầu tiên chia sẻ!")

        for post in st.session_state.community:
            st.markdown(
                f"""
                <div class="panel">
                    <div style="color:#489E82;font-weight:800">
                        💚 {safe(post["name"])}
                    </div>
                    <p style="color:#3B5266; margin-bottom:0;">{safe(post["message"])}</p>
                </div>
                """,
                unsafe_allow_html=True
            )

        st.warning("Lưu ý: Nội dung nhật ký và góc chia sẻ hiện được lưu trong session_state của phiên truy cập.")


# =========================================================
# 19. NGUỒN THAM KHẢO
# =========================================================

elif page == "Nguồn tham khảo":

    section_title(
        "REFERENCES",
        "Nguồn tham khảo",
        "Một số tổ chức và tài liệu uy tín để tìm hiểu sâu hơn."
    )

    references = [
        (
            "World Health Organization (WHO)",
            "Thông tin về sa sút trí tuệ, sức khỏe cộng đồng và các khuyến nghị.",
            "https://www.who.int/news-room/fact-sheets/detail/dementia"
        ),
        (
            "National Institute on Aging (NIA)",
            "Kiến thức về Alzheimer, triệu chứng, chẩn đoán và chăm sóc.",
            "https://www.nia.nih.gov/health/alzheimers-and-dementia"
        ),
        (
            "Alzheimer's Association",
            "Thông tin giáo dục, hướng dẫn chăm sóc và hỗ trợ gia đình.",
            "https://www.alz.org/"
        ),
        (
            "NHS",
            "Thông tin y tế và hướng dẫn về Alzheimer.",
            "https://www.nhs.uk/conditions/alzheimers-disease/"
        )
    ]

    for name, description, url in references:
        st.markdown(
            f"""
            <div class="panel">
                <h3>📖 {safe(name)}</h3>
                <p style="color:#3B5266;">{safe(description)}</p>
                <a href="{url}" target="_blank">Truy cập tài liệu →</a>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("---")
    st.subheader("Lưu ý về nội dung")
    st.write("""
    CHẠM Hub là nền tảng giáo dục và nâng cao nhận thức.
    Nội dung không nhằm thay thế chẩn đoán, điều trị hoặc tư vấn chuyên môn từ bác sĩ.
    """)

# =========================================================
# 20. CHÂN TRANG
# =========================================================

render_footer()
