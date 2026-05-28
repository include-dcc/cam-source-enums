<a href="https://github.com/dalito/linkml-project-copier"><img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/copier-org/copier/master/img/badge/badge-grayscale-inverted-border-teal.json" alt="Copier Badge" style="max-width:100%;"/></a>

# cam-source-enums

This project is a LinkML model based on the Common Access Model with enumerations separated into individual YAML files, to be used by a downstream process for enumeration definition expansion. Only the enumerations are included in this project.

## Documentation Website

[https://include-dcc.github.io/cam-source-enums](https://include-dcc.github.io/cam-source-enums)

## Repository Structure

* [docs/](docs/) - mkdocs-managed documentation
  * [elements/](docs/elements/) - generated schema documentation
* [examples/](examples/) - Examples of using the schema
* [project/](project/) - project files (these files are auto-generated, do not edit)
* [src/](src/) - source files (edit these)
  * [cam_source_enums](src/cam_source_enums)
    * [schema/](src/cam_source_enums/schema) -- LinkML schema
      (edit this)
    * [datamodel/](src/cam_source_enums/datamodel) -- generated
      Python datamodel
* [tests/](tests/) - Python tests
  * [data/](tests/data) - Example data

## Developer Tools

There are several pre-defined command-recipes available.
They are written for the command runner [just](https://github.com/casey/just/). To list all pre-defined commands, run `just` or `just --list`.

## Credits

This project uses the template [linkml-project-copier](https://github.com/dalito/linkml-project-copier) published as [doi:10.5281/zenodo.15163584](https://doi.org/10.5281/zenodo.15163584).
