import subprocess
import os

class RRTool:
    """
    A wrapper for Gunther Rademacher's Railroad Diagram Generator (RR).
    """

    def __init__(self, war_path=None):
        if war_path is None:
            # Default to rr.war in the project root
            base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            war_path = os.path.join(base_dir, "rr.war")

        self.war_path = war_path
        if not os.path.exists(war_path):
            raise FileNotFoundError(f"RR tool not found at {war_path}. Run scripts/provision_rr.py first.")

    def generate(self, ebnf_path, out_path=None, color=None, width=None, options=None):
        """
        Executes the RR tool on the given EBNF file.
        """
        cmd = ["java", "-jar", self.war_path]

        if out_path:
            cmd.append(f"-out:{out_path}")
        if color:
            cmd.append(f"-color:{color}")
        if width:
            cmd.append(f"-width:{width}")

        if options:
            for opt in options:
                cmd.append(opt)

        cmd.append(ebnf_path)

        result = subprocess.run(cmd, capture_output=True, text=True)

        if result.returncode != 0:
            raise RuntimeError(f"RR tool failed: {result.stderr}")

        return result.stdout

if __name__ == "__main__":
    # Quick self-test
    with open("test_quick.ebnf", "w") as f:
        f.write("STMT ::= 'TEST'\n")

    rr = RRTool()
    rr.generate("test_quick.ebnf", out_path="test_quick.xhtml")
    print("Quick test generated test_quick.xhtml")

    if os.path.exists("test_quick.xhtml"):
        os.remove("test_quick.xhtml")
    if os.path.exists("test_quick.ebnf"):
        os.remove("test_quick.ebnf")
