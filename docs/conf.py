from __future__ import annotations

from typing import List
import sys
import os


PROJECT_ROOT: str = os.path.abspath("..")
sys.path.insert(0, PROJECT_ROOT)

project: str = "quant-kit"
author: str = "Lorenzo Santarsieri"
release: str = "0.1.0"

extensions: List[str] = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
]

templates_path: List[str] = ["_templates"]
exclude_patterns: List[str] = []

html_theme: str = "pydata_sphinx_theme"

html_theme_options = {
    "use_edit_page_button": False,
    "navbar_align": "content",
}

html_static_path: List[str] = ["_static"]
