# lettergenerator
Using a csv of recipients, this script creates a folder of customized templates to be printed.

## installation
1. install [python](https://www.python.org/getit/)
2. install [weasyprint](http://weasyprint.readthedocs.io/en/latest/install.html)
3. run `pip3 install -r requirements.txt` or `pip3 install -r requirements.txt` for windows

## usage
* edit `config.json` file as needed
* run `python3 main.py` or `python main.py` for windows
* build executable using `python3 build.py build` or `python build.py build` for windows
* after build copy [weasyprint](https://github.com/Kozea/WeasyPrint/tree/master/weasyprint) folders (css, formatting_structure, layout, tests, tools) to the build directory created, and then copy `config.json`, your csv file, and `template.html` to that directory as well.