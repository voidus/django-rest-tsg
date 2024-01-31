{
  description = "A very basic flake";

  outputs = { self, nixpkgs }: let
    system = "x86_64-linux";
  in {

    devShells.${system}.default = let
      pkgs = nixpkgs.legacyPackages.${system};
    in pkgs.mkShell {
      packages = with pkgs; [
        python311
        poetry
      ];
    };
  };
}
