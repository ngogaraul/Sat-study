# SAT Study - Python Exercises

A collection of Python exercises covering bit manipulation, binary encoding,
endian conversion, packet validation, telemetry decoding, CCSDS packets, and
temperature scaling.

## Requirements

- Python 3.10 or newer
- Dependencies listed in `requirements.txt`

## Setup

Clone or download the project, open a terminal in the project directory, and
create a virtual environment:

```powers
py -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## Running the examples

Run a script from the project directory:

```powers
python EngScaling.py
python packetValidation.py
python endianess.py
python CCSDSPy\intocourse.py
```

The following files contain practice exercises or demonstrations:

| File | Topic |
| --- | --- |
| `bitstringsEX2.py` | Creating and manipulating bit strings |
| `btistringEX.py` | Signed and unsigned bit-string operations |
| `day1_assignment.py` | Python fundamentals assignment |
| `decodepacket.py` | Decoding an 24-bit telemetry packet |
| `decoderReuse.py` | Reusable scaling and decoding helpers |
| `EngScaling.py` | Converting raw values to engineering units |
| `endianess.py` | Byte order and endian conversion |
| `packetValidation.py` | Packet length, APID, and temperature validation |
| `struct_assingment.py` | Binary data handling with the `struct` module |
| `temperature.py` | Temperature scaling helper |
| `CCSDSPy/intocourse.py` | Defining and decoding a CCSDS packet |

## Running tests

Run the test suite with pytest:

```powers
pytest
```

The temperature tests verify positive, negative, and zero values:

```powers
pytest test_temperature.py
```
