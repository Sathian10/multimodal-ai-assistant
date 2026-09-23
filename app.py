import os
import tempfile

import pytesseract
import streamlit as st
from st_keyup import st_keyup

from PIL import Image


# ---------------------------------------------------------
# Page configuration
# ---------------------------------------------------------

st.set_page_config(
    page_title="Multimodal AI Assistant",
    page_icon="🎙️",
    layout="wide"
)


# ---------------------------------------------------------
# Custom CSS
# ---------------------------------------------------------

# ---------------------------------------------------------
# Custom CSS — Light Portfolio UI
# ---------------------------------------------------------

st.markdown(
    """
    <style>

    /* ---------- GLOBAL APP ---------- */

    .stApp {
        background:
            radial-gradient(
                circle at 10% 0%,
                rgba(99, 102, 241, 0.08),
                transparent 28%
            ),
            radial-gradient(
                circle at 92% 8%,
                rgba(14, 165, 233, 0.06),
                transparent 24%
            ),
            #f6f8fc;

        color: #0f172a;
    }

    .block-container {
        max-width: 1280px;
        padding-top: 2.4rem;
        padding-bottom: 4rem;
    }


    /* ---------- TYPOGRAPHY ---------- */

    h1, h2, h3 {
        color: #0f172a;
        letter-spacing: -0.025em;
    }

    p, label {
        color: #475569;
    }

    .main-title {
        font-size: clamp(44px, 5vw, 66px);
        line-height: 1.04;
        font-weight: 800;
        letter-spacing: -0.055em;

        background: linear-gradient(
            90deg,
            #111827 0%,
            #3730a3 48%,
            #0284c7 100%
        );

        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;

        margin-top: 6px;
        margin-bottom: 12px;
    }

    .subtitle {
        font-size: 20px;
        line-height: 1.6;
        color: #64748b;
        max-width: 760px;
        margin-bottom: 18px;
    }


    /* ---------- PORTFOLIO LABEL ---------- */

    .eyebrow {
        display: inline-flex;
        align-items: center;
        gap: 8px;

        padding: 7px 12px;
        border-radius: 999px;

        background: #eef2ff;
        border: 1px solid #c7d2fe;

        color: #4338ca;

        font-size: 12px;
        font-weight: 700;
        letter-spacing: 0.10em;
        text-transform: uppercase;

        margin-bottom: 16px;
    }


    /* ---------- TECHNOLOGY BADGES ---------- */

    .tech-badge {
        display: inline-block;

        padding: 7px 12px;
        margin: 5px 6px 5px 0;

        border-radius: 999px;

        background: #ffffff;
        border: 1px solid #dbe3ee;

        color: #334155;

        font-size: 12px;
        font-weight: 600;

        box-shadow:
            0 3px 10px rgba(15, 23, 42, 0.04);
    }


    /* ---------- PIPELINE CARDS ---------- */

    .info-card {
        padding: 18px 20px;

        border-radius: 16px;

        background: rgba(255, 255, 255, 0.96);

        border: 1px solid #e2e8f0;

        margin-top: 12px;

        color: #475569;

        box-shadow:
            0 8px 24px rgba(15, 23, 42, 0.06);

        transition:
            transform 0.2s ease,
            border-color 0.2s ease,
            box-shadow 0.2s ease;
    }

    .info-card:hover {
        transform: translateY(-2px);

        border-color: #a5b4fc;

        box-shadow:
            0 14px 32px rgba(15, 23, 42, 0.09);
    }

    .info-card b {
        color: #0f172a;
        font-size: 15px;
    }


    /* ---------- RESULT BOX ---------- */

    .result-box {
        padding: 22px;

        border-radius: 16px;

        background: #ffffff;

        border: 1px solid #e2e8f0;

        margin-top: 12px;
        margin-bottom: 18px;

        color: #334155;

        font-size: 16px;
        line-height: 1.7;

        overflow-wrap: anywhere;

        box-shadow:
            0 8px 24px rgba(15, 23, 42, 0.05);
    }


    /* ---------- METRIC CARDS ---------- */

    .metric-box {
        padding: 26px 22px;

        border-radius: 18px;

        background:
            linear-gradient(
                145deg,
                #ffffff 0%,
                #f8fafc 100%
            );

        border: 1px solid #e2e8f0;

        text-align: center;

        color: #0f172a;

        box-shadow:
            0 10px 30px rgba(15, 23, 42, 0.07);

        min-height: 145px;
    }

    .metric-box h3 {
        color: #64748b;

        font-size: 14px;
        font-weight: 600;

        margin-bottom: 12px;
    }

    .metric-box h2 {
        color: #111827;

        font-size: 29px;
        font-weight: 800;

        margin: 0;
    }


    /* ---------- BUTTONS ---------- */

    .stButton > button,
    .stDownloadButton > button {

        border: 1px solid #4f46e5;

        border-radius: 12px;

        min-height: 46px;

        font-weight: 700;

        background: linear-gradient(
            135deg,
            #4f46e5,
            #2563eb
        );

        color: #ffffff;

        box-shadow:
            0 8px 22px rgba(79, 70, 229, 0.20);

        transition:
            transform 0.18s ease,
            box-shadow 0.18s ease;
    }

    .stButton > button:hover,
    .stDownloadButton > button:hover {

        transform: translateY(-1px);

        border-color: #3730a3;

        color: #ffffff;

        box-shadow:
            0 12px 28px rgba(79, 70, 229, 0.27);
    }


    /* ---------- FILE UPLOADER ---------- */

    [data-testid="stFileUploader"] {

        background: #ffffff;

        border: 1px solid #dbe3ee;

        border-radius: 16px;

        padding: 8px;

        box-shadow:
            0 5px 18px rgba(15, 23, 42, 0.04);
    }


    /* ---------- INPUT FIELDS ---------- */

    .stTextInput input,
    .stTextArea textarea {

        background: #ffffff !important;

        color: #0f172a !important;

        border-radius: 12px !important;

        border:
            1px solid #cbd5e1
            !important;
    }


    /* ---------- RADIO OPTIONS ---------- */

    [data-testid="stRadio"] > div {
        gap: 12px;
    }


    /* ---------- DIVIDERS ---------- */

    hr {
        border-color:
            #e2e8f0
            !important;

        margin-top: 1.8rem !important;
        margin-bottom: 1.8rem !important;
    }


    /* ---------- SIDEBAR ---------- */

    [data-testid="stSidebar"] {

        background:
            linear-gradient(
                180deg,
                #111827 0%,
                #0f172a 100%
            );

        border-right:
            1px solid rgba(255, 255, 255, 0.06);
    }

    [data-testid="stSidebar"] * {
        color: #cbd5e1;
    }

    [data-testid="stSidebar"] h1,
    [data-testid="stSidebar"] h2,
    [data-testid="stSidebar"] h3 {
        color: #ffffff;
    }

    [data-testid="stSidebar"] strong {
        color: #ffffff;
    }


    /* ---------- STATUS / ALERTS ---------- */

    [data-testid="stAlert"] {
        border-radius: 12px;
    }


    /* ---------- FOOTER ---------- */

    .footer {
        text-align: center;

        color: #94a3b8;

        margin-top: 60px;

        padding-top: 25px;

        border-top: 1px solid #e2e8f0;

        font-size: 13px;

        letter-spacing: 0.02em;
    }


    /* ---------- MOBILE ---------- */

    @media (max-width: 768px) {

        .main-title {
            font-size: 42px;
        }

        .subtitle {
            font-size: 17px;
        }

        .block-container {
            padding-top: 1.5rem;
        }
    }
    /* FIX: Force textarea text to be visible */
.stTextArea textarea,
div[data-testid="stTextArea"] textarea,
div[data-baseweb="textarea"] textarea,
textarea[disabled],
textarea[readonly] {
    color: #0f172a !important;
    -webkit-text-fill-color: #0f172a !important;
    background: #ffffff !important;
    opacity: 1 !important;
}

/* Text selection */
.stTextArea textarea::selection {
    background: #bfdbfe !important;
    color: #0f172a !important;
}
   

    </style>
    """,
    unsafe_allow_html=True
)

# ---------------------------------------------------------
# Sidebar
# ---------------------------------------------------------

with st.sidebar:

    st.markdown(
        """
        <div style="
            font-size: 13px;
            font-weight: 700;
            letter-spacing: 0.12em;
            text-transform: uppercase;
            color: #818cf8;
            margin-bottom: 10px;
        ">
            Portfolio Project
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("## Multimodal AI")

    st.markdown(
        """
        A multimodal AI application that combines
        speech recognition, OCR and NLP models
        inside a unified processing workflow.
        """
    )

    st.markdown("---")

    st.markdown("### Built With")

    st.markdown(
        """
        **Whisper**  
        Speech recognition

        **DistilBERT**  
        Sentiment analysis

        **Tesseract OCR**  
        Image text extraction

        **Streamlit**  
        Interactive application interface
        """
    )

    st.markdown("---")

    st.markdown("### Developer")

    st.markdown(
        """
        **Subash Chandrabose Sathian**

        University of London  
        Computer Science Project
        """
    )

    st.success("● AI System Ready")


# ---------------------------------------------------------
# Main heading
# ---------------------------------------------------------

st.markdown(
    """
    <div class="eyebrow">
        MULTIMODAL AI • NLP • COMPUTER VISION
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    '<div class="main-title">Multimodal AI Assistant</div>',
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="subtitle">
        A unified AI workspace that transforms speech, text and
        images into sentiment insights using cascaded pre-trained models.
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <span class="tech-badge">Whisper</span>
    <span class="tech-badge">DistilBERT</span>
    <span class="tech-badge">Tesseract OCR</span>
    <span class="tech-badge">Transformers</span>
    <span class="tech-badge">Streamlit</span>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div style="
        margin-top: 24px;
        color: #64748b;
        font-size: 15px;
        line-height: 1.7;
        max-width: 900px;
    ">
        Process multiple input modalities through specialized AI models
        and generate interpretable sentiment results through a single
        interactive interface.
    </div>
    """,
    unsafe_allow_html=True
)

st.divider()


# ---------------------------------------------------------
# Model loading functions
# ---------------------------------------------------------

@st.cache_resource(show_spinner=False)
def load_whisper_model():
    """Load Whisper only when speech processing is required."""

    import whisper

    return whisper.load_model("base")


@st.cache_resource(show_spinner=False)
def load_sentiment_model():
    """Load DistilBERT only when sentiment analysis is required."""

    from transformers import pipeline

    return pipeline(
        "sentiment-analysis",
        model=(
            "distilbert/"
            "distilbert-base-uncased-finetuned-sst-2-english"
        )
    )


# ---------------------------------------------------------
# Reusable sentiment-analysis function
# ---------------------------------------------------------

def analyse_and_display_sentiment(
    text,
    input_type,
    output_filename,
    source_name=None
):
    """Analyse text, display the results and save an output file."""

    clean_text = text.strip()

    if not clean_text:
        st.warning("No text was provided for analysis.")
        return

    os.makedirs("outputs", exist_ok=True)

    with st.spinner(
        "Running sentiment analysis using DistilBERT..."
    ):
        sentiment_model = load_sentiment_model()

        sentiment = sentiment_model(
            clean_text,
            truncation=True
        )

        label = sentiment[0]["label"]
        score = sentiment[0]["score"]

    source_details = ""

    if source_name:
        source_details = f"""
Source File:
{source_name}
"""

    output_text = f"""FYP AI Orchestration Prototype Output
========================================

Input Type:
{input_type}
{source_details}
Processed Text:
{clean_text}

Sentiment:
{label}

Confidence Score:
{score * 100:.2f}%
"""

    output_path = os.path.join(
        "outputs",
        output_filename
    )

    with open(
        output_path,
        "w",
        encoding="utf-8"
    ) as output_file:
        output_file.write(output_text)

    st.success(
        "Sentiment analysis completed successfully!"
    )

    st.subheader("Processed Text")

    st.markdown(
        f'<div class="result-box">{clean_text}</div>',
        unsafe_allow_html=True
    )

    st.subheader("Sentiment Analysis Result")

    result_col1, result_col2 = st.columns(2)

    sentiment_icon = (
        "😊" if label == "POSITIVE" else "☹️"
    )

    with result_col1:
        st.markdown(
            f"""
            <div class="metric-box">
                <h3>{sentiment_icon} Sentiment</h3>
                <h2>{label}</h2>
            </div>
            """,
            unsafe_allow_html=True
        )

    with result_col2:
        st.markdown(
            f"""
            <div class="metric-box">
                <h3>Confidence Score</h3>
                <h2>{score * 100:.2f}%</h2>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.download_button(
        label="Download Analysis Result",
        data=output_text,
        file_name=output_filename,
        mime="text/plain",
        use_container_width=True
    )

    st.info(
        f"The result has also been saved to {output_path}."
    )


# ---------------------------------------------------------
# Live typed-text sentiment function
# ---------------------------------------------------------

def display_live_sentiment(text):
    """Run and display live sentiment analysis for typed text."""

    clean_text = text.strip()

    if not clean_text:
        return

    with st.spinner(
        "Updating live sentiment prediction..."
    ):
        sentiment_model = load_sentiment_model()

        sentiment = sentiment_model(
            clean_text,
            truncation=True
        )

        label = sentiment[0]["label"]
        score = sentiment[0]["score"]

    st.success(
        "Live sentiment prediction updated."
    )

    st.subheader(
        "Live Sentiment Analysis Result"
    )

    result_col1, result_col2 = st.columns(2)

    sentiment_icon = (
        "😊" if label == "POSITIVE" else "☹️"
    )

    with result_col1:
        st.markdown(
            f"""
            <div class="metric-box">
                <h3>{sentiment_icon} Sentiment</h3>
                <h2>{label}</h2>
            </div>
            """,
            unsafe_allow_html=True
        )

    with result_col2:
        st.markdown(
            f"""
            <div class="metric-box">
                <h3>Confidence Score</h3>
                <h2>{score * 100:.2f}%</h2>
            </div>
            """,
            unsafe_allow_html=True
        )

    output_text = f"""FYP AI Orchestration Prototype Output
========================================

Input Type:
Live Typed Text

Processed Text:
{clean_text}

Sentiment:
{label}

Confidence Score:
{score * 100:.2f}%
"""

    st.download_button(
        label="Download Current Live Text Result",
        data=output_text,
        file_name="live_text_result.txt",
        mime="text/plain",
        use_container_width=True,
        key="download_live_text_result"
    )


# ---------------------------------------------------------
# Input modality selection
# ---------------------------------------------------------

st.markdown("## AI Workspace")

st.caption(
    "Choose an input modality to begin processing."
)

input_mode_display = st.segmented_control(
    "Input modality",
    options=[
        "Audio",
        "Live Text",
        "Document",
        "Vision"
    ],
    default="Audio",
    label_visibility="collapsed"
)

mode_map = {
    "Audio": "Upload Audio",
    "Live Text": "Type Text",
    "Document": "Upload Text File",
    "Vision": "Upload Image"
}

input_mode = mode_map[input_mode_display]

st.divider()


# ---------------------------------------------------------
# Input and pipeline columns
# ---------------------------------------------------------

col1, col2 = st.columns([1, 1])

uploaded_file = None
typed_text = ""

uploaded_text_file = None
uploaded_text_content = ""

uploaded_image = None
image_object = None
ocr_text = ""

audio_method = None


# ---------------------------------------------------------
# Left column: user input
# ---------------------------------------------------------

with col1:

    if input_mode == "Upload Audio":

        st.subheader("Audio Input")

        audio_method = st.radio(
            "Choose how you want to provide audio:",
            [
                "Upload Audio File",
                "Record with Microphone"
            ],
            horizontal=True
        )

        if audio_method == "Upload Audio File":

            uploaded_file = st.file_uploader(
                "Choose an audio file",
                type=["wav", "mp3", "m4a"],
                key="audio_file"
            )

            if uploaded_file is not None:
                st.success(
                    "Audio file uploaded successfully."
                )
                st.audio(uploaded_file)

        else:

            uploaded_file = st.audio_input(
                "Record your voice"
            )

            if uploaded_file is not None:
                st.success(
                    "Audio recorded successfully."
                )
                st.audio(uploaded_file)


    elif input_mode == "Type Text":

        st.subheader("Live Text Input")

        st.caption(
            "Sentiment updates automatically shortly "
            "after you stop typing."
        )

        typed_text = st_keyup(
            "Enter text for live sentiment analysis",
            value="",
            debounce=600,
            key="live_text_input"
        )

        if typed_text.strip():
            st.success(
                "Live text input received."
            )


    elif input_mode == "Upload Text File":

        st.subheader("Upload Text File")

        uploaded_text_file = st.file_uploader(
            "Choose a .txt file",
            type=["txt"],
            key="text_file"
        )

        if uploaded_text_file is not None:

            try:
                uploaded_text_content = (
                    uploaded_text_file
                    .read()
                    .decode("utf-8")
                )

                st.success(
                    "Text file uploaded successfully."
                )

                st.text_area(
                    "File Content",
                    value=uploaded_text_content,
                    height=180,
                    disabled=True
                )

            except UnicodeDecodeError:
                st.error(
                    "Unable to read the file. "
                    "Please upload a UTF-8 encoded .txt file."
                )


    elif input_mode == "Upload Image":

        st.subheader("Upload Image")

        uploaded_image = st.file_uploader(
            "Choose an image containing text",
            type=["png", "jpg", "jpeg"],
            key="image_file"
        )

        if uploaded_image is not None:

            try:
                image_object = Image.open(
                    uploaded_image
                )

                st.success(
                    "Image uploaded successfully."
                )

                st.image(
                    image_object,
                    caption=uploaded_image.name,
                    use_container_width=True
                )

            except Exception as error:
                st.error(
                    f"Unable to open the image: {error}"
                )


# ---------------------------------------------------------
# Right column: dynamic system pipeline
# ---------------------------------------------------------

with col2:

    st.subheader("System Pipeline")

    if input_mode == "Upload Audio":

        if audio_method == "Record with Microphone":
            audio_input_description = (
                "User records audio directly "
                "using the microphone."
            )
        else:
            audio_input_description = (
                "User uploads an audio file."
            )

        st.markdown(
            f"""
            <div class="info-card">
                <b>Audio Input</b><br>
                {audio_input_description}
            </div>

            <div class="info-card">
                <b>Whisper Speech-to-Text</b><br>
                Converts spoken audio into text.
            </div>

            <div class="info-card">
                <b>DistilBERT Sentiment Analysis</b><br>
                Classifies the emotional tone of the transcript.
            </div>

            <div class="info-card">
                <b>Final Output</b><br>
                Displays transcript, sentiment label and
                confidence score.
            </div>
            """,
            unsafe_allow_html=True
        )


    elif input_mode == "Type Text":

        st.markdown(
            """
            <div class="info-card">
                <b>Live Text Input</b><br>
                User types text directly into the application.
            </div>

            <div class="info-card">
                <b>DistilBERT Live Sentiment Analysis</b><br>
                Automatically classifies the emotional tone shortly
                after the user stops typing.
            </div>

            <div class="info-card">
                <b>Live Output</b><br>
                Updates the sentiment label and confidence score
                without an Analyze Text button.
            </div>
            """,
            unsafe_allow_html=True
        )


    elif input_mode == "Upload Text File":

        st.markdown(
            """
            <div class="info-card">
                <b>Text File Input</b><br>
                User uploads a plain text (.txt) file.
            </div>

            <div class="info-card">
                <b>Text Extraction</b><br>
                Reads and extracts text from the uploaded file.
            </div>

            <div class="info-card">
                <b>DistilBERT Sentiment Analysis</b><br>
                Analyses the emotional tone of the extracted text.
            </div>

            <div class="info-card">
                <b>Final Output</b><br>
                Displays extracted text, sentiment label and
                confidence score.
            </div>
            """,
            unsafe_allow_html=True
        )


    elif input_mode == "Upload Image":

        st.markdown(
            """
            <div class="info-card">
                <b>Image Input</b><br>
                User uploads an image containing readable text.
            </div>

            <div class="info-card">
                <b>Tesseract OCR</b><br>
                Detects and extracts text from the uploaded image.
            </div>

            <div class="info-card">
                <b>DistilBERT Sentiment Analysis</b><br>
                Analyses the emotional tone of the extracted text.
            </div>

            <div class="info-card">
                <b>Final Output</b><br>
                Displays OCR text, sentiment label and
                confidence score.
            </div>
            """,
            unsafe_allow_html=True
        )


# ---------------------------------------------------------
# Audio processing
# ---------------------------------------------------------

if input_mode == "Upload Audio":

    st.divider()

    if uploaded_file is not None:

        if st.button(
            "Analyze Audio",
            use_container_width=True
        ):
            os.makedirs(
                "outputs",
                exist_ok=True
            )

            # Microphone recordings are WAV files.
            if audio_method == "Record with Microphone":
                suffix = ".wav"
                audio_source_name = (
                    "Microphone Recording"
                )
                input_type_name = (
                    "Live Microphone Recording"
                )
            else:
                suffix = os.path.splitext(
                    uploaded_file.name
                )[1]

                audio_source_name = (
                    uploaded_file.name
                )

                input_type_name = (
                    "Uploaded Audio"
                )

            temp_audio_path = None

            try:
                with tempfile.NamedTemporaryFile(
                    delete=False,
                    suffix=suffix
                ) as temp_audio:

                    temp_audio.write(
                        uploaded_file.getvalue()
                    )

                    temp_audio_path = (
                        temp_audio.name
                    )

                progress = st.progress(0)

                if (
                    audio_method
                    == "Record with Microphone"
                ):
                    st.write(
                        "✅ Step 1: Microphone audio "
                        "recorded successfully"
                    )
                else:
                    st.write(
                        "✅ Step 1: Audio uploaded "
                        "successfully"
                    )

                with st.spinner(
                    "Loading Whisper model..."
                ):
                    speech_model = (
                        load_whisper_model()
                    )

                    progress.progress(25)

                st.write(
                    "✅ Step 2: Whisper model loaded"
                )

                with st.spinner(
                    "Transcribing audio using Whisper..."
                ):
                    result = (
                        speech_model.transcribe(
                            temp_audio_path
                        )
                    )

                    transcript = (
                        result["text"].strip()
                    )

                    progress.progress(55)

                st.write(
                    "✅ Step 3: Speech converted to text"
                )

                if not transcript:
                    st.warning(
                        "Whisper did not detect any "
                        "speech in the audio."
                    )

                else:

                    with st.spinner(
                        "Running sentiment analysis "
                        "using DistilBERT..."
                    ):
                        sentiment_model = (
                            load_sentiment_model()
                        )

                        sentiment = (
                            sentiment_model(
                                transcript,
                                truncation=True
                            )
                        )

                        label = (
                            sentiment[0]["label"]
                        )

                        score = (
                            sentiment[0]["score"]
                        )

                        progress.progress(85)

                    st.write(
                        "✅ Step 4: Sentiment analysis "
                        "completed"
                    )

                    output_text = f"""FYP AI Orchestration Prototype Output
========================================

Input Type:
{input_type_name}

Audio Source:
{audio_source_name}

Transcript:
{transcript}

Sentiment:
{label}

Confidence Score:
{score * 100:.2f}%
"""

                    output_path = os.path.join(
                        "outputs",
                        "audio_result.txt"
                    )

                    with open(
                        output_path,
                        "w",
                        encoding="utf-8"
                    ) as output_file:

                        output_file.write(
                            output_text
                        )

                    progress.progress(100)

                    st.success(
                        "Audio analysis completed "
                        "successfully!"
                    )

                    st.subheader(
                        "Speech-to-Text Transcript"
                    )

                    st.markdown(
                        (
                            '<div class="result-box">'
                            f'{transcript}'
                            '</div>'
                        ),
                        unsafe_allow_html=True
                    )

                    st.subheader(
                        "Sentiment Analysis Result"
                    )

                    result_col1, result_col2 = (
                        st.columns(2)
                    )

                    sentiment_icon = (
                        "😊"
                        if label == "POSITIVE"
                        else "☹️"
                    )

                    with result_col1:
                        st.markdown(
                            f"""
                            <div class="metric-box">
                                <h3>
                                    {sentiment_icon}
                                    Sentiment
                                </h3>
                                <h2>
                                    {label}
                                </h2>
                            </div>
                            """,
                            unsafe_allow_html=True
                        )

                    with result_col2:
                        st.markdown(
                            f"""
                            <div class="metric-box">
                                <h3>
                                    Confidence Score
                                </h3>
                                <h2>
                                    {score * 100:.2f}%
                                </h2>
                            </div>
                            """,
                            unsafe_allow_html=True
                        )

                    st.download_button(
                        label=(
                            "Download Audio "
                            "Analysis Result"
                        ),
                        data=output_text,
                        file_name=(
                            "audio_result.txt"
                        ),
                        mime="text/plain",
                        use_container_width=True
                    )

                    st.info(
                        "The result has also been "
                        "saved to "
                        f"{output_path}."
                    )

            except Exception as error:
                st.error(
                    "Audio analysis failed: "
                    f"{error}"
                )

            finally:
                if (
                    temp_audio_path is not None
                    and os.path.exists(
                        temp_audio_path
                    )
                ):
                    os.remove(
                        temp_audio_path
                    )

    else:

        if (
            audio_method
            == "Record with Microphone"
        ):
            st.info(
                "Please record audio using your "
                "microphone to begin."
            )
        else:
            st.info(
                "Please upload an audio file "
                "to begin."
            )


# ---------------------------------------------------------
# Live typed-text processing
# ---------------------------------------------------------

elif input_mode == "Type Text":

    st.divider()

    if typed_text.strip():

        display_live_sentiment(
            typed_text
        )

    else:

        st.info(
            "Start typing above to see live "
            "sentiment prediction."
        )


# ---------------------------------------------------------
# Uploaded text-file processing
# ---------------------------------------------------------

elif input_mode == "Upload Text File":

    st.divider()

    if (
        uploaded_text_file is not None
        and uploaded_text_content.strip()
    ):

        if st.button(
            "Analyze Text File",
            use_container_width=True
        ):
            analyse_and_display_sentiment(
                text=uploaded_text_content,
                input_type="Uploaded Text File",
                output_filename=(
                    "text_file_result.txt"
                ),
                source_name=(
                    uploaded_text_file.name
                )
            )

    elif uploaded_text_file is None:

        st.info(
            "Please upload a text (.txt) "
            "file to begin."
        )

    else:

        st.warning(
            "The uploaded text file is empty."
        )


# ---------------------------------------------------------
# Uploaded image processing
# ---------------------------------------------------------

elif input_mode == "Upload Image":

    st.divider()

    if uploaded_image is None:

        st.info(
            "Please upload a PNG, JPG or "
            "JPEG image to begin."
        )

    elif image_object is not None:

        if st.button(
            "Analyze Image",
            use_container_width=True
        ):

            try:

                with st.spinner(
                    "Extracting text from the image "
                    "using Tesseract OCR..."
                ):
                    ocr_text = (
                        pytesseract.image_to_string(
                            image_object
                        ).strip()
                    )

                if not ocr_text:

                    st.warning(
                        "No readable text was detected "
                        "in the image. Please upload a "
                        "clearer image containing text."
                    )

                else:

                    st.success(
                        "Text extracted from the image "
                        "successfully!"
                    )

                    st.subheader(
                        "OCR Extracted Text"
                    )

                    st.text_area(
                        "Extracted text",
                        value=ocr_text,
                        height=180,
                        disabled=True
                    )

                    analyse_and_display_sentiment(
                        text=ocr_text,
                        input_type="Uploaded Image",
                        output_filename=(
                            "image_result.txt"
                        ),
                        source_name=(
                            uploaded_image.name
                        )
                    )

            except (
                pytesseract.TesseractNotFoundError
            ):

                st.error(
                    "Tesseract OCR was not found. "
                    "Confirm that Tesseract is "
                    "installed and restart the app."
                )

            except Exception as error:

                st.error(
                    "Image analysis failed: "
                    f"{error}"
                )


# ---------------------------------------------------------
# Footer
# ---------------------------------------------------------

st.markdown(
    """
    <div class="footer">
        University of London |
        CM3070 Project |
        Prototype Version 1.3
    </div>
    """,
    unsafe_allow_html=True
)