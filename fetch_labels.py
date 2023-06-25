import os
import numpy as np

from functools import lru_cache
from typing import Dict, Optional


@lru_cache
def fetch_labels() -> list[str]:
    return [label for label in os.listdir("training")]

@lru_cache
def fetch_labels_as_np():
    labels = fetch_labels()
    return np.array(labels)

@lru_cache
def fetch_label_map() -> Dict[str, int]:
    return {label: index for index, label in enumerate(fetch_labels())}


# TODO: this is a hack too
def find_key_for_index(i: int) -> Optional[str]:
    label_map = fetch_label_map()
    for label, index in label_map.items():
        if index == i:
            return label
    return None


if __name__ == "__main__":
    labels = fetch_labels()
    print(f"Found {len(labels)} classes.")
    for i, label in enumerate(labels):
        print(f"{i:2}: {label}")
    print(f"{fetch_labels_as_np()=}")
