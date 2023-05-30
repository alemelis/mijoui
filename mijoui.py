import streamlit as st

st.title("Mijoui")

prompt = st.text_area("prompt", "")
cmd = f"{prompt}"

neg_prompt = st.text_area("negative prompt", "")
if neg_prompt:
    cmd += f" --no {neg_prompt}"

model_version = st.selectbox(
    "version",
    [i for i in range(1, 5)]
    + [
        "niji 4",
        5,
        5.1,
        "niji 5",
        "hd",
        "testp",
        "test",
    ],
    5,
)

if model_version != "niji 5":
    cmd += f" --version {model_version}"
else:
    cmd += f" --{model_version}"

if model_version == "niji 5":
    style = st.selectbox("style", ["default", "cute", "expressive", "scenic"], 0)
    if style != "default":
        cmd += f" --style {style}"

if model_version == 4:
    style = st.selectbox("style", ["4a", "4b", "4c"], 2)
    cmd += f" --style {style}"

if model_version == 5.1:
    if st.checkbox("raw"):
        cmd += " --style raw"

if model_version in [1, 2, 3, 4, 5, 5.1]:
    if st.checkbox("tile"):
        cmd += " --tile"

if model_version in [4, 5, 5.1, "niji 5"]:
    stylize = st.slider("stylize", 0, 1000, 100)
    cmd += f" --stylize {stylize}"

if model_version in [4, 5, 5.1, "niji 5"]:
    chaos = st.slider("chaos", 0, 100, 0)
    cmd += f" --chaos {chaos}"

if model_version in [4, 5, "niji 5"]:
    quality = st.select_slider("quality", options=[0.25, 0.5, 1.0], value=1.0)
    cmd += f" --quality {quality}"

if repeat:=st.checkbox("repeat"):
    samples = st.slider("repeat", 2, 40, 2)
    cmd += f" --repeat {samples}"

st.code(cmd)
