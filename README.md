# Data Visualisation Project

This repository uses the [`uv`](https://docs.astral.sh/uv/) Python package manager to manage its dependencies.
While the Jupyter notebooks may run with an Anaconda distribution, this is not guaranteed.
To ensure you are able to reproduce our outputs, we highly recommend following the these steps to start Jupyter Lab and execute the notebooks:

- Install [`uv`](https://docs.astral.sh/uv/getting-started/installation/).

- Run the following in a shell at the root of the repository:

  ```
  uv sync
  uv run jupyter-lab
  ```

  This should start Jupyter Lab and open it in your browser.

- With Jupyter Lab opened, you can now explore and run the notebooks in this repository.
  These notebooks will fetch their required datasets and generate corresponding charts.
