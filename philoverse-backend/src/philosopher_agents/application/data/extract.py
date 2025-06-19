from langchain_community.document_loaders import WebBaseLoader, WikipediaLoader
from langchain_core.documents import Document

from tqdm import tqdm
from typing import Generator

from philosopher_agents.domain.philosopher import Philosopher, PhilosopherData
from philosopher_agents.domain.philosopher_factory import PhilosopherFactory


def get_extraction_generator(
        philosophers : list[PhilosopherData],
) -> Generator[tuple[Philosopher, list[Document]], None]:
    
    """
    Extract documents for a list of philosophers using generators.

    Args:
        philosophers: A list of PhilosopherExtract objects containing philosopher information.

    Yields:
        tuple[Philosopher, list[Document]]: A tuple containing the philosopher object and a list of
            documents extracted for that philosopher.
    """
    

    progress_bar = tqdm(
        philosophers,
        desc="Extracting docs",
        unit="philosopher",
        bar_format="{desc}: {percentage:3.0f}%|{bar}| {n_fmt}/{total_fmt} [{elapsed}<{remaining}, {rate_fmt}] {postfix}",
        ncols = 100,
        leave=True,
    )
    
    philosopher_factory = PhilosopherFactory()
    for philosopher_extract in progress_bar:
        philospher = philosopher_factory.get_philosopher(philosopher_extract.id)
        progress_bar.set_postfix_str(f"Philosopher : {philospher.name}")

        p_docs = extract(philospher, philosopher_extract.urls)

        yield (philospher, p_docs)


def extract(philosopher : Philosopher, urls : list[str]) -> list[Document]:
    """Extract documents for a single philosopher from all sources

    Args:
        philosopher: Philosopher object containing philosopher information.
        extract_urls: List of URLs to extract content from.

    Returns:
        list[Document]: List of documents extracted for the philosopher.
    """

    docs = []



    return docs

