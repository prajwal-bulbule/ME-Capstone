# Capstone Project Thesis - LaTeX Conversion

**Title:** DESIGN AND FABRICATION OF PARABOLIC WATER HEATER WITH SOLAR TRACKING AND POWER GENERATION  
**Institution:** Government Polytechnic, Amravati (Autonomous Institute of Government of Maharashtra)  
**Department:** Department of Mechanical Engineering (2025–2026)  
**Course:** ME7501 - Capstone Project  
**Author / Candidate:** Mr. Amay P. Kadam (23ME044) & Team  
**Guide:** Prof. A. R. Bansali  

---

## Directory Structure

```text
latex/
├── main.tex                    # Master modular driver LaTeX file
├── thesis_complete.tex         # Monolithic single-file LaTeX source (ideal for Overleaf)
├── figures/                    # High-resolution extracted figures & diagrams
│   ├── gpa_logo.png            # Institute emblem
│   ├── fig1_parabolic_dish.jpg
│   ├── fig_design_parameters.jpg
│   ├── fig2_receiver.jpg
│   ├── fig3_cold_water_storage_tank.jpg
│   ├── fig4_water_supply_pipe.jpg
│   ├── fig5_flow_control_valve.jpg
│   ├── fig6_arduino_nano.jpg
│   ├── fig7_motor_driver.jpg
│   ├── fig8_ldr_sensor_module.jpg
│   ├── fig8b_ldr_dual_module.jpg
│   ├── fig9_push_buttons.jpg
│   ├── fig10_pmdc_motor.jpg
│   ├── fig11_v_groove_belt_pulley.jpg
│   ├── fig12_battery.jpg
│   ├── fig13_solar_panel_unit.jpg
│   ├── fig14_wooden_base_assembly.jpg
│   ├── fig15_solar_tracking_mechanism.jpg
│   └── fig16_actual_model.jpg
└── pages/                      # 48 Individual Page LaTeX Files
    ├── page_01.tex             # Outer Cover Page (Black & Gold)
    ├── page_02.tex             # Submission Title Page
    ├── page_03.tex             # Capstone Project Certificate
    ├── page_04.tex             # Vision & Mission Statements
    ├── page_05.tex             # PEOs, POs, PSOs
    ├── page_06.tex             # Declaration & Student Signatures Table
    ├── page_07.tex             # Acknowledgement
    ├── page_08.tex             # Technical Abstract
    ├── page_09.tex             # Index / Table of Contents (Numbered Page 1)
    ├── page_10.tex             # List of Figures (Numbered Page 2)
    ├── page_11.tex             # Chapter 1: Introduction - Overview & Need (Page 3)
    ├── page_12.tex             # Chapter 1: Objectives 1 to 12 (Page 4)
    ├── page_13.tex             # Chapter 2: Literature Review (Page 5)
    ├── page_14.tex             # Chapter 2: Literature Summary Table (Page 6)
    ├── page_15.tex             # Chapter 3: Methodology - Parabolic Dish (Page 7)
    ├── page_16.tex             # Chapter 3: Design Parameters Diagram & Data (Page 8)
    ├── page_17.tex             # Chapter 3: Receiver Copper Coil (Page 9)
    ├── page_18.tex             # Chapter 3: Cold Water Storage Tank (Page 10)
    ├── page_19.tex             # Chapter 3: Water Supply Pipe (Page 11)
    ├── page_20.tex             # Chapter 3: Flow Control Valve (Page 12)
    ├── page_21.tex             # Chapter 3: Arduino Nano Microcontroller (Page 13)
    ├── page_22.tex             # Chapter 3: L298N Motor Driver Unit (Page 14)
    ├── page_23.tex             # Chapter 3: LDR Sensor Module (Page 15)
    ├── page_24.tex             # Chapter 3: Push Buttons (Page 16)
    ├── page_25.tex             # Chapter 3: PMDC Motor Specifications (Page 17)
    ├── page_26.tex             # Chapter 3: V-Groove Belt and Pulley (Page 18)
    ├── page_27.tex             # Chapter 3: Belt and Pulley Functions (Page 19)
    ├── page_28.tex             # Chapter 3: VRLA Battery (Page 20)
    ├── page_29.tex             # Chapter 3: Solar Panel Unit & Diode (Page 21)
    ├── page_30.tex             # Chapter 3: Wooden Base & PVC Shaft (Page 22)
    ├── page_31.tex             # Chapter 3: Solar Tracking Mechanism (Page 23)
    ├── page_32.tex             # Chapter 3: Tracking Components & Principle (Page 24)
    ├── page_33.tex             # Chapter 3: Tracking Activation & Advantages (Page 25)
    ├── page_34.tex             # Chapter 4: Fabrication Part 1 (Page 26)
    ├── page_35.tex             # Chapter 4: Fabrication Part 2 (Page 27)
    ├── page_36.tex             # Chapter 5: Construction - Actual Model (Page 28)
    ├── page_37.tex             # Chapter 5: Construction Details & Balancing (Page 29)
    ├── page_38.tex             # Chapter 6: Arduino Code - Pin Setup (Page 30)
    ├── page_39.tex             # Chapter 6: Arduino Code - Motor Routines (Page 31)
    ├── page_40.tex             # Chapter 6: Arduino Code - Sensor Loop (Page 32)
    ├── page_41.tex             # Chapter 6: Arduino Code - Tracking Logic (Page 33)
    ├── page_42.tex             # Chapter 7: Working Principle & Thermal Operation (Page 34)
    ├── page_43.tex             # Chapter 8: Advantages (15 Points) (Page 35)
    ├── page_44.tex             # Chapter 9: Applications (15 Points) (Page 36)
    ├── page_45.tex             # Chapter 10: Cost Estimation Table Part 1 (Page 37)
    ├── page_46.tex             # Chapter 10: Cost Estimation Table Part 2 & Total (Page 38)
    ├── page_47.tex             # Chapter 11: Conclusion (Page 39)
    └── page_48.tex             # Chapter 12: References (5 Papers) (Page 40)
```

---

## How to Compile

### 1. In Overleaf
1. Create a new blank project on [Overleaf](https://www.overleaf.com).
2. Upload the `figures/` folder and `thesis_complete.tex` (or the whole `latex/` folder with `main.tex` and `pages/`).
3. Set the compiler to **pdfLaTeX** or **XeLaTeX**.
4. Click **Recompile**.

### 2. Locally using TeX Live, MiKTeX, or MacTeX
Run the following terminal command from the `latex` directory:
```bash
pdflatex -interaction=nonstopmode main.tex
pdflatex -interaction=nonstopmode main.tex
```
or with the monolithic file:
```bash
pdflatex -interaction=nonstopmode thesis_complete.tex
```

---

## Key Design Features

1. **Page-by-Page Fidelity:** Exactly reproduces all 48 pages of the original thesis document.
2. **Page Numbering Alignment:** Preliminary pages (Cover, Certificate, Vision/Mission, Declaration, Acknowledgement, Abstract) have suppressed numbers, while Index starts at `~ 1 ~` and continues to References at `~ 40 ~`, exactly matching the original document structure.
3. **Double Page Border:** Clean black border for all technical chapters and decorative gold borders for the preliminary pages.
4. **Complete Figures Included:** All 17 figures from the thesis were extracted at native resolution and referenced cleanly.
5. **Code Syntax Highlighting:** Embedded Arduino C++ source code is typeset using the `listings` package with syntax highlighting and clear background styling.
6. **Professional Tables:** Cost estimation, literature survey, declaration members, and tracking components are rendered with clean borders and header shading.
