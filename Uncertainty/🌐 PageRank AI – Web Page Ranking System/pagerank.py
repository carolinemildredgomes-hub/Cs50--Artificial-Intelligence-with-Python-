import os
import random
import re
import sys

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
     Return probability distribution over next page.
    """

    N = len(corpus)
    distribution = {}

    links = corpus[page]

    # If no outgoing links → treat as linking to all pages
    if len(links) == 0:
        links = set(corpus.keys())

    # Base probability (random jump)
    for p in corpus:
        distribution[p] = (1 - damping_factor) / N

    # Add link probability
    for linked_page in links:
        distribution[linked_page] += damping_factor / len(links)

    return distribution


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank from sampling.
    """

    pages = list(corpus.keys())

    # initialize counts
    counts = {page: 0 for page in pages}

    # first random page
    current = random.choice(pages)
    counts[current] += 1

    # repeat sampling
    for _ in range(n - 1):

        probs = transition_model(corpus, current, damping_factor)

        # random weighted choice
        next_page = random.choices(
            population=list(probs.keys()),
            weights=list(probs.values())
        )[0]

        counts[next_page] += 1
        current = next_page

    # normalize
    return {page: counts[page] / n for page in pages}


def iterate_pagerank(corpus, damping_factor):
    """
    Compute PageRank using iterative method.
    """

    N = len(corpus)

    # initial ranks
    ranks = {page: 1 / N for page in corpus}

    convergence = False

    while not convergence:

        new_ranks = {}

        for page in corpus:

            # base probability
            new_rank = (1 - damping_factor) / N

            # sum contributions from all pages linking to this page
            for potential_linker in corpus:

                links = corpus[potential_linker]

                # if no links → treat as linking to all pages
                if len(links) == 0:
                    links = set(corpus.keys())

                if page in links:
                    new_rank += (
                        damping_factor *
                        (ranks[potential_linker] / len(links))
                    )

            new_ranks[page] = new_rank

        # check convergence
        convergence = True
        for page in corpus:
            if abs(new_ranks[page] - ranks[page]) > 0.001:
                convergence = False

        ranks = new_ranks

    return ranks


if __name__ == "__main__":
    main()
