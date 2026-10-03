# -*- coding: utf-8 -*-
"""
Script to generate all 48 modular LaTeX page files and the master thesis file.
"""
import os

pages_dir = os.path.join("latex", "pages")
os.makedirs(pages_dir, exist_ok=True)

# Page 1: Outer Cover Page (Black background, Gold border & accents)
page_01 = r"""% ==============================================================================
% PAGE 1: OUTER COVER PAGE
% ==============================================================================
\thispagestyle{empty}
\begin{tikzpicture}[remember picture, overlay]
  % Dark background
  \fill[fill=black!92] (current page.north west) rectangle (current page.south east);
  % Outer Gold Border
  \draw[line width=2.5pt, color=Goldenrod!90!black]
    ([xshift=12mm, yshift=-12mm]current page.north west) rectangle ([xshift=-12mm, yshift=12mm]current page.south east);
  % Inner Gold Border
  \draw[line width=1.0pt, color=Goldenrod!80!black]
    ([xshift=14.5mm, yshift=-14.5mm]current page.north west) rectangle ([xshift=-14.5mm, yshift=14.5mm]current page.south east);
\end{tikzpicture}

\vspace*{-8mm}
\begin{center}
  {\fontsize{18}{22}\selectfont \bfseries \textcolor{Goldenrod!95!white}{GOVERNMENT POLYTECHNIC,}\\[3mm]
  \textcolor{Goldenrod!95!white}{AMRAVATI}}\\[4mm]
  {\fontsize{10}{13}\selectfont \bfseries \textcolor{Goldenrod!80!white}{(AN AUTONOMOUS INSTITUTE OF GOVERNMENT OF MAHARASHTRA)}}\\[6mm]
  
  \includegraphics[width=32mm]{figures/gpa_logo.png}\\[6mm]
  
  {\fontsize{13}{16}\selectfont \bfseries \textcolor{Goldenrod!90!white}{DEPARTMENT OF MECHANICAL ENGINEERING}\\[2mm]
  \textcolor{Goldenrod!90!white}{(2025--2026)}}\\[8mm]
  
  {\fontsize{12}{15}\selectfont \bfseries \textcolor{Goldenrod!90!white}{A PROJECT ON}}\\[4mm]
  {\fontsize{13}{17}\selectfont \bfseries \textcolor{Goldenrod!95!white}{``DESIGN AND FABRICATION OF PARABOLIC WATER HEATER\\[2mm]
  WITH SOLAR TRACKING AND POWER GENERATION''}}\\[7mm]
  
  {\fontsize{11}{14}\selectfont \bfseries \textcolor{Goldenrod!90!white}{UNDER THE GUIDANCE OF}}\\[2mm]
  {\fontsize{13}{16}\selectfont \bfseries \underline{\textcolor{Goldenrod!95!white}{Prof. A. R. BANSALI}}}\\[7mm]
  
  {\fontsize{12}{15}\selectfont \bfseries \textcolor{Goldenrod!90!white}{$\sim$SUBMITTED BY$\sim$}}\\[4mm]
  
  \begin{tabular}{ll}
    \textbf{\textcolor{Goldenrod!95!white}{MS. ASHWINI R. HAGE}} & \textbf{\textcolor{Goldenrod!95!white}{(23ME031)}} \\[1.5mm]
    \textbf{\textcolor{Goldenrod!95!white}{MR. ROHAN S. HAGE}}    & \textbf{\textcolor{Goldenrod!95!white}{(23ME032)}} \\[1.5mm]
    \textbf{\textcolor{Goldenrod!95!white}{MR. AMAY P. KADAM}}   & \textbf{\textcolor{Goldenrod!95!white}{(23ME044)}} \\[1.5mm]
    \textbf{\textcolor{Goldenrod!95!white}{MS. NANDINI R. KALE}}  & \textbf{\textcolor{Goldenrod!95!white}{(23ME047)}} \\[1.5mm]
    \textbf{\textcolor{Goldenrod!95!white}{MR. PRANAV V. KALPANDE}} & \textbf{\textcolor{Goldenrod!95!white}{(23ME048)}}
  \end{tabular}
\end{center}
\clearpage
"""

# Page 2: Inner Title / Cover Page
page_02 = r"""% ==============================================================================
% PAGE 2: INNER TITLE / SUBMISSION COVER PAGE
% ==============================================================================
\thispagestyle{empty}
\begin{tikzpicture}[remember picture, overlay]
  \draw[line width=2.0pt, color=Goldenrod!90!black]
    ([xshift=12mm, yshift=-12mm]current page.north west) rectangle ([xshift=-12mm, yshift=12mm]current page.south east);
  \draw[line width=0.8pt, color=Goldenrod!80!black]
    ([xshift=14.5mm, yshift=-14.5mm]current page.north west) rectangle ([xshift=-14.5mm, yshift=14.5mm]current page.south east);
\end{tikzpicture}

\vspace*{-5mm}
\begin{center}
  {\fontsize{18}{22}\selectfont \bfseries \textcolor{darkred}{GOVERNMENT POLYTECHNIC,}\\[2mm]
  \textcolor{darkred}{AMRAVATI}}\\[3mm]
  {\fontsize{10}{13}\selectfont \bfseries (AN AUTONOMOUS INSTITUTE OF GOVERNMENT OF MAHARASHTRA)}\\[5mm]
  
  \includegraphics[width=30mm]{figures/gpa_logo.png}\\[5mm]
  
  {\fontsize{12}{15}\selectfont \bfseries A PROJECT REPORT ON}\\[4mm]
  {\fontsize{13}{17}\selectfont \bfseries \textcolor{red!75!black}{``DESIGN AND FABRICATION OF PARABOLIC WATER HEATER\\[2mm]
  WITH SOLAR TRACKING AND POWER GENERATION''}}\\[6mm]
  
  {\fontsize{11}{14}\selectfont \bfseries \textcolor{red!75!black}{$\sim$SUBMITTED TO$\sim$}}\\[3mm]
  {\fontsize{14}{18}\selectfont \bfseries GOVERNMENT POLYTECHNIC, AMRAVATI}\\[2mm]
  {\fontsize{9.5}{12.5}\selectfont \bfseries IN PARTIAL FULFILLMENT OF THE REQUIREMENT FOR THE AWARD OF}\\[2mm]
  {\fontsize{13}{16}\selectfont \bfseries DIPLOMA IN MECHANICAL ENGINEERING}\\[6mm]
  
  {\fontsize{11}{14}\selectfont \bfseries $\sim$SUBMITTED BY$\sim$}\\[3.5mm]
  
  \begin{tabular}{ll}
    \textbf{MS. ASHWINI R. HAGE} & \textbf{(23ME031)} \\[1.2mm]
    \textbf{MR. ROHAN S. HAGE}    & \textbf{(23ME032)} \\[1.2mm]
    \textbf{MR. AMAY P. KADAM}   & \textbf{(23ME044)} \\[1.2mm]
    \textbf{MS. NANDINI R. KALE}  & \textbf{(23ME047)} \\[1.2mm]
    \textbf{MR. PRANAV V. KALPANDE} & \textbf{(23ME048)}
  \end{tabular}\\[6mm]
  
  {\fontsize{11}{14}\selectfont \bfseries $\sim$ GUIDED BY $\sim$}\\[2.5mm]
  {\fontsize{13}{16}\selectfont \bfseries \textcolor{darkred}{\underline{Prof. A. R. BANSALI}}}\\[1.5mm]
  {\fontsize{10}{13}\selectfont \bfseries LECTURER IN MECHANICAL ENGINEERING}\\[1mm]
  {\fontsize{10}{13}\selectfont \bfseries GOVERNMENT POLYTECHNIC AMRAVATI}\\[1.5mm]
  {\fontsize{10}{13}\selectfont \bfseries (2025--2026)}
\end{center}
\clearpage
"""

# Page 3: Certificate
page_03 = r"""% ==============================================================================
% PAGE 3: CERTIFICATE
% ==============================================================================
\thispagestyle{empty}
\begin{tikzpicture}[remember picture, overlay]
  \draw[line width=2.0pt, color=Goldenrod!90!black]
    ([xshift=12mm, yshift=-12mm]current page.north west) rectangle ([xshift=-12mm, yshift=12mm]current page.south east);
  \draw[line width=0.8pt, color=Goldenrod!80!black]
    ([xshift=14.5mm, yshift=-14.5mm]current page.north west) rectangle ([xshift=-14.5mm, yshift=14.5mm]current page.south east);
\end{tikzpicture}

\vspace*{-5mm}
\begin{center}
  {\fontsize{18}{22}\selectfont \bfseries \textcolor{darkred}{GOVERNMENT POLYTECHNIC,}\\[2mm]
  \textcolor{darkred}{AMRAVATI}}\\[3mm]
  {\fontsize{10.5}{13.5}\selectfont (An Autonomous Institute of Government of Maharashtra)}\\[2mm]
  {\fontsize{12}{15}\selectfont \bfseries Department of Mechanical Engineering}\\[4mm]
  
  \includegraphics[width=28mm]{figures/gpa_logo.png}\\[6mm]
  
  {\fontsize{20}{24}\selectfont \bfseries Certificate}\\[6mm]
\end{center}

\noindent
\begin{spacing}{1.4}
{\fontsize{11.5}{16}\selectfont
This is to certify that, \textbf{Mr. Amay P. Kadam (23ME044)} of $3^{\text{rd}}$ year (Odd term) Diploma in Mechanical Engineering have satisfactorily completed the major project entitled \textbf{\textcolor{red!75!black}{``DESIGN AND FABRICATION OF PARABOLIC WATER HEATER WITH SOLAR TRACKING AND POWER GENERATION''}} of course, \textbf{ME7501- Capstone Project} for the academic year 2025--2026 as prescribed in curriculum.
}
\end{spacing}

\vfill

\begin{table}[h!]
\centering
\begin{tabular*}{\textwidth}{@{\extracolsep{\fill}}cc@{}}
  \textbf{Prof. A. R. Bansali} & \textbf{Prof. S. S. Moon} \\
  Project Guide & Head of Department \\
  (Lecturer in Mechanical Engineering) & (Mechanical Engineering Department)
\end{tabular*}
\end{table}

\vspace{10mm}

\begin{center}
  \textbf{Dr. A. B. Borade}\\[1mm]
  (Principal)\\[1mm]
  (Government polytechnic, Amravati)
\end{center}
\vspace{5mm}
\clearpage
"""

# Page 4: Vision & Mission
page_04 = r"""% ==============================================================================
% PAGE 4: VISION & MISSION
% ==============================================================================
\thispagestyle{empty}
\begin{tikzpicture}[remember picture, overlay]
  \draw[line width=2.0pt, color=Goldenrod!90!black]
    ([xshift=12mm, yshift=-12mm]current page.north west) rectangle ([xshift=-12mm, yshift=12mm]current page.south east);
  \draw[line width=0.8pt, color=Goldenrod!80!black]
    ([xshift=14.5mm, yshift=-14.5mm]current page.north west) rectangle ([xshift=-14.5mm, yshift=14.5mm]current page.south east);
\end{tikzpicture}

\vspace*{-5mm}
\begin{center}
  {\fontsize{18}{22}\selectfont \bfseries \textcolor{darkred}{GOVERNMENT POLYTECHNIC,}\\[2mm]
  \textcolor{darkred}{AMRAVATI}}\\[3mm]
  {\fontsize{10}{13}\selectfont \bfseries (AN AUTONOMOUS INSTITUTE OF GOVERNMENT OF MAHARASHTRA)}\\[8mm]
  
  {\fontsize{13}{16}\selectfont \bfseries \underline{VISION}}\\[3mm]
\end{center}
\begin{itemize}[leftmargin=12mm, label=\textbullet]
  \item To be a vibrant technical institute of global reputes contributing towards the needs of industries \& society.
\end{itemize}

\begin{center}
  \vspace{4mm}
  {\fontsize{13}{16}\selectfont \bfseries \underline{MISSION}}\\[3mm]
\end{center}
\begin{itemize}[leftmargin=12mm, label=\textbullet]
  \item To develop competent diploma engineers suitable for contemporary industrial environment.
  \item To inculcate socially accepted ethics \& values among budding engineers.
  \item To Nurture innovations and entrepreneurship.
  \item To produce engineers with psychomotor \& cognitive skills committed to lifelong learning.
\end{itemize}

\vspace{8mm}
\begin{center}
  {\fontsize{14}{18}\selectfont \bfseries \textcolor{darkred}{MECHANICAL ENGINEERING DEPARTMENT}}\\[6mm]
  {\fontsize{13}{16}\selectfont \bfseries \underline{VISION}}\\[3mm]
\end{center}
\begin{itemize}[leftmargin=12mm, label=\textbullet]
  \item To become center of excellence in Mechanical Engineering, catering to the needs of industry and society.
\end{itemize}

\begin{center}
  \vspace{4mm}
  {\fontsize{13}{16}\selectfont \bfseries \underline{MISSION}}\\[3mm]
\end{center}
\begin{itemize}[leftmargin=12mm, label=\textbullet]
  \item Provide excellent academic ambience for imparting knowledge and skills.
  \item Inculcate awareness about behavioral skills, ethical practices and sustainable development.
  \item Provide nurturing environment for promoting entrepreneurship.
  \item Respond effectively to the needs of the industry and changing world.
\end{itemize}
\clearpage
"""

# Page 5: PEOs, POs, PSOs
page_05 = r"""% ==============================================================================
% PAGE 5: PEOs, POs, PSOs
% ==============================================================================
\thispagestyle{empty}
\begin{tikzpicture}[remember picture, overlay]
  \draw[line width=2.0pt, color=Goldenrod!90!black]
    ([xshift=12mm, yshift=-12mm]current page.north west) rectangle ([xshift=-12mm, yshift=12mm]current page.south east);
  \draw[line width=0.8pt, color=Goldenrod!80!black]
    ([xshift=14.5mm, yshift=-14.5mm]current page.north west) rectangle ([xshift=-14.5mm, yshift=14.5mm]current page.south east);
\end{tikzpicture}

\vspace*{-5mm}
\begin{center}
  {\fontsize{14}{18}\selectfont \bfseries \textcolor{darkred}{MECHANICAL ENGINEERING DEPARTMENT}}\\[4mm]
  {\fontsize{12}{15}\selectfont \bfseries \textcolor{navyblue}{PROGRAMME EDUCATIONAL OBJECTIVES (PEOs)}}\\[2mm]
\end{center}
\noindent
\textbf{PEO1- Technical competence:} Diploma holders will be successful in modern mechanical engineering practice.\\[1.5mm]
\textbf{PEO2- Professional Skills:} Diploma holders will continue to acquire and demonstrate the professional skills necessary to be competent employees or entrepreneurs.\\[1.5mm]
\textbf{PEO3- Professional Attitude and Citizenship:} Diploma holders will become productive and responsible citizens with high ethical and professional standards.

\begin{center}
  \vspace{3mm}
  {\fontsize{12}{15}\selectfont \bfseries \textcolor{navyblue}{PROGRAMME OUTCOMES (POs)}}\\[2mm]
\end{center}
\noindent
\textbf{PO1: Basic and Discipline Specific Knowledge:} Apply knowledge of basic mathematics, science and engineering fundamentals and engineering specialization to solve the engineering problems.\\[1.5mm]
\textbf{PO2: Problem analysis:} Identify and analyze well defined engineering problems using codified standard methods.\\[1.5mm]
\textbf{PO3: Design/development solutions:} Design solutions for well defined technical problems and assists with the design of systems components or processes to meet specified needs.\\[1.5mm]
\textbf{PO4: Engineering tools, Experimentation and testing:} Apply modern engineering tools and appropriate technique to conduct standard tests and measurements.\\[1.5mm]
\textbf{PO5: Engineering practices for Society, sustainability and environment:} Apply appropriate technology in context of society, sustainability, environment and ethical practices.\\[1.5mm]
\textbf{PO6: Project Management:} Use engineering management principles individually, as team member or a leader to manage projects effectively communicate about well-defined engineering activities.\\[1.5mm]
\textbf{PO7: Life-long learning:} Ability to analyze individual needs and engage in updating in the context of technological changes.

\begin{center}
  \vspace{3mm}
  {\fontsize{12}{15}\selectfont \bfseries \textcolor{navyblue}{PROGRAM SPECIFIC OUTCOMES (PSOs):}}\\[2mm]
\end{center}
\noindent
\textbf{PSO1:} To inculcate and foster entrepreneurship.\\[1.5mm]
\textbf{PSO2:} To plan, design, fabricate, test, operate and maintain simple mechanical systems.
\clearpage
"""

# Page 6: Declaration
page_06 = r"""% ==============================================================================
% PAGE 6: DECLARATION
% ==============================================================================
\thispagestyle{empty}
\begin{tikzpicture}[remember picture, overlay]
  \draw[line width=2.0pt, color=Goldenrod!90!black]
    ([xshift=12mm, yshift=-12mm]current page.north west) rectangle ([xshift=-12mm, yshift=12mm]current page.south east);
  \draw[line width=0.8pt, color=Goldenrod!80!black]
    ([xshift=14.5mm, yshift=-14.5mm]current page.north west) rectangle ([xshift=-14.5mm, yshift=14.5mm]current page.south east);
\end{tikzpicture}

\vspace*{-5mm}
\begin{center}
  {\fontsize{18}{22}\selectfont \bfseries \textcolor{darkred}{GOVERNMENT POLYTECHNIC,}\\[2mm]
  \textcolor{darkred}{AMRAVATI}}\\[3mm]
  {\fontsize{10.5}{13.5}\selectfont (An Autonomous Institute of Government of Maharashtra)}\\[2mm]
  {\fontsize{12}{15}\selectfont \bfseries Department of Mechanical Engineering}\\[4mm]
  
  \includegraphics[width=28mm]{figures/gpa_logo.png}\\[6mm]
  
  {\fontsize{18}{22}\selectfont \bfseries \underline{\textit{Declaration}}}\\[6mm]
\end{center}

\noindent
\begin{spacing}{1.4}
{\fontsize{11}{15}\selectfont
I am the student of Mechanical Engineering (\textbf{Section-A}) of \textbf{Government Polytechnic, Amravati} and I hereby declare that the entire work embodied in this Major-Project Report Entitled \textbf{``DESIGN AND FABRICATION OF PARABOLIC STEAM GENERATION WITH SOLAR TRACKING AND POWER GENERATION''} has been carried out by me under the supervision and guidance of \textbf{Shri. A. R. Bansali}, Project Guide \& Lecturer in Mechanical Engineering. I further declare that no part of this report has not been previously submitted for any degree, diploma or to any other diploma examining Body or University.
}
\end{spacing}

\vspace{6mm}
\noindent
\textbf{Place:- Amravati,}\\[1.5mm]
\textbf{Date:- \quad / \quad /2025.}

\vspace{6mm}
\begin{center}
\renewcommand{\arraystretch}{1.5}
\begin{tabular}{|c|l|c|p{40mm}|}
\hline
\rowcolor{gray!20}
\textbf{Sr. No.} & \multicolumn{1}{c|}{\textbf{Project Members}} & \textbf{Id code} & \multicolumn{1}{c|}{\textbf{Sign}} \\
\hline
1. & Ashwini R. Hage & 23ME031 & \\
\hline
2. & Rohan S. Hage & 23ME032 & \\
\hline
3. & Amay P. Kadam & 23ME044 & \\
\hline
4. & Nandini R. Kale & 23ME047 & \\
\hline
5. & Pranav V. Kalpande & 23ME048 & \\
\hline
\end{tabular}
\end{center}
\clearpage
"""

# Page 7: Acknowledgement
page_07 = r"""% ==============================================================================
% PAGE 7: ACKNOWLEDGEMENT
% ==============================================================================
\thispagestyle{empty}
\begin{tikzpicture}[remember picture, overlay]
  \draw[line width=2.0pt, color=Goldenrod!90!black]
    ([xshift=12mm, yshift=-12mm]current page.north west) rectangle ([xshift=-12mm, yshift=12mm]current page.south east);
  \draw[line width=0.8pt, color=Goldenrod!80!black]
    ([xshift=14.5mm, yshift=-14.5mm]current page.north west) rectangle ([xshift=-14.5mm, yshift=14.5mm]current page.south east);
\end{tikzpicture}

\vspace*{-5mm}
\begin{center}
  {\fontsize{18}{22}\selectfont \bfseries \textcolor{red!80!black}{\underline{ACKNOWLEDGEMENT}}}\\[8mm]
\end{center}

\noindent
\begin{spacing}{1.45}
{\fontsize{11}{16}\selectfont
It is my great pleasure by getting the opportunity of high lighting a fraction of knowledge, I acquired during my technical education through this project.\\[3mm]
This would not have been possible without guidance and help of many people. This is only page where I have opportunity of expressing my emotions and gratitude from the bottom of my heart to them.\\[3mm]
It is my immense pleasure to express my gratitude to respected guide \textbf{Prof. A. R. Bansali} without his best guidance this would have been impossible to prepare this project.\\[3mm]
I express my deep sense of gratitude to our head of department, Mechanical Engineering \textbf{Prof. S. S. Moon} for the most valuable guidance provided by him.\\[3mm]
I would like to thank \textbf{Dr. A. B. Borade} Principal of our institute for providing necessary facilities during the period of working on this project.\\[3mm]
Last but not the least; I would like to express our thankfulness to teaching and non-teaching staff, my friends and well-wishes.
}
\end{spacing}

\vspace{8mm}
\noindent
\textbf{Project Members:-}\\[3mm]
\begin{tabular}{ll}
  1. Mrs. Ashwini R. Hage & (23ME031) \\
  2. Mr. Rohan S. Hage & (23ME032) \\
  3. Mr. Amay P. Kadam & (23ME044) \\
  4. Mrs. Nandini R. Kale & (23ME047) \\
  5. Mr. Pranav V. Kalpande & (23ME048)
\end{tabular}
\clearpage
"""

# Page 8: Abstract
page_08 = r"""% ==============================================================================
% PAGE 8: ABSTRACT
% ==============================================================================
\thispagestyle{empty}
\begin{tikzpicture}[remember picture, overlay]
  \draw[line width=2.0pt, color=Goldenrod!90!black]
    ([xshift=12mm, yshift=-12mm]current page.north west) rectangle ([xshift=-12mm, yshift=12mm]current page.south east);
  \draw[line width=0.8pt, color=Goldenrod!80!black]
    ([xshift=14.5mm, yshift=-14.5mm]current page.north west) rectangle ([xshift=-14.5mm, yshift=14.5mm]current page.south east);
\end{tikzpicture}

\vspace*{-5mm}
\begin{center}
  {\fontsize{18}{22}\selectfont \bfseries \textcolor{red!80!black}{\underline{ABSTRACT}}}\\[6mm]
\end{center}

\noindent
\begin{spacing}{1.25}
{\fontsize{10.2}{14}\selectfont
The increasing global energy demand and depletion of fossil fuels have accelerated the need for sustainable energy solutions. Solar energy, being clean, renewable, and abundant, is a reliable alternative for thermal and electrical applications. In this work, a solar water heater and steam generator system is designed and fabricated using a cylindrical parabolic concentrator (CPC). The CPC focuses incident solar radiation onto a receiver tube, thereby enhancing the thermal efficiency. Unlike flat plate collectors, the concentrator achieves higher temperatures suitable for both water heating and steam generation. The proposed design ensures optimum utilization of solar energy for domestic, industrial, and agricultural applications.\\[2.5mm]
The system incorporates real-time automated solar tracking to overcome limitations of fixed-angle collectors. A dual-axis tracking mechanism powered by sensors and microcontroller logic adjusts the concentrator to maintain perpendicularity to solar rays. This ensures maximum concentration of energy throughout the day, significantly improving thermal output. The tracking system reduces losses caused by diurnal variations and seasonal shifts in solar position. Automation also minimizes human intervention and enhances operational reliability. With improved efficiency, the system provides consistent steam production even during partial sunlight conditions.\\[2.5mm]
The fabricated prototype consists of a cylindrical concentrator, absorber tube, insulated water storage, and control electronics. Mild steel and reflective aluminum are used for the concentrator frame and surface to ensure durability and high reflectivity. The receiver tube, coated with selective absorptive material, minimizes heat losses while maximizing absorption. Heat transfer to the working fluid (water) occurs rapidly, raising its temperature to produce hot water and steam. Insulated storage prevents thermal losses and allows continuous supply even after sunset. The compact and modular design enables easy scalability for domestic as well as industrial usage.\\[2.5mm]
Experimental testing demonstrated the system's ability to achieve water heating up to boiling point and generate steam at controlled rates. Real-time tracking improved efficiency by 30--40\% compared to fixed concentrators. The study concludes that the developed system is an efficient, low-cost, and eco-friendly alternative to conventional water heating and steam generation methods. It offers significant potential in rural areas where grid energy is limited. Additionally, the system reduces carbon emissions, promoting green technology adoption.\\[2.5mm]
Further research may involve hybridization with other renewable systems and performance optimization under varying climatic conditions.
}
\end{spacing}
\clearpage
"""

# Page 9: Index (Numbered 1)
page_09 = r"""% ==============================================================================
% PAGE 9: INDEX / TABLE OF CONTENTS (Numbered Page 1)
% ==============================================================================
\setcounter{page}{1}
\pagestyle{fancy}

\vspace*{-2mm}
\begin{center}
  {\fontsize{16}{20}\selectfont \bfseries \textcolor{red!80!black}{\underline{INDEX}}}\\[6mm]
\end{center}

\begin{center}
\renewcommand{\arraystretch}{1.35}
\begin{tabular}{|c|c|l|c|}
\hline
\rowcolor{gray!20}
\textbf{Sr. No.} & \multicolumn{2}{c|}{\textbf{Title}} & \textbf{Page. No.} \\
\hline
1. & & \textbf{INTRODUCTION} & 3--4 \\
\cline{2-4}
   & 1.1 & OVERVIEW & 3 \\
\cline{2-4}
   & 1.2 & NEED OF PROJECT & 3 \\
\cline{2-4}
   & 1.3 & OBJECTIVE & 4 \\
\hline
2. & & \textbf{LITERATURE REVIEW} & 5--6 \\
\hline
3. & & \textbf{METHODOLOGY} & 7--25 \\
\cline{2-4}
   & 3.1 & DESING PARAMETER AND SELECTION OF COMPONENTS & 7--22 \\
\cline{2-4}
   & 3.2 & SOLAR TRACKING MECHANISM & 23--25 \\
\hline
4. & & \textbf{FABRICATION} & 26--27 \\
\hline
5. & & \textbf{CONSTRUCTION} & 28--29 \\
\hline
6. & & \textbf{PROGRAMING} & 30--33 \\
\hline
7. & & \textbf{WORKING} & 34 \\
\hline
8. & & \textbf{ADVANTAGES} & 35 \\
\hline
9. & & \textbf{APPLICATION} & 36 \\
\hline
10. & & \textbf{COST ESTIMATION} & 37--38 \\
\hline
11. & & \textbf{CONCLUSION} & 39 \\
\hline
12. & & \textbf{REFERANCES} & 40 \\
\hline
\end{tabular}
\end{center}
\clearpage
"""

# Page 10: List of Figures (Numbered 2)
page_10 = r"""% ==============================================================================
% PAGE 10: LIST OF FIGURES (Numbered Page 2)
% ==============================================================================
\vspace*{-2mm}
\begin{center}
  {\fontsize{16}{20}\selectfont \bfseries \textcolor{red!80!black}{\underline{LIST OF FIGURES}}}\\[6mm]
\end{center}

\begin{center}
\renewcommand{\arraystretch}{1.28}
\begin{tabular}{|c|p{80mm}|c|}
\hline
\rowcolor{gray!20}
\textbf{Sr. No.} & \multicolumn{1}{c|}{\textbf{Title}} & \textbf{Page. No.} \\
\hline
1. & PARABOLIC DISH & 7 \\
\hline
2. & RECEIVER & 9 \\
\hline
3. & COLD WATER STOREAG TANK & 10 \\
\hline
4. & WATER SUPPLY PIPE & 11 \\
\hline
5. & FLOW CONTROL VALVE & 12 \\
\hline
6. & ARDUINO NANO & 13 \\
\hline
7. & MOTOR DRIVER & 14 \\
\hline
8. & LDR SENSOR MODULE & 15 \\
\hline
9. & PUSH BUTTON & 16 \\
\hline
10. & PMDC MOTOR & 17 \\
\hline
12. & V-GROOVE BELT AND PULLEY & 18 \\
\hline
13. & BATTERY & 20 \\
\hline
14. & SOLAR PANEL UNIT & 21 \\
\hline
15. & WOODEN BASE, PVC PIPE AND VARIOUS TYPES OF NUT & 22 \\
\hline
16. & SOLAR TRACKING MECHANISM & 23 \\
\hline
17. & ACTUAL MODEL & 28 \\
\hline
\end{tabular}
\end{center}
\clearpage
"""

with open(os.path.join(pages_dir, "page_01.tex"), "w", encoding="utf-8") as f: f.write(page_01)
with open(os.path.join(pages_dir, "page_02.tex"), "w", encoding="utf-8") as f: f.write(page_02)
with open(os.path.join(pages_dir, "page_03.tex"), "w", encoding="utf-8") as f: f.write(page_03)
with open(os.path.join(pages_dir, "page_04.tex"), "w", encoding="utf-8") as f: f.write(page_04)
with open(os.path.join(pages_dir, "page_05.tex"), "w", encoding="utf-8") as f: f.write(page_05)
with open(os.path.join(pages_dir, "page_06.tex"), "w", encoding="utf-8") as f: f.write(page_06)
with open(os.path.join(pages_dir, "page_07.tex"), "w", encoding="utf-8") as f: f.write(page_07)
with open(os.path.join(pages_dir, "page_08.tex"), "w", encoding="utf-8") as f: f.write(page_08)
with open(os.path.join(pages_dir, "page_09.tex"), "w", encoding="utf-8") as f: f.write(page_09)
with open(os.path.join(pages_dir, "page_10.tex"), "w", encoding="utf-8") as f: f.write(page_10)

print("Generated pages 1 to 10 successfully.")
