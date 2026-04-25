#!/bin/bash
SCRIPT_DIR=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" &> /dev/null && pwd)
java -Xmx500M -cp "$SCRIPT_DIR/../build/antlr-complete.jar:$CLASSPATH" org.antlr.v4.Tool "$@"
