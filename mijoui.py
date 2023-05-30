import pyperclip
import streamlit as st

st.title("mijoui")

prompt = st.text_area("prompt", "")
cmd = [prompt]

col1, col2 = st.columns(2)
with col1:
    if neg_prompt := st.text_area("negative prompt", ""):
        cmd.append(f"--no {neg_prompt}")


with col2:
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

    ar = st.text_input(
        "aspect ratio",
        label_visibility="collapsed",
        placeholder="aspect ratio",
    )
    if ar:
        cmd.append(f"--ar {ar}")

if model_version != "niji 5":
    cmd.append(f"--version {model_version}")
else:
    cmd.append(f"--{model_version}")

with st.expander("Options"):
    col3, col4 = st.columns(2)

    with col3:
        if model_version == "niji 5":
            style = st.selectbox(
                "style", ["default", "cute", "expressive", "scenic"], 0
            )
            if style != "default":
                cmd.append(f"--style {style}")

        if model_version == 4:
            style = st.selectbox("style", ["4a", "4b", "4c"], 2)
            cmd.append(f"--style {style}")

        if model_version == 5.1:
            if st.checkbox("raw"):
                cmd.append("--style raw")

        if model_version in [1, 2, 3, 4, 5, 5.1]:
            if st.checkbox("tile"):
                cmd.append("--tile")

        repeat = st.checkbox("repeat")

    with col4:
        if repeat:
            samples = st.slider("repeat", 2, 40, 2)
            cmd.append(f"--repeat {samples}")

        if model_version in [4, 5, "niji 5"]:
            quality = st.radio(
                "quality",
                (0.25, 0.5, 1),
                horizontal=True,
                index=2,
            )
            if quality != 1:
                cmd.append(f"--quality {quality}")

    if model_version in [4, 5, 5.1, "niji 5"]:
        stylize = st.slider("stylize", 0, 1000, 100)
        if stylize != 100:
            cmd.append(f"--stylize {stylize}")

    if model_version in [4, 5, 5.1, "niji 5"]:
        chaos = st.slider("chaos", 0, 100, 0)
        if chaos != 0:
            cmd.append(f"--chaos {chaos}")

    stop = st.slider("stop", 0, 100, 100)
    if stop != 100:
        cmd.append(f"--stop {stop}")

col5, col6 = st.columns(2)

with col5:
    seed = st.text_input("seed", label_visibility="collapsed", placeholder="seed")
    if seed:
        cmd.append(f"--seed {max(min(int(seed), 4294967295), 0)}")

with col6:
    iw = st.text_input(
        "image weight",
        label_visibility="collapsed",
        placeholder="image weight",
    )
    if iw and iw != 0.25:
        cmd.append(f"--iw {max(min(1.0, float(iw)), 0.0)}")

st.code("\n  ".join(cmd))

if st.button("Copy", type="secondary"):
    pyperclip.copy(" ".join(cmd))
