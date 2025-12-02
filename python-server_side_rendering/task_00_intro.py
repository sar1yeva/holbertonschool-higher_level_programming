#!/usr/bin/python3
"""
Task 0: Simple templating program
Generates invitation files based on a template and attendee data.
"""

import os


def generate_invitations(template, attendees):
    """
    Generates personalized invitation files from a template and list of attendees.

    Args:
        template (str): The invitation template string.
        attendees (list): A list of dictionaries containing attendee data.

    Behavior:
        - Validates input types
        - Handles empty template
        - Handles empty attendees list
        - Replaces missing fields with "N/A"
        - Generates output_X.txt files for each attendee
    """

    # Validate template type
    if not isinstance(template, str):
        print("Error: Template should be a string.")
        return

    # Validate attendees type
    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print("Error: Attendees should be a list of dictionaries.")
        return

    # Empty template check
    if template.strip() == "":
        print("Template is empty, no output files generated.")
        return

    # Empty attendees list check
    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    # Process attendees and generate files
    for i, attendee in enumerate(attendees, start=1):

        # Replace placeholders; missing values become "N/A"
        processed = template
        for key in ["name", "event_title", "event_date", "event_location"]:
            value = attendee.get(key)
            if value is None or value == "":
                value = "N/A"
            processed = processed.replace(f"{{{key}}}", str(value))

        # Output file name
        filename = f"output_{i}.txt"

        try:
            with open(filename, "w", encoding="utf-8") as f:
                f.write(processed)
        except Exception as e:
            print(f"Error writing file {filename}: {e}")
            continue
