# excel2parquet

### Prerequisites
#### Python 3.6.*
* NOTE: Issues with one of the library pyarrow with Python 3.7 or above version.

See installation instructions at: https://www.python.org/downloads/

Check you have python3 installed:

```bash
python3 --version
```

### Dependencies and data

#### Creating a virtual environment

Ensure your pip (package manager) is up to date:

```
pip install --upgrade pip
```

To check your pip version run:

```
pip --version
```

Create the virtual environment in the root of the cloned project:
```bash
python3.6 -m venv .venv
```
```windows
pip install virtualenv
virtualenv .venv
```

#### Activating the newly created virtual environment

You always want your virtual environment to be active when working on this project.

```bash
source ./.venv/bin/activate
```
```windows
.\.venv\Scripts\activate
```

#### Installing Python requirements

This will install some of the packages you might find useful:
```bash
pip install -r ./requirements.txt
```
```windows
pip install -r .\requirements.txt
```
#### Excel2Parquet (PANDAS)

#### Repo Tree

```
├── main                                                --> Main programs that has the python logic to convert excel to parquet and get max temp rec  std out.
│   ├── __init__.py
│   └──excel2parquet.py                    --> This is the main Script which converts excel files from input folder into parrquet
├── input                                               --> kindly copy your excel files into this folder that need to convert to parquet
│   ├── <INPUT EXCEL FILES>   
├── output                                             --> when ran excel2parquet.py from repo root, parquet file will be generated in this folder
│   ├── <OUTPUT PARQUET FILES>
├── tests                                                 -->  UNITTEST framework used to write the tests which covers main module programs
│   ├── __init__.py
│   ├── excel2parquet_main_test.py   --> test cases that covering few functions in excel2parquet.py and get_max_temp_rec.py
│   └── resources                                  --> place that holds sample datafiles used for tests
│       ├── output.parquet
│       ├── pd_df.csv
│       └── weather.xlsx
├── README.md                                    --> Repo description and documentation of repo
└──requirements.txt                             --> will have list of Python Libraries that required for this project
```
#### INPUT

Excel files are expected to be placed in this folder

#### Running tests to ensure everything is working correctly
```bash
pytest ./tests
```
```windows
pytest .\tests
```
#### OUTPUT

#### Execution of main program

Parquet file will be generated with *.parquet extension in this folder once below command is executed.
```bash
./main/excel2parquet.py
```
```windows
.\main\excel2parquet.py
```


####  Input Excel Info

This repo is not specifically designed for considered Excel to convert to parquet

    * Considered
    Will consider all the excel's in input folder considering first sheet and converts into single parquet file.
    Dynamically defines the datatypes
    * Not Considered
    Will not consider sheets inside the Excel if more than one.

####  Output Parquet Info

successful execution will give you the unique file name with *.parquet extension.
* NOTE: rerunning on same input will give you duplicate data.

####  Feature Roadmap
    1. Considering all the sheets in any provided excel.
    2. Eliminating empty rows if any.
    3. Predefining datatypes which will help Schema Evolution which eliminates reading exceptions.(use case data specific)


#### Assumptions on this Excel to get MAX Temp rec

ScreenTemperature column assumed to be the temperature in ```°C```  as no temperature column is provided nor the columns that suits to calculate temperature.
