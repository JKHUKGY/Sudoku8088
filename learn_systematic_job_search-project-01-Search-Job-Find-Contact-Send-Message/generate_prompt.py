#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Manual Prompt Generator Script

Comment in/out the generators you want to run, then execute:
    python generate_prompt.py
"""

from pathlib import Path

from prompt_generator import (
    generate_linkedin_cold_message_prompt,
    generate_linkedin_contact_finder_prompt,
    generate_linkedin_job_search_prompt,
)


def main() -> None:
    """Main entry point for manual prompt generation."""
    base_dir = Path(__file__).parent.resolve()

    # Comment in/out the generators you want to run:
    # generate_linkedin_job_search_prompt(base_dir)
    # generate_linkedin_contact_finder_prompt(base_dir)
    generate_linkedin_cold_message_prompt(base_dir)


if __name__ == "__main__":
    main()
