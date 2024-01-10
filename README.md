<p align="left" >
<a href='https://carbonplan.org'>
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://carbonplan-assets.s3.amazonaws.com/monogram/light-small.png">
  <img alt="CarbonPlan monogram." height="48" src="https://carbonplan-assets.s3.amazonaws.com/monogram/dark-small.png">
</picture>
</a>
</p>

# carbonplan / carbonplan-python

**namespace package for python utilities and subprojects**

[![CI](https://github.com/carbonplan/carbonplan-python/actions/workflows/main.yaml/badge.svg)](https://github.com/carbonplan/carbonplan-python/actions/workflows/main.yaml)
![PyPI](https://img.shields.io/pypi/v/carbonplan)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

This repository includes the `carbonplan` namespace Python package. The package itself includes very little of substance, and is distributed to act as the top-level namespace for other Python packages developed by CarbonPlan. Other packages include:

| Package                   | Import                             | GitHub Repo                                                                                  |
| ------------------------- | ---------------------------------- | -------------------------------------------------------------------------------------------- |
| carbonplan-data           | `import carbonplan.data`           | [https://github.com/carbonplan/data](https://github.com/carbonplan/data)                     |
| carbonplan-forest-offsets | `import carbonplan.forest_offsets` | [https://github.com/carbonplan/forest-offsets](https://github.com/carbonplan/forest-offsets) |
| carbonplan-forest-risks   | `import carbonplan.forest_risks`   | [https://github.com/carbonplan/forest-risks](https://github.com/carbonplan/forest-risks)     |
| carbonplan-styles         | `import carbonplan.styles`         | [https://github.com/carbonplan/styles](https://github.com/carbonplan/styles)                 |

## install

```shell
pip install carbonplan[all]
# or individual sub packages
pip install carbonplan[styles]
```

## usage

```python
from carbonplan.styles.mpl import set_theme
# this is the same things as
from carbonplan_styles.mpl import set_theme
```

## license

All the code in this repository is [MIT](https://choosealicense.com/licenses/mit/)-licensed. We include attribution for this content, and we please request that you also maintain that attribution if using this data.

## about us

CarbonPlan is a nonprofit organization that uses data and science for climate action. We aim to improve the transparency and scientific integrity of climate solutions with open data and tools. Find out more at [carbonplan.org](https://carbonplan.org/) or get in touch by [opening an issue](https://github.com/carbonplan/carbonplan-python/issues/new) or [sending us an email](mailto:hello@carbonplan.org).
