# -*- coding: utf-8 -*-
"""
Generate LaTeX pages 41 to 48
"""
import os

pages_dir = os.path.join("latex", "pages")
os.makedirs(pages_dir, exist_ok=True)

# Page 41: Programing - Part 4 (Numbered 33)
page_41 = r"""% ==============================================================================
% PAGE 41: PROGRAMING - PART 4 (Numbered Page 33)
% ==============================================================================
\begin{lstlisting}[language=C++]
  if (east_button_state == LOW){ 
    Serial.println("East Button Is Pressed"); 
    motorButtoneast(); 
  } 
  else 
    motorStop(); 

  if (west_button_state == LOW){ 
    Serial.println("West Button Is Pressed"); 
    motorButtonwest(); 
  } 
  else 
    motorStop(); 

  if (eastLDRreading > westLDRreading){ 
    motorLDReast(); 
  } 
  else 
    motorStop(); 

  if (eastLDRreading < westLDRreading){ 
    motorLDRwest(); 
  } 
  else 
    motorStop(); 

  if (eastLDRreading == westLDRreading){ 
    motorStop(); 
  } 
}
\end{lstlisting}
\clearpage
"""

# Page 42: Chapter-7 Working (Numbered 34)
page_42 = r"""% ==============================================================================
% PAGE 42: CHAPTER-7 WORKING (Numbered Page 34)
% ==============================================================================
\begin{center}
  {\fontsize{15}{18}\selectfont \bfseries \textcolor{red!80!black}{\underline{CHAPTER-7}}}\\[2mm]
  {\fontsize{16}{20}\selectfont \bfseries \textcolor{red!80!black}{\underline{WORKING}}}\\[5mm]
\end{center}

\noindent
\begin{spacing}{1.2}
{\fontsize{10}{14}\selectfont
The working of the Parabolic Solar Water Heater with Automatic Tracking and Power Generation is based on the principle of solar energy concentration and automatic solar tracking. The parabolic dish collects and focuses sunlight onto a single focal point. The surface of the dish is covered with mirror pieces, which act as reflective material to direct the sunlight accurately toward the center. A black-painted copper receiver tube is fixed at this focal point to absorb the maximum heat. When water passes through the receiver tube, it gains thermal energy from the concentrated solar rays, causing a steady rise in its temperature. The setup ensures that maximum solar radiation is utilized for heating the water efficiently.\\[3.5mm]
The automatic solar tracking mechanism allows the parabolic dish to continuously face the sun from morning to evening. Two Light Dependent Resistors (LDRs) are mounted on opposite sides of the dish and connected to the control circuit. These sensors detect the difference in sunlight intensity between the two sides. When one sensor receives more light, the control circuit sends a signal to the microcontroller and with help of motor driver motor is start rotating, which rotates the dish slightly---about 4 to 5 degrees at a time---until both LDRs receive equal sunlight. This gradual movement keeps the dish properly aligned with the sun throughout the day, maintaining the correct focus on the receiver and improving overall heat absorption efficiency.\\[3.5mm]
The electrical power system of the project operates through a 6V solar-powered battery. A solar panel converts sunlight into electrical energy and charges the 6V battery via a charge controller. The stored electrical energy is used to power the PMDC motor, LDR sensors, and the motor driver circuit for automatic tracking. A blocking diode is used in the circuit to allow one-way current flow, preventing reverse discharge of the battery at night. The combined operation of the solar panel, battery, sensors, and motor ensures that the system runs automatically without manual adjustment. Thus, the parabolic solar heater continuously tracks the sun, heats the water efficiently, and uses clean solar energy both for heating and for controlling its own movement.
}
\end{spacing}
\clearpage
"""

# Page 43: Chapter-8 Advantages (Numbered 35)
page_43 = r"""% ==============================================================================
% PAGE 43: CHAPTER-8 ADVANTAGES (Numbered Page 35)
% ==============================================================================
\begin{center}
  {\fontsize{15}{18}\selectfont \bfseries \textcolor{red!80!black}{\underline{CHAPTER-8}}}\\[2mm]
  {\fontsize{16}{20}\selectfont \bfseries \textcolor{red!80!black}{\underline{ADVANTAGES}}}\\[6mm]
\end{center}

\begin{spacing}{1.25}
{\fontsize{10.5}{14.5}\selectfont
\begin{enumerate}[leftmargin=8mm, itemsep=2.2mm]
  \item Uses free and renewable solar energy.
  \item Reduces electricity bills.
  \item Eco-friendly and pollution-free operation.
  \item Provides hot water without fossil fuels.
  \item Easy to operate and maintain.
  \item Increases efficiency through solar tracking.
  \item Works even in remote areas without grid power.
  \item Reduces dependency on conventional energy sources.
  \item Compact and cost-effective design.
  \item Provides both heating and power generation.
  \item Promotes the use of clean energy technology.
  \item Suitable for domestic and industrial use.
  \item Helps conserve non-renewable energy resources.
  \item Encourages awareness of solar energy applications.
  \item Long service life with low running cost.
\end{enumerate}
}
\end{spacing}
\clearpage
"""

# Page 44: Chapter-9 Applications (Numbered 36)
page_44 = r"""% ==============================================================================
% PAGE 44: CHAPTER-9 APPLICATIONS (Numbered Page 36)
% ==============================================================================
\begin{center}
  {\fontsize{15}{18}\selectfont \bfseries \textcolor{red!80!black}{\underline{CHAPTER-9}}}\\[2mm]
  {\fontsize{16}{20}\selectfont \bfseries \textcolor{red!80!black}{\underline{APPLICATIONS}}}\\[6mm]
\end{center}

\begin{spacing}{1.25}
{\fontsize{10.5}{14.5}\selectfont
\begin{enumerate}[leftmargin=8mm, itemsep=2.2mm]
  \item Domestic water heating for homes.
  \item Solar cooking and food preparation.
  \item Water heating for hostels, hospitals, and hotels.
  \item Steam generation for small-scale industries.
  \item Laundry and cleaning operations needing hot water.
  \item Solar-powered water distillation systems.
  \item Dairy processing (milk pasteurization, cleaning, etc.).
  \item Power generation for small electrical appliances.
  \item Agricultural drying and greenhouse heating.
  \item Community solar kitchens and canteens.
  \item Heating water for swimming pools.
  \item Solar-based desalination plants.
  \item Boiler feed water preheating in industries.
  \item Educational and research purposes in renewable energy studies.
  \item Emergency water heating in off-grid or remote locations.
\end{enumerate}
}
\end{spacing}
\clearpage
"""

# Page 45: Chapter-10 Cost Estimation - Part 1 (Numbered 37)
page_45 = r"""% ==============================================================================
% PAGE 45: CHAPTER-10 COST ESTIMATION - PART 1 (Numbered Page 37)
% ==============================================================================
\begin{center}
  {\fontsize{15}{18}\selectfont \bfseries \textcolor{red!80!black}{\underline{CHAPTER-10}}}\\[2mm]
  {\fontsize{16}{20}\selectfont \bfseries \textcolor{red!80!black}{\underline{COST ESTIMATION}}}\\[5mm]
\end{center}

\begin{center}
\renewcommand{\arraystretch}{1.22}
\begin{tabular}{|c|p{45mm}|c|p{35mm}|c|}
\hline
\rowcolor{gray!20}
\textbf{Sr. No.} & \multicolumn{1}{c|}{\textbf{Components}} & \textbf{QYT} & \multicolumn{1}{c|}{\textbf{Materials}} & \textbf{Cost (Rs)} \\
\hline
1. & Parabola dish & 1 & Mild Steel & 600 \\
\hline
2. & Wooden Base & 1 & MDF Sheet & 650 \\
\hline
3. & Mirror Pieces & 2500 & Mirror & 400 \\
\hline
4. & Copper Tube & 1 & copper & 450 \\
\hline
5. & PVC Pipe \& Iron Rod & 1 (Each) & PVC \& Iron & 350 \\
\hline
6. & End Caps & 2 & PVC & 50 \\
\hline
7. & Arduino Nano, Motor Driver, Push Buttons (2), LDR Sensors (2) \& Wires & Set & -- & 1000 \\
\hline
8. & PMDC Motor & 1 & -- & 150 \\
\hline
9. & Battery & 1 & Lead Acid & 400 \\
\hline
10. & Stud Nut, Nut \& Bolt & Set & Iron & 150 \\
\hline
11. & Dead Weight & 1 & Ceramic & 50 \\
\hline
12. & Pulley (25cm \& 5cm) diameter & 1 (Each) & Fiber and Brass & 75 \\
\hline
13. & Supply Pipes (5mm \& 10mm) & 1 (Each) & Polyethylene \& Synthetic & 100 \\
\hline
14. & Paint and Insulation & Set & Body Paint \& Aluminium Sheet & 200 \\
\hline
\end{tabular}
\end{center}
\clearpage
"""

# Page 46: Cost Estimation - Part 2 (Numbered 38)
page_46 = r"""% ==============================================================================
% PAGE 46: COST ESTIMATION - PART 2 (Numbered Page 38)
% ==============================================================================
\vspace*{10mm}
\begin{center}
\renewcommand{\arraystretch}{1.35}
\begin{tabular}{|c|p{45mm}|c|p{35mm}|c|}
\hline
\rowcolor{gray!20}
\textbf{Sr. No.} & \multicolumn{1}{c|}{\textbf{Components}} & \textbf{QYT} & \multicolumn{1}{c|}{\textbf{Materials}} & \textbf{Cost (Rs)} \\
\hline
15. & Special Glue & 4 & -- & 400 \\
\hline
16. & Labour Cost & -- & -- & 1000 \\
\hline
17. & Auto & -- & -- & 700 \\
\hline
18. & Waste Material & -- & -- & 275 \\
\hline
\rowcolor{gray!15}
\multicolumn{4}{|r|}{\textbf{TOTAL}} & \textbf{7000 RS} \\
\hline
\end{tabular}
\end{center}
\clearpage
"""

# Page 47: Chapter-11 Conclusion (Numbered 39)
page_47 = r"""% ==============================================================================
% PAGE 47: CHAPTER-11 CONCLUSION (Numbered Page 39)
% ==============================================================================
\begin{center}
  {\fontsize{15}{18}\selectfont \bfseries \textcolor{red!80!black}{\underline{CHAPTER-11}}}\\[2mm]
  {\fontsize{16}{20}\selectfont \bfseries \textcolor{red!80!black}{\underline{CONCLUSION}}}\\[6mm]
\end{center}

\noindent
\begin{spacing}{1.25}
{\fontsize{10.2}{15}\selectfont
The designed parabolic solar water heater successfully utilizes solar energy for water heating and small-scale power generation.\\[3mm]
The use of a parabolic dish with mirror pieces ensures effective concentration of sunlight on the receiver tube.\\[3mm]
The automatic single-axis tracking system increases the efficiency by keeping the dish aligned with the sun throughout the day.\\[3mm]
A 6V DC motor controlled by LDR sensors enables gradual rotation of about 4--5 degrees per movement for accurate tracking.\\[3mm]
The generated heat is stored in water, providing a renewable and eco-friendly source of energy.\\[3mm]
The attached solar panel also generates power to charge the 6V battery used for operating the tracking system.\\[3mm]
This project demonstrates the practical use of solar energy in both heating and automation applications.\\[3mm]
The system design is simple, cost-effective, and suitable for domestic and educational purposes.\\[3mm]
It helps in reducing dependence on conventional energy sources and promotes sustainable technology.\\[3mm]
Overall, the project meets its objectives of energy conservation, automation, and efficient solar energy utilization.
}
\end{spacing}
\clearpage
"""

# Page 48: Chapter-12 References (Numbered 40)
page_48 = r"""% ==============================================================================
% PAGE 48: CHAPTER-12 REFERENCES (Numbered Page 40)
% ==============================================================================
\begin{center}
  {\fontsize{15}{18}\selectfont \bfseries \textcolor{red!80!black}{\underline{CHAPTER-12}}}\\[2mm]
  {\fontsize{16}{20}\selectfont \bfseries \textcolor{red!80!black}{\underline{REFERANCES}}}\\[6mm]
\end{center}

\noindent
\begin{spacing}{1.3}
{\fontsize{10.2}{15}\selectfont
``Design and Fabrication of Parabolic Solar Water Heater with Inbuilt Automatic Solar Tracking System.'' Available at:\\[1mm]
\url{https://ijirt.org/article?manuscript=159489}\\[4mm]
``Design Parameters of Parabolic Solar Water Heater with Inbuilt Automatic Solar Tracking System.'' Available at:\\[1mm]
\url{https://www.ijraset.com/research-paper/design-parameters-of-parabolic-solar-water-heater-with-inbuilt-automatic-solar-tracking-system}\\[4mm]
``Design \& Fabrication of Solar Tracking System.'' Available at:\\[1mm]
\url{https://ijrpr.com/uploads/V3ISSUE5/IJRPR3843.pdf}\\[4mm]
``Design and Fabrication of an Automatic Dual Axis Solar Tracker by Using LDR Sensors.'' Available at:\\[1mm]
\url{https://api.semanticscholar.org/CorpusID:113706763}\\[4mm]
``Design of Automatic Tracking Solar Dish with Integrated Panels \& IoT-Based Control.'' Available at:\\[1mm]
\url{https://ijnrd.org/papers/IJNRD2410259.pdf}
}
\end{spacing}
\clearpage
"""

with open(os.path.join(pages_dir, "page_41.tex"), "w", encoding="utf-8") as f: f.write(page_41)
with open(os.path.join(pages_dir, "page_42.tex"), "w", encoding="utf-8") as f: f.write(page_42)
with open(os.path.join(pages_dir, "page_43.tex"), "w", encoding="utf-8") as f: f.write(page_43)
with open(os.path.join(pages_dir, "page_44.tex"), "w", encoding="utf-8") as f: f.write(page_44)
with open(os.path.join(pages_dir, "page_45.tex"), "w", encoding="utf-8") as f: f.write(page_45)
with open(os.path.join(pages_dir, "page_46.tex"), "w", encoding="utf-8") as f: f.write(page_46)
with open(os.path.join(pages_dir, "page_47.tex"), "w", encoding="utf-8") as f: f.write(page_47)
with open(os.path.join(pages_dir, "page_48.tex"), "w", encoding="utf-8") as f: f.write(page_48)

print("Generated pages 41 to 48 successfully.")
