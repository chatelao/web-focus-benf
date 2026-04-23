# Goal

Define the WebFOCUS programming language syntax and functionality in a formal way.

# Structure

- `CONCEPT.md`: The overall structure of the product, including Business Cases & Use Cases as well as the overall High-Level Architecture, etc.
- `DESIGN.md`: The detailed design of the solution, including the architecture, used tech stack for development, production and testing, etc.
- `ROADMAP.md`: The list of accomplished and planned steps of the project, it should be  grouped into Phases, Tasks and Subtasks if necessary. Checkboxes show the progress to be updated with every increment. Split and add new tasks if reasonable.
- `TECHNICAL_DEBTS.md`: If you find technical debts, like outdate components, security flaws, old patterns, etc. log them here, but don’t fix them until asked to do so.
- `/specification/`: External Know-How as datasheet, standards, etc. Should be converted to Markdown if PDF, etc.
- `/src/`: The source code of the project
- `/src/docs/`: The documentation of the resulting product (not the input standards)
- `/test/`: All tools, configurations & test cases
- `/build/`: Only temporary place for compilation, may be cached by Github

# HOWTO

- Keep `src/install.sh` to install all tools to build the application (test only tools, see below)
- Use releated informations to gather a full syntax definition.
- Use this manual `https://docs.tibco.com/pub/wf-wf/8207.27.0/doc/pdf/TIB_wfwf_8207.27.0_cr_language.pdf`
- Create a "readthedocs" documentation of the anaytics.

# Testing Locally & with Github Action Workflow

- Setup the empty CI/CD pipeline before coding anything
- Write CI/CD test independent as `test` script of the Github action workflows
- Create screenshots of each UI step tested and store it as asset of the Action Workflow for review
- Use `test/install.sh` to install test tools.
- Use the Github action workflows to run the tests after commits.
- Before committing fetch all changes from the remote repository and merge the changes
- Run the CI/CD on every commit on every branch
- Add as much caching as possible to the Github action workflows

# Jules Agent Instructions

## ROADMAP rules
- The `ROADMAP.md` is automatically managed by the `Jules Automation` workflow.
- When working on tasks from the `ROADMAP.md`, always **execute from bottom to top**.
- New tasks are added to the top of the list.
- Tasks are marked as completed with a timestamp when the corresponding issue is closed.

## Guidelines
- Ensure that you are picking the oldest pending task (at the bottom of the list) to maintain a consistent workflow.
- Do not manually edit the completion status of tasks in `ROADMAP.md` unless necessary; the automation handles this upon issue closure.
