# pip & Packages

**pip** = Python's package installer. Think of it like an app store for Python code.

**Packages** = Pre-written code libraries that add functionality. Instead of writing everything from scratch, you install what others have built:

| Package | Purpose |
|---------|---------|
| `numpy` | math/arrays |
| `pandas` | data tables |
| `matplotlib` | charts/graphs |

---

## Upgrading pip

**Why?** Newer versions fix bugs and support newer packages. Optional but good practice.

python -m pip install --upgrade pip

## Example Flow

**Install Package**: python -m pip install pandas   # download pandas package
import pandas  # now use it in your code

**Uninstall Package**: python -m pip uninstall pandas