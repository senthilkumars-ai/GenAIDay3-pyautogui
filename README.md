# Automated Daily Website Report Generator

## Overview

This Python script automates the process of:

1. Opening a website in the default browser.
2. Capturing text content from the webpage.
3. Extracting a headline/summary from the copied content.
4. Launching Microsoft Excel.
5. Creating a new workbook and entering report data.
6. Saving the workbook with the current date.
7. Taking a screenshot of the desktop.
8. Storing all generated files in a `reports` folder.

The script is designed for simple daily reporting and status tracking tasks.

---

## Features

* Automated website access
* Automatic data capture from webpage
* Timestamp generation
* Excel report creation
* Automated workbook saving
* Screenshot capture
* Daily file naming based on current date
* Report organization inside a dedicated folder

---

## Requirements

### Python Version

* Python 3.8+

### Required Packages

Install dependencies using:

```bash
pip install pyautogui pyperclip
```

### Additional Requirements

* Microsoft Excel installed
* Windows operating system
* Default web browser configured
* Sufficient screen resolution for GUI automation

---

## Configuration

Modify the following variables at the top of the script:

```python
WEBSITE_URL = "https://www.artificialintelligence-news.com/"
COMMENT = "Daily status generated automatically"
```

### WEBSITE_URL

The website from which data will be collected.

### COMMENT

A custom comment inserted into the generated report.

---

## Output

The script automatically creates a folder:

```text
reports/
```

Generated files:

### Excel Report

```text
daily_report_YYYY-MM-DD.xlsx
```

Example:

```text
daily_report_2026-06-21.xlsx
```

### Screenshot

```text
daily_report_YYYY-MM-DD.png
```

Example:

```text
daily_report_2026-06-21.png
```

---

## Report Structure

The generated Excel workbook contains:

| Date & Time | Website Data           | Comment            |
| ----------- | ---------------------- | ------------------ |
| Timestamp   | Captured headline text | Configured comment |

Example:

| Date & Time         | Website Data               | Comment                              |
| ------------------- | -------------------------- | ------------------------------------ |
| 2026-06-21 09:15:22 | Latest AI news headline... | Daily status generated automatically |

---

## How It Works

### 1. Open Website

The script launches the configured URL using the default browser.

### 2. Capture Content

The webpage content is selected and copied using keyboard shortcuts:

```text
Ctrl + A
Ctrl + C
```

### 3. Extract Headline

The first 100 characters of the copied text are used as a headline/summary.

### 4. Launch Excel

Excel is opened automatically and a new workbook is created.

### 5. Populate Data

Headers and report data are entered into the worksheet using clipboard-based automation.

### 6. Save Workbook

The workbook is saved using a date-based filename.

### 7. Take Screenshot

A screenshot is captured and stored in the reports directory.

### 8. Close Excel

Excel is closed and focus returns to the previous application.

---

## Running the Script

Execute:

```bash
python report_generator.py
```

Console output example:

```text
Opening browser...
Copying website data...
Data Captured: Latest AI industry updates...

Opening Excel...
Entering data into Excel...
Saving workbook...
Taking screenshot...

===== REPORT GENERATED =====
Excel File : reports/daily_report_2026-06-21.xlsx
Screenshot : reports/daily_report_2026-06-21.png
============================
Automation Process completed successfully.
```

---

## Notes

* GUI automation relies on screen focus and timing.
* Avoid using the keyboard or mouse while the script is running.
* Some websites may block or limit content copying.
* If Excel opens slowly on your system, increase the `wait()` durations.
* Ensure Excel is available in the system PATH for automatic launching.

---

## Limitations

* Windows-specific Excel launch command.
* Depends on GUI interactions rather than Excel APIs.
* Browser window must remain active during data capture.
* Timing delays may need adjustment on slower machines.

---

## Future Improvements

* Use `openpyxl` instead of GUI-based Excel automation.
* Add logging support.
* Export reports to CSV and PDF.
* Capture specific webpage elements.
* Add scheduling with Windows Task Scheduler.
* Improve error handling and recovery.
* Support multiple websites.

---

## License

This project is provided as-is for educational and automation purposes.
