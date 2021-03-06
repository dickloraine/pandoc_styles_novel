"""
Insert a new page. If "odd-page" is given as a class, the next page is odd.
"""

from pandoc_styles import run_transform_filter


def latex(self):
    if "odd-page" in self.classes:
        return r"\cleardoublepage"
    return r"\clearpage"


if __name__ == "__main__":
    run_transform_filter(["new_page", "new-page"],
                         latex=latex,
                         html=['<div class="pagebreak"></div>'],
                         other=["\n----\n"])
