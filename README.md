# WebFOCUS to PostgreSQL Transpiler

This project implements a Multi-Pass Source-to-Source Compiler (Transpiler) to migrate legacy WebFOCUS codebases to modern PostgreSQL (PL/pgSQL).

## Overview

The transpiler moves beyond simple syntax parsing to understand the semantic context of WebFOCUS requests, including Dialogue Manager state and procedural logic, optimizing them for set-based execution in PostgreSQL.

## Structure

- `CONCEPT.md`: High-Level Architecture and Multi-Pass Compiler pattern.
- `DESIGN.md`: Detailed design, transpiler pipeline, and tech stack (ANTLR4, SSA-IR, Jinja2).
- `ROADMAP.md`: Planned and accomplished steps for the migration engine.
- `TECHNICAL_DEBTS.md`: Log of technical debts and architectural shifts.
- `WEBFOCUS_TO_POSTGRE.md`: Migration strategy and technical reasoning.
- `/src/`: Transpiler source code.
- `/test/`: Test suite and real-world samples.
- `/specifications/`: Formal WebFOCUS language manuals (Markdown).
