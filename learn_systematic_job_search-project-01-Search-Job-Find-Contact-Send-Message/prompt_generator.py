#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Prompt Generator Library & CLI

This module generates prompt files from templates by:
1. Reading template files with placeholders ({{PLACEHOLDER}})
2. Replacing placeholders with content from source files
3. Removing HTML comments (<!-- ... -->)
4. Writing the processed output to destination files

Usage as CLI:
    python prompt_generator.py job-search
    python prompt_generator.py contact-finder
    python prompt_generator.py cold-message

Usage as library:
    from prompt_generator import generate_linkedin_job_search_prompt
    generate_linkedin_job_search_prompt(base_dir)
"""

import argparse
import re
import sys
from pathlib import Path


# =============================================================================
# Core Utility Functions (Reusable)
# =============================================================================

def read_file(file_path: Path) -> str:
    """Read and return the content of a file."""
    return file_path.read_text(encoding="utf-8")


def write_file(file_path: Path, content: str) -> None:
    """Write content to a file, creating parent directories if needed."""
    file_path.parent.mkdir(parents=True, exist_ok=True)
    file_path.write_text(content, encoding="utf-8")


def remove_html_comments(content: str) -> str:
    """
    Remove HTML comments from content.
    Handles both single-line and multi-line comments.
    Pattern: <!-- ... -->
    """
    # DOTALL flag allows . to match newlines for multi-line comments
    pattern = r"<!--.*?-->"
    return re.sub(pattern, "", content, flags=re.DOTALL)


def replace_placeholders(content: str, replacements: dict[str, str]) -> str:
    """
    Replace {{PLACEHOLDER}} patterns with corresponding values.

    Args:
        content: The template content with placeholders
        replacements: Dict mapping placeholder names to replacement values
                     e.g., {"RESUME_CONTENT": "actual resume text"}

    Returns:
        Content with all placeholders replaced
    """
    result = content
    for placeholder, value in replacements.items():
        pattern = "{{" + placeholder + "}}"
        result = result.replace(pattern, value)
    return result


def process_template(
    template_content: str,
    replacements: dict[str, str],
    remove_comments: bool = True,
) -> str:
    """
    Process a template by replacing placeholders and optionally removing comments.

    Args:
        template_content: The raw template content
        replacements: Dict of placeholder name -> replacement value
        remove_comments: Whether to remove HTML comments (default: True)

    Returns:
        Processed content ready for output
    """
    result = replace_placeholders(template_content, replacements)
    if remove_comments:
        result = remove_html_comments(result)
    return result


def generate_prompt_from_template(
    template_path: Path,
    output_path: Path,
    replacements: dict[str, str],
    remove_comments: bool = True,
) -> None:
    """
    Generate a prompt file from a template.

    Args:
        template_path: Path to the template file
        output_path: Path where the output will be written
        replacements: Dict of placeholder name -> replacement value
        remove_comments: Whether to remove HTML comments
    """
    template_content = read_file(template_path)
    processed_content = process_template(
        template_content, replacements, remove_comments
    )
    write_file(output_path, processed_content)
    print(f"Generated: {output_path}")


# =============================================================================
# Specific Prompt Generators
# =============================================================================

def generate_linkedin_job_search_prompt(base_dir: Path) -> None:
    """
    Generate the LinkedIn job search prompt from template.

    Reads:
        - docs/linkedin-job-search-prompt.template.md (template)
        - profile/resume.md
        - profile/objective.md
        - profile/narrative.md

    Outputs:
        - docs/linkedin-job-search-prompt.md
    """
    # Define paths
    template_path = base_dir / "docs" / "linkedin-job-search-prompt.template.md"
    output_path = base_dir / "docs" / "linkedin-job-search-prompt.md"

    profile_dir = base_dir / "profile"

    # Read source files for replacements
    replacements = {
        "RESUME_CONTENT": read_file(profile_dir / "resume.md"),
        "OBJECTIVE_CONTENT": read_file(profile_dir / "objective.md"),
        "NARRATIVE_CONTENT": read_file(profile_dir / "narrative.md"),
    }

    # Read additional requirements for job search
    replacements["ADDITIONAL_REQUIREMENTS"] = read_file(
        profile_dir / "job-search-additional-requirements.md"
    )

    # Generate the prompt
    generate_prompt_from_template(
        template_path=template_path,
        output_path=output_path,
        replacements=replacements,
        remove_comments=True,
    )


def generate_linkedin_contact_finder_prompt(base_dir: Path) -> None:
    """
    Generate the LinkedIn contact finder prompt from template.

    Reads:
        - docs/linkedin-contact-finder-prompt.template.md (template)
        - profile/job-description.md
        - profile/resume.md

    Outputs:
        - docs/linkedin-contact-finder-prompt.md
    """
    template_path = base_dir / "docs" / "linkedin-contact-finder-prompt.template.md"
    output_path = base_dir / "docs" / "linkedin-contact-finder-prompt.md"

    profile_dir = base_dir / "profile"

    replacements = {
        "JOB_DESCRIPTION": read_file(profile_dir / "job-description.md"),
        "RESUME": read_file(profile_dir / "resume.md"),
        "SEARCH_PREFERENCES": "",  # Optional, leave empty by default
    }

    generate_prompt_from_template(
        template_path=template_path,
        output_path=output_path,
        replacements=replacements,
        remove_comments=True,
    )


def generate_linkedin_cold_message_prompt(base_dir: Path) -> None:
    """
    Generate the LinkedIn cold message prompt from template.

    Reads:
        - docs/linkedin-cold-message-prompt.template.md (template)
        - profile/resume.md
        - profile/job-description.md
        - profile/code-message-target-person.md
        - profile/code-message-out-reach-key.md
        - profile/code-message-outcome.md

    Outputs:
        - docs/linkedin-cold-message-prompt.md
    """
    template_path = base_dir / "docs" / "linkedin-cold-message-prompt.template.md"
    output_path = base_dir / "docs" / "linkedin-cold-message-prompt.md"

    profile_dir = base_dir / "profile"

    replacements = {
        "RESUME": read_file(profile_dir / "resume.md"),
        "JOB_DESCRIPTION": read_file(profile_dir / "job-description.md"),
        "TARGET_PERSON": read_file(profile_dir / "code-message-target-person.md"),
        "OUTREACH_KEY": read_file(profile_dir / "code-message-out-reach-key.md"),
        "OBJECTIVE": read_file(profile_dir / "code-message-outcome.md"),
    }

    generate_prompt_from_template(
        template_path=template_path,
        output_path=output_path,
        replacements=replacements,
        remove_comments=True,
    )


# =============================================================================
# CLI Entry Point
# =============================================================================

# Map CLI argument to generator function
GENERATORS = {
    "job-search": generate_linkedin_job_search_prompt,
    "contact-finder": generate_linkedin_contact_finder_prompt,
    "cold-message": generate_linkedin_cold_message_prompt,
}


def main() -> int:
    """CLI entry point."""
    parser = argparse.ArgumentParser(
        description="Generate prompt files from templates.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Available prompt types:
  job-search      Generate LinkedIn job search prompt
  contact-finder  Generate LinkedIn contact finder prompt
  cold-message    Generate LinkedIn cold message prompt

Examples:
  python prompt_generator.py job-search
  python prompt_generator.py contact-finder
  python prompt_generator.py cold-message
""",
    )
    parser.add_argument(
        "prompt_type",
        choices=GENERATORS.keys(),
        help="Type of prompt to generate",
    )

    args = parser.parse_args()

    # Get the base directory (where this script is located)
    base_dir = Path(__file__).parent.resolve()

    # Run the appropriate generator
    generator = GENERATORS[args.prompt_type]
    generator(base_dir)

    return 0


if __name__ == "__main__":
    sys.exit(main())
