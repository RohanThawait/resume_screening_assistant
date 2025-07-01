from pathlib import Path
from pdf_parser import parse_all_resumes
from utils import save_json


def main():
    # Define paths using Pathlib for OS-independent handling
    resume_folder = Path("C:/Users/Rohan/Projects/project_1/resume_screening_assistant/data/resumes")
    output_file = Path("C:/Users/Rohan/Projects/project_1/resume_screening_assistant/data/resume_texts.json")

    # Parse resumes and save to JSON
    resumes = parse_all_resumes(resume_folder)
    save_json(resumes, output_file)

    print(f"✅ Parsed and saved {len(resumes)} resumes to '{output_file}'.")


if __name__ == "__main__":
    main()
