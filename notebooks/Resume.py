from fpdf import FPDF

class OnePageResume(FPDF):
    def header(self):
        self.set_font("Arial", "B", 14)
        self.cell(0, 8, "SAIYAM TUTEJA", ln=True, align="C")
        self.set_font("Arial", "", 10)
        self.cell(0, 6, "Solanipuram, Roorkee, 247667 | 7505835347 | saiyamtuteja@gmail.com | linkedin.com/in/saiyam-tuteja", ln=True, align="C")
        self.ln(4)

    def section_title(self, title):
        self.set_font("Arial", "B", 11)
        self.set_fill_color(230, 230, 230)
        self.cell(0, 7, title.upper(), ln=True, fill=True)
        self.ln(1)
        self.set_font("Arial", "", 10)

    def bullet_point(self, text):
        self.multi_cell(0, 5, "- " + text)

    def add_table(self, data, col_widths):
        self.set_font("Arial", "", 10)
        line_height = self.font_size * 1.5
        for row in data:
            for datum, width in zip(row, col_widths):
                self.multi_cell(width, line_height, datum, border=0)
            self.ln(line_height * 0.5)

# Create PDF
resume = OnePageResume(format='A4')
resume.set_auto_page_break(auto=True, margin=10)
resume.add_page()

# PROFESSIONAL SUMMARY
resume.section_title("Professional Summary")
resume.multi_cell(0, 5,
    "Results-driven Data Analyst and Aspiring Software Engineer with expertise in C++, Python, Power BI, and SQL. "
    "Experienced in transforming data into actionable insights, developing scalable applications, and mentoring budding analysts. "
    "Committed to delivering data-driven solutions and excelling in fast-paced, collaborative environments."
)

# SKILLS (Tabular Format)
resume.section_title("Skills")
skills_data = [
    ["Programming Languages:", "C++, Python, PHP, SQL"],
    ["Data Tools:", "Power BI, Pandas, NumPy, Scikit-learn"],
    ["Web Technologies:", "HTML, CSS, MySQL"],
    ["Soft Skills:", "Leadership, Communication, Time Management, Problem Solving"]
]
resume.add_table(skills_data, [45, 140])

# EXPERIENCE
resume.section_title("Professional Experience")
resume.set_font("Arial", "B", 10)
resume.cell(0, 5, "Software Engineering Intern - COER University, Roorkee (Sep 2023 - June 2024)", ln=True)
resume.set_font("Arial", "", 10)
resume.bullet_point("Built Power BI dashboards for academic performance monitoring.")
resume.bullet_point("Developed AQMS to improve education assessments.")
resume.bullet_point("Streamlined student data for actionable insights.")

resume.set_font("Arial", "B", 10)
resume.cell(0, 5, "Tech Intern - F3S InfoTech Pvt. Ltd. (June - Aug 2023)", ln=True)
resume.set_font("Arial", "", 10)
resume.bullet_point("Revamped the Bhangola website; increased engagement by 40%.")
resume.bullet_point("Designed product labels, contributing to a 15% sales boost.")
resume.bullet_point("Improved product features based on user feedback.")

resume.set_font("Arial", "B", 10)
resume.cell(0, 5, "Software Developer - F1 InfoTech Pvt. Ltd. (July - Aug 2022)", ln=True)
resume.set_font("Arial", "", 10)
resume.bullet_point("Developed Fixed Assets Register to manage internal assets.")
resume.bullet_point("Integrated asset data into centralized systems.")
resume.bullet_point("Contributed to platform feature enhancements.")

# WORKSHOPS & MENTORSHIP
resume.section_title("Workshops & Mentorship")
resume.bullet_point("Conducted 2-week Data Analysis Workshop at Quantum University for 60+ students.")
resume.bullet_point("Conducted 2-week Data Analysis Workshop at COER University for MBA & BCA students.")
resume.bullet_point("Mentored 50+ students online on Capzora platform, guiding them in data analyst roadmap and skills.")

# PROJECTS
resume.section_title("Projects")
resume.set_font("Arial", "B", 10)
resume.cell(0, 5, "Employment and Unemployment Data Analysis", ln=True)
resume.set_font("Arial", "", 10)
resume.bullet_point("Built predictive models using Python, Pandas, NumPy, Scikit-learn.")
resume.bullet_point("Visualized trends using bar charts, scatter plots, and heatmaps.")
resume.bullet_point("Interpreted results using R-squared for actionable insights.")

resume.set_font("Arial", "B", 10)
resume.cell(0, 5, "ProfPraisal - Faculty Evaluation System", ln=True)
resume.set_font("Arial", "", 10)
resume.bullet_point("Developed PHP/MySQL system to streamline student feedback.")
resume.bullet_point("Enabled role-based access for administrators, faculty, and students.")
resume.bullet_point("Provided intuitive UI with actionable teaching insights.")

# EDUCATION
resume.section_title("Education")
edu_data = [
    ["MCA (Pursuing)", "Graphic Era Hill University (2024 - 2026)"],
    ["BCA", "COER University (2021 - 2024) - CGPA: 9.7"],
    ["Intermediate", "Greenway Modern School (2020 - 2021) - 91.4%"]
]
resume.add_table(edu_data, [55, 130])

# CERTIFICATIONS
resume.section_title("Certifications & Achievements")
resume.bullet_point("AI with Machine Learning - IIT Roorkee")
resume.bullet_point("Google Data Analyst Professional Certificate")
resume.bullet_point("Power BI & Python - Udemy")
resume.bullet_point("Excel and Word - Udemy")
resume.bullet_point("1st Position (2nd Year), 3rd Position (1st Year), BCA")
resume.bullet_point("3rd Place - Hackathon, Roorkee College of Engineering")

# OPEN SOURCE
resume.section_title("Open Source Contributions")
resume.bullet_point("10+ projects in GirlScript Summer of Code (2023 & 2024).")
resume.bullet_point("Ranked 150/5000 participants in 2024 cohort.")

# LINKS
resume.section_title("Links")
resume.bullet_point("GitHub: github.com/SaiyamTuteja")
resume.bullet_point("Projects: Employment Data Analysis, Faculty Evaluation System")

# Save the resume
resume.output("Saiyam_Tuteja_OnePage_Resume.pdf")
print("✅ Resume saved as 'Saiyam_Tuteja_OnePage_Resume.pdf'")
