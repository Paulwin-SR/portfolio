import sys
import re

file_path = "/home/trivand/Documents/portfolio/src/pages/About.jsx"
with open(file_path, "r") as f:
    content = f.read()

old_ui_text = """              <p>
                I'm currently a Class 12 student with PCMB, but honestly,
                my main interest is not in Biology anymore. Before 9th class,
                I used to think that I would go into the medical field in the
                future, but as time passed, I started getting more interested
                in computers and technology.
              </p>

              <p>
                In 11th class, I explored coding more seriously and slowly
                developed a strong interest in programming, cybersecurity,
                and AI.
              </p>

              <p>
                Now, coding is something I genuinely enjoy. I like learning
                new programming languages, building things, and understanding
                how technology works behind the scenes.
              </p>

              <p>
                Out of everything in tech, ethical hacking and cybersecurity
                interest me the most because I find it exciting to learn about
                system security, vulnerabilities, and how hackers think.
              </p>

              <p>
                At the same time, I also enjoy using AI tools and understanding
                how AI can make work smarter and easier.
              </p>

              <p>
                After completing Class 12, I want to move completely into the
                coding and tech field. My goal is to build a future in
                cybersecurity, ethical hacking, and AI.
              </p>

              <p>
                I know there's still a lot to learn, but I enjoy the process
                and always try to improve my skills step by step.
              </p>

              <p>
                For me, technology is not just a career option anymore —
                it's something I truly connect with and see myself doing
                in the future.
              </p>"""

new_ui_text = """              <p>
                Hi, I'm Paulwin, a Full-stack Software Engineer with hands-on experience in database design, data collection systems, and backend development.
              </p>

              <p>
                Currently working at Trivand Technologies, I specialize in building robust web applications and managing complex database collections using MongoDB, SQL, and Python. I have a strong focus on data extraction, transformation, analysis, and system integration.
              </p>

              <p>
                I hold a B.Tech in Computer Science and Engineering from Lourdes Matha College of Science and Technology. Throughout my journey, I've developed a passion for creating impactful solutions, such as an AI-powered Cyber-bullying Detection system and a Food Donation platform to connect donors with those in need.
              </p>

              <p>
                My technical toolkit includes Java, React, Node.js, Express, TypeScript, and Prompt Engineering, complemented by soft skills like empathetic communication, teamwork, and problem-solving.
              </p>

              <p>
                I'm always eager to learn and grow, looking to leverage my software engineering expertise to deliver actionable insights and build meaningful digital experiences.
              </p>"""

if old_ui_text in content:
    content = content.replace(old_ui_text, new_ui_text)
else:
    print("Could not find old UI text")

html_pattern = re.compile(r'(<div class="container">\s*<div class="resume-wrapper">)(.*?)(</div>\s*</div>\s*</div>\s*</body>)', re.DOTALL)

new_html_content = """
            <!-- Header -->
            <div class="header">
                <img src="/profile.jpeg" alt="PAULWIN S R" class="profile-photo">
                <div class="header-content">
                    <h1>PAULWIN S R</h1>
                    <p class="title">Full-stack Software Engineer</p>
                    <div class="contact-info">
                        <div class="contact-item">
                            <span class="contact-icon">🏠︎</span>
                            <span>Trivandrum, India</span>
                        </div>
                        <div class="contact-item">
                            <span class="contact-icon">✉︎</span>
                            <a href="paulwinpaul2001@gmail.com">paulwinpaul2001@gmail.com</a>
                        </div>
                        <div class="contact-item">
                            <span class="contact-icon">🆆</span>
                            <a href="https://paulwin-singh-rouge.vercel.app/" target="_blank">Portfolio Website</a>
                        </div>
                        <div class="contact-item">
                            <span class="contact-icon">⛆</span>
                            <a href="https://github.com/paulwin" target="_blank">paulwin</a>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Main Content -->
            <div class="content">
                <!-- Professional Summary -->
                <section class="section">
                    <h2 class="section-title">Profile</h2>
                    <div class="summary-text">
                        Full-stack Software Engineer with hands-on experience in database design, data collection systems, and backend development using MongoDB, SQL, and Python. Skilled in data extraction, transformation, and analysis, with a strong focus on data accuracy and system integration. Looking to leverage software engineering expertise in a data analyst role to deliver actionable insights.
                    </div>
                </section>

                <!-- Work Experience -->
                <section class="section">
                    <h2 class="section-title">Work Experience</h2>
                    <div class="education-item">
                        <h3>Software Engineer - Trivand Technologies</h3>
                        <p style="color: #888; font-size: 12px; margin-bottom: 8px;">06/2024 – present</p>
                        <p>• Full-stack developer with experience in developing web applications and managing database collections using MongoDB and SQL.</p>
                    </div>
                </section>

                <!-- Technical Skills -->
                <section class="section">
                    <h2 class="section-title">Skills</h2>
                    <div class="skills-grid">
                        <div class="skill-category">
                            <h3>Technical Skills</h3>
                            <div class="skill-tags">
                                <span class="skill-tag">Java</span>
                                <span class="skill-tag">HTML/CSS/JS</span>
                                <span class="skill-tag">SQL</span>
                                <span class="skill-tag">React & Node.js</span>
                                <span class="skill-tag">MongoDB</span>
                                <span class="skill-tag">Express.js</span>
                                <span class="skill-tag">Adobe Photoshop</span>
                                <span class="skill-tag">TypeScript</span>
                                <span class="skill-tag">Prompt Engineering</span>
                            </div>
                        </div>
                        <div class="skill-category">
                            <h3>Soft Skills</h3>
                            <div class="skill-tags">
                                <span class="skill-tag">Communication</span>
                                <span class="skill-tag">Teamwork</span>
                                <span class="skill-tag">Time Management</span>
                                <span class="skill-tag">Empathetic</span>
                                <span class="skill-tag">Report Preparation</span>
                                <span class="skill-tag">Problem Solving</span>
                                <span class="skill-tag">Quick learner</span>
                            </div>
                        </div>
                    </div>
                </section>

                <!-- Projects -->
                <section class="section">
                    <h2 class="section-title">Projects</h2>
                    <div class="section-content">
                        <div class="project">
                            <h3>Cyber-bullying Detection</h3>
                            <p>The purpose is to design and develop an effective technique to detect online abusive and bullying messages by merging natural language processing and machine learning.</p>
                        </div>
                        <div class="project">
                            <h3>Food Donation System (Mini Project)</h3>
                            <p>This website revolves around helping the needy by connecting donors and donation recipients. The goal of this website is to reduce food waste and feed the needy.</p>
                        </div>
                    </div>
                </section>

                <!-- Education -->
                <section class="section">
                    <h2 class="section-title">Education</h2>
                    <div class="education-item" style="margin-bottom: 12px;">
                        <h3>B. Tech in Computer Science and Engineering</h3>
                        <p>Lourdes Matha College of Science and Technology (2019 – 2023) | CGPA: 6.74</p>
                    </div>
                    <div class="education-item" style="margin-bottom: 12px;">
                        <h3>Higher Secondary Education</h3>
                        <p>M. C. H. S. S Kottukalkonam (2017 – 2019) | 72%</p>
                    </div>
                    <div class="education-item">
                        <h3>Secondary School Education</h3>
                        <p>N. S. S. PUBLIC SCHOOL Perunthanni (2017) | 82%</p>
                    </div>
                </section>

                <!-- Internships & Certificates -->
                <section class="section">
                    <h2 class="section-title">Internships & Certificates</h2>
                    <div class="section-content">
                        <div class="project">
                            <h3>Internships</h3>
                            <p>• Java Full Stack Development (08/2023 – 04/2024)</p>
                        </div>
                        <div class="project">
                            <h3>Certificates & Workshops</h3>
                            <p>• Certificate for completion of Python 3.4.3 Training</p>
                            <p>• 6 days internship programme on 'Scientific Computing with Python'</p>
                            <p>• Workshop on "Artificial Intelligence Creating the Future" and "Exploring Machine Learning techniques in Data Mining"</p>
                            <p>• AI for All Certificate – AI for All Program (2026)</p>
                        </div>
                    </div>
                </section>

                <!-- Languages -->
                <section class="section">
                    <h2 class="section-title">Languages</h2>
                    <div class="strengths-list">
                        <div class="strength-item">
                            <span class="strength-icon">✔</span>
                            <p>English (Professional Working Proficiency)</p>
                        </div>
                        <div class="strength-item">
                            <span class="strength-icon">✔</span>
                            <p>Malayalam (Native or Bilingual)</p>
                        </div>
                    </div>
                </section>
            </div>
        """

if html_pattern.search(content):
    content = html_pattern.sub(r'\1' + new_html_content + r'\3', content)
else:
    print("Could not find HTML pattern")

with open(file_path, "w") as f:
    f.write(content)

print("Update completed.")
