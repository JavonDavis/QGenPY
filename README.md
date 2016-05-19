# QGenPY Command Line app

[![Join the chat at https://gitter.im/JA-VON/QGenPY](https://badges.gitter.im/JA-VON/QGenPY.svg)](https://gitter.im/JA-VON/QGenPY?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

Generate a volume of questions based on a template. Source for Django app located at https://github.com/JA-VON/QGen-UI

## Installation

QGen is available through PyPi and be installed using pip

```Bash
pip install qgen
```

## Usage

QGen needs either a yaml file or a python dictionary describing the configuration of question to be able to generate questions. 

Open up a python console and then import qgen and use as follows:

### YAML file 
```Python
import qgen
qgen.build_moodle_xml('/path/to/yaml/file/test.yml', number_of_questions=50)
```

### Python Dictionary

```Python
import qgen
qgen.build_moodle_xml(dict_value=configuation_as_dictionary, number_of_questions=50)
```
