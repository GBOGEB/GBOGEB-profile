#!/usr/bin/env python3
"""
Digital Twin Parser - Core functionality
Converts DOCX documents to structured data and Markdown.
"""

import os
import json
from typing import Dict, Any, List

def docx_to_structured_data(docx_path: str) -> Dict[str, Any]:
    """
    Parse DOCX file into structured data.
    In a real implementation, this would use python-docx to extract
    content, styles, list numbering, and attempt to interpret SEQ/LISTNUM fields.
    """
    print(f"DEBUG: Parsing DOCX file: {docx_path}")
    
    # Example structure - replace with actual parsing logic
    structured_data = {
        "metadata": {
            "title": "MYRRHA Cryoplant Technical Requirements",
            "source_file": os.path.basename(docx_path),
            "version": "1.0.0"
        },
        "content_blocks": [
            {
                "type": "heading",
                "level": 1,
                "word_style": "Heading 1",
                "outline_number": "1",
                "text": "Introduction",
                "location_id": "h1-intro",
                "line_start": 1,
                "properties": {"font_size": "24pt", "color": "#003f5c"}
            },
            {
                "type": "paragraph",
                "word_style": "Normal",
                "text": "This document outlines the technical requirements for the MYRRHA Cryoplant (QPLANT) based on the Deep Research report.",
                "location_id": "p1",
                "line_start": 3,
                "properties": {"font_size": "12pt", "color": "#374c80"}
            },
            {
                "type": "table",
                "table_id": "table1",
                "headers": ["Estimated weight", "Cryomodule (QM)", "For 1 QM", "Cold Valve Box (QVB)", "For 1 QM", "Cryogenic lines 4.5 K pipes", "TOTAL cold mass for 30 cryomodules (4.5 K-2 K)"],
                "rows": [
                    ["Component A", "1000 kg", "500 kg", "200 kg", "100 kg", "50 kg", "52500 kg"],
                    ["Component B", "800 kg", "400 kg", "150 kg", "75 kg", "25 kg", "42750 kg"]
                ],
                "location_id": "table1",
                "line_start": 5
            }
        ]
    }
    return structured_data

def structured_data_to_markdown(structured_data: Dict[str, Any]) -> str:
    """
    Convert structured data to Markdown format.
    """
    print("DEBUG: Converting structured data to Markdown...")
    
    markdown_lines = []
    
    # Add title from metadata
    markdown_lines.append(f"# {structured_data['metadata']['title']}")
    markdown_lines.append("")
    
    # Process content blocks
    for block in structured_data['content_blocks']:
        if block['type'] == 'heading':
            markdown_lines.append('#' * block['level'] + ' ' + block['text'])
        elif block['type'] == 'paragraph':
            markdown_lines.append(block['text'])
        elif block['type'] == 'table':
            # Add table headers
            markdown_lines.append('| ' + ' | '.join(block['headers']) + ' |')
            markdown_lines.append('|' + '---|' * len(block['headers']))
            # Add table rows
            for row in block['rows']:
                markdown_lines.append('| ' + ' | '.join(row) + ' |')
        
        markdown_lines.append("")
    
    return '\n'.join(markdown_lines)

def main_process(input_docx: str, output_md: str, output_json: str):
    """
    Main processing function that orchestrates the conversion.
    """
    print(f"INFO: Starting digital twin parsing for '{input_docx}'...")
    
    # Step 1: DOCX to Structured Data
    structured_data = docx_to_structured_data(input_docx)
    
    # Save structured data as JSON
    with open(output_json, 'w', encoding='utf-8') as f:
        json.dump(structured_data, f, indent=2, ensure_ascii=False)
    print(f"INFO: Structured data saved to '{output_json}'")
    
    # Step 2: Structured Data to Markdown
    markdown_content = structured_data_to_markdown(structured_data)
    with open(output_md, 'w', encoding='utf-8') as f:
        f.write(markdown_content)
    print(f"INFO: Markdown output saved to '{output_md}'")
    
    print("INFO: Digital twin parsing complete.")

if __name__ == "__main__":
    # Example usage
    input_docx = os.path.join('input', '0604_parseme.docx')
    output_markdown = os.path.join('output', 'MAIN.md')
    output_structured_json = os.path.join('output', 'MAIN_STRUCTURED_DATA.json')
    
    # Create input and output directories if they don't exist
    os.makedirs('input', exist_ok=True)
    os.makedirs('output', exist_ok=True)
    
    # Check if input file exists
    if not os.path.exists(input_docx):
        print(f"WARNING: Input DOCX '{input_docx}' not found. Using dummy data.")
    
    main_process(input_docx, output_markdown, output_structured_json)