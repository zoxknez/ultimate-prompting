import subprocess


def run_shell_command(command: str) -> str:
    """Tool exposed to the agent for 'running diagnostic commands'.

    Vulnerable: the agent's own LLM-generated `command` string is passed
    straight to a shell with no allowlist of permitted commands, no
    argument validation, and no sandboxing. A prompt injected into any
    document the agent retrieves (a support ticket, a web page fetched by
    another tool, a file the agent was asked to summarize) can steer the
    model into calling this tool with an attacker-chosen command, turning a
    text-processing agent into remote code execution on whatever host runs
    it.
    """
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout + result.stderr
