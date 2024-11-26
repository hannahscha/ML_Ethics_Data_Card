import streamlit as st

# Title
st.title("Ethics Data Card Checklist")

# Introduction
st.write("""
This checklist ensures that the ethical considerations of this project are properly addressed and documented. Below is a detailed breakdown of the ethical evaluation for this project.
""")

# Sections of the checklist
st.header("1. Project Purpose and Scope")
st.write("""
- **What is the primary purpose of this project, and how does it benefit stakeholders?**
  - The purpose of this project is to determine if a student will likely pass or fail a course using machine learning and historical data about students' lives and performance. This can help prioritize students needing extra support and reveal insights into aspects of their lives most correlated with their performance for targeted help.
- **Is the project scope clear and justifiable in terms of ethical impact?**
  - The project scope is clear as it helps determine performance in a specific course based on personal attributes while keeping student identities anonymous. It is emphasized that the model should not be used in isolation but as a complement to instructor evaluations.
""")

st.header("2. Data Sources and Reliability")
st.write("""
- **What are the sources of data, and are they credible and ethical?**
  - The data is sourced from a public dataset on Kaggle, containing records of 395 students from two secondary schools in Portugal, reflecting various academic and personal attributes.
- **Are potential biases in the data sources acknowledged and mitigated?**
  - The dataset reflects the demographics of the two schools involved, with potential biases from their geographic and cultural context. These biases are acknowledged and addressed through transparency to users.
""")

st.header("3. Stakeholder Transparency")
st.write("""
- **Are stakeholders informed about the project's aims, data use, and potential outcomes?**
  - Stakeholders, including students, instructors, and their families, were informed via a survey. Student data is anonymized using ID numbers to protect identities.
- **Is there clear documentation accessible to stakeholders for full transparency?**
  - Documentation on the project's usage and performance impacts will be maintained and made accessible within the school district.
""")

st.header("4. Bias and Fairness Checks")
st.write("""
- **Has the project undergone rigorous checks to identify and mitigate biases?**
  - Feature distributions and data collection methods were analyzed and shared to ensure representation. The project emphasizes that the model should not be the sole tool for identifying at-risk students.
- **How does the project ensure fairness in its outputs, especially for marginalized groups?**
  - The model predicts average student performance to help flag at-risk students while acknowledging potential biases in the dataset. These biases are documented and disclosed to the users.
""")

st.header("5. Data Protection and Anonymization")
st.write("""
- **Are data protection measures like anonymization in place?**
  - Students' identities are anonymized using unique ID numbers.
- **How does the project secure data to prevent unauthorized access?**
  - The model is designed for use within the school district, with a disclosure that it is not intended for use outside its scope or as a standalone decision-making tool.
""")

st.header("6. Ethical Impact Assessment")
st.write("""
- **Are there mechanisms to assess and track the ethical impact of the project over time?**
  - The model's impact will be monitored through periodic surveys and comparisons of student performance before and after implementation.
- **Have potential risks been identified, and are there mitigation strategies in place?**
  - Risks, such as instructors over-relying on the model or overlooking students, are addressed through training and emphasizing the model's supportive role rather than as a standalone tool.
""")

st.header("7. Ongoing Monitoring and Accountability")
st.write("""
- **Is there a plan for ongoing monitoring of the project's ethical impact?**
  - Student performance will be continuously recorded and analyzed to identify potential biases or disproportional impacts. The model will be updated as needed to reflect new data and demographics.
- **Are roles and responsibilities clearly defined to ensure accountability?**
  - Instructors are responsible for using the model ethically, with school districts monitoring its impacts and training users on proper implementation.
""")
