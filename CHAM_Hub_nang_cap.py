from pathlib import Path
import random
import html
import streamlit as st
import streamlit.components.v1 as components

# ============================================================
# CHẠM HUB
# Nền tảng giáo dục và nâng cao nhận thức về Alzheimer
# ============================================================

BASE_DIR = Path(__file__).resolve().parent
LOGO_PATH = BASE_DIR / "logo_cham.png" 

st.set_page_config(
    page_title="CHẠM Hub | Thấu hiểu để kết nối",
    page_icon="🤝",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ============================================================
# 1. DỮ LIỆU NỘI DUNG (ĐÃ NÂNG CẤP MODULE 1)
# ============================================================

KNOWLEDGE = [
    {
        "title": "Bản chất y học của bệnh Alzheimer",
        "category": "Kiến thức nền tảng",
        "icon": "🧬",
        "summary": "Alzheimer là một rối loạn não bộ tiến triển mạn tính, làm tổn thương và tiêu diệt dần các tế bào thần kinh.",
        "body": [
            "Dưới góc độ sinh học thần kinh, Alzheimer đặc trưng bởi sự tích tụ bất thường của các mảng bám protein amyloid-beta bên ngoài tế bào thần kinh và các đám rối sợi thần kinh tau bên trong tế bào.",
            "Quá trình tích tụ này làm gián đoạn nghiêm trọng các xung điện và thông tin giữa các tế bào thần kinh, dẫn đến teo dần các vùng não chịu trách nhiệm về trí nhớ, ngôn ngữ và tư duy.",
            "Bệnh không phải là một phần tất yếu của quá trình lão hóa tự nhiên, mà là một bệnh lý có cơ chế sinh bệnh phức tạp cần được cộng đồng thấu hiểu và hỗ trợ đúng cách."
        ],
        "takeaway": "Nhìn nhận Alzheimer dưới góc độ bệnh lý giúp chúng ta loại bỏ định kiến, kiên nhẫn hơn với người bệnh và gia đình họ."
    },
    {
        "title": "Hiểu đúng về các giai đoạn tiến triển của bệnh",
        "category": "Kiến thức nền tảng",
        "icon": "📈",
        "summary": "Bệnh Alzheimer tiến triển theo các mốc từ nhẹ đến nặng, mỗi giai đoạn có những biểu hiện và nhu cầu hỗ trợ riêng.",
        "body": [
            "Giai đoạn sớm (Nhẹ): Người bệnh thường bắt đầu quên các sự kiện gần đây, khó tìm từ ngữ khi nói chuyện, hoặc đôi khi lạc ở những nơi quen thuộc nhưng vẫn có thể tự chủ trong nhiều việc.",
            "Giai đoạn trung bình (Trung bình): Vùng não bị tổn thương lan rộng hơn. Người bệnh có thể nhầm lẫn về thời gian, địa điểm, lặp lại câu hỏi, thay đổi tâm trạng rõ rệt và cần sự hỗ trợ nhiều hơn trong sinh hoạt.",
            "Giai đoạn tiến triển (Nặng): Khả năng giao tiếp bằng lời nói suy giảm rõ rệt, người bệnh phụ thuộc hoàn toàn vào người chăm sóc trong các hoạt động hằng ngày và cần sự chăm sóc y tế toàn diện."
        ],
        "takeaway": "Mỗi giai đoạn đòi hỏi người đồng hành một sự điều chỉnh về cách giao tiếp và phương pháp chăm sóc phù hợp."
    },
    {
        "title": "Phân biệt quên thông thường và dấu hiệu cần lưu ý",
        "category": "Nhận biết",
        "icon": "🔎",
        "summary": "Không phải mọi lần quên đều là Alzheimer. Điều đáng chú ý là tần suất, mức độ và ảnh hưởng đến sinh hoạt.",
        "body": [
            "Quên thông thường có thể là quên nơi để chìa khóa nhưng sau đó nhớ lại, hoặc đôi lúc quên tên một người quen.",
            "Dấu hiệu cần lưu ý có thể gồm: thường xuyên quên thông tin mới, lặp lại cùng một câu hỏi, lạc đường ở nơi quen thuộc hoặc khó hoàn thành công việc vốn rất quen.",
            "Nếu những thay đổi về trí nhớ và tư duy ảnh hưởng đến cuộc sống, gia đình nên trao đổi với nhân viên y tế để được đánh giá phù hợp."
        ],
        "takeaway": "Quan sát bình tĩnh, không tự chẩn đoán và tìm tư vấn chuyên môn khi có lo ngại."
    },
    {
        "title": "Não bộ và trí nhớ",
        "category": "Khoa học dễ hiểu",
        "icon": "🌐",
        "summary": "Trí nhớ là kết quả hoạt động phối hợp của nhiều vùng não và mạng lưới thần kinh.",
        "body": [
            "Não bộ tiếp nhận, xử lý, lưu trữ và gợi lại thông tin thông qua hoạt động của các tế bào thần kinh và kết nối giữa chúng.",
            "Hồi hải mã có vai trò quan trọng trong việc hình thành ký ức mới. Nhiều vùng não khác tham gia vào ngôn ngữ, cảm xúc, định hướng và vận động.",
            "Khi bệnh Alzheimer tiến triển, các mạng lưới thần kinh bị ảnh hưởng, khiến một số chức năng nhận thức suy giảm."
        ],
        "takeaway": "Một ký ức có thể phai mờ, nhưng cảm xúc và nhu cầu được tôn trọng của con người vẫn cần được quan tâm."
    },
    {
        "title": "Giao tiếp đồng cảm",
        "category": "Kỹ năng đồng hành",
        "icon": "💬",
        "summary": "Cách chúng ta nói chuyện có thể giúp người gặp khó khăn về trí nhớ cảm thấy an toàn và được tôn trọng.",
        "body": [
            "Dùng câu ngắn, rõ ràng; nói chậm vừa phải và dành thời gian để người đối diện phản hồi.",
            "Hạn chế chất vấn, tranh cãi hoặc liên tục kiểm tra trí nhớ. Nếu họ nhầm lẫn, hãy nhẹ nhàng chuyển hướng thay vì làm họ xấu hổ.",
            "Gọi tên người đó, duy trì giao tiếp bằng mắt phù hợp và chú ý đến cảm xúc phía sau lời nói."
        ],
        "takeaway": "Đôi khi điều người đối diện cần không phải là một lời sửa sai, mà là cảm giác được lắng nghe."
    },
    {
        "title": "Môi trường sống an toàn",
        "category": "Chăm sóc và hỗ trợ",
        "icon": "🏡",
        "summary": "Một không gian quen thuộc, dễ định hướng và giảm nguy cơ tai nạn có thể hỗ trợ sinh hoạt hằng ngày.",
        "body": [
            "Giữ lối đi thông thoáng, đủ ánh sáng; cất gọn dây điện và vật dễ gây vấp ngã.",
            "Đặt các vật dụng thường dùng ở vị trí ổn định, có thể dùng nhãn hoặc hình minh họa dễ hiểu.",
            "Duy trì lịch sinh hoạt quen thuộc và có người hỗ trợ khi thực hiện những hoạt động có nguy cơ mất an toàn."
        ],
        "takeaway": "Hỗ trợ tốt không có nghĩa là làm thay tất cả; hãy tạo điều kiện để người bệnh làm những việc họ vẫn có thể làm."
    },
    {
        "title": "Người chăm sóc cũng cần được chăm sóc",
        "category": "Sẻ chia",
        "icon": "🤝",
        "summary": "Đồng hành lâu dài có thể tạo áp lực. Người chăm sóc cần được nghỉ ngơi, chia sẻ và hỗ trợ.",
        "body": [
            "Cảm giác mệt mỏi, lo lắng hoặc bất lực có thể xuất hiện khi chăm sóc người thân trong thời gian dài.",
            "Gia đình nên phân chia trách nhiệm, trao đổi thẳng thắn về nhu cầu và tìm kiếm sự trợ giúp từ cộng đồng hoặc chuyên gia.",
            "Nghỉ ngơi không phải ích kỷ. Đó là một phần quan trọng để duy trì khả năng chăm sóc bền vững."
        ],
        "takeaway": "Không ai phải đi một mình – cả người cần hỗ trợ lẫn người đang chăm sóc."
    }
]

CARE_SCENARIOS = [
    {
        "title": "Người thân hỏi đi hỏi lại cùng một câu",
        "situation": "Bà hỏi: “Hôm nay mẹ con có về ăn cơm không?” dù bạn đã trả lời vài lần.",
        "options": [
            ("A", "Nói lớn rằng bà đã hỏi câu này rất nhiều lần rồi."),
            ("B", "Bình tĩnh trả lời ngắn gọn, sau đó chuyển sang hoạt động quen thuộc."),
            ("C", "Bỏ đi vì không muốn trả lời nữa.")
        ],
        "best": "B",
        "explain": "Trả lời bình tĩnh và chuyển hướng nhẹ nhàng giúp giảm căng thẳng. Tránh trách móc vì người bệnh có thể không nhớ mình vừa hỏi."
    },
    {
        "title": "Người thân không nhớ tên bạn",
        "situation": "Ông nhìn bạn bối rối và gọi nhầm tên.",
        "options": [
            ("A", "Bắt ông phải đoán đúng tên."),
            ("B", "Giận dỗi và bỏ đi."),
            ("C", "Nhẹ nhàng giới thiệu lại mình và tiếp tục trò chuyện.")
        ],
        "best": "C",
        "explain": "Giới thiệu lại bằng thái độ thân thiện giúp người thân bớt áp lực và giữ được kết nối."
    },
    {
        "title": "Người thân lo lắng khi ở nơi đông người",
        "situation": "Trong buổi họp mặt gia đình, người thân trở nên bồn chồn và muốn rời đi.",
        "options": [
            ("A", "Ép họ ở lại để không mất vui."),
            ("B", "Đưa họ đến nơi yên tĩnh hơn và hỏi xem họ cần gì."),
            ("C", "Trêu đùa để mọi người cùng cười.")
        ],
        "best": "B",
        "explain": "Giảm kích thích, tìm không gian yên tĩnh và lắng nghe nhu cầu có thể giúp người thân cảm thấy an toàn hơn."
    },
    {
        "title": "Người thân làm rơi đồ vật",
        "situation": "Người thân vô tình làm rơi chiếc cốc khi đang tự uống nước.",
        "options": [
            ("A", "Mắng vì đã bất cẩn."),
            ("B", "Giật ngay chiếc cốc và không cho tự làm nữa."),
            ("C", "Hỗ trợ dọn dẹp an toàn, sau đó xem xét cách bố trí phù hợp hơn.")
        ],
        "best": "C",
        "explain": "Ưu tiên an toàn nhưng vẫn tôn trọng khả năng tự chủ. Có thể thay bằng cốc phù hợp hoặc hỗ trợ khi cần."
    }
]

QUIZ = [
    {
        "q": "Alzheimer thường ảnh hưởng trực tiếp đến hệ cơ quan nào?",
        "opts": ["Hệ tiêu hóa", "Não bộ", "Hệ hô hấp", "Da"],
        "ans": 1,
        "why": "Alzheimer là bệnh lý não tiến triển, ảnh hưởng đến trí nhớ và các chức năng nhận thức."
    },
    {
        "q": "Điều nào sau đây là cách giao tiếp phù hợp?",
        "opts": [
            "Liên tục kiểm tra trí nhớ",
            "Tranh luận để chứng minh người bệnh sai",
            "Dùng câu ngắn, rõ ràng và kiên nhẫn",
            "Nói thật nhanh để tiết kiệm thời gian"
        ],
        "ans": 2,
        "why": "Câu ngắn, rõ ràng và nhịp nói vừa phải giúp cuộc trò chuyện dễ theo dõi hơn."
    },
    {
        "q": "Khi một người lớn tuổi thường xuyên gặp khó khăn về trí nhớ và sinh hoạt, gia đình nên làm gì?",
        "opts": [
            "Tự kết luận là Alzheimer",
            "Phớt lờ vì đó luôn là lão hóa bình thường",
            "Trao đổi với nhân viên y tế để được đánh giá",
            "Trách móc để họ cố gắng nhớ"
        ],
        "ans": 2,
        "why": "Không thể tự chẩn đoán qua một vài biểu hiện. Đánh giá chuyên môn giúp xác định nguyên nhân và hướng hỗ trợ."
    },
    {
        "q": "Vì sao người chăm sóc cần được nghỉ ngơi?",
        "opts": [
            "Vì chăm sóc không quan trọng",
            "Để duy trì sức khỏe và khả năng đồng hành lâu dài",
            "Để tránh tiếp xúc với người bệnh",
            "Vì người bệnh không cần hỗ trợ"
        ],
        "ans": 1,
        "why": "Chăm sóc bền vững cần sự chia sẻ trách nhiệm và quan tâm đến sức khỏe của người chăm sóc."
    },
    {
        "q": "Khi người thân lặp lại một câu hỏi, phản ứng nào nên được ưu tiên?",
        "opts": [
            "Bình tĩnh trả lời và chuyển hướng nhẹ nhàng",
            "Cáu gắt để họ nhớ",
            "Chế giễu trước mặt mọi người",
            "Cố tình không phản hồi"
        ],
        "ans": 0,
        "why": "Thái độ bình tĩnh giúp giảm căng thẳng và duy trì cảm giác an toàn."
    }
]

REFLECTION_PROMPTS = [
    "Một điều tôi hiểu hơn về người gặp khó khăn về trí nhớ là…",
    "Nếu người thân lặp lại một câu hỏi, tôi có thể…",
    "Một hành động nhỏ tôi muốn thực hiện để giúp gia đình/cộng đồng là…",
    "Tôi muốn nhắn gửi điều gì đến người đang chăm sóc người thân?"
]

CARD_PROMPTS = [
    "Một người có thể quên tên bạn nhưng vẫn cần cảm nhận được sự an toàn.",
    "Kiên nhẫn không phải là im lặng chịu đựng; đó là lựa chọn phản hồi bằng sự tôn trọng.",
    "Một không gian quen thuộc có thể giúp người gặp khó khăn về trí nhớ bớt bối rối.",
    "Người chăm sóc cũng cần được lắng nghe và nghỉ ngơi.",
    "Đừng chỉ hỏi người bệnh còn nhớ gì. Hãy hỏi họ đang cảm thấy thế nào.",
    "Sự đồng hành bắt đầu từ việc nhìn thấy con người, không chỉ nhìn thấy căn bệnh."
]

# ============================================================
# 2. SESSION STATE
# ============================================================

DEFAULTS = {
    "intro_done": False,
    "journal": [],
    "community": [],
    "completed": [],
    "quiz_index": 0,
    "quiz_score": 0,
    "quiz_answered": [],
    "care_answers": {},
    "drawn_cards": [],
    "current_card": None,
    "reflection_text": ""
}

for key, value in DEFAULTS.items():
    if key not in st.session_state:
        st.session_state[key] = value.copy() if isinstance(value, (list, dict)) else value

def mark_complete(item):
    if item not in st.session_state.completed:
        st.session_state.completed.append(item)

def render_logo(width=130):
    if LOGO_PATH.exists():
        st.image(str(LOGO_PATH), width=width)
    else:
        st.markdown('<div class="brand-mark">🤝 <b>CHẠM</b></div>', unsafe_allow_html=True)

def section_header(eyebrow, title, subtitle=None):
    st.markdown(
        f'<div class="eyebrow">{html.escape(eyebrow)}</div>',
        unsafe_allow_html=True
    )
    st.title(title)
    if subtitle:
        st.markdown(f'<p class="muted lead">{subtitle}</p>', unsafe_allow_html=True)

def render_footer():
    st.markdown("""
    <div class="footer">
      <div class="footer-brand">🤝 CHẠM HUB</div>
      <div>Thấu hiểu để kết nối – Kết nối để sẻ chia.</div>
      <small>Nền tảng giáo dục và nâng cao nhận thức. Không thay thế chẩn đoán, tư vấn hoặc điều trị y tế.</small>
    </div>
    """, unsafe_allow_html=True)

# ============================================================
# 3. CSS – NHẬN DIỆN GIAO DIỆN
# ============================================================

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:wght@300;400;500;600;700;800&display=swap');

:root {
    --deep:#092f2d;
    --green:#0d6255;
    --mint:#dff3eb;
    --gold:#e7c77a;
    --ink:#183b37;
}

html, body, [class*="css"] {
    font-family:'Be Vietnam Pro',sans-serif;
}

.stApp {
    background:linear-gradient(180deg,#f5faf7 0%,#eef6f1 100%);
    color:var(--ink);
}

.block-container {
    max-width:1220px;
    padding-top:2rem;
    padding-bottom:3rem;
}

h1,h2,h3 {
    color:#103e38;
    letter-spacing:-.03em;
}

h1 {font-weight:800;}

p,li {line-height:1.75;}

.muted {color:#617a73;}

.lead {
    font-size:1.05rem;
    max-width:850px;
}

.eyebrow {
    color:#b18a39;
    text-transform:uppercase;
    letter-spacing:.16em;
    font-size:.75rem;
    font-weight:800;
    margin-bottom:.45rem;
}

.brand-mark {
    color:#0b5148;
    font-size:2rem;
    letter-spacing:.08em;
    padding:.4rem 0;
}

.hero {
    background:
        radial-gradient(circle at 85% 15%,#246d5d 0%,transparent 30%),
        linear-gradient(125deg,#082f2d,#105b4e);
    color:white;
    border-radius:28px;
    padding:clamp(28px,5vw,62px);
    position:relative;
    overflow:hidden;
}

.hero h1 {
    color:white;
    font-size:clamp(2.3rem,5vw,4.5rem);
    margin:.4rem 0;
    line-height:1.08;
}

.hero p {
    color:#d8eee5;
    max-width:720px;
    font-size:1.08rem;
}

.hero-kicker {
    color:#f0d48c;
    letter-spacing:.2em;
    text-transform:uppercase;
    font-size:.78rem;
    font-weight:800;
}

.hero-orb {
    position:absolute;
    right:7%;
    top:12%;
    width:190px;
    height:190px;
    border:1px solid #ffffff35;
    border-radius:50%;
    box-shadow:0 0 0 28px #ffffff0b,0 0 0 58px #ffffff08;
}

.panel {
    background:white;
    border:1px solid #e1eee7;
    border-radius:20px;
    padding:22px;
    box-shadow:0 8px 26px #164c3710;
    height:100%;
}

.panel h3 {margin-top:.2rem;}

.panel-icon {font-size:1.8rem;}

.tag {
    display:inline-block;
    background:#e7f4ed;
    color:#17634f;
    border-radius:99px;
    padding:5px 11px;
    font-size:.72rem;
    font-weight:700;
    margin-bottom:10px;
}

.quote {
    border-left:4px solid #d6b35d;
    padding:12px 18px;
    background:#fffaf0;
    border-radius:0 14px 14px 0;
    color:#5c5137;
    margin:18px 0;
}

.metric {
    background:#fff;
    border:1px solid #e0eee7;
    border-radius:18px;
    padding:18px;
}

.metric-number {
    font-size:2rem;
    color:#0c6253;
    font-weight:800;
}

.footer {
    border-top:1px solid #dcebe2;
    margin-top:55px;
    padding:24px 0 10px;
    text-align:center;
    color:#698078;
}

.footer-brand {
    color:#0d5147;
    font-weight:800;
    letter-spacing:.16em;
    margin-bottom:5px;
}

.footer small {
    display:block;
    margin-top:8px;
    font-size:.75rem;
}

div.stButton > button {
    border-radius:12px;
    font-weight:700;
    min-height:2.8rem;
    border:1px solid #c9dfd3;
}

div.stButton > button[kind="primary"] {
    background:#0c5b4e;
    border-color:#0c5b4e;
}

div.stButton > button[kind="primary"]:hover {
    background:#09473e;
    border-color:#09473e;
}

.stTabs [data-baseweb="tab-list"] {gap:8px;}

.stTabs [data-baseweb="tab"] {
    background:#e7f2eb;
    border-radius:10px 10px 0 0;
    padding:10px 18px;
}

[data-testid="stSidebar"] {background:#e9f4ed;}

hr {border-color:#dcebe2;}

div[data-testid="stProgress"] > div > div {
    background:#0c7661;
}
</style>
""", unsafe_allow_html=True)

# ============================================================
# 4. MÀN HÌNH CHÀO + GIỌNG ĐỌC
# ============================================================

def welcome_screen():

    st.markdown("""
    <style>
    [data-testid="stSidebar"], header, footer {visibility:hidden;}

    .block-container {
        max-width:1000px;
        padding-top:5vh;
    }

    .welcome-shell {
        background:
            radial-gradient(circle at 80% 20%,#286e60 0%,transparent 28%),
            linear-gradient(135deg,#062c2b,#0d5147);
        padding:clamp(28px,6vw,72px);
        border-radius:30px;
        color:white;
        text-align:center;
        box-shadow:0 24px 70px #092f2d35;
    }

    .welcome-shell h1 {
        color:white;
        font-size:clamp(3rem,8vw,5.8rem);
        letter-spacing:.12em;
        margin:.2rem 0;
    }

    .welcome-shell h3 {
        color:#efd58f;
        font-size:clamp(1rem,2vw,1.35rem);
        letter-spacing:.16em;
    }

    .welcome-shell p {
        color:#e0f0e9;
        max-width:700px;
        margin:18px auto;
        line-height:1.9;
    }

    .welcome-symbol {font-size:3.5rem;}
    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="welcome-shell">
        <div class="welcome-symbol">🤝</div>
        <h1>CHẠM</h1>
        <h3>THẤU HIỂU ĐỂ KẾT NỐI</h3>
        <p>
        Chào mừng bạn đến với CHẠM Hub – không gian khám phá
        kiến thức về Alzheimer, tìm hiểu cách trí nhớ vận hành
        và học cách đồng hành bằng sự kiên nhẫn, tôn trọng
        và yêu thương.
        </p>
        <p><b>Không ai phải đi một mình.</b></p>
    </div>
    """, unsafe_allow_html=True)

    if LOGO_PATH.exists():
        st.image(str(LOGO_PATH), width=110)

    intro_text = (
        "Chào mừng bạn đến với Chạm Hub. "
        "Alzheimer không chỉ là câu chuyện về trí nhớ, "
        "mà còn là câu chuyện về sinh học não bộ, con người và sự kết nối. "
        "Tại đây, bạn sẽ khám phá kiến thức khoa học chi tiết, "
        "thử sức với các tình huống đồng hành, tham gia trò chơi tương tác "
        "và viết nên những hành động sẻ chia của riêng mình. "
        "Hãy cùng CHẠM thấu hiểu để kết nối, kết nối để sẻ chia. "
        "Không ai phải đi một mình."
    )

    safe_text = (
        intro_text
        .replace("\\", "\\\\")
        .replace("'", "\\'")
        .replace("\n", " ")
    )

    components.html(f"""
    <div style="display:flex;gap:12px;justify-content:center;flex-wrap:wrap;margin:18px 0 6px">
      <button id="speak"
      style="background:#e8d18e;color:#173e36;border:0;border-radius:12px;padding:13px 22px;font-weight:800;cursor:pointer">
      🔊 NGHE GIỚI THIỆU
      </button>

      <button id="stop"
      style="background:#ffffff18;color:white;border:1px solid #ffffff66;border-radius:12px;padding:13px 22px;font-weight:700;cursor:pointer">
      ■ DỪNG ĐỌC
      </button>
    </div>

    <div id="voice-status"
    style="text-align:center;color:#d7eee5;font:13px Arial;margin-top:8px">
    Giọng đọc sử dụng tính năng đọc tiếng Việt có sẵn trên trình duyệt/thiết bị.
    </div>

    <script>
      const message = '{safe_text}';
      const status = document.getElementById('voice-status');

      document.getElementById('speak').onclick = () => {{
        if (!('speechSynthesis' in window)) {{
          status.textContent='Trình duyệt này chưa hỗ trợ đọc văn bản.';
          return;
        }}

        window.speechSynthesis.cancel();

        const utter = new SpeechSynthesisUtterance(message);
        utter.lang='vi-VN';
        utter.rate=0.9;
        utter.pitch=1;
        utter.volume=1;

        const voices=window.speechSynthesis.getVoices();
        const vi=voices.find(v =>
          v.lang && v.lang.toLowerCase().startsWith('vi')
        );

        if (vi) utter.voice=vi;

        utter.onstart=() =>
          status.textContent='Đang phát lời giới thiệu…';

        utter.onend=() =>
          status.textContent='Đã phát xong lời giới thiệu.';

        utter.onerror=() =>
          status.textContent='Không thể phát giọng đọc trên thiết bị này.';

        window.speechSynthesis.speak(utter);
      }};

      document.getElementById('stop').onclick = () => {{
        if ('speechSynthesis' in window) {{
          window.speechSynthesis.cancel();
        }}
        status.textContent='Đã dừng giọng đọc.';
      }};
    </script>
    """, height=105)

    st.markdown("<div style='height:8px'></div>", unsafe_allow_html=True)

    c1, c2, c3 = st.columns([1, 2, 1])

    with c2:
        if st.button(
            "BẮT ĐẦU KHÁM PHÁ CHẠM HUB  →",
            type="primary",
            use_container_width=True
        ):
            st.session_state.intro_done = True
            st.rerun()

    st.caption(
        "Trình duyệt thường yêu cầu người dùng chủ động bấm nút "
        "để cho phép phát giọng đọc."
    )


if not st.session_state.intro_done:
    welcome_screen()
    st.stop()

# ============================================================
# 5. SIDEBAR – ĐIỀU HƯỚNG
# ============================================================

with st.sidebar:

    render_logo(115)

    st.markdown("### CHẠM HUB")
    st.caption("Thấu hiểu để kết nối")

    page = st.radio(
        "KHÁM PHÁ",
        [
            "Trang chủ",
            "Khám phá Alzheimer",
            "Não bộ & trí nhớ",
            "Thư viện tri thức",
            "Cẩm nang đồng hành",
            "Trạm trải nghiệm",
            "Hành trình thấu cảm",
            "Không gian sẻ chia",
            "Nguồn tham khảo"
        ],
        label_visibility="collapsed",
        key="main_navigation"
    )

    st.divider()

    st.markdown("**Tiến trình khám phá**")

    progress = min(len(st.session_state.completed) / 6, 1.0)

    st.progress(progress)

    st.caption(
        f"{len(st.session_state.completed)} hoạt động đã hoàn thành"
    )

    if st.button("↩ Xem lại màn hình chào", use_container_width=True):
        st.session_state.intro_done = False
        st.rerun()

# ============================================================
# 6. TRANG CHỦ
# ============================================================

if page == "Trang chủ":

    st.markdown("""
    <div class="hero">
      <div class="hero-orb"></div>
      <div class="hero-kicker">A SPACE FOR UNDERSTANDING</div>

      <h1>CHẠM<br>để thấu hiểu.</h1>

      <p>
      Một hành trình học hỏi nâng cao về Alzheimer, cơ chế sinh học não bộ và sự đồng hành.
      Bắt đầu từ kiến thức chuẩn y khoa, tiếp nối bằng trải nghiệm
      và kết thúc bằng một hành động sẻ chia.
      </p>

      <div style="color:#f0d48c;font-weight:700;letter-spacing:.04em">
      THẤU HIỂU ĐỂ KẾT NỐI – KẾT NỐI ĐỂ SẺ CHIA.
      </div>
    </div>
    """, unsafe_allow_html=True)

    st.write("")

    st.subheader("Một hành trình gồm nhiều điểm chạm")

    cols = st.columns(3)

    cards = [
        ("🧠", "Hiểu sâu bản chất",
         "Khám phá cơ chế sinh học thần kinh và các giai đoạn tiến triển của Alzheimer."),
        ("🤝", "Biết cách đồng hành",
         "Thực hành phản hồi trong những tình huống đời sống gần gũi."),
        ("💚", "Lan tỏa sẻ chia",
         "Ghi lại suy nghĩ và biến sự thấu hiểu thành hành động nhỏ.")
    ]

    for col, (icon, title, desc) in zip(cols, cards):
        with col:
            st.markdown(
                f'<div class="panel"><div class="panel-icon">{icon}</div>'
                f'<h3>{title}</h3><p class="muted">{desc}</p></div>',
                unsafe_allow_html=True
            )

    st.write("")
    st.subheader("Khám phá nhanh")

    quick = st.columns(4)

    quick_items = [
        ("📚", "Thư viện tri thức", "Kiến thức chuyên sâu & nền tảng"),
        ("🧩", "Trạm trải nghiệm", "Mini-game và câu hỏi"),
        ("💬", "Cẩm nang đồng hành", "Tình huống đời sống"),
        ("🌱", "Hành trình thấu cảm", "Viết điều bạn muốn làm")
    ]

    for col, (ic, title, desc) in zip(quick, quick_items):
        with col:
            st.markdown(
                f'<div class="panel"><div class="panel-icon">{ic}</div>'
                f'<b>{title}</b><p class="muted">{desc}</p></div>',
                unsafe_allow_html=True
            )

    st.write("")

    a, b = st.columns([2, 1])

    with a:
        st.markdown(
            '<div class="quote"><b>“Không ai phải đi một mình.”</b>'
            '<br>Một lời nhắc rằng sự thấu hiểu và hỗ trợ '
            'có thể bắt đầu từ những hành động rất nhỏ.</div>',
            unsafe_allow_html=True
        )

    with b:
        st.markdown(
            '<div class="metric"><div class="metric-number">CHẠM</div>'
            '<div class="muted">Kiến thức · Trải nghiệm · Đồng cảm</div></div>',
            unsafe_allow_html=True
        )

# ============================================================
# 7. KHÁM PHÁ ALZHEIMER (MODULE 1 NÂNG CẤP TOÀN DIỆN)
# ============================================================

elif page == "Khám phá Alzheimer":

    section_header(
        "01 / MODULE 1: HIỂU SÂU VỀ ALZHEIMER",
        "Khám phá Alzheimer & Cơ chế sinh học",
        "Trang bị kiến thức khoa học cốt lõi, góc nhìn chuyên sâu và lộ trình tiến triển của bệnh."
    )

    st.markdown(
        '<div class="quote"><b>Góc nhìn nhân văn:</b> Alzheimer không xóa nhòa nhân cách hay tình cảm sâu kín của một con người. '
        'Hiểu đúng về căn bệnh giúp chúng ta nhìn thấu những nhu cầu đằng sau biểu hiện bên ngoài.</div>',
        unsafe_allow_html=True
    )

    # Chia các Tab nâng cấp cho Module 1
    mod1_tabs = st.tabs([
        "🧬 Cơ chế sinh học thần kinh",
        "📊 Các giai đoạn tiến triển",
        "⚠️ Nhận diện & Lưu ý y tế"
    ])

    with mod1_tabs[0]:
        st.subheader("Bản chất phân tử và cấu trúc não bộ bị ảnh hưởng")
        st.write(
            "Bệnh Alzheimer là kết quả của sự suy thoái tế bào thần kinh diễn ra âm thầm trong nhiều năm trước khi các triệu chứng lâm sàng xuất hiện rõ rệt. "
            "Hai 'dấu ấn sinh học' chính cấu thành bệnh bao gồm:"
        )
        
        col_a, col_b = st.columns(2)
        with col_a:
            st.markdown("""
            <div class="panel">
              <h4>🧱 Mảng bám Amyloid-beta</h4>
              <p class="muted">Các đoạn protein amyloid tích tụ lại thành mảng bám cứng đầu nằm giữa các tế bào thần kinh trong não, cản trở trực tiếp quá trình truyền tín hiệu sinh hóa giữa các synapse.</p>
            </div>
            """, unsafe_allow_html=True)
        with col_b:
            st.markdown("""
            <div class="panel">
              <h4>🧵 Đám rối sợi Tau</h4>
              <p class="muted">Bên trong tế bào thần kinh, các protein tau thay đổi cấu trúc, quấn xoắn lại với nhau thành các đám rối, khiến hệ thống vận chuyển chất dinh dưỡng bên trong tế bào bị sụp đổ.</p>
            </div>
            """, unsafe_allow_html=True)

        st.write("")
        st.info("💡 **Hậu quả:** Sự kết hợp của mảng bám và đám rối sợi thần kinh làm cho các tế bào não teo dần (teo vỏ não và vùng hồi hải mã), làm mất dần khả năng ghi nhớ và điều phối hành vi.")

    with mod1_tabs[1]:
        st.subheader("Hành trình tiến triển của bệnh qua 3 giai đoạn chính")
        st.write("Việc nắm bắt các giai đoạn giúp người chăm sóc chuẩn bị tâm lý và phương án hỗ trợ phù hợp cho từng mốc thời gian:")

        stage_cols = st.columns(3)
        stages_info = [
            ("Giai đoạn 1: Sớm (Nhẹ)", "🌱", "Bắt đầu quên các cuộc trò chuyện gần đây, hay để lẫn lộn đồ đạc, khó tập trung hoặc lập kế hoạch. Người bệnh vẫn có thể tự chăm sóc bản thân nhưng bắt đầu nhận thấy sự khác biệt."),
            ("Giai đoạn 2: Trung bình", "⚡", "Vùng não tổn thương lan rộng. Người bệnh gặp khó khăn khi mặc quần áo, nhầm lẫn thứ ngày/tháng, hay đi lạc, có thể có các thay đổi về cảm xúc hoặc hoang tưởng nhẹ."),
            ("Giai đoạn 3: Tiến triển (Nặng)", "🛡️", "Mất khả năng giao tiếp mạch lạc, không nhận diện được người thân quen, phụ thuộc hoàn toàn vào người chăm sóc trong mọi hoạt động ăn uống, vệ sinh hằng ngày.")
        ]
        for col, (st_title, st_icon, st_desc) in zip(stage_cols, stages_info):
            with col:
                st.markdown(f'<div class="panel"><div class="panel-icon">{st_icon}</div><h3>{st_title}</h3><p class="muted">{st_desc}</p></div>', unsafe_allow_html=True)

    with mod1_tabs[2]:
        st.subheader("Lưu ý y tế quan trọng và khuyến cáo chẩn đoán")
        st.write(
            "Việc chẩn đoán chính xác đòi hỏi sự thăm khám kỹ lưỡng từ các bác sĩ chuyên khoa thần kinh thông qua bài kiểm tra nhận thức, "
            "chụp chiếu thần kinh (MRI/CT) và loại trừ các nguyên nhân khác gây suy giảm trí nhớ (như thiếu hụt vitamin, trầm cảm, hoặc bệnh lý tuyến giáp)."
        )
        st.warning(
            "⚠️ **Lưu ý quan trọng:** Không tự ý kết luận người lớn tuổi bị Alzheimer chỉ qua một vài lần quên lẫn thông thường. "
            "Hãy đưa người thân đến cơ sở y tế uy tín để được đánh giá toàn diện và nhận tư vấn phác đồ chuẩn y khoa."
        )

    st.write("")
    if st.button("Đã hoàn thành tìm hiểu Module 1", type="primary"):
        mark_complete("basics")
        st.success("Tuyệt vời! Tiến trình Module 1 của bạn đã được ghi nhận.")

# ============================================================
# 8. NÃO BỘ & TRÍ NHỚ
# ============================================================

elif page == "Não bộ & trí nhớ":

    section_header(
        "02 / THE BRAIN",
        "Não bộ & trí nhớ",
        "Tìm hiểu cách não bộ tiếp nhận, lưu trữ và gợi lại những điều làm nên ký ức."
    )

    st.markdown("""
    <div class="panel">
      <div class="panel-icon">🧠</div>
      <h3>Trí nhớ là một mạng lưới</h3>
      <p>Trí nhớ hình thành từ hoạt động phối hợp của nhiều vùng não
      và các kết nối thần kinh. Không có một “ngăn kéo ký ức”
      duy nhất trong não.</p>
    </div>
    """, unsafe_allow_html=True)

    st.write("")

    brain_cols = st.columns(3)

    brain_data = [
        ("🧭", "Hồi hải mã",
         "Có vai trò quan trọng trong việc hình thành và củng cố ký ức mới."),
        ("🗣️", "Vùng ngôn ngữ",
         "Tham gia hiểu lời nói, lựa chọn từ ngữ và diễn đạt suy nghĩ."),
        ("❤️", "Mạng lưới cảm xúc",
         "Góp phần tạo nên sắc thái cảm xúc gắn với trải nghiệm và ký ức.")
    ]

    for col, (icon, title, desc) in zip(brain_cols, brain_data):
        with col:
            st.markdown(
                f'<div class="panel"><div class="panel-icon">{icon}</div>'
                f'<h3>{title}</h3><p class="muted">{desc}</p></div>',
                unsafe_allow_html=True
            )

    st.write("")
    st.subheader("Một ký ức được hình thành như thế nào?")

    stages = st.columns(4)

    stage_data = [
        ("01", "Tiếp nhận", "Não bộ tiếp nhận thông tin từ giác quan."),
        ("02", "Mã hóa", "Thông tin được xử lý và liên kết với trải nghiệm."),
        ("03", "Lưu trữ", "Các kết nối thần kinh tham gia duy trì thông tin."),
        ("04", "Gợi lại", "Ta truy xuất thông tin khi cần sử dụng.")
    ]

    for col, (n, title, desc) in zip(stages, stage_data):
        with col:
            st.markdown(
                f'<div class="panel"><div class="tag">BƯỚC {n}</div>'
                f'<h3>{title}</h3><p class="muted">{desc}</p></div>',
                unsafe_allow_html=True
            )

    st.markdown(
        '<div class="quote">Khi một người không thể nhớ lại điều gì đó, '
        'điều đó không có nghĩa là tình cảm, nhân cách hay giá trị '
        'của họ biến mất.</div>',
        unsafe_allow_html=True
    )

    if st.button("Hoàn thành chủ đề Não bộ & trí nhớ", type="primary"):
        mark_complete("brain")
        st.success("Bạn đã hoàn thành chủ đề này.")

# ============================================================
# 9. THƯ VIỆN TRI THỨC
# ============================================================

elif page == "Thư viện tri thức":

    section_header(
        "03 / KNOWLEDGE LIBRARY",
        "Thư viện tri thức",
        "Chọn một chủ đề để đọc. Nội dung được thiết kế ngắn gọn, gần gũi và dễ ghi nhớ."
    )

    categories = ["Tất cả"] + sorted(
        set(x["category"] for x in KNOWLEDGE)
    )

    selected_category = st.selectbox(
        "Lọc theo chủ đề",
        categories
    )

    search = st.text_input(
        "Tìm kiếm nội dung",
        placeholder="Ví dụ: trí nhớ, giao tiếp, chăm sóc…"
    )

    filtered = [
        x for x in KNOWLEDGE
        if (
            selected_category == "Tất cả"
            or x["category"] == selected_category
        )
        and (
            not search
            or search.lower() in (
                x["title"] + x["summary"] + x["category"]
            ).lower()
        )
    ]

    if not filtered:
        st.warning("Không tìm thấy chủ đề phù hợp. Hãy thử từ khóa khác.")

    for item in filtered:

        item_index = KNOWLEDGE.index(item)

        with st.expander(
            f'{item["icon"]}  {item["title"]}  ·  {item["category"]}'
        ):

            st.write(item["summary"])

            for paragraph in item["body"]:
                st.write(paragraph)

            st.markdown(
                f'<div class="quote"><b>Điều cần nhớ:</b> '
                f'{item["takeaway"]}</div>',
                unsafe_allow_html=True
            )

            if st.button(
                "Đánh dấu đã đọc",
                key=f"read_{item_index}"
            ):
                mark_complete(f"knowledge_{item_index}")
                st.success("Đã đánh dấu chủ đề đã đọc.")

    st.caption(
        f"Đang hiển thị {len(filtered)} / {len(KNOWLEDGE)} chủ đề."
    )

# ============================================================
# 10. CẨM NANG ĐỒNG HÀNH
# ============================================================

elif page == "Cẩm nang đồng hành":

    section_header(
        "04 / CARE GUIDE",
        "Cẩm nang đồng hành",
        "Thử đặt mình vào những tình huống quen thuộc và lựa chọn cách phản hồi giàu tôn trọng."
    )

    st.markdown(
        '<div class="quote">Mục tiêu không phải là “thắng” một cuộc tranh luận '
        'hay buộc ai đó phải nhớ đúng. Mục tiêu là giữ an toàn, '
        'giảm căng thẳng và duy trì kết nối.</div>',
        unsafe_allow_html=True
    )

    for i, scenario in enumerate(CARE_SCENARIOS):

        with st.container(border=True):

            st.markdown(
                f"### Tình huống {i+1}: {scenario['title']}"
            )

            st.write(scenario["situation"])

            choice = st.radio(
                "Bạn sẽ phản hồi thế nào?",
                options=[
                    f"{letter}. {text}"
                    for letter, text in scenario["options"]
                ],
                key=f"care_choice_{i}",
                index=None
            )

            if st.button("Xem gợi ý", key=f"care_reveal_{i}"):

                selected_letter = choice[0] if choice else None

                st.session_state.care_answers[i] = selected_letter

            if i in st.session_state.care_answers:

                selected_letter = st.session_state.care_answers[i]

                if selected_letter == scenario["best"]:
                    st.success(
                        "Lựa chọn phù hợp. " + scenario["explain"]
                    )

                elif selected_letter is None:
                    st.info(
                        "Hãy thử chọn một phương án trước. "
                        + scenario["explain"]
                    )

                else:
                    st.warning(
                        f"Phương án nên ưu tiên là {scenario['best']}. "
                        + scenario["explain"]
                    )

    if len(st.session_state.care_answers) == len(CARE_SCENARIOS):

        if st.button(
            "Hoàn thành cẩm nang đồng hành",
            type="primary"
        ):
            mark_complete("care")
            st.success("Đã hoàn thành các tình huống.")

# ============================================================
# 11. TRẠM TRẢI NGHIỆM
# ============================================================

elif page == "Trạm trải nghiệm":

    section_header(
        "05 / INTERACTIVE LAB",
        "Trạm trải nghiệm",
        "Học qua câu hỏi, lựa chọn và phản hồi tức thì."
    )

    tab_quiz, tab_cards = st.tabs([
        "🧠 Thử thách kiến thức",
        "🃏 Thẻ suy ngẫm"
    ])

    # ----- QUIZ -----

    with tab_quiz:

        total = len(QUIZ)
        idx = st.session_state.quiz_index

        if idx < total:

            q = QUIZ[idx]

            st.progress(idx / total)

            st.caption(f"CÂU HỎI {idx+1}/{total}")

            st.subheader(q["q"])

            answer = st.radio(
                "Chọn một đáp án",
                q["opts"],
                key=f"quiz_option_{idx}",
                index=None
            )

            if st.button(
                "Kiểm tra đáp án",
                type="primary",
                key=f"quiz_submit_{idx}"
            ):

                if answer is None:
                    st.warning("Hãy chọn một đáp án trước khi kiểm tra.")

                else:

                    selected = q["opts"].index(answer)
                    correct = selected == q["ans"]

                    if correct:
                        st.session_state.quiz_score += 1
                        st.success("Chính xác! " + q["why"])
                    else:
                        st.error("Chưa chính xác. " + q["why"])

                    st.session_state.quiz_answered.append(selected)
                    st.session_state.quiz_index += 1

                    st.rerun()

        else:

            st.markdown("### Bạn đã hoàn thành thử thách!")

            st.markdown(
                f'<div class="metric">'
                f'<div class="metric-number">'
                f'{st.session_state.quiz_score}/{total}'
                f'</div><div class="muted">Số câu trả lời đúng</div></div>',
                unsafe_allow_html=True
            )

            st.write(
                "Điều quan trọng không chỉ là điểm số, "
                "mà là những kiến thức bạn có thể mang vào đời sống."
            )

            if st.button("Làm lại thử thách"):

                st.session_state.quiz_index = 0
                st.session_state.quiz_score = 0
                st.session_state.quiz_answered = []

                st.rerun()

            if st.button("Ghi nhận hoàn thành", type="primary"):

                mark_complete("quiz")
                st.success("Đã ghi nhận hoạt động.")

    # ----- THẺ SUY NGẪM -----

    with tab_cards:

        if st.button(
            "Rút một thẻ suy ngẫm",
            type="primary"
        ):

            available = [
                x for x in CARD_PROMPTS
                if x not in st.session_state.drawn_cards
            ]

            if not available:
                st.session_state.drawn_cards = []
                available = CARD_PROMPTS[:]

            picked = random.choice(available)

            st.session_state.drawn_cards.append(picked)
            st.session_state.current_card = picked

        if st.session_state.current_card:

            st.markdown(
                f'<div class="hero">'
                f'<div class="hero-kicker">A MOMENT TO REFLECT</div>'
                f'<h2 style="color:white">{st.session_state.current_card}</h2>'
                f'<p>Hãy dành một chút thời gian nghĩ về cách bạn '
                f'có thể áp dụng thông điệp này trong đời sống.</p>'
                f'</div>',
                unsafe_allow_html=True
            )

# ============================================================
# 12. HÀNH TRÌNH THẤU CẢM
# ============================================================

elif page == "Hành trình thấu cảm":

    section_header(
        "06 / EMPATHY JOURNEY",
        "Hành trình thấu cảm",
        "Một khoảng dừng để nhìn lại điều bạn đã học và chọn một hành động nhỏ."
    )

    st.markdown(
        '<div class="quote">Thấu cảm không chỉ là hiểu người khác đang trải qua '
        'điều gì. Thấu cảm còn là điều chỉnh cách ta hiện diện bên cạnh họ.</div>',
        unsafe_allow_html=True
    )

    st.subheader("Viết một lời nhắn cho chính mình")

    prompt = st.selectbox(
        "Gợi ý suy ngẫm",
        REFLECTION_PROMPTS
    )

    reflection = st.text_area(
        "Suy nghĩ của bạn",
        value=st.session_state.reflection_text,
        height=150,
        placeholder="Viết vài dòng theo cách của bạn…"
    )

    st.session_state.reflection_text = reflection

    if st.button(
        "Lưu vào nhật ký hành trình",
        type="primary"
    ):

        if reflection.strip():

            st.session_state.journal.append({
                "prompt": prompt,
                "text": reflection.strip()
            })

            mark_complete("reflection")

            st.success(
                "Đã lưu suy ngẫm trong phiên sử dụng hiện tại."
            )

        else:
            st.warning("Hãy viết một vài dòng trước khi lưu.")

    if st.session_state.journal:

        st.divider()
        st.subheader("Nhật ký của bạn")

        for i, entry in enumerate(
            reversed(st.session_state.journal),
            1
        ):

            with st.expander(
                f"Suy ngẫm {i}: {entry['prompt']}"
            ):
                st.write(entry["text"])

    st.caption(
        "Nhật ký hiện được lưu trong phiên sử dụng hiện tại; "
        "nội dung có thể mất khi phiên kết thúc."
    )

# ============================================================
# 13. KHÔNG GIAN SẺ CHIA
# ============================================================

elif page == "Không gian sẻ chia":

    section_header(
        "07 / COMMUNITY",
        "Không gian sẻ chia",
        "Một góc nhỏ để gửi đi thông điệp tích cực và lời động viên."
    )

    st.info(
        "Bản hiện tại lưu bài viết trong phiên Streamlit đang hoạt động. "
        "Để nhiều người dùng nhìn thấy bài đăng chung, cần tích hợp "
        "cơ sở dữ liệu hoặc dịch vụ backend."
    )

    with st.form("share_form", clear_on_submit=True):

        nickname = st.text_input(
            "Tên hiển thị (không bắt buộc)",
            placeholder="Ví dụ: Một người bạn"
        )

        message = st.text_area(
            "Thông điệp bạn muốn chia sẻ",
            placeholder="Một lời động viên, một điều bạn học được hoặc một hành động nhỏ…",
            height=120
        )

        submitted = st.form_submit_button(
            "Gửi thông điệp",
            type="primary"
        )

        if submitted:

            if len(message.strip()) < 5:

                st.warning("Thông điệp cần ít nhất 5 ký tự.")

            else:

                st.session_state.community.insert(
                    0,
                    {
                        "name": nickname.strip() or "Một người bạn",
                        "message": message.strip()
                    }
                )

                st.success(
                    "Thông điệp đã được thêm vào không gian sẻ chia của phiên này."
                )

    st.divider()

    st.subheader("Những lời nhắn được gửi đi")

    if not st.session_state.community:

        st.markdown(
            '<div class="panel"><h3>🌱 Hãy là người gửi lời nhắn đầu tiên</h3>'
            '<p class="muted">Một câu nói tử tế cũng có thể mở đầu cho sự kết nối.</p></div>',
            unsafe_allow_html=True
        )

    else:

        for post in st.session_state.community:

            safe_message = html.escape(post["message"])
            safe_name = html.escape(post["name"])

            st.markdown(
                f'<div class="panel">'
                f'<span class="tag">LỜI NHẮN TỪ CỘNG ĐỒNG</span>'
                f'<p>{safe_message}</p>'
                f'<b>— {safe_name}</b>'
                f'</div><div style="height:10px"></div>',
                unsafe_allow_html=True
            )

# ============================================================
# 14. NGUỒN THAM KHẢO
# ============================================================

elif page == "Nguồn tham khảo":

    section_header(
        "08 / REFERENCES",
        "Nguồn tham khảo",
        "Các nguồn dưới đây là điểm bắt đầu để tìm hiểu sâu hơn. "
        "Hãy ưu tiên hướng dẫn từ cơ quan y tế và tổ chức chuyên môn."
    )

    refs = [
        (
            "World Health Organization (WHO) – Dementia",
            "Thông tin tổng quan về sa sút trí tuệ, tác động và ứng phó y tế công cộng.",
            "https://www.who.int/news-room/fact-sheets/detail/dementia"
        ),
        (
            "Alzheimer's Association",
            "Tài liệu giáo dục về bệnh Alzheimer, dấu hiệu, chăm sóc và hỗ trợ gia đình.",
            "https://www.alz.org/"
        ),
        (
            "National Institute on Aging (NIA)",
            "Thông tin khoa học và hướng dẫn dành cho cộng đồng về Alzheimer và sức khỏe não bộ.",
            "https://www.nia.nih.gov/health/alzheimers"
        ),
        (
            "NHS – Dementia",
            "Thông tin sức khỏe cộng đồng về sa sút trí tuệ và các vấn đề liên quan.",
            "https://www.nhs.uk/conditions/dementia/"
        )
    ]

    for title, desc, url in refs:

        st.markdown(
            f'<div class="panel">'
            f'<h3>{html.escape(title)}</h3>'
            f'<p class="muted">{html.escape(desc)}</p>'
            f'<a href="{url}" target="_blank" rel="noopener noreferrer">{url}</a>'
            f'</div><div style="height:10px"></div>',
            unsafe_allow_html=True
        )

    st.warning(
        "Nội dung CHẠM Hub mang tính giáo dục, không thay thế tư vấn y tế. "
        "Khi có dấu hiệu đáng lo ngại, hãy tìm đến nhân viên y tế."
    )

# ============================================================
# 15. CHÂN TRANG
# ============================================================

render_footer()
