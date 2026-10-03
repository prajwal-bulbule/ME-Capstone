# -*- coding: utf-8 -*-
"""
Generate LaTeX pages 31 to 40
"""
import os

pages_dir = os.path.join("latex", "pages")
os.makedirs(pages_dir, exist_ok=True)

# Page 31: 3.2 Solar Tracking Mechanism - Introduction (Numbered 23)
page_31 = r"""% ==============================================================================
% PAGE 31: 3.2 SOLAR TRACKING MECHANISM - INTRODUCTION (Numbered Page 23)
% ==============================================================================
\subsection*{3.2) SOLAR TRACKING MECHANISM :}

\begin{center}
  \includegraphics[width=45mm]{figures/fig15_solar_tracking_mechanism.jpg}
\end{center}

\subsubsection*{1. Introduction}
\noindent
\begin{spacing}{1.25}
{\fontsize{10.2}{15}\selectfont
The single-axis solar tracking mechanism is used to automatically rotate the parabolic dish from east to west to follow the sun's movement.\\[2.5mm]
It helps maintain maximum sunlight focus on the receiver throughout the day.\\[2.5mm]
The system works using LDR sensors, a PMDC motor, and a control circuit powered by solar energy.\\[2.5mm]
This automatic motion increases the overall efficiency and heat output of the solar water heater. It is a simple, low-cost, and effective method for improving solar energy utilization.
}
\end{spacing}
\clearpage
"""

# Page 32: Tracking Components & Working Principle (Numbered 24)
page_32 = r"""% ==============================================================================
% PAGE 32: TRACKING COMPONENTS & WORKING PRINCIPLE (Numbered Page 24)
% ==============================================================================
\subsubsection*{2. Type of Tracking}
\noindent
{\fontsize{10}{14}\selectfont
\textbf{Type:} Single Axis Automatic Tracking\\[1mm]
\textbf{Axis of Rotation:} East--West (horizontal axis)\\[1mm]
\textbf{Purpose:} To maintain continuous alignment of the parabolic dish with the moving sun during the day.\\[1mm]
\textbf{Control:} Automatic using sensors and motor.
}

\vspace{3mm}
\subsubsection*{3. Components of Single Axis Tracking System}
\begin{center}
\renewcommand{\arraystretch}{1.2}
\begin{tabular}{|p{42mm}|p{82mm}|}
\hline
\rowcolor{gray!20}
\textbf{Component} & \textbf{Specification / Function} \\
\hline
LDR Sensors (2 No.) & Detect sunlight intensity difference on both sides \\
\hline
Control Circuit / Comparator & Compares LDR signals and controls motor direction \\
\hline
PMDC Motor (6--9V, 10--15W) & Provides rotary motion for dish movement \\
\hline
Motor Driver (L293D / Relay) & Drives motor forward or reverse based on sensor input \\
\hline
V-Groove Belt \& Pulley (25 cm Pulley) & Transfers motion from motor to dish \\
\hline
Power Supply & 12V DC battery charged by small solar panel \\
\hline
Dish Support Frame & Allows rotation of dish around single horizontal axis \\
\hline
\end{tabular}
\end{center}

\vspace{2mm}
\subsubsection*{4. Working Principle}
\noindent
{\fontsize{10}{14}\selectfont
\textbf{$\blacklozenge$ Sensing Sunlight:}
\begin{itemize}[leftmargin=6mm, itemsep=1mm, label=\textbullet]
  \item Two LDR sensors are placed on either side of a small divider.
  \item When sunlight falls equally on both $\rightarrow$ system is balanced $\rightarrow$ motor off.
\end{itemize}
\textbf{$\blacklozenge$ Sun Movement:}
\begin{itemize}[leftmargin=6mm, itemsep=1mm, label=\textbullet]
  \item As the sun shifts from East to West, one LDR receives more light.
  \item The control circuit detects the difference in voltage between LDRs.
\end{itemize}
}
\clearpage
"""

# Page 33: Tracking Activation & Advantages (Numbered 25)
page_33 = r"""% ==============================================================================
% PAGE 33: TRACKING ACTIVATION & ADVANTAGES (Numbered Page 25)
% ==============================================================================
\noindent
{\fontsize{10.2}{14.5}\selectfont
\textbf{$\blacklozenge$ Motor Activation:}
\begin{itemize}[leftmargin=6mm, itemsep=1.5mm, label=\textbullet]
  \item The comparator or controller sends a signal to the motor driver.
  \item The PMDC motor rotates the dish toward the brighter side.
\end{itemize}

\vspace{2mm}
\textbf{$\blacklozenge$ Balancing:}
\begin{itemize}[leftmargin=6mm, itemsep=1.5mm, label=\textbullet]
  \item When both sensors receive equal light again, the motor stops.
  \item The dish stays aligned with the sun automatically.
\end{itemize}

\vspace{2mm}
\textbf{$\blacklozenge$ End of Day:}
\begin{itemize}[leftmargin=6mm, itemsep=1.5mm, label=\textbullet]
  \item The dish remains in the West position at sunset.
  \item It can be manually or automatically reset to the East in the morning.
\end{itemize}
}

\vspace{4mm}
\subsubsection*{5. Functions of Tracking Mechanism}
\begin{itemize}[leftmargin=8mm, itemsep=2mm, label=\textbullet]
  \item Continuously aligns the dish with the sun's position.
  \item Ensures maximum solar radiation is focused on the receiver.
  \item Eliminates need for manual adjustment.
  \item Increases water heating and overall system efficiency.
  \item Operates using solar power, making it self-sufficient.
\end{itemize}

\vspace{4mm}
\subsubsection*{6. Advantages}
\begin{itemize}[leftmargin=8mm, itemsep=2mm, label=\textbullet]
  \item Simple and cost-effective compared to dual-axis systems.
  \item Reduces human effort.
  \item Compact and energy-efficient.
  \item Ideal for small- to medium-size parabolic dish systems.
  \item Improves output by 20--30\% over fixed-position setup.
\end{itemize}
\clearpage
"""

# Page 34: Chapter-4 Fabrication - Part 1 (Numbered 26)
page_34 = r"""% ==============================================================================
% PAGE 34: CHAPTER-4 FABRICATION - PART 1 (Numbered Page 26)
% ==============================================================================
\begin{center}
  {\fontsize{15}{18}\selectfont \bfseries \textcolor{red!80!black}{\underline{CHAPTER-4}}}\\[2mm]
  {\fontsize{16}{20}\selectfont \bfseries \textcolor{red!80!black}{\underline{FABRICATION}}}\\[5mm]
\end{center}

\subsubsection*{1. Frame Construction}
\noindent
\begin{spacing}{1.2}
{\fontsize{10.2}{14.5}\selectfont
The base frame is made of wooden sheet ($60 \times 60$~cm) to provide stability and support to the setup. Holes are drilled to fix the shaft supports at the center.\\[2.5mm]
The frame is painted by white colour because it reflect solar rays to prevent electronic component from over heating.
}
\end{spacing}

\vspace{4mm}
\subsubsection*{2. Parabolic Dish Fabrication}
\noindent
\begin{spacing}{1.2}
{\fontsize{10.2}{14.5}\selectfont
A parabolic dish is made using satellite dish for lightweight and good reflection.\\[2.5mm]
The dish surface is covered with reflective mirror pieces to concentrate sunlight at the focus point. The dish is mounted on a PVC pipe shaft that allows rotational motion.
}
\end{spacing}

\vspace{4mm}
\subsubsection*{3. Receiver Fabrication}
\noindent
\begin{spacing}{1.2}
{\fontsize{10.2}{14.5}\selectfont
The receiver pipe (usually copper tube) is placed at the focal point of the parabola dish.\\[2.5mm]
The copper tube is black-painted for maximum heat absorption. The tube is connected with inlet and outlet pipes to circulate water.\\[2.5mm]
Copper tube is placed on the insulating material (aluminium plate and glass wool) for reducing heat loss.
}
\end{spacing}

\vspace{4mm}
\subsubsection*{4. Tracking Mechanism}
\noindent
\begin{spacing}{1.2}
{\fontsize{10.2}{14.5}\selectfont
A single-axis solar tracking system is used to follow the sun's motion east to west.\\[2.5mm]
A PMDC motor with pulley and V-belt attached with the PVC pipe shaft which is used to rotate the parabolic dish. Sensors (LDRs) are placed on both sides of the dish to detect sunlight intensity difference.\\[2.5mm]
A motor driver circuit and microcontroller (Arduino nano) control the motor rotation based on sensor signals.
}
\end{spacing}
\clearpage
"""

# Page 35: Fabrication - Part 2 (Numbered 27)
page_35 = r"""% ==============================================================================
% PAGE 35: FABRICATION - PART 2 (Numbered Page 27)
% ==============================================================================
\subsubsection*{5. Power Supplying Unit (Solar Panel \& Battery)}
\noindent
\begin{spacing}{1.2}
{\fontsize{10.2}{14.5}\selectfont
A small solar panel (12V) is mounted on the base frame or beside the dish.\\[2.5mm]
The panel converts sunlight into electrical energy to charge a 6V battery.\\[2.5mm]
The battery supplies power to the motor driver, sensors, and control circuit for automatic tracking.\\[2.5mm]
A blocking diode is used to ensure one-way current flow from the panel to the battery, preventing discharge at night.
}
\end{spacing}

\vspace{4mm}
\subsubsection*{6. Water Circulation System}
\noindent
\begin{spacing}{1.2}
{\fontsize{10.2}{14.5}\selectfont
Water from the storage tank which is placed at a certain height for direct flow of water to the inlet of receiver tube.\\[2.5mm]
Heated water exits from the outlet of the receiver tube and is collected in another container.
}
\end{spacing}

\vspace{4mm}
\subsubsection*{7. Assembly \& Testing}
\noindent
\begin{spacing}{1.2}
{\fontsize{10.2}{14.5}\selectfont
All components (frame, dish, receiver, motor, sensors, battery) are assembled.\\[2.5mm]
The system is tested under sunlight to check tracking accuracy and water temperature rise. Temperature readings are taken at regular intervals for performance analysis.
}
\end{spacing}

\vspace{4mm}
\subsubsection*{8. Finishing}
\noindent
\begin{spacing}{1.2}
{\fontsize{10.2}{14.5}\selectfont
Wiring is neatly arranged using cable ties.\\[2.5mm]
Components are painted or coated to prevent corrosion.\\[2.5mm]
Labels are added for inlet, outlet, and electrical parts for clarity.
}
\end{spacing}
\clearpage
"""

# Page 36: Chapter-5 Construction - Part 1 (Numbered 28)
page_36 = r"""% ==============================================================================
% PAGE 36: CHAPTER-5 CONSTRUCTION - PART 1 (Numbered Page 28)
% ==============================================================================
\begin{center}
  {\fontsize{15}{18}\selectfont \bfseries \textcolor{red!80!black}{\underline{CHAPTER-5}}}\\[2mm]
  {\fontsize{16}{20}\selectfont \bfseries \textcolor{red!80!black}{\underline{CONSTRUCTION}}}\\[4mm]
  \includegraphics[width=90mm]{figures/fig16_actual_model.jpg}\\[5mm]
\end{center}

\noindent
\begin{spacing}{1.2}
{\fontsize{10.2}{14.5}\selectfont
The construction of the Parabolic Solar Water Heater with Automatic Tracking and Power Generation begins with preparing a strong base structure. A wooden sheet of $60\text{ cm} \times 60\text{ cm}$ is used as the base platform to support all components. A PVC pipe shaft is mounted horizontally at the center of this base to act as the main support for the parabolic dish. The end caps are fitted at the end of the shaft to allow smooth rotational movement. The base and supporting parts are properly aligned, drilled, and painted with white colour to prevent damage of electronic components from sunlight. All joints are fixed using nuts, bolts, and adhesive for proper strength and balance.
}
\end{spacing}
\clearpage
"""

# Page 37: Construction - Part 2 (Numbered 29)
page_37 = r"""% ==============================================================================
% PAGE 37: CONSTRUCTION - PART 2 (Numbered Page 29)
% ==============================================================================
\noindent
\begin{spacing}{1.25}
{\fontsize{10.2}{14.5}\selectfont
The parabolic dish is then mounted on the top of the PVC shaft using a pulley and stud arrangement. The parabolic dish is made of satellite dish which is light in weight , and its surface is coated with reflective mirror pices to improve the reflection of sunlight. The shape of the dish is maintained accurately so that all reflected rays meet at one focal point. A copper tube painted in blackbody colour is fixed at this focal point using a supporting frame. This tube is connected with inlet and outlet pipes for water flow. To ensure smooth and stable rotation of the dish, a balancing weight is attached to the stud nut on the opposite side of the dish. This dead weight helps maintain proper balance of the parabolic reflector and prevents vibration or tilting during movement. The entire receiver assembly is held in place with metal nut \& bolts , and insulation material is added back side the tube to prevent heat loss.\\[4mm]
Next, the solar panel and battery system are installed on the same base frame. A 12V solar panel is fixed at a suitable angle to receive maximum sunlight. The panel output is connected to a 6V rechargeable battery through a charge controller. A PMDC motor is mounted on the base near to the shaft and connected to it using a V-belt and pulley arrangement of 25 cm diameter. Two LDR sensors are fixed on both sides of the parabolic dish, and all wiring between the panel, battery, sensors, and motor is neatly arranged using insulation tape and clips. After completing the assembly, the entire setup is checked for proper alignment, balance, and secure fitting of each component, ensuring the system is mechanically stable and ready for operation.
}
\end{spacing}
\clearpage
"""

# Page 38: Chapter-6 Programing - Part 1 (Numbered 30)
page_38 = r"""% ==============================================================================
% PAGE 38: CHAPTER-6 PROGRAMING - PART 1 (Numbered Page 30)
% ==============================================================================
\begin{center}
  {\fontsize{15}{18}\selectfont \bfseries \textcolor{red!80!black}{\underline{CHAPTER-6}}}\\[2mm]
  {\fontsize{16}{20}\selectfont \bfseries \textcolor{red!80!black}{\underline{PROGRAMING}}}\\[5mm]
\end{center}

\begin{lstlisting}[language=C++]
#define east_button_pin 2 
#define west_button_pin 3

int motr1 = 4; 
int motr2 = 5;

int eastLDR = 6; 
int westLDR = 7;

int eastLDRreading = 0; 
int westLDRreading = 0;

void setup(){ 
  pinMode(motr1, OUTPUT); 
  pinMode(motr2, OUTPUT);

  pinMode(east_button_pin, INPUT_PULLUP); 
  pinMode(west_button_pin, INPUT_PULLUP);

  pinMode(eastLDR, INPUT); 
  pinMode(westLDR, INPUT);

  digitalWrite(motr1, LOW); 
  digitalWrite(motr2, LOW);

  Serial.begin(9600);
  Serial.println("Design and Fabrication of Solar Air Heater With "); 
  Serial.println("Active Solar Tracking");
}
\end{lstlisting}
\clearpage
"""

# Page 39: Programing - Part 2 (Numbered 31)
page_39 = r"""% ==============================================================================
% PAGE 39: PROGRAMING - PART 2 (Numbered Page 31)
% ==============================================================================
\begin{lstlisting}[language=C++]
void motorButtoneast(){
  digitalWrite(motr1, LOW); 
  digitalWrite(motr2, HIGH); 
  delay(2000); 
  digitalWrite(motr1, LOW); 
  digitalWrite(motr2, LOW); 
  delay(1500);
}

void motorButtonwest(){
  digitalWrite(motr1, HIGH); 
  digitalWrite(motr2, LOW); 
  delay(2000); 
  digitalWrite(motr1, LOW); 
  digitalWrite(motr2, LOW); 
  delay(1500);
}

void motorLDReast(){
  digitalWrite(motr1, LOW); 
  digitalWrite(motr2, HIGH); 
  delay(2000); 
  digitalWrite(motr1, LOW); 
  digitalWrite(motr2, LOW); 
  delay(1500);
}
\end{lstlisting}
\clearpage
"""

# Page 40: Programing - Part 3 (Numbered 32)
page_40 = r"""% ==============================================================================
% PAGE 40: PROGRAMING - PART 3 (Numbered Page 32)
% ==============================================================================
\begin{lstlisting}[language=C++]
void motorLDRwest(){
  digitalWrite(motr1, HIGH); 
  digitalWrite(motr2, LOW); 
  delay(2000); 
  digitalWrite(motr1, LOW); 
  digitalWrite(motr2, LOW); 
  delay(1500);
}

void motorStop(){
  digitalWrite(motr1, LOW); 
  digitalWrite(motr2, LOW);
}

void loop(){
  byte east_button_state = digitalRead(east_button_pin); 
  byte west_button_state = digitalRead(west_button_pin);

  eastLDRreading = digitalRead(eastLDR); 
  westLDRreading = digitalRead(westLDR);

  Serial.print(" East = "); 
  Serial.println(eastLDRreading); 
  Serial.print(" West = "); 
  Serial.println(westLDRreading); 
  Serial.println(" ");
\end{lstlisting}
\clearpage
"""

with open(os.path.join(pages_dir, "page_31.tex"), "w", encoding="utf-8") as f: f.write(page_31)
with open(os.path.join(pages_dir, "page_32.tex"), "w", encoding="utf-8") as f: f.write(page_32)
with open(os.path.join(pages_dir, "page_33.tex"), "w", encoding="utf-8") as f: f.write(page_33)
with open(os.path.join(pages_dir, "page_34.tex"), "w", encoding="utf-8") as f: f.write(page_34)
with open(os.path.join(pages_dir, "page_35.tex"), "w", encoding="utf-8") as f: f.write(page_35)
with open(os.path.join(pages_dir, "page_36.tex"), "w", encoding="utf-8") as f: f.write(page_36)
with open(os.path.join(pages_dir, "page_37.tex"), "w", encoding="utf-8") as f: f.write(page_37)
with open(os.path.join(pages_dir, "page_38.tex"), "w", encoding="utf-8") as f: f.write(page_38)
with open(os.path.join(pages_dir, "page_39.tex"), "w", encoding="utf-8") as f: f.write(page_39)
with open(os.path.join(pages_dir, "page_40.tex"), "w", encoding="utf-8") as f: f.write(page_40)

print("Generated pages 31 to 40 successfully.")
