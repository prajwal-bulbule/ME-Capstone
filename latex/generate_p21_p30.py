# -*- coding: utf-8 -*-
"""
Generate LaTeX pages 21 to 30
"""
import os

pages_dir = os.path.join("latex", "pages")
os.makedirs(pages_dir, exist_ok=True)

# Page 21: 6) Arduino Nano (Numbered 13)
page_21 = r"""% ==============================================================================
% PAGE 21: 6) ARDUINO NANO (Numbered Page 13)
% ==============================================================================
\subsubsection*{6) ARDUINO NANO}

\begin{center}
  \includegraphics[width=65mm]{figures/fig6_arduino_nano.jpg}
\end{center}

\noindent
\begin{spacing}{1.2}
{\fontsize{10.2}{14.5}\selectfont
The Arduino Nano is a compact, microcontroller-based development board used as the main control unit in the solar tracking system of this project. It is responsible for processing the signals received from the Light Dependent Resistors (LDRs) and controlling the PMDC motor through the motor driver module, ensuring that the parabolic collector continuously follows the Sun's position throughout the day.\\[3.5mm]
\textbf{Function:}
\begin{itemize}[leftmargin=8mm, itemsep=2mm, label=\textbullet]
  \item Two LDR sensors are mounted on opposite sides of the collector.
  \item When sunlight intensity Differs between the two sensors, the Arduino Nano detects the voltage difference.
  \item It sends a control signal to the motor driver circuit, which activates the PMDC motor to rotate the collector toward the brighter side (toward the Sun).
  \item Once both LDRs sense equal light, the Arduino stops the motor --- meaning the collector is correctly aligned with the Sun.
\end{itemize}
}
\end{spacing}
\clearpage
"""

# Page 22: 7) Motor Driver Unit (Numbered 14)
page_22 = r"""% ==============================================================================
% PAGE 22: 7) MOTOR DRIVER UNIT (Numbered Page 14)
% ==============================================================================
\subsubsection*{7) MOTOR DRIVER UNIT}

\begin{center}
  \includegraphics[width=55mm]{figures/fig7_motor_driver.jpg}
\end{center}

\noindent
\begin{spacing}{1.2}
{\fontsize{10.2}{14.5}\selectfont
The motor driver unit used in my project is an L298N motor driver module, which is designed to control the speed and direction of a Permanent Magnet DC (PMDC) motor. It acts as an interface between the microcontroller and the motor because a microcontroller cannot supply the high current required by the motor. The L298N is a dual H-bridge motor driver IC that can control two PMDC motors or one stepper motor. It operates using an external power supply (usually 5V--35V) and provides sufficient current (up to 2A per channel) to drive the motors efficiently.\\[3.5mm]
\textbf{Function:}
\begin{itemize}[leftmargin=8mm, itemsep=2mm, label=\textbullet]
  \item The motor driver works on the H-bridge principle, which allows the motor to rotate in both forward and reverse directions.
  \item When control signals from the microcontroller are applied to the input pins, the driver sends the proper polarity of voltage to the motor terminals.
  \item By changing the logic of the inputs, the direction of current through the motor changes, which changes the rotation direction.
  \item The enable pins control the motor speed using Pulse Width Modulation (PWM) signals.
  \item Thus, the L298N motor driver helps to easily control the speed and direction of a PMDC motor in the project.
\end{itemize}
}
\end{spacing}
\clearpage
"""

# Page 23: 8) LDR Sensor Module (Numbered 15)
page_23 = r"""% ==============================================================================
% PAGE 23: 8) LDR SENSOR MODULE (Numbered Page 15)
% ==============================================================================
\subsubsection*{8) LDR SENSOR MODULE (Light Detection Unit)}

\begin{center}
  \begin{tabular}{cc}
    \includegraphics[width=48mm]{figures/fig8_ldr_sensor_module.jpg} &
    \includegraphics[width=42mm]{figures/fig8b_ldr_dual_module.jpg}
  \end{tabular}
\end{center}

\noindent
\begin{spacing}{1.2}
{\fontsize{10.2}{14.5}\selectfont
The LDR (Light Dependent Resistor) sensor module is used in this project to detect the intensity of sunlight and provide input to the Arduino Nano for automatic solar tracking. It works on the principle that the resistance of an LDR changes with the intensity of light falling on it.\\[3.5mm]
\textbf{Function:}
\begin{itemize}[leftmargin=8mm, itemsep=2mm, label=\textbullet]
  \item Two LDR modules are placed at slightly different positions on the parabolic collector.
  \item When sunlight intensity is unequal between the two sensors, the resistance difference creates a voltage difference.
  \item This voltage difference is sent to the Arduino Nano, which processes the signal.
  \item The Arduino then commands the motor driver to rotate the collector toward the side receiving less light, aligning it perfectly with the Sun.
  \item Once both LDRs sense equal sunlight, the system stops the motor --- indicating correct alignment.
\end{itemize}
}
\end{spacing}
\clearpage
"""

# Page 24: 9) Push Buttons (Numbered 16)
page_24 = r"""% ==============================================================================
% PAGE 24: 9) PUSH BUTTONS (Numbered Page 16)
% ==============================================================================
\subsubsection*{9) PUSH BUTTONS}

\begin{center}
  \includegraphics[width=65mm]{figures/fig9_push_buttons.jpg}
\end{center}

\noindent
\begin{spacing}{1.2}
{\fontsize{10.2}{14.5}\selectfont
Push button switches are used as control inputs to operate the motor's direction of rotation. These push buttons are simple, momentary-type switches that make or break an electrical connection when pressed. They are compact, easy to use, and reliable for controlling electronic circuits. Each button is connected to the control pins of the motor driver circuit, which in turn determines the motor's movement direction.\\[3.5mm]
\textbf{Function:}
\begin{itemize}[leftmargin=8mm, itemsep=2mm, label=\textbullet]
  \item There are two push buttons used in the project --- one for right (forward) rotation and the other for left (reverse) rotation of the PMDC motor.
  \item When the right push button is pressed, it sends a signal to the motor driver to rotate the motor in the forward direction.
  \item Similarly, pressing the left push button changes the signal polarity through the driver, causing the motor to rotate in the reverse direction.
  \item Once the button is released, the circuit opens, and the motor stops.
  \item This simple push button control allows easy and manual direction control of the motor.
\end{itemize}
}
\end{spacing}
\clearpage
"""

# Page 25: 9) PMDC Motor (Numbered 17)
page_25 = r"""% ==============================================================================
% PAGE 25: 9) PERMANENT MAGNET DIRECT CURRENT (PDMC) MOTOR (Numbered Page 17)
% ==============================================================================
\subsubsection*{9) PERMANENT MAGNET DIRECT CURRENT (PDMC) MOTOR}

\begin{center}
  \includegraphics[width=70mm]{figures/fig10_pmdc_motor.jpg}
\end{center}

\noindent
{\fontsize{10.5}{15}\selectfont
\textbf{Specifications}\\[1.5mm]
\textbf{Voltage:} 6V or 9V DC\\[1.5mm]
\textbf{Speed:} 100--300 RPM (depends on load)\\[1.5mm]
\textbf{Power:} 5--15 Watts\\[1.5mm]
\textbf{Control:} Easily reversible by changing polarity\\[3.5mm]
\textbf{Function}\\[2mm]
\textbf{1. Tracking Motion:}\\
The motor is used to rotate the dish (either horizontally or vertically) to follow the sun's movement throughout the day. It ensures maximum solar radiation is focused on the receiver.\\[2.5mm]
\textbf{2. Automatic Control:}\\
The motor operates through a motor driver and sensor system (like LDR sensors) that detect sunlight direction.\\[2.5mm]
\textbf{3. Power Source:}\\
It is powered by a battery or solar panel output, making the system self-sustainable.
}
\clearpage
"""

# Page 26: 10) V-Groove Belt and Pully (Numbered 18)
page_26 = r"""% ==============================================================================
% PAGE 26: 10) V-GROOVE BELT AND PULLY (Numbered Page 18)
% ==============================================================================
\subsubsection*{10) V-GROOVE BELT AND PULLY}

\begin{center}
  \includegraphics[width=48mm]{figures/fig11_v_groove_belt_pulley.jpg}
\end{center}

\noindent
\begin{spacing}{1.2}
{\fontsize{10.2}{14.5}\selectfont
\textbf{Specifications of V-Groove Belt and Pulley}
\begin{enumerate}[leftmargin=8mm, itemsep=2mm]
  \item Type of drive -- V-belt drive
  \item Belt type -- V-groove
  \item Belt material -- Reinforced rubber
  \item Belt length -- Around 600 mm to 800 mm
  \item Driven pulley diameter -- 25 cm (250 mm)
  \item Driver pulley diameter -- 5 cm to 10 cm (mounted on motor shaft)
  \item Speed ratio -- 1 : 2.5 to 1 : 5 (for speed reduction and torque increase)
  \item Driver pulley material -- Mild steel or aluminum alloy
  \item Driven pulley material -- Fiber
  \item Center distance between shafts -- 175 mm to 180 mm (adjustable)
\end{enumerate}
}
\end{spacing}
\clearpage
"""

# Page 27: Function of Belt and Pulley (Numbered 19)
page_27 = r"""% ==============================================================================
% PAGE 27: FUNCTION OF BELT AND PULLEY (Numbered Page 19)
% ==============================================================================
\subsubsection*{Function}
\vspace{3mm}

\noindent
\begin{spacing}{1.3}
{\fontsize{10.5}{15.5}\selectfont
\textbf{1. Power Transmission:}\\
The V-groove belt connects the PMDC motor to the dish rotation shaft via the 25 cm pulley. It transmits the rotational motion from the motor to the parabolic dish assembly.\\[4mm]
\textbf{2. Speed Reduction and Torque Increase:}\\
A larger pulley (25 cm) helps reduce speed and increase torque, which is ideal for slow and steady dish rotation.\\[4mm]
\textbf{3. Smooth and Silent Operation:}\\
The V-belt drive provides smooth, shock-free motion with minimal vibration and noise.\\[4mm]
\textbf{4. Protection Against Overload:}\\
If the dish is obstructed, the belt may slip slightly, protecting the motor from damage.\\[4mm]
\textbf{5. Easy Maintenance:}\\
Simple to install, adjust, and replace; no lubrication required.
}
\end{spacing}
\clearpage
"""

# Page 28: 10) Battery (Numbered 20)
page_28 = r"""% ==============================================================================
% PAGE 28: 10) BATTERY(6V,6AMP) (Numbered Page 20)
% ==============================================================================
\subsubsection*{10) BATERY(6V,6AMP)}

\begin{center}
  \includegraphics[width=55mm]{figures/fig12_battery.jpg}
\end{center}

\noindent
\begin{spacing}{1.2}
{\fontsize{10.2}{14.5}\selectfont
The system uses a Spice VRLA Battery (6V, 6Ah) made with graphene and carbon fiber technology. It is a sealed lead-acid, maintenance-free battery that provides stable DC power for operating the motor and sensors.\\[3mm]
\textbf{Main Specifications:}
\begin{itemize}[leftmargin=8mm, itemsep=1.5mm, label=\textbullet]
  \item \textbf{Type:} VRLA (Valve Regulated Lead Acid) Battery
  \item \textbf{Rated Voltage:} 6V
  \item \textbf{Capacity:} 6Ah
  \item \textbf{Charging Voltage:} 7.2V -- 7.5V (Cycle use)
  \item \textbf{Standby Voltage:} 6.78V -- 6.90V
  \item \textbf{Maximum Charging Current:} 1.35A
  \item \textbf{Features:} Maintenance-free, long service life, and safe sealed design
\end{itemize}
\vspace{2mm}
This battery ensures reliable power supply for small DC motors and electronic sensor circuits in the project.
}
\end{spacing}
\clearpage
"""

# Page 29: 11) Solar Panel Unit (Numbered 21)
page_29 = r"""% ==============================================================================
% PAGE 29: 11) SOLAR PANEL UNIT (Numbered Page 21)
% ==============================================================================
\subsubsection*{11) SOLAR PANEL UNIT}

\begin{center}
  \includegraphics[width=90mm]{figures/fig13_solar_panel_unit.jpg}
\end{center}

\noindent
\begin{spacing}{1.2}
{\fontsize{10.2}{14.5}\selectfont
A solar panel unit is used as the main source of electrical power generation. Each solar panel is capable of producing around 6 amperes of current, and when connected together in a suitable configuration, the entire system generates a total output voltage of about 10 to 12 volts. This generated DC power is used for charging the battery, which later supplies energy to the control and motor units of the system. Solar energy is a renewable and eco-friendly source, making the setup efficient and sustainable for long-term operation.\\[3mm]
To ensure safe operation, a diode is connected in the circuit to allow one-way power flow from the solar panels to the battery. This prevents the reverse flow of current, protecting the solar panels from short-circuiting or back current during low or no sunlight conditions. This arrangement helps maintain the reliability and safety of the charging system.
}
\end{spacing}
\clearpage
"""

# Page 30: 12) Wooden Base, PVC Pipe & Various Types of Nut (Numbered 22)
page_30 = r"""% ==============================================================================
% PAGE 30: 12) WOODEN BASE, PVC PIPE & VARIOUS TYPES OF NUT (Numbered Page 22)
% ==============================================================================
\subsubsection*{12) WOODEN BASE, PVC PIPE \& VARIOUS TYPES OF NUT}

\begin{center}
  \includegraphics[width=75mm]{figures/fig14_wooden_base_assembly.jpg}
\end{center}

\noindent
\begin{spacing}{1.2}
{\fontsize{10.2}{14.5}\selectfont
The stud rod is a fully threaded rod that provides adjustable connections using nuts and washers at both ends. Different types of nuts and bolts are used to fix and support various parts of the assembly securely. The PVC pipe acts as the main shaft, on which the pulley is mounted. This shaft transmits rotational motion from the motor to the parabolic dish, allowing smooth and stable operation.\\[3mm]
The motor and pulley arrangement are connected through a belt drive, which transfers torque efficiently to the PVC shaft. The base platform of size 60 $\times$ 60 cm is made from a wooden sheet, providing a strong and stable foundation for the entire setup. This design ensures that all components remain firmly in place during the operation and allows precise and balanced rotation of the parabolic dish for tracking or positioning purposes.
}
\end{spacing}
\clearpage
"""

with open(os.path.join(pages_dir, "page_21.tex"), "w", encoding="utf-8") as f: f.write(page_21)
with open(os.path.join(pages_dir, "page_22.tex"), "w", encoding="utf-8") as f: f.write(page_22)
with open(os.path.join(pages_dir, "page_23.tex"), "w", encoding="utf-8") as f: f.write(page_23)
with open(os.path.join(pages_dir, "page_24.tex"), "w", encoding="utf-8") as f: f.write(page_24)
with open(os.path.join(pages_dir, "page_25.tex"), "w", encoding="utf-8") as f: f.write(page_25)
with open(os.path.join(pages_dir, "page_26.tex"), "w", encoding="utf-8") as f: f.write(page_26)
with open(os.path.join(pages_dir, "page_27.tex"), "w", encoding="utf-8") as f: f.write(page_27)
with open(os.path.join(pages_dir, "page_28.tex"), "w", encoding="utf-8") as f: f.write(page_28)
with open(os.path.join(pages_dir, "page_29.tex"), "w", encoding="utf-8") as f: f.write(page_29)
with open(os.path.join(pages_dir, "page_30.tex"), "w", encoding="utf-8") as f: f.write(page_30)

print("Generated pages 21 to 30 successfully.")
