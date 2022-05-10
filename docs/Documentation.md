# Decimal (Arabic) to Roman Number Conversion - Software Documentation
This document establishes the requirements, installation and execution, acceptance criteria and test cases (end-to-end & unit tests) of this application.

## Table of contents
1. [Software requirements](#software-requirements)
2. [Acceptance criteria](#acceptance-criteria)
3. [Test cases](#test-cases)
    1. [End-to-end tests](#end-to-end-tests)
    2. [Unit testing](#unit-testing)

## Software requirements
Given the problem, the following software requirements were surveyed and documented:

- **Req-1:** The application must convert arabic numbers to roman numerals.

## Acceptance criteria
Based on the previous software requirements, the following criteria for acceptance were produced:

- **Crit-1-1:** The application must show the roman numeral equivalent of the arabic numeral inserted.
- **Crit-1-2:** The application must convert non-zero and non-negative arabic numbers.
- **Crit-1-3:** The application must convert arabic numeral values to its roman numeral equivalent if it does not contain letters or symbols.

## Test cases and scenarios
Given that test cases must be both end-to-end (E2E) and unit based (UT), the following were created: 

### End-to-end tests
- **E2E-1-1-1:** Validate function of decimal to roman numeral conversion with valid input:
  1. Launch program via console interface (Command Prompt, Powershell, Terminal, etc.)
  2. Insert valid arabic numeral value.
  3. Press the ENTER key.
  4. Check output given valid input.
  5. Close the console interface.

- **E2E-1-2-1:** Validate function of decimal to roman numeral conversion with invalid input:
  1. Launch program via console interface (Command Prompt, Powershell, Terminal, etc.)
  2. Insert invalid arabic numeral value.
  3. Press the ENTER key.
  4. Check error message given invalid input.
  5. Close the console interface.

### Unit testing
- **UT-1-1-1:** If the input is "1", then the roman numeral equivalent must be I.
- **UT-1-1-2:** If the input is "34", then the roman numeral equivalent must be XXXIV.
- **UT-1-1-3:** If the input is "99", then the roman numeral equivalent must be XCIX.
- **UT-1-1-4:** If the input is "2995", then the roman numeral equivalent must be MMCMCXCV.
- **UT-1-2-1:** If the input is "0", then no roman numeral exists.
- **UT-1-2-2:** If the input is "-3", then no roman numeral exists.
- **UT-1-2-3:** If the input is "-64", then no roman numeral exists.
- **UT-1-3-1:** If the input is "T", then an error is raised.
- **UT-1-3-2:** If the input is "INS364L", then an error is raised.