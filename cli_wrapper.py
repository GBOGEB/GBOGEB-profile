#!/usr/bin/env python3
"""
CLI wrapper for the Digital Twin Parser.
Provides command-line interface for parsing DOCX documents.
"""

import argparse
import os
import sys
from main import main_process

def main():
    parser = argparse.ArgumentParser(
        description="Digital Twin Parser: Convert DOCX documents to structured data and Markdown.",
        formatter_class=argparse.RawTextHelpFormatter
    )
    
    parser.add_argument(
        "input_docx",
        type=str,
        help="Path to the input DOCX file"
    )
    
    parser.add_argument(
        "--output-md",
        type=str,
        default="output/MAIN.md",
        help="Path for the output Markdown file (default: output/MAIN.md)"
    )
    
    parser.add_argument(
        "--output-json",
        type=str,
        default="output/MAIN_STRUCTURED_DATA.json",
        help="Path for the output JSON file (default: output/MAIN_STRUCTURED_DATA.json)"
    )
    
    args = parser.parse_args()
    
    # Validate input file exists
    if not os.path.exists(args.input_docx):
        print(f"ERROR: Input file '{args.input_docx}' not found.")
        sys.exit(1)
    
    # Ensure output directories exist
    os.makedirs(os.path.dirname(args.output_md), exist_ok=True)
    os.makedirs(os.path.dirname(args.output_json), exist_ok=True)
    
    # Run the main processing
    main_process(args.input_docx, args.output_md, args.output_json)

if __name__ == "__main__":
    main()