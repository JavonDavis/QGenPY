# QGenPY Command Line app

Generate a volume of questions based on a template. Source for Web app located at https://github.com/JA-VON/QGen-UI

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

For a description of what the YAML file should look like, please see the Getting Started guide in the Wiki.

### Python Dictionary

```Python
import qgen
qgen.build_moodle_xml(dict_value=configuation_as_dictionary, number_of_questions=50)
```
