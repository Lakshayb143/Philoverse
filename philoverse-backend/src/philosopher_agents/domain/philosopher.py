import json
from pathlib import Path
from typing import List

from pydantic import BaseModel, Field


class PhilosopherData(BaseModel):
    """
    Above class represents raw philosopher data extracted from the sources(external).

    This class follows the structure of the philosophers.json file and contains
    basic information about philosophers before enrichment.

    Args:
        id (str): Unique identifier for the philosopher.
        urls (List[str]): List of URLs with information about the philosopher.
    """


    id :str = Field(description="Unique identifier for the philosopher")
    urls : List[str] = Field(description="List of urls that have information about the philospher")

    @classmethod
    def from_json(cls, metadata_file :Path) -> list["PhilosopherData"]:
        with open(metadata_file, "r") as f:
            philosopher_data = json.load(f)
        
        return [cls(**philosopher) for philosopher in philosopher_data]
    

class Philosopher(BaseModel):

    """
    A class representing a philosopher agent with added memory.

    Args:
        id (str): Unique identifier for the philosopher.
        name (str): Name of the philosopher.
        perspective (str): Description of the philosopher's theoretical views
            about AI.
        style (str): Description of the philosopher's talking style.
    """

    id: str = Field(description="Unique identifier for the philosopher")
    name: str = Field(description="Name of the philosopher")
    perspective: str = Field(
        description="Description of the philosopher's theoretical views about AI"
    )
    style: str = Field(description="Description of the philosopher's talking style")

    def __str__(self) -> str:
        return f"Philosopher(id={self.id}, name={self.name}, perspective={self.perspective}, style={self.style})"
    

