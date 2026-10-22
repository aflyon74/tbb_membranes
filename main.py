import numpy as np
import pandas as pd
import streamlit as st

st.set_page_config(layout="wide")
st.title("Team Bath Biodevices: Membrane Testing App")

tab_controls, tab_charts = st.tabs(["Environmental Parameters", "Analysis"])

# =====================================================
# Tab 1: parameters
# =====================================================
with tab_controls:
    left, right = st.columns(2)

    # ---------- Left: sliders ----------
    with left:
        with st.container(border=True):
            st.header("Controls")

            st.subheader("System operating pressure")
            system_operating_pressure = st.slider(
                "System operating pressure (bar)", min_value=0.0, max_value=6.0, value=3.0, step=0.1
            )

            st.subheader("Cross-flow velocity")
            cross_flow_velocity = st.slider(
                "Cross-flow velocity (m/s)", min_value=0.5, max_value=2.5, value=1.5, step=0.1
            )

            st.subheader("Membrane flux")
            membrane_flux = st.slider(
                "Membrane flux (LMH)", min_value=30, max_value=50, value=40
            )

            st.subheader("Fluid temperature")
            fluid_temperature = st.slider(
                "Fluid temperature (°C)", min_value=5, max_value=25, value=15
            )

            st.subheader("Valve openings")
            valve_opening = st.slider(
                "Valve opening (°)", min_value=0, max_value=90, value=45
            )

            st.subheader("Transducer pressure")
            transducer_pressure = st.slider(
                "Transducer pressure (bar)", min_value=0.0, max_value=6.0, value=3.0, step=0.1
            )

    # ---------- Right: current values ----------
    with right:
        with st.container(border=True):
            st.header("Current values")

            row1 = st.columns(3)
            row1[0].metric("System pressure", f"{system_operating_pressure:.1f} bar")
            row1[1].metric("Cross-flow velocity", f"{cross_flow_velocity:.1f} m/s")
            row1[2].metric("Membrane flux", f"{membrane_flux} LMH")

            row2 = st.columns(3)
            row2[0].metric("Fluid temperature", f"{fluid_temperature} °C")
            row2[1].metric("Valve opening", f"{valve_opening}°")
            row2[2].metric("Transducer pressure", f"{transducer_pressure:.1f} bar")

# =====================================================
# Tab 2: metals (placeholder data - replace with your own)
# =====================================================
with tab_charts:
    st.header("Sensor data visualisation")
    st.caption("Graphs from sensor data here")

    rng = np.random.default_rng(42)
    time = np.arange(0, 61, 5)  # minutes

    # Concentration over time (placeholder)
    conc = pd.DataFrame(
        {
            "Metal 1": 10 * np.exp(-time / 40) + rng.normal(0, 0.2, len(time)),
            "Metal 2": 7 * np.exp(-time / 25) + rng.normal(0, 0.2, len(time)),
            "Metal 3": 5 * np.exp(-time / 60) + rng.normal(0, 0.2, len(time)),
        },
        index=pd.Index(time, name="Time (min)"),
    )

    # Rejection per metal (placeholder)
    rejection = pd.DataFrame(
        {"Rejection (%)": [92.0, 85.5, 78.0]},
        index=["Metal 1", "Metal 2", "Metal 3"],
    )

    # Cumulative removal over time (placeholder)
    cumulative = (10 - conc).clip(lower=0)

    c1, c2, c3 = st.columns(3)

    with c1:
        with st.container(border=True):
            st.subheader("Concentration over time")
            st.line_chart(conc, y_label="Concentration (mg/L)")

    with c2:
        with st.container(border=True):
            st.subheader("Rejection by metal")
            st.bar_chart(rejection, y_label="Rejection (%)")

    with c3:
        with st.container(border=True):
            st.subheader("Cumulative removal")
            st.area_chart(cumulative, y_label="Removed (mg/L)")