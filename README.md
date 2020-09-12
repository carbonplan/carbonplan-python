<img
  src='https://carbonplan-assets.s3.amazonaws.com/monogram/dark-small.png'
  height='48'
/>

# carbonplan / carbonplan-python

**namespace package for python utilities and subprojects**

[![GitHub][github-badge]][github]
![Build Status][]
![MIT License][]

[github]: https://github.com/carbonplan/carbonplan-python
[github-badge]: https://flat.badgen.net/badge/-/github?icon=github&label
[build status]: https://flat.badgen.net/github/checks/carbonplan/carbonplan-python
[mit license]: https://flat.badgen.net/badge/license/MIT/blue

This repository includes the `carbonplan` namespace Python package. The package itself includes very little of substance, and is distributed to act as the top-level namespace for other Python packages developed by CarbonPlan. Other packages include:

| Package           | Import                     | GitHub Repo                                                                  |
| ----------------- | -------------------------- | ---------------------------------------------------------------------------- |
| carbonplan-data   | `import carbonplan.data`   | [https://github.com/carbonplan/data](https://github.com/carbonplan/data)     |
| carbonplan-styles | `import carbonplan.styles` | [https://github.com/carbonplan/styles](https://github.com/carbonplan/styles) |

## install

```shell
pip install carbonplan[styles,data]
```

## usage

```python
from carbonplan.styles.mpl import dark
# this is the same things as
from carbonplan_styles.mpl import dark
```

## license

All the code in this repository is [MIT](https://choosealicense.com/licenses/mit/) licensed. We include attribution for this content, and we please request that you also maintain that attribution if using this data.

## about us

CarbonPlan is a non-profit organization that uses data and science for carbon removal. We aim to improve the transparency and scientific integrity of carbon removal and climate solutions through open data and tools. Find out more at [carbonplan.org](https://carbonplan.org/) or get in touch by [opening an issue](https://github.com/carbonplan/carbonplan-python/issues/new) or [sending us an email](mailto:hello@carbonplan.org).
