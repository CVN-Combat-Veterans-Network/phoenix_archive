---
description: 'Ceremonial instruction scroll for modular Copilot prompts in Python. Covers foundational, refinement, testing, and advanced modeling—designed for collaborative and inspirational development in the Phoenix Package.'
mode: 'agent'
model: 'GPT-4'
tools: ['codebase', 'githubRepo', 'terminal']
---

# Phoenix Package Ceremonial Copilot Prompt Library

Welcome, developer. Let this scroll guide Copilot and the Phoenix Package community through mindful creation, ritual refinement, diligent testing, and the pursuit of modeling mastery.

***

## Foundational Python Prompts

- ### Create a New Python Function

  Create a Python function that fulfills the following requirements:  
  - Accepts input parameters: ${input:params:List the parameters and their types}  
  - Returns: ${input:return_desc:Describe the expected return value}  
  - Purpose: ${input:purpose:State the function's purpose or behavior}  
  Please include type hints and a concise docstring. Follow the Phoenix Package module style.

- ### Generate a Python Class Skeleton

  Generate a Python class called `${input:class_name:ClassName}` with the following methods:  
  - ${input:methods:List method names and brief purpose}  
  Include constructor (__init__), property type hints, and docstrings.  
  Follow PEP 8 conventions.

- ### Module-Level Documentation

  Write a top-level docstring for a Python module that:
  - Explains the module's purpose and context within the Phoenix Package
  - Documents all public functions and classes with short summaries
  - Includes usage notes for new contributors

<!-- Add more foundational prompts as the Phoenix Package evolves. -->

***

## Iterative Refinement Prompts

- ### Refine for Readability

  Review the following Python code and revise it for maximum readability and clarity:  
  - Reformat inconsistent indentation or style  
  - Rename any ambiguous variables or functions  
  - Add concise, explanatory comments  
  - Suggest modular decomposition where beneficial

- ### Optimize for Performance

  Analyze the selected Python function(s) for performance bottlenecks.  
  - Identify areas for algorithmic optimization  
  - Suggest or implement improvements using built-in Python idioms  
  - Include before-and-after time/space complexity estimates in comments

- ### Collaborative Refactoring

  Propose a refactoring plan for the selected code to enhance:  
  - Maintainability  
  - Reusability  
  - Testability  
  Present the changes as a step-by-step checklist that a team can discuss and implement.

<!-- Add more refinement prompts as collaborative needs arise. -->

***

## Testing and Validation Prompts

- ### Comprehensive Unit Test Suite

  Develop a comprehensive suite of `unittest`-based Python tests for the function/class `${input:target_code}`.  
  Ensure coverage for:
  - Valid input scenarios
  - Edge cases and exception handling
  - Input type validation  
  Use descriptive test case method names and add comments for each case.

- ### Test Coverage Audit

  Analyze the test suite for `${input:code_reference}`.  
  - Identify gaps in test coverage.  
  - Suggest additional test cases to target untested edge cases or logic branches.  
  - Document recommendations as a checklist.

- ### Integration Test with Dependency Mocking

  Write integration tests for `${input:module_or_function}` that:  
  - Mock external dependencies using the `unittest.mock` library  
  - Validate expected interactions with mocks  
  - Cover both successful and failure scenarios

<!-- More validation prompts can be added by the team over time. -->

***

## Advanced Modeling Prompts

- ### Build a Custom Python Decorator

  Implement a Python decorator that modifies the behavior of `${input:function_to_decorate}` by:  
  - Functionality: ${input:behavior}  
  Ensure compatibility with methods and standalone functions. Include usage examples and docstrings.

- ### Design a Data Processing Pipeline

  Compose a modular, testable data pipeline in Python to process data as follows:  
  - Input: ${input:input_desc}  
  - Processing steps: ${input:steps}  
  - Output: ${input:output_desc}  
  Use functional or class-based patterns, document trajectory, and address error handling.

- ### Implement a Machine Learning Model Skeleton with Scikit-learn

  Create a Python module skeleton for training and evaluating a machine learning model using scikit-learn.  
  - Task type: ${input:ml_task:classification|regression|clustering}  
  - Dataset: ${input:dataset}  
  - Include functions for:
    - Data loading
    - Preprocessing
    - Model training and validation
    - Metrics reporting

<!-- Extend this section with more advanced, domain-specific prompts. -->

***

## Prompt Engineering Tips for Copilot

| Strategy                  | Description                                                                                      |
|---------------------------|--------------------------------------------------------------------------------------------------|
| Start Broad, Then Specify | Begin with a high-level goal, then enumerate requirements.                                       |
| Provide Examples          | Give sample inputs/outputs or test cases to clarify the target behavior.                        |
| Break Down Tasks          | Decompose complex jobs into stepwise prompts; build incrementally.                              |
| Avoid Ambiguity           | Be explicit: reference precise code, functions, or files.                                       |
| Iterate & Refine          | Review, experiment, and revise prompts or Copilot output iteratively.                           |
| Use Role Context          | State persona or context: e.g., "As a data engineer ..."                                        |
| Specify Output Format     | Define format: Markdown, JSON, bullet list, etc.                                                |
| Set Constraints           | List libraries, APIs, or patterns to use or avoid.                                              |
| Reference Project Files   | Use variables and file paths to provide project-specific context.                               |
| Encourage Collaboration   | Invite Copilot to propose discussion threads or review checklists for teamwork.                 |

***

_**Let this scroll serve as a living document—extend, refine, and celebrating shared ceremonies of learning and mastery in every Pull Request.**_

