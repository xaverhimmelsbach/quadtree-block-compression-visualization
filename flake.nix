{
  description = "Visualize measurements made with quadtree-block-compression";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixpkgs-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = import nixpkgs { inherit system; };
      in
      {
        devShell = pkgs.mkShell {
          buildInputs = with pkgs;[
            (
              let
                local-python-packages = python-packages: with python-packages; [
                  # Jupyter dependencies
                  ipython
                  ipykernel
                  jupyter
                  # Formatting in vscode
                  autopep8
                  # Visualization libs
                  pandas
                  seaborn
                  pyyaml
                  opencv4
                ];
                local-python = python3.withPackages local-python-packages;
              in
              local-python
            )
          ];
        };
      });
}
