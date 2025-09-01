# Digital Twin Parser for DOCX Documents

Digital Twin Parser is a Python-based Jupyter notebook project that converts Microsoft Word DOCX documents into structured JSON data and Markdown format. The project provides both notebook and command-line interfaces for document processing.

Always reference these instructions first and fallback to search or bash commands only when you encounter unexpected information that does not match the info here.

## Working Effectively

### Bootstrap and Setup (NEVER CANCEL)
- Install Python dependencies: `pip3 install --user jupyter python-docx` -- takes 2-3 minutes. NEVER CANCEL. Set timeout to 5+ minutes.
- Verify installation: `python3 -c "import jupyter, docx; print('Dependencies OK')"`
- Check Python version: `python3 --version` (requires Python 3.7+)

### Build and Test the Repository
- No formal build process required - this is a pure Python project
- Run comprehensive tests: `python3 test_all.py` -- takes 30 seconds. NEVER CANCEL. Set timeout to 2+ minutes.
- Create sample DOCX for testing: `python3 create_sample.py` -- takes <1 second
- Test core functionality: `python3 main.py` -- takes <1 second

### Run the Digital Twin Parser
- **Main Python script**: `python3 main.py` 
- **CLI interface**: `python3 cli_wrapper.py input/your_file.docx`
- **Jupyter notebook**: `jupyter notebook --no-browser --port=8888` -- starts in 2-3 seconds. NEVER CANCEL.
- **Convert notebook to Python**: `jupyter nbconvert --to python Digital_Twin_Parser_Starter_Pack.ipynb` -- takes 2-3 seconds. NEVER CANCEL.

## Validation

### Always Run Manual Validation After Changes
1. **Create sample DOCX**: Run `python3 create_sample.py` to generate test input
2. **Test main parser**: Run `python3 main.py` and verify both `output/MAIN.md` and `output/MAIN_STRUCTURED_DATA.json` are created
3. **Test CLI wrapper**: Run `python3 cli_wrapper.py input/0604_parseme.docx` and verify output files
4. **Validate JSON structure**: Ensure output JSON contains `metadata` and `content_blocks` keys
5. **Check Markdown output**: Verify readable Markdown is generated with headers, paragraphs, and tables

### Complete End-to-End Scenario Testing
- ALWAYS test the complete document parsing workflow: DOCX → JSON → Markdown
- Test with both dummy data (when no DOCX exists) and real DOCX files
- Verify CLI help works: `python3 cli_wrapper.py --help`
- Test Jupyter notebook conversion (may show warnings but should complete)

## Common Tasks

### Working with the Digital Twin Parser
- **Input directory**: `input/` - place DOCX files here
- **Output directory**: `output/` - generated JSON and Markdown files appear here
- **Main processing**: Handled by `main.py` with functions `docx_to_structured_data()` and `structured_data_to_markdown()`
- **CLI wrapper**: Use `cli_wrapper.py` for command-line processing with custom output paths

### Repository Structure
```
/
├── Digital_Twin_Parser_Starter_Pack.ipynb  # Main Jupyter notebook (contains all code)
├── main.py                                  # Extracted core functionality
├── cli_wrapper.py                           # Command-line interface
├── create_sample.py                         # Generate test DOCX files
├── test_all.py                              # Comprehensive test suite
├── input/                                   # Input DOCX files
├── output/                                  # Generated JSON and Markdown outputs
├── README.md                                # Basic repository info
└── AGENT_0606_GG, Word_rountrip_en_shit    # Additional notebook files (JSON format)
```

### Key Files and Their Purpose
- **main.py**: Core parser logic with `main_process()`, `docx_to_structured_data()`, and `structured_data_to_markdown()`
- **cli_wrapper.py**: Command-line interface for the parser
- **Digital_Twin_Parser_Starter_Pack.ipynb**: Original Jupyter notebook with all code and documentation
- **create_sample.py**: Utility to create test DOCX files using python-docx
- **test_all.py**: Comprehensive test suite that validates all functionality

### Timing Expectations and Timeouts
- **Dependency installation**: 2-3 minutes. NEVER CANCEL. Use 5+ minute timeout.
- **Document parsing**: <1 second for typical documents
- **Jupyter notebook operations**: 2-3 seconds. NEVER CANCEL. Use 1+ minute timeout.
- **Test suite execution**: 30 seconds total. NEVER CANCEL. Use 2+ minute timeout.
- **Sample DOCX creation**: <1 second

### Dependencies and Requirements
- **Python**: 3.7+ (tested with 3.12.3)
- **Required packages**: `jupyter`, `python-docx`
- **Optional packages**: Standard library modules (`os`, `json`, `argparse`)
- **Installation command**: `pip3 install --user jupyter python-docx`

### Error Handling and Known Issues
- **Missing input DOCX**: Parser gracefully handles missing files with dummy data
- **Notebook conversion warnings**: Expected due to Colab-specific JSON format in original notebook
- **No build failures**: This is a pure Python project with no compilation step
- **Import errors**: Run dependency installation if `import jupyter, docx` fails

### Development Workflow
1. Make changes to `main.py` for core functionality
2. Update `cli_wrapper.py` for command-line interface changes  
3. Test changes with `python3 test_all.py`
4. Validate with manual end-to-end testing
5. Update notebook if needed (though main development happens in Python files)

### Validation Commands Reference
```bash
# Quick validation
python3 -c "import jupyter, docx; print('Dependencies OK')"
python3 main.py
python3 cli_wrapper.py --help

# Full validation
python3 test_all.py

# Manual end-to-end test
python3 create_sample.py
python3 main.py
ls -la output/
cat output/MAIN.md
```

## Critical Notes
- **NEVER CANCEL** dependency installations or Jupyter operations - they need time to complete
- Always test both with and without actual DOCX files (parser handles both scenarios)
- The project creates `input/` and `output/` directories automatically
- JSON output includes structured metadata and content blocks for downstream processing
- Markdown output provides human-readable document representation
- No linting or formal testing framework - use the provided `test_all.py` for validation