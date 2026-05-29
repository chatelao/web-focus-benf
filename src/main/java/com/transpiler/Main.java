package com.transpiler;

import picocli.CommandLine;
import picocli.CommandLine.Command;
import picocli.CommandLine.Option;
import picocli.CommandLine.Parameters;

import java.io.File;
import java.util.List;
import java.util.concurrent.Callable;

@Command(name = "wf2pg", mixinStandardHelpOptions = true, version = "1.0",
        description = "WebFOCUS to PostgreSQL Transpiler CLI",
        subcommands = {Main.TranspileCommand.class, Main.CheckCommand.class, Main.LineageCommand.class})
public class Main implements Runnable {

    @Override
    public void run() {
        CommandLine.usage(this, System.out);
    }

    @Command(name = "transpile", description = "Main command to convert .fex files")
    static class TranspileCommand implements Callable<Integer> {
        @Option(names = {"-i", "--input"}, required = true, description = "Input .fex file or directory")
        private File input;

        @Option(names = {"-o", "--output"}, description = "Output directory")
        private File output;

        @Option(names = {"-m", "--master-path"}, description = "Search paths for Master Files")
        private List<File> masterPaths;

        @Option(names = {"--stats"}, description = "Display source code statistics")
        private boolean showStats;

        @Override
        public Integer call() {
            System.out.println("Transpiling: " + input.getAbsolutePath());
            return 0;
        }
    }

    @Command(name = "check", description = "Validate WebFOCUS syntax without full transpilation")
    static class CheckCommand implements Callable<Integer> {
        @Option(names = {"-i", "--input"}, required = true, description = "Input .fex file")
        private File input;

        @Override
        public Integer call() {
            System.out.println("Checking syntax: " + input.getAbsolutePath());
            return 0;
        }
    }

    @Command(name = "lineage", description = "Output data lineage in JSON format")
    static class LineageCommand implements Callable<Integer> {
        @Option(names = {"-i", "--input"}, required = true, description = "Input .fex file")
        private File input;

        @Override
        public Integer call() {
            System.out.println("Analyzing lineage: " + input.getAbsolutePath());
            return 0;
        }
    }

    public static void main(String[] args) {
        int exitCode = new CommandLine(new Main()).execute(args);
        System.exit(exitCode);
    }
}
