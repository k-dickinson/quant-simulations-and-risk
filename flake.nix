{
  description = "GBM simulation with Python and yfinance";

  nixConfig = {
    extra-trusted-public-keys = "devenv.cachix.org-1:w1cLUi8dv3hnoSPGAuibQv+f9TZLr6cv/Hm9XgU50cw=";
    extra-substituters = "https://devenv.cachix.org";
  };

  inputs = {
    nixpkgs.url           = "github:NixOS/nixpkgs/nixos-25.05";
    devenv.url            = "github:cachix/devenv";
    flake-utils.url       = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, devenv, flake-utils, ... }@inputs:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = import nixpkgs {
          inherit system;
          config = {
            allowUnfree = true;
            # This helps resolve apple-sdk issues
            darwin.apple_sdk.frameworks = [
              "CoreFoundation"
              "Security"
              "Foundation"
              "AppKit"
            ];
          };
        };
      in
        {
          devShells.default = devenv.lib.mkShell {
            inherit inputs pkgs;
            modules = [ ./devenv.nix ];
          };
        }
    );
}
