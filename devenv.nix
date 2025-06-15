{ pkgs, ... }:

{
  languages.python = {
    enable = true;
    uv.enable = true;
  };

  packages = [ pkgs.uv ];

  processes.jupyterlab.exec = ''
    set -euo pipefail

    echo "[devenv] Creating virtual environment at .venv..."
    if [ ! -x .venv/bin/python ]; then
      uv venv --venv .venv
    fi

    echo "[devenv] Installing Python packages into .venv..."
    UV_VENV_PATH=.venv uv pip install -r pyproject.toml

    echo "[devenv] Registering Jupyter kernel..."
    .venv/bin/python -m ipykernel install --user --name gbm-sim --display-name "Python (GBM Sim)"

    echo "[devenv] Starting JupyterLab..."
    exec .venv/bin/jupyter lab --notebook-dir=notebooks --no-browser --ip=127.0.0.1 --port=8888
  '';

  enterShell = ''
    echo "✨ Welcome to the GBM simulation environment"
    echo "✅ devenv shell ready — use '.venv/bin/jupyter lab' or 'devenv up'"
  '';
}
