# -*- coding: utf-8 -*-
"""
Generate LaTeX pages 11 to 20
"""
import os

pages_dir = os.path.join("latex", "pages")
os.makedirs(pages_dir, exist_ok=True)

# Page 11: Chapter-1 Introduction (Numbered 3)
page_11 = r"""% ==============================================================================
% PAGE 11: CHAPTER-1 INTRODUCTION (Numbered Page 3)
% ==============================================================================
\begin{center}
  {\fontsize{15}{18}\selectfont \bfseries \textcolor{red!80!black}{\underline{CHAPTER-1}}}\\[2mm]
  {\fontsize{16}{20}\selectfont \bfseries \textcolor{red!80!black}{\underline{INTRODUCTION}}}\\[6mm]
\end{center}

\subsection*{1.1 OVERVIEW}
\noindent
\begin{spacing}{1.2}
{\fontsize{10.5}{14.5}\selectfont
Energy plays a vital role in the development of any country. The increasing demand for energy and the depletion of conventional energy sources like coal, oil, and natural gas have made it necessary to explore renewable energy resources. Among these, solar energy is the most abundant, clean, and sustainable form of energy available.\\[3mm]
The Sun radiates a huge amount of energy in the form of light and heat. If effectively utilized, this energy can fulfill a major part of the world's energy needs. Solar energy can be converted into useful heat energy or electrical energy through various technologies such as solar water heaters, photovoltaic cells, and solar cookers.\\[3mm]
The present project, titled \textbf{``Design and Fabrication of Parabolic Water Heater with Solar Tracking and Power Generation,''} is a step toward utilizing this renewable energy for practical use. The system focuses on capturing solar radiation using a parabolic collector to heat water efficiently and uses solar tracking to improve performance. It also integrates a small-scale power generation unit, making it a multipurpose and eco-friendly system.
}
\end{spacing}

\vspace{5mm}
\subsection*{1.2 NEED OF PROJECT}
\noindent
\begin{spacing}{1.2}
{\fontsize{10.5}{14.5}\selectfont
In most rural and semi-urban areas, people still depend on firewood, kerosene, and LPG gas for heating water. These fuels not only increase household expenses but also contribute to pollution and environmental degradation.\\[3mm]
Using solar energy for heating water is an ideal solution because:
\begin{itemize}[leftmargin=8mm, itemsep=1.5mm, label=\textbullet]
  \item It is freely available and inexhaustible.
  \item It reduces dependency on non-renewable energy sources.
  \item It helps save fuel and electricity.
  \item It lowers carbon emissions and environmental pollution.
\end{itemize}
However, most existing solar water heaters are fixed in one direction and cannot follow the Sun's movement throughout the day. This results in a considerable loss of efficiency. To overcome this problem, a solar tracking mechanism is introduced to maintain the collector's orientation toward the Sun, thereby increasing heat gain and system output.
}
\end{spacing}
\clearpage
"""

# Page 12: 1.3 Objective (Numbered 4)
page_12 = r"""% ==============================================================================
% PAGE 12: 1.3 OBJECTIVE (Numbered Page 4)
% ==============================================================================
\subsection*{1.3 OBJECTIVE}
\vspace{3mm}

\begin{spacing}{1.25}
{\fontsize{10.5}{14.5}\selectfont
\begin{enumerate}[leftmargin=8mm, itemsep=2.5mm]
  \item To design and develop a parabolic concentrator capable of focusing solar rays onto a focal point for efficient heat generation.
  \item To fabricate a cost-effective parabolic water heater using locally available materials.
  \item To utilize solar energy for heating water and producing steam suitable for domestic or small-scale industrial applications.
  \item To design and implement an automatic solar tracking system for continuous alignment of the parabola with the sun.
  \item To enhance the thermal efficiency of the system by maintaining maximum solar exposure throughout the day.
  \item To integrate a solar panel for generating electrical power required to operate the tracking motor and control system.
  \item To create a self-sustaining hybrid system capable of both thermal and electrical energy generation.
  \item To analyze the performance of the parabolic heater under different climatic and sunlight conditions.
  \item To reduce dependency on non-renewable energy sources through the use of clean solar energy.
  \item To promote the application of renewable technologies for domestic water heating and rural energy solutions.
  \item To evaluate the temperature rise, efficiency, and overall performance of the fabricated system.
  \item To demonstrate the environmental benefits of using solar-based hybrid energy system.
\end{enumerate}
}
\end{spacing}
\clearpage
"""

# Page 13: Chapter-2 Literature Review (Numbered 5)
page_13 = r"""% ==============================================================================
% PAGE 13: CHAPTER-2 LITERATURE REVIEW (Numbered Page 5)
% ==============================================================================
\begin{center}
  {\fontsize{15}{18}\selectfont \bfseries \textcolor{red!80!black}{\underline{CHAPTER-2}}}\\[2mm]
  {\fontsize{16}{20}\selectfont \bfseries \textcolor{red!80!black}{\underline{Literature Review}}}\\[5mm]
\end{center}

\noindent
\begin{spacing}{1.25}
{\fontsize{10.2}{14.5}\selectfont
\textbf{Literature Survey} Solar energy has been harnessed for heating and power generation for several centuries, dating back to ancient civilizations that used mirrors and lenses to concentrate sunlight for practical applications. Early research on solar concentrators and parabolic reflectors in the 18th and 19th centuries laid the foundation for modern solar thermal systems. Initial designs were simple, often stationary reflectors used for heating water or cooking food, and lacked automation or efficiency optimization, but they demonstrated the potential of concentrated solar energy.\\[3.5mm]
In the latter half of the 20th century, advancements in materials, reflectors, and control systems enabled the development of more efficient parabolic troughs and dishes. Researchers focused on improving the concentration ratio, heat transfer efficiency, and receiver design. During this period, solar tracking mechanisms also began to emerge, initially as manual or semi-automatic systems, allowing solar concentrators to follow the sun's path and improve energy capture. These developments highlighted the importance of combining solar tracking with concentrators for optimal performance.\\[3.5mm]
In the present era, significant improvements in photovoltaic (PV) technology and automated solar tracking systems have made hybrid systems combining thermal and electrical energy feasible. Modern parabolic water heaters now integrate solar tracking, temperature sensors, and electric motors powered by solar panels, creating partially self-sustaining systems. Studies in recent years have shown that such hybrid systems can improve overall energy utilization by up to 30--50\% compared to fixed or non-tracked systems. Additionally, the use of readily available materials and cost-effective fabrication methods has made these technologies accessible for both domestic and industrial applications.\\[3.5mm]
Future trends in parabolic water heating and power generation focus on smart automation, AI-based tracking, and multi-functional hybrid systems. Researchers are exploring the integration of IoT devices for real-time monitoring, predictive control of solar tracking, and energy storage optimization. Advanced materials like selective coatings for receivers and high-reflectivity mirrors are also being developed to enhance heat absorption and reduce energy losses. These innovations aim to create more efficient, durable, and environmentally friendly solar systems capable of meeting increasing energy demands.
}
\end{spacing}
\clearpage
"""

# Page 14: Literature Review Summary & Table (Numbered 6)
page_14 = r"""% ==============================================================================
% PAGE 14: LITERATURE SURVEY SUMMARY & TABLE (Numbered Page 6)
% ==============================================================================
\noindent
\begin{spacing}{1.2}
{\fontsize{10.5}{14.5}\selectfont
In summary, the evolution of parabolic water heaters reflects a continuous effort to maximize the efficiency of solar energy utilization. From simple stationary concentrators in the past to modern automated hybrid systems today, and towards intelligent, smart solar devices in the future, research consistently aims to improve thermal and electrical output, reduce costs, and promote sustainable energy solutions. This project builds on this foundation by designing and fabricating a parabolic water heater with solar tracking and power generation, contributing to the growing field of renewable energy technology.
}
\end{spacing}

\vspace{5mm}
\begin{center}
  {\fontsize{12}{15}\selectfont \bfseries \underline{This Table Summarizes The Literature Survey}}\\[4mm]
\end{center}

\begin{center}
\renewcommand{\arraystretch}{1.3}
\begin{tabular}{|p{38mm}|p{85mm}|}
\hline
\rowcolor{gray!20}
\textbf{Aspect} & \textbf{Present} \\
\hline
Technology Type & Automated parabolic dishes with solar tracking; hybrid thermal and PV systems \\
\hline
Energy Utilization & Thermal + electrical energy (heating + power generation) \\
\hline
Efficiency & Moderate to high (30--50\% improvement with tracking and hybrid integration) \\
\hline
Materials & Improved reflectors, insulated receivers, durable metals, and solar panels \\
\hline
Automation & Motorized solar tracking, sensor-based alignment \\
\hline
Environmental Impact & Clean energy with partial reduction of fossil fuel use \\
\hline
Cost & Moderate cost with improved efficiency \\
\hline
Applications & Domestic and small industrial heating, electricity generation, Smart homes \\
\hline
\end{tabular}
\end{center}
\clearpage
"""

# Page 15: Chapter-3 Methodology - Parabolic Dish (Numbered 7)
page_15 = r"""% ==============================================================================
% PAGE 15: CHAPTER-3 METHODOLOGY - 1) PARABOLIC DISH (Numbered Page 7)
% ==============================================================================
\begin{center}
  {\fontsize{15}{18}\selectfont \bfseries \textcolor{red!80!black}{\underline{CHAPTER-3}}}\\[2mm]
  {\fontsize{16}{20}\selectfont \bfseries \textcolor{red!80!black}{\underline{METHODOLOGY}}}\\[4mm]
\end{center}

\subsection*{3.1 DESING PARAMETER AND SELECTION OF COMPONANTS}
\subsubsection*{1) PARABOLIC DISH}

\begin{center}
  \includegraphics[width=68mm]{figures/fig1_parabolic_dish.jpg}
\end{center}

\vspace{2mm}
\noindent
\begin{spacing}{1.15}
{\fontsize{9.8}{13.5}\selectfont
The image shows the fabricated parabolic solar concentrator developed for this project, which is designed to focus sunlight onto a single focal point for efficient heat generation. The concentrator surface is constructed using multiple small square mirror pieces carefully arranged on a curved parabolic base to achieve the desired reflective geometry. Each mirror segment reflects incoming solar radiation toward the focal point, where a receiver tube or container is placed to absorb concentrated heat energy. This design allows the system to attain high temperatures suitable for water heating and steam generation, utilizing clean and renewable solar energy.\\[2.5mm]
The use of mirror tiles instead of a single reflective sheet significantly reduces fabrication costs while maintaining high reflectivity and durability. The circular structure provides better light focusing and structural stability. The concentrator, with a 60~cm diameter and 40~cm focal length, is integrated with a real-time automated solar tracking system to maintain optimal alignment with the sun throughout the day. This practical and cost-effective design demonstrates the potential of locally fabricated solar concentrators for sustainable thermal energy applications in domestic and industrial sectors. A parabolic concentrator is a reflective device that focuses incoming solar radiation onto a focal point or line. The design is based on the geometric properties of a parabola, where all rays parallel to the principal axis are reflected through a single focal point. In this project, a cylindrical parabolic concentrator is used to concentrate sunlight onto a receiver tube located at the focal point to achieve efficient heating and steam generation.
}
\end{spacing}
\clearpage
"""

# Page 16: Design Parameters (Numbered 8)
page_16 = r"""% ==============================================================================
% PAGE 16: DESIGN PARAMETERS (Numbered Page 8)
% ==============================================================================
\begin{center}
  {\fontsize{14}{17}\selectfont \bfseries \underline{DESIGN PARAMETERS}}\\[4mm]
  \includegraphics[width=85mm]{figures/fig_design_parameters.jpg}\\[6mm]
\end{center}

\noindent
{\fontsize{11}{16}\selectfont
\textbf{From the given design:}\\[4mm]
\textbf{Aperture Diameter (D):} 60 cm\\[3mm]
\textbf{Focal Length (f):} 40 cm\\[3mm]
\textbf{Shape:} Cylindrical Parabolic Reflector\\[3mm]
\textbf{Type:} Linear-focus concentrator\\[3mm]
\textbf{Material:} mirror-finished sheet\\[3mm]
\textbf{Receiver Position:} Placed along the focal line at a height equal to the focal length (40 cm from the vertex)
}
\clearpage
"""

# Page 17: 2) Receiver (Numbered 9)
page_17 = r"""% ==============================================================================
% PAGE 17: 2) RECEIVER (Numbered Page 9)
% ==============================================================================
\subsubsection*{2) RECEIVER}

\begin{center}
  \includegraphics[width=90mm]{figures/fig2_receiver.jpg}
\end{center}

\vspace{3mm}
\noindent
\begin{spacing}{1.2}
{\fontsize{10.2}{14.5}\selectfont
In this project, the receiver plays a vital role in absorbing concentrated solar radiation and converting it into thermal energy. The receiver is fabricated from a copper coil with an internal diameter of 3~mm, selected for its excellent thermal conductivity and corrosion resistance. Copper is an ideal material for solar thermal systems as it ensures rapid heat transfer from the concentrated sunlight to the working fluid circulating inside the coil.\\[3mm]
The receiver coil is positioned precisely at the focal point of the parabolic concentrator, where maximum solar energy is focused.\\[3mm]
To enhance heat absorption and minimize reflective losses, the copper coil is coated with matte black heat-resistant paint. The black surface increases the absorptivity of the receiver, allowing it to capture a greater portion of incident solar radiation. The small internal diameter ensures a higher rate of heat transfer to the flowing water, enabling quick temperature rise and even steam generation under continuous solar exposure. This receiver design ensures efficient energy utilization and contributes significantly to the overall performance and thermal efficiency of the solar water heater and steam generator system.
}
\end{spacing}
\clearpage
"""

# Page 18: 3) Cold Water Storage Tank (Numbered 10)
page_18 = r"""% ==============================================================================
% PAGE 18: 3) COLD WATER STORAGE TANK (Pre-Heating Unit) (Numbered Page 10)
% ==============================================================================
\subsubsection*{3) COLD WATER STORAGE TANK (Pre-Heating Unit)}

\begin{center}
  \includegraphics[width=50mm]{figures/fig3_cold_water_storage_tank.jpg}
\end{center}

\noindent
\begin{spacing}{1.2}
{\fontsize{10.2}{14.5}\selectfont
A black-colored cold storage water tank is installed as a pre-heating unit in the system. It serves two purposes:\\[3mm]
\textbf{SPECIFICATION:}
\begin{enumerate}[leftmargin=8mm, itemsep=2mm]
  \item \textbf{Pre-heating of water:} The black surface absorbs solar radiation effectively, slightly increasing the temperature of the water before it enters the copper receiver. This pre-heating process improves overall system efficiency and reduces the time required to reach the desired hot-water temperature.
  \item \textbf{Storage:} The tank also acts as a temporary storage reservoir that supplies a steady flow of water to the parabolic collector.\\[1.5mm]
  The tank is made of lightweight aluminium material, coated with black paint to maximize solar absorption.\\[1.5mm]
  A small outlet at the bottom connects to the copper receiver tube through a flexible pipe. This simple addition improves energy utilization and makes the design cost-effective and efficient.
  \item \textbf{Capacity of the tank :} 5 lit
\end{enumerate}
}
\end{spacing}
\clearpage
"""

# Page 19: 4) Water Supply Pipe (Numbered 11)
page_19 = r"""% ==============================================================================
% PAGE 19: 4) WATER SUPPLY PIPE (Connecting Line) (Numbered Page 11)
% ==============================================================================
\subsubsection*{4) WATER SUPPLY PIPE (Connecting Line)}

\begin{center}
  \includegraphics[width=65mm]{figures/fig4_water_supply_pipe.jpg}
\end{center}

\noindent
\begin{spacing}{1.2}
{\fontsize{10.2}{14.5}\selectfont
A flexible blue plastic pipe is used in the system to connect the cold storage water tank with the copper receiver tube. This pipe serves as the main water supply line and ensures a smooth, continuous flow of water from the tank to the receiver during operation.\\[3mm]
\textbf{Material and Function:}
\begin{itemize}[leftmargin=8mm, itemsep=1.5mm, label=\textbullet]
  \item The pipe is made of high-density polyethylene (HDPE), which is lightweight, durable, and resistant to heat and corrosion.
  \item It is capable of withstanding moderate pressure and temperature, making it suitable for small scale solar heating systems.
  \item The inner surface is smooth, allowing easy water flow with minimal frictional losses.
  \item Its blue color helps in identifying it as the cold-water line, preventing confusion with the hot-water outlet.
\end{itemize}
\vspace{2mm}
\textbf{Role in the Project:}
\begin{itemize}[leftmargin=8mm, itemsep=1.5mm, label=\textbullet]
  \item Carries water from the pre-heating storage tank to the copper receiver.
  \item Maintains a constant water level and flow rate in the heating section.
  \item Improves system performance by ensuring that no air pockets or leaks occur.
  \item Flexible enough to accommodate small movements in the solar tracking assembly.
\end{itemize}
}
\end{spacing}
\clearpage
"""

# Page 20: 5) Flow Control Valve (Numbered 12)
page_20 = r"""% ==============================================================================
% PAGE 20: 5) FLOW CONTROL VALVE (Hoffman Clamp Arrangement) (Numbered Page 12)
% ==============================================================================
\subsubsection*{5) FLOW CONTROL VALVE (Hoffman Clamp Arrangement)}

\begin{center}
  \includegraphics[width=80mm]{figures/fig5_flow_control_valve.jpg}
\end{center}

\noindent
\begin{spacing}{1.2}
{\fontsize{10.2}{14.5}\selectfont
A Hoffman clamp is used in the project as a manual flow control valve for the water passing through the blue supply pipe. It allows precise regulation of the water flow from the storage tank to the copper receiver tube, ensuring that the heating process remains efficient and steady.\\[3mm]
\textbf{Construction:}
\begin{itemize}[leftmargin=8mm, itemsep=1.5mm, label=\textbullet]
  \item The clamp consists of a U-shaped metal frame with a threaded screw and a knob at the top.
  \item The blue flexible pipe passes through the clamp opening.
  \item By rotating the knob clockwise, the screw presses against the pipe, restricting or stopping the water flow.
  \item Turning it anti-clockwise loosens the pressure, allowing smooth water passage.
\end{itemize}
\vspace{2mm}
\textbf{Function in the Project:}
\begin{enumerate}[leftmargin=8mm, itemsep=2mm]
  \item Controls the rate of water flow to maintain proper heat absorption in the copper tube.
  \item Prevents wastage of hot water and maintains uniform temperature rise.
  \item Acts as a simple and low-cost valve system, eliminating the need for expensive plumbing fittings.
  \item Makes the experimental setup easy to adjust during testing. This component ensures better temperature control and improves the overall performance and efficiency of the solar water heater.
\end{enumerate}
}
\end{spacing}
\clearpage
"""

with open(os.path.join(pages_dir, "page_11.tex"), "w", encoding="utf-8") as f: f.write(page_11)
with open(os.path.join(pages_dir, "page_12.tex"), "w", encoding="utf-8") as f: f.write(page_12)
with open(os.path.join(pages_dir, "page_13.tex"), "w", encoding="utf-8") as f: f.write(page_13)
with open(os.path.join(pages_dir, "page_14.tex"), "w", encoding="utf-8") as f: f.write(page_14)
with open(os.path.join(pages_dir, "page_15.tex"), "w", encoding="utf-8") as f: f.write(page_15)
with open(os.path.join(pages_dir, "page_16.tex"), "w", encoding="utf-8") as f: f.write(page_16)
with open(os.path.join(pages_dir, "page_17.tex"), "w", encoding="utf-8") as f: f.write(page_17)
with open(os.path.join(pages_dir, "page_18.tex"), "w", encoding="utf-8") as f: f.write(page_18)
with open(os.path.join(pages_dir, "page_19.tex"), "w", encoding="utf-8") as f: f.write(page_19)
with open(os.path.join(pages_dir, "page_20.tex"), "w", encoding="utf-8") as f: f.write(page_20)

print("Generated pages 11 to 20 successfully.")
