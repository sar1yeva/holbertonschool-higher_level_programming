#!/usr/bin/python3
"""
Task 02 - Fetching and Saving Posts using requests and csv
"""

import requests
import csv


def fetch_and_print_posts():
    """Fetch posts and print status code + titles"""
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    # Print status code
    print(f"Status Code: {response.status_code}")

    # If OK (status 200), parse JSON
    if response.status_code == 200:
        posts = response.json()

        # Print titles
        for post in posts:
            print(post.get("title"))


def fetch_and_save_posts():
    """Fetch posts and save them to posts.csv"""
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    # If OK (status 200), write to CSV
    if response.status_code == 200:
        posts = response.json()

        # Prepare list of dictionaries
        data = [
            {
                "id": post.get("id"),
                "title": post.get("title"),
                "body": post.get("body")
            }
            for post in posts
        ]

        # Write to CSV file
        with open("posts.csv", "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=["id", "title", "body"])
            writer.writeheader()
            writer.writerows(data)
