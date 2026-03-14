# PDF Launcher

A small command-line utility for opening and searching PDF files on Windows. The CLI normalizes paths to absolute paths and delegates file opening to the system default PDF viewer.

**Overview**

PDF Launcher helps you:
- Open a PDF by path.
- Search a folder (recursively) for PDF files.
- View a history of opened files and searches.

**Features**

- Open PDFs with the default Windows viewer.
- Recursive search for `.pdf` files in a directory.
- History tracking for opened files and search locations.
- Simple CLI with three subcommands: `open`, `search`, `recent`.

**Requirements**

- Windows (uses `os.startfile`).
- Python 3.8+.
- Third-party dependency: `tabulate` (used to format tables).

**Installation**

Windows (recommended):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install tabulate
```

**Usage**

The CLI uses absolute paths internally. You can pass relative paths; they will be normalized by the parser.

Open a PDF:

```powershell
python main.py open "C:\path\to\file.pdf"
```

Search a folder for PDFs:

```powershell
python main.py search "C:\path\to\folder"
```

Show history:

```powershell
python main.py recent
```

**Data & History**

History is stored in `data/history.json` and is updated when you open files or run searches. The current schema uses these top-level keys (kept as-is for compatibility):

- `opend_files`: list of opened file records.
- `search_history`: list of search records.

Example shape:

```json
{
  "opend_files": [
    {
      "filename": "Report.pdf",
      "path": "C:\\docs\\Report.pdf",
      "opend-at": "2026-03-12 20:37:22"
    }
  ],
  "search_history": [
    {
      "path": "C:\\docs",
      "date": "2026-03-12 21:46:50"
    }
  ]
}
```

**Project Layout**

```text
pdf-launcher/
│
├── features/
│   ├── pdf_launcher.py
│   ├── pdf_searcher.py
│   └── history_manager.py
│
├── utils/
│   └── input_validator.py
│
├── data/
|  └── history.json
├── main.py
├── requirements.txt
└── README.md 
```

**Limitations**

- Windows-only: relies on `os.startfile`.
- `data/history.json` must exist and contain valid JSON before running commands.

**Roadmap / Improvements**

- Add cross-platform open support (macOS `open`, Linux `xdg-open`).
- Create a proper package with a console entrypoint (`pdf-launcher`).
- Initialize and validate history storage automatically on first run.
- Add tests for validators, search, and history behavior.

**License**

Not specified yet.
