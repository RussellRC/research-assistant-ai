"""Configuration management for AI Research Assistant.

This module handles environment configuration and settings.
"""

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


class Config:
    """Configuration settings for the research assistant."""

    def __init__(self):
        """Initialize configuration from environment variables."""
        # GCP Configuration
        self.project_id = os.getenv("GOOGLE_CLOUD_PROJECT", "")
        self.location = os.getenv("GOOGLE_CLOUD_LOCATION", "us-central1")
        self.model_name = os.getenv("MODEL_NAME", "gemini-2.5-flash")
        self.use_vertex_ai = os.getenv("GOOGLE_GENAI_USE_VERTEXAI", "false")
        self.application_credentials = os.getenv("GOOGLE_APPLICATION_CREDENTIALS", "")

        # Research Settings
        self.max_iterations = int(os.getenv("MAX_ITERATIONS", "3"))
        self.quality_threshold = float(os.getenv("QUALITY_THRESHOLD", "0.8"))

        # Validate required settings
        if not self.project_id:
            print("⚠️  Warning: PROJECT_ID not set in environment")

    def __repr__(self):
        """String representation of config."""
        return (
            f"Config("
            f"application_credentials='{self.application_credentials}', "
            f"project_id='{self.project_id}', "
            f"location='{self.location}', "
            f"model='{self.model_name}', "
            f"use_vertex_ai='{self.use_vertex_ai}', "
            f")"
        )


# Global config instance
config = Config()
