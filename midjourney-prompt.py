import streamlit as st

st.set_page_config(
   page_title="Ex-stream-ly Cool App",
   page_icon="🧊",
   layout="wide",
   initial_sidebar_state="expanded",
)

# Title
st.title("Midjourney Prompt Generator")

# Variable setup



col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Aspect Ratio")
    aspect_ratios = ["1:1 (Default)", "4:3", "3:4", "16:9", "9:16", "4:5", "5:4", "21:9", "9:21", "2:3", "3:2", "8.5:11", "11:8.5", "210:297", "297:210"]
    aspect_ratio = st.selectbox("Select aspect ratio", aspect_ratios)

    st.subheader("Style")
    style = st.slider("Select style level (Default=500)", 0, 1000, 500)
    with st.expander("Style Examples"):
        st.image("style-2.png", use_column_width=True)
    style_raw = st.checkbox("Raw Style")
    with st.expander("Raw Style Examples"):
        st.image("style_raw.png", use_column_width=True)

    st.divider()

    st.subheader("Chaos")
    chaos = st.slider("Select chaos level (Default=0)", 0, 100, 0)
    with st.expander("Chaos Examples"):
        st.image("chaos.png", use_column_width=True)
    
    st.subheader("Weirdness")
    weirdness_options = ["0", "250", "500", "750", "1000"]
    weirdness = st.select_slider("Select weirdness level (Default=0)", weirdness_options)

    st.subheader("Exclude from Image")
    no = st.text_input("Enter items to exclude from image", "")

    st.subheader("Seed Number")
    seed = st.text_input("Enter seed number", "")


with col2:

    st.subheader("Prompt Words")
    prompt_words = st.text_area("Enter prompt words", "")


    keywords_list = ["Trending on Dribbble", "Pulitzer Prize-winning photography", "Fashion photography", "Automotive photography rolling shot", "Bokeh", "Volumetric Lighting", "Beautiful Lighting", "Golden Hour", "Depth of Field", "Soft natural lighting", "Film grain"]
    keywords = st.multiselect("Select keywords", keywords_list)

    digital_art_list = ["Unreal", "Unity", "Cinema4d", "Vector", "Blender", "Vray", "3d art", "CG rendering", "Digital painting", "Pixar trend"]
    digital_art = st.multiselect("Select digital art keywords", digital_art_list)

    photo_angles_list = ["", "Full-Shot Angle", "Full-Body Shot", "Wide-Angle Shot", "Ultra-Wide Angle", "Eye-Level Shot", "Far-Shot Angle", "Medium-Shot Angle", "Ground-Shot Angle", "Low-Angle Shot", "Glamour Shot"]
    photo_angle = st.selectbox("Select photo angle keyword", photo_angles_list)

    lens_size_list = ["", "Wide Angle", "Telephoto", "Macro", "Fisheye", "Tilt-Shift", "Zoom", "Prime", "Normal", "Portrait", "Wide-Angle", "Telephoto", "Macro", "Fisheye", "Tilt-Shift", "Zoom", "Prime", "Normal", "Portrait"]
    lens_size = st.selectbox("Select lens size keyword", lens_size_list)

    lens_mm_list = ["", "10mm", "12mm", "14mm", "16mm", "18mm", "20mm", "24mm", "28mm", "35mm", "50mm", "85mm", "100mm", "135mm", "200mm", "300mm", "400mm", "500mm", "600mm", "800mm", "1000mm"]
    lens_mm = st.selectbox("Select lens mm keyword", lens_mm_list)

    aperture_list = ["", "f/1.0", "f/1.2", "f/1.4", "f/1.8", "f/2.0", "f/2.8", "f/3.5", "f/4.0", "f/5.6", "f/8.0", "f/11", "f/16", "f/22", "f/32", "f/45", "f/64"]
    aperture = st.selectbox("Select aperture keyword", aperture_list)

with col3:
    prompt = prompt_words + " "

    if len(keywords) > 0:
        # Iterate through keywords
        for keyword in keywords:
            prompt += f"{keyword}. "
    
    if len(digital_art) > 0:
        # Iterate through keywords
        for keyword in digital_art:
            prompt += f"{keyword} "

    if photo_angle != "":
        prompt += f"{photo_angle} "
    
    if lens_size != "":
        prompt += f"{lens_size} "
    
    if lens_mm != "":
        prompt += f"{lens_mm} "
    
    if aperture != "":
        prompt += f"{aperture} "

    if style_raw:
        prompt += f"--style raw "
    
    if chaos > 0:
        prompt += f"--chaos {chaos} "

    if no != "":
        prompt += f"--no {no} "

    if seed != "":
        prompt += f"--seed {seed} "

    if aspect_ratio != "1:1 (Default)":
        prompt += f"--ar {aspect_ratio} "

    if style != 500:
        prompt += f"--stylize {style} "

    if weirdness != "0":
        prompt += f"--weird {weirdness} "


    st.subheader("Prompt:")
    st.code(prompt)

    # if st.button("Save Prompt"):
    #     with open("prompts.txt", "a") as f:
    #         f.write(prompt + "\n")

    # with open("prompts.txt", "r") as f:
    #     prompts = f.readlines()

    # st.markdown("##### Saved Prompts")
    # with st.expander("Saved Prompts"):
    #     for prompt in prompts:
    #         st.code(prompt)