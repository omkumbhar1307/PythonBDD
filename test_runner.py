import os
import sys
import subprocess
import time

# Set this to False to disable report generation
ENABLE_REPORT = False

def run_behave_tests(dry_run=False):
    features_dir = os.path.join(os.path.dirname(__file__), "features")

    if not os.path.exists(features_dir):
        print(f"Error: {features_dir} does not exist!")
        sys.exit(1)

    # Add --dry-run if needed
    dry_run_flag = "--dry-run" if dry_run else ""

    # Add --no-capture to allow print() output
    command = f'behave "{features_dir}" --format pretty {dry_run_flag} --no-capture'

    # Run tests
    result = subprocess.run(command, shell=True)

    # Generate Allure report only if enabled and not in dry-run mode
    if ENABLE_REPORT and not dry_run:
        generate_allure_report(features_dir)

    sys.exit(result.returncode)

def generate_allure_report(features_dir):
    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    report_dir = f"reports/allure_report_{timestamp}"

    # Ensure reports directory exists
    os.makedirs(report_dir, exist_ok=True)

    # Run Behave again to generate Allure results
    behave_command = f'behave "{features_dir}" -f allure_behave.formatter:AllureFormatter -o {report_dir}/'
    os.system(behave_command)

    # Generate Allure HTML report
    os.system(f"allure generate {report_dir}/ -o {report_dir}/html --clean")

    print(f"Allure report generated at: {report_dir}/html")
    print(f"To view the report, run: allure open {report_dir}/html\n")

if __name__ == "__main__":
    run_behave_tests(dry_run=False)  # Set to True for dry-run mode