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
    "sphinx.ext.autosummary",
    "sphinx.ext.napoleon",
]

autosummary_generate = True

napoleon_google_docstring = False
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = False
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = False
napoleon_use_param = True
napoleon_use_rtype = True

templates_path: List[str] = ["_templates"]
exclude_patterns: List[str] = []

html_theme: str = "pydata_sphinx_theme"

html_theme_options = {
    "use_edit_page_button": False,
    "secondary_sidebar_items": [],
}

html_static_path: List[str] = ["_static"]
