import subprocess
from pathlib import Path

def run_deepsems_predict(gbk_path: str, output_dir: str = "results/predicted_smiles"):
    # Define caminhos baseados na raiz do projeto
    project_root = Path(__file__).resolve().parent.parent
    deepsems_script = project_root / "models" / "DeepSeMS" / "predict.py"
    gbk_path = project_root / gbk_path
    output_dir = project_root / output_dir

    output_dir.mkdir(parents=True, exist_ok=True)

    result = subprocess.run(
        ["python", str(deepsems_script), "--input", str(gbk_path), "--output", str(output_dir)],
        capture_output=True,
        text=True,
    )

    print("=== DeepSeMS STDOUT ===")
    print(result.stdout)
    print("=== DeepSeMS STDERR ===")
    print(result.stderr)

    return result

if __name__ == "__main__":
    run_deepsems_predict("data/deepsems_sample.gbk")
