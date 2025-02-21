# UI Testing Project with Selenium, Cucumber, and Python

## 📌 Project Overview
This project performs **UI Testing** using:
- **Selenium** for browser automation
- **Cucumber (Behave)** for BDD
- **Pytest** for test execution
- **Jenkins** for CI/CD

## 🚀 How to Run Locally
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo.git
   cd your-repo

2. Install dependencies:
    ```bash
   pip install -r requirements.txt

3. Run tests:
    ```bash
   python test_runner.py
   
## 🛠 Running in Jenkins
    Add the Jenkinsfile to your pipeline
    Configure Jenkins to execute the pipeline

## 📝 Reporting
- Test results are stored in reports/
- Jenkins will show JUnit reports

## ✅ Allure report
- Allure reports are getting generated automatically. To disable this report make ENABLE_REPORT = False in test_runner.py file
- To view the allure report run following command in the project directory update the YYYY-MM-DD_HH-MM-SS accordingly.

      allure open reports/allure_report_YYYY-MM-DD_HH-MM-SS/html
- Delete all allure report folders before commiting the code to git.

### ✅ **Final Notes**
- These files will **help structure your project** properly  
- They ensure **smooth execution in PyCharm, CMD, and Jenkins**  
- Modify as needed for **your specific project setup**  

