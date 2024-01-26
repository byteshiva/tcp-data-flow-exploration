# flake.nix

{
  description = "TCP Data Analysis with Python: Explore three-way handshake and data transfer phases for networking insights.";
  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
  };

  outputs = { self, nixpkgs }: {
    devShell.x86_64-linux =
      let
        pkgs = nixpkgs.legacyPackages.x86_64-linux;
      in pkgs.mkShell {
        buildInputs = [
          pkgs.python3
          pkgs.tcpdump
          pkgs.wireshark
        ];

        shellHook = ''
          echo "Entering the development environment!"
        '';
      };

    devShells = rec {
      default = self.devShell.x86_64-linux;
    };
  };
}
