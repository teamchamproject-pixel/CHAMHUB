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
    },
    {
        "title": "Dinh dưỡng và lối sống hỗ trợ sức khỏe não bộ",
        "category": "Sức khỏe não bộ",
        "icon": "🥗",
        "summary": "Những thói quen lành mạnh có lợi cho sức khỏe tổng thể và có thể góp phần hỗ trợ sức khỏe nhận thức.",
        "body": [
            "Ưu tiên chế độ ăn đa dạng với rau, trái cây, ngũ cốc nguyên hạt, các loại đậu, hạt và nguồn đạm phù hợp; hạn chế muối, đồ uống nhiều đường và thực phẩm chế biến quá mức.",
            "Vận động thể chất phù hợp, ngủ đủ, duy trì kết nối xã hội, kiểm soát các yếu tố nguy cơ tim mạch và không hút thuốc có lợi cho sức khỏe tổng thể.",
            "Không có thực phẩm, chế độ ăn hay thực phẩm bổ sung nào được bảo đảm ngăn ngừa hoặc chữa khỏi Alzheimer. Người có bệnh nền hoặc chế độ ăn đặc biệt nên trao đổi với chuyên gia y tế/dinh dưỡng."
        ],
        "takeaway": "Hãy hướng đến thói quen bền vững và phù hợp cá nhân; không quảng bá một món ăn hay sản phẩm như phương pháp chữa bệnh."
    },
    {
        "title": "Chuẩn bị pháp lý và tài chính khi gia đình chăm sóc",
        "category": "Gia đình và quyền lợi",
        "icon": "📑",
        "summary": "Trao đổi sớm về mong muốn, giấy tờ, phân công chăm sóc và chi phí giúp gia đình chủ động hơn.",
        "body": [
            "Khi người thân còn có thể tham gia quyết định, gia đình nên trò chuyện tôn trọng về mong muốn chăm sóc, người liên hệ đáng tin cậy và cách lưu giữ giấy tờ quan trọng.",
            "Lập bảng chi phí thường xuyên, thuốc/khám theo hướng dẫn, đi lại, hỗ trợ sinh hoạt và khoản dự phòng; thống nhất cách chia sẻ trách nhiệm giữa các thành viên.",
            "Quy định pháp luật về đại diện, tài sản, trợ cấp và quyền của người bệnh phụ thuộc từng quốc gia và tình huống. Với quyết định pháp lý cụ thể, hãy hỏi cơ quan có thẩm quyền hoặc luật sư; không dùng bài viết này thay tư vấn pháp lý."
        ],
        "takeaway": "Tôn trọng ý chí và quyền lợi của người bệnh; chuẩn bị giấy tờ và tài chính minh bạch, có tư vấn phù hợp."
    },
    {
        "title": "Công nghệ hỗ trợ và phòng tránh đi lạc",
        "category": "Công nghệ hỗ trợ",
        "icon": "📍",
        "summary": "Thiết bị định vị, nhắc lịch và điều chỉnh môi trường có thể hỗ trợ an toàn khi được sử dụng có đồng thuận và kế hoạch.",
        "body": [
            "Một số gia đình cân nhắc thiết bị định vị GPS, điện thoại có chia sẻ vị trí, nút liên hệ khẩn cấp, nhắc lịch hoặc cảm biến cửa. Hiệu quả phụ thuộc vào thiết bị, kết nối, pin và khả năng người dùng mang theo.",
            "Nên lập kế hoạch phòng tránh đi lạc: ảnh gần đây, thông tin liên hệ, địa điểm thường đến, người cần gọi và cách phối hợp khi không tìm thấy người thân.",
            "Cần tôn trọng quyền riêng tư, trao đổi với người bệnh trong khả năng có thể, bảo vệ dữ liệu vị trí và không phụ thuộc hoàn toàn vào công nghệ. Thiết bị không thay thế giám sát và đánh giá nguy cơ phù hợp."
        ],
        "takeaway": "Công nghệ là công cụ hỗ trợ, không phải bảo đảm an toàn tuyệt đối; hãy kết hợp với môi trường thân thiện và kế hoạch gia đình."
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
    "community_filter": "Tất cả chủ đề",
    "completed": [],
    "quiz_index": 0,
    "quiz_score": 0,
    "quiz_answered": [],
    "care_answers": {},
    "drawn_cards": [],
    "current_card": None,
    "reflection_text": "",
    "knowledge_saved": [],
    "knowledge_read": [],
    "brain_quiz_answer": {},
    "brain_quiz_submitted": False,
    "care_revealed": [],
    "care_notes": "",
    "brain_deep_submitted": False,
    "brain_deep_score": 0,
    "memory_game_score": 0,
    "memory_game_done": False,
    "navigation_score": 0,
    "micro_actions_done": [],
    "care_branch_history": []
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

/* Tabs: màu chữ/nền tương phản ở cả chế độ sáng và tối */
.stTabs [data-baseweb="tab-list"] {
    gap:8px;
    flex-wrap:nowrap;
    overflow-x:auto;
    scrollbar-width:thin;
}

.stTabs [data-baseweb="tab"] {
    background:#e7f2eb !important;
    color:#244b40 !important;
    border:1px solid #cbd8cf !important;
    border-radius:10px 10px 0 0;
    padding:10px 16px;
    min-height:44px;
    white-space:nowrap;
}

.stTabs [data-baseweb="tab"] p,
.stTabs [data-baseweb="tab"] div,
.stTabs [data-baseweb="tab"] span {
    color:#244b40 !important;
    -webkit-text-fill-color:#244b40 !important;
    opacity:1 !important;
}

.stTabs [data-baseweb="tab"][aria-selected="true"] {
    background:#0d6255 !important;
    color:#ffffff !important;
    border-color:#0d6255 !important;
}

.stTabs [data-baseweb="tab"][aria-selected="true"] p,
.stTabs [data-baseweb="tab"][aria-selected="true"] div,
.stTabs [data-baseweb="tab"][aria-selected="true"] span {
    color:#ffffff !important;
    -webkit-text-fill-color:#ffffff !important;
    opacity:1 !important;
}

.stTabs [data-baseweb="tab-panel"] {
    color:inherit !important;
}

/* Dark Mode: tab chưa chọn sáng chữ trên nền tối */
@media (prefers-color-scheme: dark) {
    .stTabs [data-baseweb="tab"] {
        background:#263b33 !important;
        color:#e4eee8 !important;
        border-color:#526c60 !important;
    }
    .stTabs [data-baseweb="tab"] p,
    .stTabs [data-baseweb="tab"] div,
    .stTabs [data-baseweb="tab"] span {
        color:#e4eee8 !important;
        -webkit-text-fill-color:#e4eee8 !important;
    }
    .stTabs [data-baseweb="tab"][aria-selected="true"] {
        background:#267763 !important;
        color:#ffffff !important;
        border-color:#267763 !important;
    }
    .stTabs [data-baseweb="tab"][aria-selected="true"] p,
    .stTabs [data-baseweb="tab"][aria-selected="true"] div,
    .stTabs [data-baseweb="tab"][aria-selected="true"] span {
        color:#ffffff !important;
        -webkit-text-fill-color:#ffffff !important;
    }
}

@media (max-width:640px) {
    .stTabs [data-baseweb="tab-list"] {gap:5px;}
    .stTabs [data-baseweb="tab"] {padding:9px 11px; font-size:.84rem;}
}

[data-testid="stSidebar"] {background:#e9f4ed;}

hr {border-color:#dcebe2;}

div[data-testid="stProgress"] > div > div {
    background:#0c7661;
}
/* Tăng tương phản chữ phụ và chữ trong các widget */
[data-testid="stCaptionContainer"] p, .stCaption, .stCaption p {
    color:#244b42 !important;
    -webkit-text-fill-color:#244b42 !important;
    opacity:1 !important;
}
[data-testid="stMarkdownContainer"] p,
[data-testid="stMarkdownContainer"] li,
[data-testid="stText"] {
    color:inherit;
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

    .welcome-shell,
    .welcome-shell * {
        color:#F7FBF9 !important;
        -webkit-text-fill-color:#F7FBF9 !important;
        opacity:1 !important;
    }
    .welcome-shell h1 { color:#FFFFFF !important; -webkit-text-fill-color:#FFFFFF !important; }
    .welcome-shell h3 { color:#FFE3A0 !important; -webkit-text-fill-color:#FFE3A0 !important; }
    .welcome-shell p {
        color:#EAF5F0 !important;
        -webkit-text-fill-color:#EAF5F0 !important;
        max-width:700px;
        margin:18px auto;
        line-height:1.9;
        font-size:1.04rem;
    }
    .welcome-shell b, .welcome-shell strong {
        color:#FFE3A0 !important;
        -webkit-text-fill-color:#FFE3A0 !important;
    }
    /* Chữ phụ trên màn hình chào: màu đậm, không dùng màu xám nhạt */
    [data-testid="stCaptionContainer"],
    [data-testid="stCaptionContainer"] p,
    .stCaption, .stCaption p {
        color:#31564D !important;
        -webkit-text-fill-color:#31564D !important;
        opacity:1 !important;
        font-weight:600 !important;
    }
    /* Chỉ phần nội dung trong thẻ xanh dùng chữ sáng */
    .welcome-shell { color:#FFFFFF !important; }
    .welcome-shell p { color:#F3FAF7 !important; }
    .welcome-shell h1 { color:#FFFFFF !important; }
    .welcome-shell h3 { color:#FFE3A0 !important; }
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
      style="background:#eaf4ef;color:#173e36;border:1px solid #b8d5c8;border-radius:12px;padding:13px 22px;font-weight:800;cursor:pointer">
      ■ DỪNG ĐỌC
      </button>
    </div>

    <div id="voice-status"
    style="text-align:center;color:#31564d;background:#f5faf7;font:600 13px Arial;margin-top:8px;padding:6px 10px;border-radius:8px">
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
        "Từ phân tử APP, amyloid-beta và tau đến tiến trình thay đổi âm thầm của não bộ."
    )
    st.markdown('<div class="quote"><b>Góc nhìn nhân văn:</b> Hiểu cơ chế bệnh giúp chúng ta giảm định kiến, không quy kết biểu hiện của người bệnh thành sự cố ý và biết khi nào cần tìm hỗ trợ chuyên môn.</div>', unsafe_allow_html=True)

    tabs = st.tabs(["🧬 APP → Amyloid-beta", "🧵 Protein Tau", "⏳ Timeline sinh học", "🪷 Các giai đoạn & hỗ trợ", "⚕️ Nhận diện & y tế"])

    with tabs[0]:
        st.subheader("APP có thể được xử lý theo những con đường khác nhau")
        st.write("APP (amyloid precursor protein) là protein xuyên màng. Cách các enzyme secretase cắt APP góp phần quyết định có tạo ra peptide amyloid-beta hay không.")
        c1, c2 = st.columns(2)
        with c1:
            st.markdown('<div class="panel"><div class="tag">CON ĐƯỜNG KHÔNG TẠO Aβ</div><h3>α-secretase → γ-secretase</h3><p>α-secretase cắt APP bên trong vùng Aβ, vì vậy chuỗi amyloid-beta nguyên vẹn không được tạo thành. Đây thường được gọi là con đường không sinh amyloid.</p></div>', unsafe_allow_html=True)
        with c2:
            st.markdown('<div class="panel"><div class="tag">CON ĐƯỜNG SINH Aβ</div><h3>β-secretase (BACE1) → γ-secretase</h3><p>β-secretase cắt APP tạo mảnh đầu C; γ-secretase tiếp tục cắt mảnh này và có thể giải phóng các peptide Aβ, trong đó có Aβ40 và Aβ42.</p></div>', unsafe_allow_html=True)
        st.markdown("#### Sơ đồ tương tác phân tử")
        st.markdown('''<div class="panel" style="text-align:center"><div style="background:#e8f4ee;padding:14px;border-radius:12px;color:#164c40;font-weight:800">APP – protein tiền chất amyloid</div><div style="font-size:24px;color:#b18a39">↓</div><div style="display:grid;grid-template-columns:1fr 1fr;gap:12px"><div style="background:#e9f4ff;padding:14px;border-radius:12px;color:#164c40"><b>α-secretase</b><br>cắt trong vùng Aβ<br><b>Không tạo Aβ nguyên vẹn</b></div><div style="background:#fff3df;padding:14px;border-radius:12px;color:#674b19"><b>β-secretase / BACE1</b><br>tạo mảnh C-terminal</div></div><div style="font-size:24px;color:#b18a39">↓ (nhánh β tiếp tục)</div><div style="background:#fff3df;padding:14px;border-radius:12px;color:#674b19"><b>γ-secretase</b><br>giải phóng peptide Aβ (ví dụ Aβ40, Aβ42)</div><div style="font-size:24px;color:#b18a39">↓</div><div style="background:#fbe9e8;padding:14px;border-radius:12px;color:#6d3330"><b>Aβ có thể kết tụ</b><br>oligomer → cấu trúc dạng sợi → mảng amyloid</div></div>''', unsafe_allow_html=True)
        st.info("Aβ42 có xu hướng kết tụ cao hơn Aβ40. Sự tích tụ amyloid là một phần của bệnh sinh; tổn thương thần kinh còn liên quan đến tau, viêm thần kinh, rối loạn synapse và nhiều yếu tố khác.")
        st.caption("Đọc thêm: NIA – What Happens to the Brain in Alzheimer's Disease: https://www.nia.nih.gov/health/alzheimers-causes-and-risk-factors/what-happens-brain-alzheimers-disease")

    with tabs[1]:
        st.subheader("Tau: từ protein ổn định vi ống đến đám rối sợi")
        st.write("Tau là protein gắn với vi ống, góp phần ổn định hệ thống vận chuyển bên trong tế bào thần kinh. Trong Alzheimer, tau có thể bị phosphoryl hóa quá mức, thay đổi khả năng gắn vi ống và có xu hướng kết tụ.")
        tau_steps = [
            ("01 · Tau bình thường", "Tau gắn với vi ống, hỗ trợ duy trì cấu trúc và vận chuyển vật chất dọc theo sợi trục."),
            ("02 · Biến đổi phosphoryl hóa", "Cân bằng giữa các quá trình phosphoryl hóa và khử phosphoryl hóa bị thay đổi; tau có thể trở nên phosphoryl hóa quá mức."),
            ("03 · Mất ổn định vi ống", "Tau giảm khả năng gắn vi ống; hệ thống vận chuyển nội bào bị ảnh hưởng."),
            ("04 · Kết tụ tau", "Tau bất thường có thể kết tụ thành sợi xoắn đôi và các đám rối sợi thần kinh bên trong tế bào.")]
        for title, desc in tau_steps:
            with st.expander(title): st.write(desc)
        st.warning("Không nên hiểu tau là nguyên nhân duy nhất hoặc mọi trường hợp đều diễn tiến theo một đường thẳng đơn giản. Amyloid, tau và các quá trình sinh học khác có tương tác phức tạp.")

    with tabs[2]:
        st.subheader("Timeline: thay đổi sinh học có thể xuất hiện trước triệu chứng")
        st.write("Ở một số người, các thay đổi sinh học liên quan Alzheimer có thể bắt đầu từ nhiều năm, thậm chí khoảng 15–20 năm trước khi triệu chứng rõ rệt. Đây là mô hình khái quát, không phải đồng hồ dự báo cho từng cá nhân.")
        timeline = [
            ("Giai đoạn tiền lâm sàng", "Có thể đã xuất hiện thay đổi amyloid và các dấu ấn sinh học; người đó chưa biểu hiện suy giảm nhận thức rõ rệt."),
            ("Giai đoạn thay đổi nhận thức rất nhẹ", "Một số người có thể nhận thấy thay đổi tinh tế ở trí nhớ hoặc tư duy; chưa chắc đã ảnh hưởng đáng kể đến sinh hoạt."),
            ("Suy giảm nhận thức nhẹ (MCI)", "Khó khăn nhận thức rõ hơn so với trước; mức độ ảnh hưởng sinh hoạt khác nhau và không phải ai cũng tiến triển thành Alzheimer."),
            ("Sa sút trí tuệ do Alzheimer", "Khó khăn nhận thức ảnh hưởng đến khả năng tự thực hiện các hoạt động thường ngày; nhu cầu hỗ trợ tăng dần.")]
        for i,(title,desc) in enumerate(timeline):
            st.markdown(f'<div class="panel"><div class="tag">MỐC {i+1}</div><h3>{title}</h3><p>{desc}</p></div>',unsafe_allow_html=True)
        st.caption("Mốc 15–20 năm là ước lượng được mô tả trong một số nghiên cứu về tiến trình sinh học; thời điểm và tốc độ thay đổi rất khác nhau giữa các cá nhân. Tham khảo: NIA – Alzheimer's Disease Fact Sheet: https://www.nia.nih.gov/health/alzheimers-and-dementia/alzheimers-disease-fact-sheet")

    with tabs[3]:
        st.subheader("Thẻ khám phá giai đoạn – bấm để lật nội dung")
        stages = {
            "Sớm / nhẹ": ("Biểu hiện có thể gặp", "Quên thông tin mới, khó tìm từ, khó sắp xếp công việc phức tạp; vẫn có thể tự chủ trong nhiều hoạt động.", "Nhu cầu hỗ trợ", "Tôn trọng quyền tự quyết; hỗ trợ lịch hẹn, ghi chú, nhãn đồ vật và khám y tế khi có thay đổi đáng lo."),
            "Trung bình": ("Biểu hiện có thể gặp", "Lặp lại câu hỏi, nhầm lẫn thời gian/địa điểm, khó thực hiện một số sinh hoạt và có thể thay đổi cảm xúc.", "Nhu cầu hỗ trợ", "Duy trì nếp quen thuộc, hướng dẫn từng bước, giảm tiếng ồn và tăng giám sát an toàn phù hợp."),
            "Tiến triển / nặng": ("Biểu hiện có thể gặp", "Khả năng giao tiếp và tự chăm sóc có thể suy giảm đáng kể; cần hỗ trợ nhiều trong sinh hoạt.", "Nhu cầu hỗ trợ", "Chú trọng thoải mái, vệ sinh, dinh dưỡng, phòng ngừa nguy cơ và phối hợp nhân viên y tế/gia đình.")}
        chosen_stage = st.radio("Chọn một giai đoạn", list(stages), horizontal=True, key="mod1_flip_stage")
        a,b = st.columns(2)
        with a:
            st.markdown(f'<div class="panel"><div class="tag">MẶT TRƯỚC · {chosen_stage}</div><h3>{stages[chosen_stage][0]}</h3><p>{stages[chosen_stage][1]}</p></div>',unsafe_allow_html=True)
        with b:
            st.markdown(f'<div class="panel"><div class="tag">MẶT SAU · ĐỒNG HÀNH</div><h3>{stages[chosen_stage][2]}</h3><p>{stages[chosen_stage][3]}</p></div>',unsafe_allow_html=True)

    with tabs[4]:
        st.subheader("Nhận diện thay đổi – không tự chẩn đoán")
        st.write("Không phải mọi lần quên đều là Alzheimer. Nếu trí nhớ, ngôn ngữ, định hướng hoặc khả năng sinh hoạt thay đổi dai dẳng và ảnh hưởng cuộc sống, gia đình nên trao đổi với nhân viên y tế. Đánh giá có thể cần khai thác bệnh sử, kiểm tra nhận thức, khám lâm sàng và xét nghiệm/chẩn đoán hình ảnh khi phù hợp.")
        st.warning("Nếu lú lẫn xuất hiện đột ngột, đặc biệt kèm yếu liệt, méo miệng, nói khó, sốt, đau dữ dội hoặc thay đổi ý thức, cần tìm trợ giúp y tế khẩn cấp; không mặc định đó là Alzheimer.")

    if st.button("✓ Hoàn thành Module 1", type="primary", key="complete_mod1_deep"):
        mark_complete("basics")
        st.success("Đã ghi nhận tiến trình học Module 1.")

# ============================================================
# 8. NÃO BỘ & TRÍ NHỚ
# ============================================================

elif page == "Não bộ & trí nhớ":

    section_header("02 / THE BRAIN", "Cấu trúc não bộ & Mạng lưới ký ức", "Tìm hiểu các vùng não, hệ thống ký ức và cách tín hiệu thần kinh được truyền qua synapse.")
    st.markdown('<div class="quote"><b>Nguyên tắc quan trọng:</b> Không có một vùng não đơn lẻ “chứa” toàn bộ ký ức. Trí nhớ hình thành từ hoạt động của các mạng lưới phân bố và phối hợp với nhau.</div>', unsafe_allow_html=True)

    tabs = st.tabs(["🧠 Bản đồ vùng não", "🔗 Mạng lưới synapse", "📚 Hai hệ thống trí nhớ", "🧩 Alzheimer tác động", "🎯 Tự kiểm tra"])
    with tabs[0]:
        st.subheader("Các vùng thường được nhắc đến trong học tập về Alzheimer")
        regions = [
            ("Hồi hải mã", "Quan trọng đối với việc hình thành và củng cố ký ức mới, đặc biệt là ký ức sự kiện."),
            ("Thùy thái dương", "Tham gia xử lý âm thanh, ngôn ngữ và kiến thức ngữ nghĩa; vùng thái dương trong có liên hệ chặt với trí nhớ."),
            ("Thùy đỉnh", "Tham gia chú ý, tích hợp cảm giác, định hướng không gian và một số hoạt động nhận thức."),
            ("Vỏ não trước trán", "Tham gia lập kế hoạch, trí nhớ làm việc, kiểm soát hành vi và ra quyết định.")]
        st.caption("Sơ đồ dưới đây là tuyến giải thích khái quát, không phải thứ tự tổn thương cố định ở mọi người.")
        for i,(name,desc) in enumerate(regions):
            st.markdown(f'<div class="panel"><div class="tag">VÙNG {i+1}</div><h3>{name}</h3><p>{desc}</p></div>',unsafe_allow_html=True)
            if i < len(regions)-1: st.markdown('<div style="text-align:center;color:#b18a39;font-size:24px">↓</div>',unsafe_allow_html=True)
        st.info("Trên thực tế, mức độ và thứ tự ảnh hưởng khác nhau giữa các cá nhân. Alzheimer thường ảnh hưởng sớm đến mạng lưới liên quan trí nhớ, nhưng không thể dùng một sơ đồ tuyến tính để dự đoán từng người.")

    with tabs[1]:
        st.subheader("Synapse – điểm kết nối giữa các tế bào thần kinh")
        st.write("Tín hiệu có thể truyền từ tế bào thần kinh này sang tế bào khác qua synapse. Chất dẫn truyền thần kinh được giải phóng, gắn vào thụ thể và tạo thay đổi ở tế bào nhận.")
        st.markdown('''<div class="panel" style="text-align:center"><div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:10px;align-items:center"><div style="background:#e2f3eb;padding:18px;border-radius:14px;color:#164c40"><b>Tế bào A</b><br>Phát tín hiệu</div><div style="color:#b18a39;font-size:28px">→</div><div style="background:#e2f3eb;padding:18px;border-radius:14px;color:#164c40"><b>Tế bào B</b><br>Nhận tín hiệu</div></div><div style="margin:14px auto;background:#fff3df;color:#694d1c;padding:12px;border-radius:12px;max-width:520px"><b>Khe synapse</b><br>Chất dẫn truyền – thụ thể – điều chỉnh cường độ tín hiệu</div><small style="color:#526c64">Mô hình minh họa đơn giản, không theo tỷ lệ giải phẫu.</small></div>''',unsafe_allow_html=True)
        st.subheader("Mạng lưới khi kết nối bị suy yếu")
        grid = st.columns(5)
        for i,col in enumerate(grid):
            with col:
                st.markdown(f'<div style="text-align:center;background:{"#fbe8e5" if i in (1,3) else "#e5f2ec"};padding:15px 4px;border-radius:12px;color:#24483f;font-weight:800">●<br>Neuron {i+1}</div>',unsafe_allow_html=True)
        st.markdown('<div class="quote">Amyloid-beta, tau bất thường, viêm thần kinh và các quá trình bệnh sinh khác có thể góp phần làm rối loạn chức năng synapse và mạng lưới thần kinh. Hình minh họa chỉ diễn giải ý tưởng, không mô phỏng dữ liệu sinh học thực nghiệm.</div>',unsafe_allow_html=True)

    with tabs[2]:
        st.subheader("Trí nhớ tường thuật và trí nhớ thủ tục")
        c1,c2=st.columns(2)
        with c1:
            st.markdown('<div class="panel"><div class="tag">TRÍ NHỚ TƯỜNG THUẬT</div><h3>Biết và kể lại điều đã xảy ra</h3><p>Gồm trí nhớ sự kiện cá nhân (ví dụ một buổi sinh nhật) và trí nhớ ngữ nghĩa (khái niệm, sự kiện, tên gọi). Việc hình thành và gợi lại thường cần phối hợp hồi hải mã cùng nhiều vùng vỏ não.</p></div>',unsafe_allow_html=True)
        with c2:
            st.markdown('<div class="panel"><div class="tag">TRÍ NHỚ THỦ TỤC</div><h3>Biết cách thực hiện một kỹ năng</h3><p>Liên quan kỹ năng và thói quen đã luyện tập, như đạp xe, thao tác quen thuộc hoặc chơi một đoạn nhạc. Hệ thống này có sự tham gia của hạch nền, tiểu não và mạng lưới vận động.</p></div>',unsafe_allow_html=True)
        st.info("Vì các hệ thống trí nhớ có cơ sở thần kinh khác nhau, một số kỹ năng hoặc phản ứng quen thuộc có thể còn được duy trì khi khả năng nhớ sự kiện/tên gọi đã suy giảm. Tuy nhiên, điều này không đúng với mọi người và không có nghĩa người bệnh chắc chắn vẫn chơi nhạc cụ thành thạo.")
        st.caption("Tham khảo nền tảng: Squire, L.R. (2004), Memory systems of the brain: a brief history and current perspective, Neurobiology of Learning and Memory.")
        example = st.selectbox("Thử phân loại ví dụ", ["Nhớ tên trường đã học", "Thực hiện động tác đạp xe đã luyện tập", "Kể lại chuyến du lịch năm ngoái", "Nhớ nghĩa của từ ‘synapse’"], key="memory_kind_example")
        if st.button("Phân loại ví dụ", key="memory_kind_check"):
            procedural = "đạp xe" in example
            st.success("Ví dụ gần với trí nhớ thủ tục." if procedural else "Ví dụ gần với trí nhớ tường thuật (sự kiện hoặc ngữ nghĩa).")

    with tabs[3]:
        st.subheader("Những thay đổi có thể gặp")
        stage = st.select_slider("Chọn mức độ ảnh hưởng khái quát", ["Sớm", "Trung bình", "Tiến triển"], key="brain_stage_slider")
        descriptions = {
            "Sớm":"Khó hình thành ký ức mới, quên cuộc trò chuyện gần đây hoặc khó tìm từ; nhiều hoạt động độc lập vẫn có thể duy trì.",
            "Trung bình":"Khó khăn có thể lan sang ngôn ngữ, định hướng, lập kế hoạch và sinh hoạt; cần hướng dẫn từng bước và hỗ trợ an toàn.",
            "Tiến triển":"Nhiều chức năng nhận thức và tự chăm sóc có thể suy giảm đáng kể; ưu tiên thoải mái, giao tiếp phù hợp và hỗ trợ liên tục."}
        st.info(descriptions[stage])
        st.warning("Các giai đoạn không phải khuôn mẫu cứng. Chỉ nhân viên y tế mới có thể đánh giá tình trạng cụ thể.")

    with tabs[4]:
        questions = [
            ("Vùng nào đặc biệt quan trọng với việc hình thành ký ức mới?", ["Hồi hải mã", "Da", "Phổi"], 0, "Hồi hải mã có vai trò quan trọng trong hình thành và củng cố ký ức mới."),
            ("Trí nhớ tường thuật thường liên quan đến điều gì?", ["Sự kiện và kiến thức có thể kể lại", "Chỉ kỹ năng vận động", "Chỉ phản xạ"], 0, "Trí nhớ tường thuật gồm trí nhớ sự kiện và trí nhớ ngữ nghĩa."),
            ("Đạp xe sau khi đã luyện tập lâu năm gần với dạng nào?", ["Trí nhớ thủ tục", "Trí nhớ ngữ nghĩa", "Trí nhớ làm việc"], 0, "Kỹ năng vận động đã luyện tập là ví dụ điển hình của trí nhớ thủ tục.")]
        for i,(q,opts,ans,why) in enumerate(questions):
            st.radio(f"{i+1}. {q}",opts,key=f"brain_deep_q_{i}",index=None)
        if st.button("Chấm điểm",key="brain_deep_submit",type="primary"):
            score=sum(st.session_state.get(f"brain_deep_q_{i}")==opts[ans] for i,(_,opts,ans,_) in enumerate(questions))
            st.session_state.brain_deep_score=score
            st.session_state.brain_deep_submitted=True
        if st.session_state.get("brain_deep_submitted"):
            st.success(f"Kết quả: {st.session_state.get('brain_deep_score',0)}/{len(questions)} câu đúng.")
            for i,(_,opts,ans,why) in enumerate(questions): st.caption(f"Câu {i+1}: {why}")
            if st.button("Làm lại",key="brain_deep_reset"):
                for i in range(len(questions)): st.session_state.pop(f"brain_deep_q_{i}",None)
                st.session_state.brain_deep_submitted=False
                st.rerun()

    if st.button("✓ Hoàn thành Module 2",type="primary",key="complete_brain_deep"):
        mark_complete("brain")
        st.success("Đã ghi nhận tiến trình học Module 2.")

# ============================================================
# 9. THƯ VIỆN TRI THỨC
# ============================================================

elif page == "Thư viện tri thức":

    section_header("03 / KNOWLEDGE LIBRARY", "Thư viện tri thức", "Đọc – nghe – tải xuống – lưu lại. Mỗi chuyên đề có thời gian đọc ước tính và tiến độ học tập.")
    total=len(KNOWLEDGE)
    read_count=len(st.session_state.knowledge_read)
    saved_count=len(st.session_state.knowledge_saved)
    a,b,c=st.columns(3)
    a.metric("Chuyên đề",total); b.metric("Đã đọc",f"{read_count}/{total}"); c.metric("Đã lưu",saved_count)
    st.progress(min(read_count/total,1) if total else 0)

    search_col,category_col=st.columns([2,1])
    with search_col:
        search=st.text_input("🔎 Tìm kiếm tri thức",placeholder="Ví dụ: APP, tau, dinh dưỡng, định vị…",key="knowledge_search")
    with category_col:
        categories=["Tất cả"]+sorted({x["category"] for x in KNOWLEDGE})
        selected_category=st.selectbox("Lọc chuyên đề",categories,key="knowledge_category")
    view_mode=st.radio("Bộ sưu tập",["Tất cả", "Đã lưu", "Đã đọc"],horizontal=True,key="knowledge_view")

    filtered=[]
    for idx,item in enumerate(KNOWLEDGE):
        searchable=" ".join([item["title"],item["summary"],item["category"]," ".join(item["body"]),item["takeaway"]]).casefold()
        if selected_category!="Tất cả" and item["category"]!=selected_category: continue
        if search and search.casefold() not in searchable: continue
        if view_mode=="Đã lưu" and idx not in st.session_state.knowledge_saved: continue
        if view_mode=="Đã đọc" and idx not in st.session_state.knowledge_read: continue
        filtered.append((idx,item))
    st.markdown(f"**{len(filtered)} chuyên đề phù hợp**")
    if not filtered: st.info("Không tìm thấy bài phù hợp. Thử từ khóa hoặc danh mục khác.")

    for idx,item in filtered:
        words=sum(len(part.split()) for part in item["body"])+len(item["summary"].split())
        minutes=max(1,(words+179)//180)
        read=idx in st.session_state.knowledge_read
        with st.container(border=True):
            left,right=st.columns([5,1])
            with left:
                st.markdown(f"### {item['icon']} {item['title']}")
                st.caption(f"{item['category']} · {minutes} phút đọc · {len(item['body'])} phần")
                st.write(item["summary"])
                st.progress(1.0 if read else 0.0)
                st.caption("Đã hoàn thành" if read else "Chưa đánh dấu hoàn thành")
            with right:
                saved=idx in st.session_state.knowledge_saved
                if st.button("★ Đã lưu" if saved else "☆ Lưu bài",key=f"save_knowledge_v3_{idx}",use_container_width=True):
                    if saved: st.session_state.knowledge_saved.remove(idx)
                    else: st.session_state.knowledge_saved.append(idx)
                    st.rerun()
            with st.expander("Mở chuyên đề"):
                for paragraph in item["body"]: st.write(paragraph)
                st.markdown(f'<div class="quote"><b>Điều cần nhớ:</b> {html.escape(item["takeaway"])}</div>',unsafe_allow_html=True)
                d1,d2=st.columns(2)
                with d1:
                    speech=html.escape(item["title"]+". "+item["summary"]+". "+". ".join(item["body"])+". Điều cần nhớ: "+item["takeaway"])
                    components.html(f'''<button onclick="(function(){{if(!('speechSynthesis' in window)){{alert('Trình duyệt chưa hỗ trợ đọc văn bản.');return;}}speechSynthesis.cancel();var u=new SpeechSynthesisUtterance('{speech}');u.lang='vi-VN';u.rate=0.92;speechSynthesis.speak(u);}})()" style="width:100%;padding:10px;border-radius:9px;border:1px solid #b8d5c8;background:#e8f4ed;color:#164c40;font-weight:700;cursor:pointer">🔊 Nghe bài viết</button>''',height=48)
                with d2:
                    if st.button("✓ Đánh dấu đã đọc" if not read else "Đã đọc",key=f"mark_knowledge_v3_{idx}",type="primary" if not read else "secondary",use_container_width=True):
                        if idx not in st.session_state.knowledge_read: st.session_state.knowledge_read.append(idx)
                        mark_complete(f"knowledge_{idx}")
                        st.success("Đã cập nhật tiến độ đọc.")

    with st.expander("📖 Bảng thuật ngữ nhanh"):
        glossary={
            "APP":"Protein tiền chất amyloid, có thể được cắt bởi các enzyme secretase.",
            "Amyloid-beta (Aβ)":"Peptide được tạo ra từ quá trình xử lý APP; có thể kết tụ thành các cấu trúc amyloid.",
            "BACE1 / β-secretase":"Enzyme tham gia bước cắt APP theo con đường sinh amyloid.",
            "Tau":"Protein liên quan vi ống; tau bất thường có thể kết tụ thành đám rối sợi thần kinh.",
            "Synapse":"Vị trí kết nối giúp tế bào thần kinh truyền tín hiệu.",
            "Trí nhớ thủ tục":"Hệ thống trí nhớ liên quan kỹ năng và thói quen đã luyện tập.",
            "GPS":"Hệ thống định vị có thể hỗ trợ chia sẻ vị trí khi được thiết lập phù hợp."
        }
        for term,definition in glossary.items(): st.markdown(f"**{term}** — {definition}")
    st.caption("Tiến độ và danh sách đã lưu được giữ trong phiên sử dụng hiện tại; chưa đồng bộ giữa các thiết bị hoặc người dùng.")

# ============================================================
# 10. CẨM NANG ĐỒNG HÀNH
# ============================================================

elif page == "Cẩm nang đồng hành":

    section_header(
        "04 / CARE GUIDE", "Cẩm nang đồng hành",
        "Luyện cách phản hồi trong những tình huống đời sống. Không có một công thức áp dụng cho tất cả; hãy ưu tiên an toàn, tôn trọng và nhu cầu của từng người."
    )

    st.markdown('<div class="quote">Mục tiêu không phải buộc người thân phải nhớ đúng. Mục tiêu là giữ an toàn, giảm căng thẳng và duy trì kết nối.</div>', unsafe_allow_html=True)

    st.subheader("🎭 Mô phỏng hội thoại nhiều bước")
    st.caption("Chọn phản hồi ở từng lượt, quan sát phản ứng có thể xảy ra rồi quyết định bước tiếp theo. Đây là tình huống học tập minh họa; phản ứng thực tế của mỗi người có thể khác nhau.")
    branch_cases = {
        "Từ chối tắm rửa": {
            "opening":"Người thân lùi lại và nói: ‘Tôi không muốn tắm. Đừng bắt tôi!’",
            "q1":"Bạn sẽ mở đầu thế nào?",
            "a1":["A. ‘Có gì đâu mà sợ, phải tắm ngay!’", "B. ‘Con thấy mẹ chưa thoải mái. Mẹ đang thấy lạnh hay lo điều gì ạ?’", "C. Im lặng kéo tay người thân vào phòng tắm."],
            "best1":1,
            "responses":[
                ("Người thân có thể cảm thấy bị thúc ép và phản ứng gay gắt hơn. Hãy dừng lại, tạo khoảng cách an toàn và giảm áp lực.", ["A. Tranh luận rằng việc tắm là bắt buộc.","B. Cho người thân thời gian, làm ấm phòng, chuẩn bị khăn và hỏi họ muốn rửa mặt/tay trước hay tắm sau.","C. Tiếp tục kéo người thân vào phòng tắm."], 1, "Đưa ra lựa chọn nhỏ, chuẩn bị môi trường ấm và an toàn, tôn trọng riêng tư. Có thể chia hoạt động vệ sinh thành nhiều bước."),
                ("Người thân nói: ‘Phòng tắm lạnh và trơn, tôi sợ ngã’. Bạn đã nhận diện được mối lo cụ thể.", ["A. Kiểm tra nhiệt độ, sàn, tay vịn; giải thích từng bước và hỏi sự đồng ý.","B. Nói rằng không có gì đáng sợ.","C. Bỏ qua nỗi lo và làm thật nhanh."], 0, "Giải quyết nguyên nhân thực tế, phòng ngừa té ngã và giữ quyền lựa chọn cho người thân."),
                ("Người thân dịu lại nhưng vẫn chưa muốn tắm toàn thân.", ["A. Ép hoàn tất ngay.","B. Chấp nhận làm vệ sinh từng phần phù hợp hôm nay và thử lại lúc khác.","C. Trách móc người thân."], 1, "Linh hoạt, bảo đảm vệ sinh cần thiết và tôn trọng phẩm giá. Nếu có vấn đề da, đau hoặc vệ sinh khó khăn kéo dài, hỏi nhân viên y tế.")
            ]
        },
        "Bồn chồn, đi lại vào buổi tối (Sundowning)": {
            "opening":"Cuối ngày, người thân liên tục đi qua lại, nói rằng phải đi đón con dù con đã trưởng thành.",
            "q1":"Bạn phản hồi ra sao?",
            "a1":["A. ‘Con đã lớn rồi, mẹ nhớ sai rồi!’", "B. ‘Mẹ đang lo cho con. Mình ngồi nghỉ một chút nhé, mẹ có muốn uống nước không?’", "C. Khóa cửa và yêu cầu người thân ngồi yên."],
            "best1":1,
            "responses":[
                ("Người thân có thể cảm thấy bị phủ nhận và lo lắng tăng lên.",["A. Tranh cãi về tuổi của người con.","B. Xác nhận cảm xúc, nói ngắn gọn, giảm tiếng ồn và kiểm tra nhu cầu cơ bản.","C. Bật TV thật lớn để đánh lạc hướng."],1,"Kiểm tra đói, khát, đau, mệt, buồn tiểu, ánh sáng và tiếng ồn; duy trì lịch sinh hoạt dễ đoán."),
                ("Người thân vẫn đi lại. Bạn nhận thấy phòng hơi tối, TV ồn và người thân chưa ăn nhẹ.",["A. Điều chỉnh ánh sáng, giảm tiếng ồn, đề nghị bữa nhẹ/nước nếu phù hợp và đi cùng trong không gian an toàn.","B. Quát yêu cầu dừng lại.","C. Để người thân tự đi ra ngoài."],0,"Giảm tác nhân gây kích thích, đồng hành khi di chuyển và bảo đảm cửa/lối ra an toàn mà không dùng biện pháp giam giữ nguy hiểm."),
                ("Tình trạng bồn chồn mới xuất hiện đột ngột, khác hẳn thường ngày.",["A. Mặc định đây là Alzheimer.","B. Ghi nhận thay đổi và liên hệ nhân viên y tế để đánh giá nguyên nhân như đau, nhiễm trùng hoặc tác dụng thuốc.","C. Tự ý cho dùng thuốc an thần."],1,"Thay đổi hành vi đột ngột cần được đánh giá y tế; không tự ý dùng hoặc đổi thuốc. Nếu có nguy cơ cấp cứu, tìm trợ giúp khẩn cấp.")
            ]
        },
        "Nghi ngờ người khác lấy/cất giấu đồ": {
            "opening":"Người thân nói: ‘Ai đó lấy ví của tôi rồi!’ và bắt đầu tức giận.",
            "q1":"Bạn nên nói gì trước?",
            "a1":["A. ‘Không ai lấy cả, mẹ lại tưởng tượng rồi!’", "B. ‘Con thấy mẹ đang rất lo. Mình cùng tìm chiếc ví nhé.’", "C. Buộc người thân nhận rằng họ đã để quên."],
            "best1":1,
            "responses":[
                ("Người thân có thể cảm thấy bị xem nhẹ hoặc bị buộc tội.",["A. Tranh luận để chứng minh họ sai.","B. Thừa nhận cảm xúc, cùng tìm ở những nơi quen thuộc và giữ giọng bình tĩnh.","C. Đe dọa sẽ không cho dùng ví nữa."],1,"Không đối đầu hay chế giễu; cùng tìm kiếm có hệ thống và trấn an cảm xúc."),
                ("Hai người chưa tìm thấy ví. Người thân càng sốt ruột.",["A. Chuyển hướng nhẹ nhàng sang việc bình tâm, sau đó kiểm tra lại các vị trí cố định.","B. Nói ‘mẹ lúc nào cũng làm mất đồ’.","C. Lục soát đồ đạc của người thân trước mặt mọi người."],0,"Tạo nơi cất đồ cố định, nhãn dễ nhận biết và bản sao/biện pháp bảo quản phù hợp; tránh làm người thân xấu hổ."),
                ("Tình huống lặp lại nhiều lần và gây xung đột trong gia đình.",["A. Ghi nhận thời điểm, món đồ và yếu tố kích hoạt; trao đổi với người chăm sóc và chuyên gia khi cần.","B. Mặc định người thân cố tình nói dối.","C. Tranh cãi mỗi lần xảy ra."],0,"Theo dõi mẫu hành vi, giảm thất lạc bằng thói quen sắp xếp; tìm tư vấn nếu nghi ngờ, sợ hãi hoặc kích động kéo dài.")
            ]
        }
    }
    selected_branch = st.selectbox("Chọn kịch bản", list(branch_cases.keys()), key="branch_case_v3")
    case = branch_cases[selected_branch]
    st.markdown(f'<div class="panel"><span class="tag">HỘI THOẠI · NGƯỜI THÂN</span><p><b>Người thân:</b> {html.escape(case["opening"])}</p></div>', unsafe_allow_html=True)
    first = st.radio(case["q1"], case["a1"], key=f"branch_first_{selected_branch}", index=None)
    if first is not None:
        first_index = case["a1"].index(first)
        if first_index == case["best1"]:
            st.success("Phản hồi mở đầu phù hợp: ưu tiên cảm xúc, bình tĩnh và tôn trọng.")
        else:
            st.warning("Lựa chọn này có thể làm căng thẳng tăng lên. Hãy cân nhắc cách phản hồi ít đối đầu hơn.")
        st.markdown('<div class="panel"><b>Người thân:</b> ' + html.escape(case["responses"][first_index][0] if first_index < len(case["responses"]) else case["responses"][0][0]) + '</div>', unsafe_allow_html=True)
        # Each opening choice leads to the corresponding next turn; the branches are illustrative.
        branch_response = case["responses"][first_index if first_index < len(case["responses"]) else 0]
        st.markdown("**Lượt tiếp theo – Người chăm sóc:** " + branch_response[0])
        second = st.radio("Bạn sẽ làm gì tiếp theo?", branch_response[1], key=f"branch_second_{selected_branch}_{first_index}", index=None)
        if second is not None:
            second_index = branch_response[1].index(second)
            st.markdown('<div class="panel"><b>Phản hồi có thể xảy ra:</b><p>' + html.escape(branch_response[0]) + '</p></div>', unsafe_allow_html=True)
            if second_index == branch_response[2]:
                st.success("Đây là hướng xử lý phù hợp hơn. " + branch_response[3])
            else:
                st.warning("Hãy thử đặt sự an toàn, cảm xúc và quyền lựa chọn của người thân lên trước. " + branch_response[3])
            third = st.radio("Bước tiếp theo bạn muốn chọn?", ["Tiếp tục theo hướng tôn trọng và an toàn", "Dừng lại, quan sát và thử lại sau", "Xin hỗ trợ từ thành viên gia đình/chuyên gia"], key=f"branch_third_{selected_branch}_{first_index}", index=None)
            if third:
                st.info("Gợi ý: " + branch_response[3])
                if st.button("Ghi nhận đã thực hành kịch bản", key=f"branch_done_{selected_branch}"):
                    st.session_state.care_branch_history.append(selected_branch)
                    st.success("Đã ghi nhận kịch bản trong phiên này.")

    st.divider()
    extra_scenarios = [
        {"title":"Người thân muốn về nhà dù đang ở nhà", "situation":"Người thân đứng dậy, lo lắng và nói: “Tôi phải về nhà thôi”.", "options":[("A","Tranh luận rằng đây chính là nhà của họ."),("B","Bình tĩnh hỏi điều gì đang khiến họ lo lắng, trấn an và thử chuyển sang hoạt động quen thuộc."),("C","Quát lớn để họ ngồi xuống.")], "best":"B", "explain":"Cảm giác muốn về nhà có thể gắn với lo lắng hoặc nhu cầu tìm sự an toàn. Hãy lắng nghe cảm xúc, trấn an và đánh giá xem có nguy cơ an toàn nào cần xử lý."},
        {"title":"Người thân từ chối tắm", "situation":"Đến giờ vệ sinh cá nhân, người thân tỏ ra khó chịu và không muốn vào phòng tắm.", "options":[("A","Ép buộc ngay lập tức."),("B","Bỏ mặc hoàn toàn dù vệ sinh đang ảnh hưởng sức khỏe."),("C","Tìm hiểu nguyên nhân, giải thích từng bước, giữ riêng tư và cho họ lựa chọn phù hợp.")], "best":"C", "explain":"Có thể người thân thấy lạnh, sợ trượt ngã, xấu hổ hoặc chưa hiểu việc sắp diễn ra. Tôn trọng riêng tư, chuẩn bị môi trường an toàn và chia nhỏ thao tác."},
        {"title":"Người thân đi lại bồn chồn vào buổi chiều", "situation":"Cuối ngày, người thân liên tục đi quanh nhà và khó ngồi yên.", "options":[("A","La mắng và yêu cầu ngồi im."),("B","Quan sát yếu tố gây khó chịu, kiểm tra nhu cầu cơ bản và tạo hoạt động nhẹ nhàng trong không gian an toàn."),("C","Khóa họ một mình trong phòng.")], "best":"B", "explain":"Hãy kiểm tra đói, khát, đau, mệt, nhu cầu đi vệ sinh, tiếng ồn hoặc thay đổi môi trường. Nếu hành vi mới xuất hiện đột ngột hoặc bất thường, cần trao đổi với nhân viên y tế."},
        {"title":"Người thân quên uống thuốc", "situation":"Bạn nhận ra người thân không chắc mình đã uống thuốc hay chưa.", "options":[("A","Cho uống bù ngay để chắc chắn."),("B","Tự ý thay đổi liều."),("C","Kiểm tra lịch/khay thuốc và liên hệ người phụ trách hoặc nhân viên y tế để được hướng dẫn; không tự cho uống thêm khi chưa rõ.")], "best":"C", "explain":"Dùng thuốc cần tuân theo hướng dẫn chuyên môn. Không tự ý tăng, giảm hoặc uống bù liều khi chưa xác minh; có thể dùng hộp chia thuốc và lịch nhắc do gia đình thống nhất."},
        {"title":"Nghi ngờ người khác lấy đồ", "situation":"Người thân khẳng định ai đó đã lấy chiếc ví dù ví có thể đã được cất ở nơi khác.", "options":[("A","Tranh cãi và nói họ tưởng tượng."),("B","Lắng nghe nỗi lo, cùng tìm ở vị trí quen thuộc và tránh buộc tội."),("C","Chế giễu để họ quên chuyện đó.")], "best":"B", "explain":"Xác nhận cảm xúc thay vì tranh luận đúng sai; thiết lập vị trí cất đồ cố định và ghi nhận nếu tình trạng lặp lại."}
    ]
    all_scenarios = CARE_SCENARIOS + extra_scenarios
    st.markdown("### Bộ tình huống thực hành")
    st.caption(f"{len(all_scenarios)} tình huống · Chọn cách phản hồi, xem phân tích và rút ra nguyên tắc.")
    score = 0
    answered = 0
    for i, scenario in enumerate(all_scenarios):
        with st.container(border=True):
            st.markdown(f"### Tình huống {i+1:02d} · {scenario['title']}")
            st.write(scenario["situation"])
            choice = st.radio("Bạn sẽ làm gì?", [f"{letter}. {text}" for letter, text in scenario["options"]], key=f"care_choice_v2_{i}", index=None, label_visibility="visible")
            if st.button("Phân tích lựa chọn", key=f"care_reveal_v2_{i}"):
                if choice:
                    st.session_state.care_revealed.append(i)
                else:
                    st.warning("Hãy chọn một phương án trước khi xem phân tích.")
            if i in st.session_state.care_revealed:
                selected = choice[0] if choice else None
                if selected:
                    answered += 1
                    if selected == scenario["best"]:
                        score += 1
                        st.success("Lựa chọn phù hợp. " + scenario["explain"])
                    else:
                        st.warning(f"Trong tình huống này, nên ưu tiên phương án {scenario['best']}. " + scenario["explain"])
                else:
                    st.info(scenario["explain"])

    st.divider()
    st.subheader("Bộ nguyên tắc đồng hành hằng ngày")
    tips = [
        "Tiếp cận từ phía trước, giới thiệu bản thân nếu cần và gọi tên người thân.",
        "Dùng câu ngắn, mỗi lần một hướng dẫn; dành đủ thời gian để họ phản hồi.",
        "Tránh tranh cãi, chất vấn hoặc làm người thân xấu hổ khi họ nhầm lẫn.",
        "Giữ lối đi thông thoáng, ánh sáng phù hợp và vật dụng quen thuộc ở vị trí ổn định.",
        "Khuyến khích người thân tự làm phần việc họ còn có thể làm; hỗ trợ khi cần.",
        "Chia sẻ trách nhiệm chăm sóc và dành thời gian nghỉ ngơi cho người chăm sóc."
    ]
    checked = []
    for i, tip in enumerate(tips):
        if st.checkbox(tip, key=f"care_checklist_{i}"):
            checked.append(i)
    st.progress(len(checked) / len(tips))
    st.caption(f"Bạn đã rà soát {len(checked)}/{len(tips)} nguyên tắc.")

    st.subheader("Soạn một kế hoạch hỗ trợ nhỏ")
    st.text_area("Một điều tôi muốn thử áp dụng trong tuần này", key="care_notes", placeholder="Ví dụ: nói chậm hơn, giảm tiếng ồn khi trò chuyện, cùng gia đình sắp xếp lối đi an toàn…")
    if st.button("Lưu kế hoạch trong phiên này", key="save_care_plan"):
        if st.session_state.care_notes.strip():
            st.success("Đã lưu nội dung trong phiên sử dụng hiện tại.")
        else:
            st.info("Bạn hãy viết một hành động nhỏ trước nhé.")

    if len(st.session_state.care_revealed) >= len(all_scenarios):
        if st.button("Hoàn thành cẩm nang đồng hành", type="primary", key="complete_care_v2"):
            mark_complete("care")
            st.success("Bạn đã hoàn thành bộ tình huống thực hành.")

    st.warning("Cẩm nang mang tính giáo dục, không thay thế hướng dẫn cá nhân từ bác sĩ hoặc chuyên gia chăm sóc. Khi có thay đổi sức khỏe/hành vi đột ngột, té ngã, đau hoặc nguy cơ mất an toàn, hãy tìm trợ giúp y tế phù hợp.")

# ============================================================
# 11. TRẠM TRẢI NGHIỆM
# ============================================================

elif page == "Trạm trải nghiệm":

    section_header(
        "05 / INTERACTIVE LAB",
        "Trạm trải nghiệm",
        "Học qua câu hỏi, lựa chọn và phản hồi tức thì."
    )

    tab_quiz, tab_cards, tab_memory, tab_board = st.tabs([
        "🧠 Thử thách kiến thức",
        "🃏 Thẻ suy ngẫm",
        "🧩 Phòng thí nghiệm trí nhớ",
        "🏆 Bảng thành tích"
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

    # ----- MINI GAME: GHÉP CẶP KÝ ỨC -----
    with tab_memory:
        st.markdown("### 🧩 Thử thách ghép cặp thông tin")
        st.write("Hãy ghép gợi ý với thông tin tương ứng. Đây là trò chơi học tập mô phỏng việc truy xuất thông tin, **không tái hiện cảm giác hay mức độ suy giảm trí nhớ của người mắc Alzheimer**.")
        pairs = [("Ảnh gia đình", "Kỷ niệm"), ("Chìa khóa", "Mở cửa"), ("Lịch treo tường", "Ngày tháng"), ("Bản đồ", "Định hướng")]
        labels = [p[0] for p in pairs]
        answers = [p[1] for p in pairs]
        left_col, right_col = st.columns(2)
        chosen_pairs=[]
        for j, label in enumerate(labels):
            with left_col:
                st.markdown(f"**{j+1}. {label}**")
            with right_col:
                chosen=st.selectbox(f"Ghép với", ["— Chọn —"]+answers, key=f"memory_pair_v3_{j}", label_visibility="collapsed")
                chosen_pairs.append(chosen)
        if st.button("Kiểm tra ghép cặp", key="memory_match_check_v3", type="primary"):
            if "— Chọn —" in chosen_pairs:
                st.warning("Hãy hoàn thành cả bốn cặp trước khi kiểm tra.")
            else:
                points=sum(chosen_pairs[j]==answers[j] for j in range(len(pairs)))
                st.session_state.memory_game_score=points
                st.session_state.memory_game_done=True
                if points==len(pairs):
                    st.balloons(); st.success(f"🎉 Hoàn hảo! {points}/4 cặp chính xác.")
                else:
                    st.info(f"Bạn ghép đúng {points}/4 cặp. Hãy xem lại và thử lần nữa.")
        if st.session_state.memory_game_done:
            st.metric("Kết quả gần nhất", f"{st.session_state.memory_game_score}/4")
            if st.button("Chơi lại trò ghép cặp", key="memory_match_reset_v3"):
                for j in range(4): st.session_state.pop(f"memory_pair_v3_{j}", None)
                st.session_state.memory_game_done=False
                st.rerun()

        st.divider()
        st.markdown("### 🧭 Thử thách định hướng")
        st.write("Bạn đang ở **Sảnh**. Hãy chọn đường đi để đến **Thư viện** theo sơ đồ đơn giản dưới đây.")
        st.markdown('<div class="panel" style="text-align:center"><b>🏠 Sảnh</b><br>↓<br><b>🪴 Vườn</b>　↔　🚪 Cổng<br>↓　　　　　↓<br><b>📚 Thư viện</b>　　🚌 Trạm xe</div>', unsafe_allow_html=True)
        route=st.radio("Lộ trình nào đến Thư viện?", ["Sảnh → Vườn → Thư viện", "Sảnh → Cổng → Trạm xe", "Sảnh → Trạm xe → Vườn"], key="navigation_route_v3", index=None)
        if st.button("Kiểm tra lộ trình", key="navigation_check_v3"):
            if route is None: st.warning("Hãy chọn một lộ trình.")
            elif route.startswith("Sảnh → Vườn"):
                st.session_state.navigation_score += 1
                st.balloons(); st.success("Đúng rồi! Bạn đã đến Thư viện.")
            else: st.warning("Lộ trình này chưa đến Thư viện. Hãy quan sát lại sơ đồ.")
        st.caption("Các thử thách không phải công cụ sàng lọc, chẩn đoán hoặc đo lường trí nhớ.")

    with tab_board:
        st.markdown("### 🏆 Thành tích trong phiên")
        achievements=[("Kiến thức",st.session_state.quiz_score,f"/{len(QUIZ)} câu đúng"),("Ghép cặp trí nhớ",st.session_state.memory_game_score,"/4 cặp"),("Định hướng",st.session_state.navigation_score," lượt tìm đúng đường"),("Kịch bản đồng hành",len(set(st.session_state.care_branch_history))," kịch bản đã thực hành")]
        for name,value,suffix in achievements:
            st.metric(name, f"{value}{suffix}")
        st.caption("Bảng thành tích chỉ lưu trong phiên trình duyệt hiện tại, không phải bảng xếp hạng công khai giữa các người dùng.")
        if st.session_state.quiz_index>=len(QUIZ) and st.session_state.quiz_score==len(QUIZ):
            st.success("🏅 Huy hiệu: Người khám phá tri thức")

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

    st.subheader("🌱 Sổ tay cam kết – Hành động nhỏ mỗi ngày")
    micro_actions = [
        "Hôm nay tôi sẽ lắng nghe trọn vẹn 5 phút mà không ngắt lời.",
        "Tôi sẽ nói chậm, dùng câu ngắn và cho người thân thêm thời gian phản hồi.",
        "Tôi sẽ hỏi người thân muốn lựa chọn nào thay vì ra lệnh.",
        "Tôi sẽ cùng gia đình kiểm tra một nguy cơ mất an toàn trong nhà.",
        "Tôi sẽ dành một khoảnh khắc cùng người thân nghe nhạc hoặc xem ảnh quen thuộc.",
        "Tôi sẽ chia sẻ một phần việc chăm sóc để người chăm sóc chính được nghỉ ngơi.",
        "Tôi sẽ tìm hiểu thêm một kiến thức đáng tin cậy về Alzheimer."
    ]
    st.caption("Chọn những việc nhỏ, cụ thể và có thể thực hiện. Bạn có thể thay đổi cam kết theo hoàn cảnh thực tế.")
    for i, action in enumerate(micro_actions):
        checked_action=st.checkbox(action, key=f"micro_action_{i}", value=i in st.session_state.micro_actions_done)
        if checked_action and i not in st.session_state.micro_actions_done:
            st.session_state.micro_actions_done.append(i)
        elif not checked_action and i in st.session_state.micro_actions_done:
            st.session_state.micro_actions_done.remove(i)
    st.progress(len(st.session_state.micro_actions_done)/len(micro_actions))
    st.caption(f"Đã chọn {len(st.session_state.micro_actions_done)}/{len(micro_actions)} cam kết.")

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

    if st.button("📄 Tạo bản tổng kết hành trình", key="create_empathy_summary_v3", type="primary"):
        selected_names=[micro_actions[i] for i in st.session_state.micro_actions_done if i < len(micro_actions)]
        journal_lines=[]
        for n,entry in enumerate(st.session_state.journal,1):
            journal_lines.append(f"{n}. {entry['prompt']}\n{entry['text']}")
        summary=("CHẠM HUB – TỔNG KẾT HÀNH TRÌNH THẤU CẢM\n"
                 "==========================================\n\n"
                 f"Cam kết đã chọn ({len(selected_names)}):\n"+
                 ("\n".join(f"- {x}" for x in selected_names) if selected_names else "- Chưa chọn cam kết nào.")+
                 "\n\nNHẬT KÝ SUY NGẪM\n"+
                 ("\n\n".join(journal_lines) if journal_lines else "Chưa có nội dung nhật ký.")+
                 "\n\nTiến trình học tập: "+", ".join(st.session_state.completed)+
                 "\n\nCHẠM – Thấu hiểu để kết nối, kết nối để sẻ chia.\n"
                 "Tài liệu cá nhân được tạo từ dữ liệu trong phiên hiện tại.")
        st.download_button("⬇ Tải bản tổng kết (.txt)", data=summary, file_name="CHAM_Hanh_trinh_thau_cam.txt", mime="text/plain", key="download_empathy_summary_v3")

    st.caption(
        "Nhật ký hiện được lưu trong phiên sử dụng hiện tại; "
        "nội dung có thể mất khi phiên kết thúc."
    )

# ============================================================
# 13. KHÔNG GIAN SẺ CHIA
# ============================================================

elif page == "Không gian sẻ chia":

    section_header(
        "07 / COMMUNITY WALL",
        "Không gian sẻ chia",
        "Mỗi lời nhắn là một điểm chạm tử tế. Hãy gửi đi sự động viên, sẻ chia và những hành động nhỏ."
    )

    st.markdown("""
    <div class="panel" style="background:linear-gradient(135deg,#fff8e8,#f0faf5);border:1px solid #ead9ad;">
      <div style="font-size:30px">💌 🌿 🤝</div>
      <h3 style="color:#14594d;margin-bottom:6px">Wall of Kindness – Bức tường tử tế</h3>
      <p style="color:#365b53;margin:0">Một lời động viên không cần dài. Một hành động nhỏ cũng có thể làm hành trình chăm sóc bớt đơn độc.</p>
    </div>
    """, unsafe_allow_html=True)

    topic_labels = ["#LờiĐộngViên", "#GócChiaSẻ", "#HànhĐộngNhỏ"]

    with st.form("share_form_v4", clear_on_submit=True):
        nickname = st.text_input(
            "Tên hiển thị (không bắt buộc)",
            placeholder="Ví dụ: Một người bạn"
        )
        topic = st.selectbox("Chọn chủ đề thông điệp", topic_labels, index=0)
        message = st.text_area(
            "Thông điệp bạn muốn gửi đến cộng đồng",
            placeholder="Hãy viết một lời động viên, một trải nghiệm hoặc một hành động tử tế…",
            height=120
        )
        submitted = st.form_submit_button("💌 Gửi lời nhắn", type="primary", use_container_width=True)
        if submitted:
            if len(message.strip()) < 5:
                st.warning("Thông điệp cần ít nhất 5 ký tự.")
            else:
                st.session_state.community.insert(0, {
                    "name": nickname.strip() or "Một người bạn",
                    "message": message.strip(),
                    "topic": topic
                })
                st.success("Lời nhắn đã được thêm vào bức tường tử tế trong phiên này.")

    st.divider()
    st.subheader("🌼 Bảng tin cộng đồng")
    filter_options = ["Tất cả chủ đề"] + topic_labels
    selected_filter = st.selectbox(
        "Lọc lời nhắn theo chủ đề",
        filter_options,
        key="community_filter_v4"
    )
    visible_posts = [
        post for post in st.session_state.community
        if selected_filter == "Tất cả chủ đề" or post.get("topic", "#LờiĐộngViên") == selected_filter
    ]

    count_a, count_b = st.columns(2)
    count_a.metric("Lời nhắn trong phiên", len(st.session_state.community))
    count_b.metric("Đang hiển thị", len(visible_posts))

    if not visible_posts:
        st.markdown(
            '<div class="panel" style="text-align:center;background:#f3faf6;">'
            '<div style="font-size:34px">🌱</div>'
            '<h3 style="color:#14594d">Hãy là người gửi lời nhắn đầu tiên</h3>'
            '<p style="color:#55746c">Một câu nói tử tế cũng có thể mở đầu cho sự kết nối.</p>'
            '</div>',
            unsafe_allow_html=True
        )
    else:
        for post_index, post in enumerate(visible_posts):
            safe_message = html.escape(post.get("message", ""))
            safe_name = html.escape(post.get("name", "Một người bạn"))
            safe_topic = html.escape(post.get("topic", "#LờiĐộngViên"))
            palette = ["#fff8e8", "#eff8f3", "#f4f1fb", "#fff1ed"]
            card_bg = palette[post_index % len(palette)]
            st.markdown(
                f'<div style="background:{card_bg};border:1px solid #e8e2d2;'
                f'border-radius:18px;padding:20px 22px;margin:10px 0;'
                f'box-shadow:0 5px 18px rgba(24,70,58,.06);">'
                f'<div style="display:flex;justify-content:space-between;gap:10px;flex-wrap:wrap;">'
                f'<span style="background:#e3efe8;color:#14594d;border-radius:30px;padding:5px 12px;font-size:12px;font-weight:700;">{safe_topic}</span>'
                f'<span style="color:#9a8051;font-size:20px">✦</span></div>'
                f'<p style="font-size:17px;line-height:1.7;color:#294b43;margin:16px 0;">“{safe_message}”</p>'
                f'<div style="text-align:right;color:#537168;font-weight:700;">— {safe_name}</div>'
                f'</div>',
                unsafe_allow_html=True
            )

    st.caption(
        "Quyền riêng tư: lời nhắn hiện chỉ được lưu trong phiên Streamlit đang hoạt động. "
        "Muốn tạo bảng tin dùng chung giữa nhiều người, cần kết nối cơ sở dữ liệu và bổ sung kiểm duyệt nội dung."
    )

# ============================================================
# 14. NGUỒN THAM KHẢO & KẾT NỐI HỖ TRỢ
# ============================================================

elif page == "Nguồn tham khảo":

    section_header(
        "08 / REFERENCES & SUPPORT",
        "Nguồn tham khảo & Kết nối chuyên gia",
        "Tra cứu tài liệu chuyên môn và thông tin liên hệ cơ sở y tế. Vui lòng xác nhận lại số điện thoại, lịch khám và chuyên khoa trước khi đến."
    )

    st.subheader("🏥 Danh bạ cơ sở y tế tại Việt Nam")
    st.info(
        "Các bệnh viện dưới đây là đầu mối để gia đình liên hệ hỏi về khám thần kinh, lão khoa hoặc đánh giá suy giảm trí nhớ. "
        "Danh sách không phải bảng xếp hạng và không thay thế việc lựa chọn cơ sở phù hợp theo nơi ở, tình trạng và hướng dẫn chuyển tuyến."
    )

    hospitals = [
        {
            "name": "Bệnh viện Đại học Y Dược TP. Hồ Chí Minh – Cơ sở 1",
            "area": "TP. Hồ Chí Minh",
            "address": "215 Hồng Bàng, Phường Chợ Lớn, TP. Hồ Chí Minh",
            "phone": "(028) 3855 4269",
            "tel": "+842838554269",
            "website": "https://bvdaihoc.com.vn/",
            "map": "https://www.google.com/maps/search/?api=1&query=215+Hong+Bang+Cho+Lon+Ho+Chi+Minh",
            "note": "Liên hệ tổng đài bệnh viện để hỏi lịch khám phù hợp và hướng dẫn đến chuyên khoa liên quan."
        },
        {
            "name": "Bệnh viện Chợ Rẫy",
            "area": "TP. Hồ Chí Minh",
            "address": "201B Nguyễn Chí Thanh, Phường Chợ Lớn, TP. Hồ Chí Minh",
            "phone": "(028) 3855 4137",
            "tel": "+842838554137",
            "website": "https://bvchoray.vn/",
            "map": "https://www.google.com/maps/search/?api=1&query=Benh+vien+Cho+Ray+201B+Nguyen+Chi+Thanh+Ho+Chi+Minh",
            "note": "Gọi bệnh viện để xác nhận quy trình đăng ký khám và đơn vị tiếp nhận vấn đề thần kinh/trí nhớ."
        },
        {
            "name": "Bệnh viện Lão khoa Trung ương",
            "area": "Hà Nội",
            "address": "1A Phương Mai, Phường Kim Liên, TP. Hà Nội",
            "phone": "024 3576 4558",
            "tel": "+842435764558",
            "website": "https://benhvienlaokhoa.vn/",
            "map": "https://www.google.com/maps/search/?api=1&query=Benh+vien+Lao+khoa+Trung+uong+1A+Phuong+Mai+Ha+Noi",
            "note": "Bệnh viện chuyên khoa lão khoa; liên hệ trước để hỏi lịch khám và dịch vụ phù hợp."
        }
    ]

    for h in hospitals:
        st.markdown(
            f'<div class="panel" style="border-left:5px solid #d9b968;">'
            f'<div style="color:#a17c32;font-size:12px;font-weight:800;letter-spacing:.08em">{html.escape(h["area"])}</div>'
            f'<h3 style="color:#14594d;margin:7px 0 10px">🏥 {html.escape(h["name"])}</h3>'
            f'<p style="color:#365b53;margin:5px 0"><b>Địa chỉ:</b> {html.escape(h["address"])}</p>'
            f'<p style="color:#365b53;margin:5px 0"><b>Điện thoại:</b> {html.escape(h["phone"])}</p>'
            f'<p style="color:#557168;margin:8px 0">{html.escape(h["note"])}</p>'
            f'<a href="tel:{h["tel"]}" style="display:inline-block;background:#0d6657;color:white;padding:9px 15px;border-radius:9px;text-decoration:none;font-weight:700;margin:5px 6px 4px 0">☎ Gọi điện</a>'
            f'<a href="{h["map"]}" target="_blank" rel="noopener noreferrer" style="display:inline-block;background:#eaf3ee;color:#14594d;padding:9px 15px;border-radius:9px;text-decoration:none;font-weight:700;margin:5px 6px 4px 0">📍 Chỉ đường</a>'
            f'<a href="{h["website"]}" target="_blank" rel="noopener noreferrer" style="display:inline-block;background:#f5f0e3;color:#725b2d;padding:9px 15px;border-radius:9px;text-decoration:none;font-weight:700;margin:5px 0 4px">🌐 Website chính thức</a>'
            f'</div><div style="height:10px"></div>',
            unsafe_allow_html=True
        )

    st.subheader("☎️ Hỗ trợ khẩn cấp và hỗ trợ cộng đồng")
    st.markdown("""
    <div class="panel" style="background:#fff3ef;border-left:5px solid #d96b55;">
      <h3 style="color:#9e392b">115 – Cấp cứu y tế</h3>
      <p style="color:#573b35">Dành cho tình huống cấp cứu y tế cần hỗ trợ khẩn cấp. Nếu người bệnh đột ngột lú lẫn, yếu liệt, méo miệng, khó nói, co giật, bất tỉnh hoặc có nguy cơ tức thời, hãy gọi cấp cứu hoặc đến khoa Cấp cứu gần nhất.</p>
      <a href="tel:115" style="display:inline-block;background:#b84635;color:white;padding:10px 18px;border-radius:9px;text-decoration:none;font-weight:800">☎ Gọi 115</a>
    </div>
    <div class="panel" style="background:#f0f8f3;">
      <h3 style="color:#14594d">Kết nối hỗ trợ tâm lý – xã hội</h3>
      <p style="color:#365b53">Với căng thẳng kéo dài, kiệt sức khi chăm sóc hoặc cần hỗ trợ tâm lý, gia đình có thể trao đổi với khoa Tâm thần/Tâm lý lâm sàng tại bệnh viện đa khoa, cơ sở sức khỏe tâm thần công lập hoặc nhân viên y tế địa phương để được hướng dẫn phù hợp.</p>
      <p style="color:#365b53"><b>Lưu ý:</b> CHẠM Hub chưa xác minh được một đường dây nóng tư vấn tâm lý toàn quốc chuyên biệt, chính thức và đang hoạt động thường trực dành riêng cho mọi đối tượng. Không nên dùng các số tổng đài không rõ nguồn gốc.</p>
    </div>
    """, unsafe_allow_html=True)

    st.caption("Thông tin liên hệ được tổng hợp từ website chính thức của các bệnh viện và cổng thông tin cơ quan nhà nước. Số điện thoại, địa chỉ, lịch khám có thể thay đổi; hãy kiểm tra lại trước khi sử dụng.")

    st.divider()
    st.subheader("🌐 Thư viện nguồn tham khảo quốc tế")
    refs = [
        ("World Health Organization (WHO) – Dementia", "Thông tin tổng quan về sa sút trí tuệ và ứng phó y tế công cộng.", "https://www.who.int/news-room/fact-sheets/detail/dementia"),
        ("Alzheimer's Association", "Tài liệu giáo dục về Alzheimer, dấu hiệu, chăm sóc và hỗ trợ gia đình.", "https://www.alz.org/"),
        ("National Institute on Aging (NIA)", "Thông tin khoa học và hướng dẫn cộng đồng về Alzheimer và sức khỏe não bộ.", "https://www.nia.nih.gov/health/alzheimers"),
        ("NHS – Dementia", "Thông tin sức khỏe cộng đồng về sa sút trí tuệ và các vấn đề liên quan.", "https://www.nhs.uk/conditions/dementia/")
    ]
    for title, desc, url in refs:
        st.markdown(
            f'<div class="panel"><h3 style="color:#14594d">{html.escape(title)}</h3>'
            f'<p class="muted">{html.escape(desc)}</p>'
            f'<a href="{url}" target="_blank" rel="noopener noreferrer">Mở nguồn chính thức ↗</a></div><div style="height:8px"></div>',
            unsafe_allow_html=True
        )

    st.warning(
        "CHẠM Hub là nền tảng giáo dục và nâng cao nhận thức, không chẩn đoán, không kê đơn và không thay thế tư vấn y tế. "
        "Khi có thay đổi đáng lo ngại về trí nhớ hoặc hành vi, hãy đưa người thân đến cơ sở y tế để được đánh giá."
    )

# ============================================================
# 15. CHÂN TRANG
# ============================================================

render_footer()
