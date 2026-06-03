# File Format Support Gap Analysis

This document outlines the support status for various WebFOCUS application and metadata file formats within the transpiler.

| File Extension | Format Name | Support Status | Details |
| :--- | :--- | :--- | :--- |
| **.fex** | Procedure (FOCEXEC) | **Fully Supported** | Supported via `WebFocusReport.g4` grammar and associated Python (`asg_builder.py`) and Java (`WebFocusReportVisitor`) components. |
| **.mas** | Master File | **Fully Supported** | Supported via `MasterFile.g4` grammar and `master_file_parser.py`. |
| **.acx** | Access File | **Unsupported** | No grammar or parser implementation exists for Access Files. These files contain system-specific information and connection parameters which are currently not handled. |
| **.sty** | StyleSheet | **Partially Supported** | Inline `SET STYLE * ... ENDSTYLE` blocks within `.fex` files are parsed into `StyleBlock` ASG nodes. However, external `.sty` files are not supported and no separate parser exists for them. |
