#!/usr/bin/env python3

"""
Programme qui calcule l'aire d'un cylindre

Par Sébastien Fortier
"""

import math
import argparse


def parse_args() -> argparse.Namespace:
    """Gère le arguments passé à la ligne de commande"""
    parser = argparse.ArgumentParser(description='Calculateur de volume pour cylindre -- @2020, par Sébastien Fortier')
    parser.add_argument('-r', '--rayon', type=float, metavar='R', required=True, help='Rayon du cylindre')
    parser.add_argument('-H', '--hauteur', type=float, metavar='H', required=True, help='Hauteur du cylindre')
    parser.add_argument('-p', '--précision', type=int, metavar='P', help='Précision du calcul')
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-q', '--quiet', action='store_true', help='Afficher seulement le volume')
    group.add_argument('-v', '--verbeux', action='store_true', help='Afficher le maximum d''info')
    return parser.parse_args()


def main() -> None:
    """Fonction principale"""
    args = parse_args()
    volume = volume_cylindre(args.rayon, args.hauteur)

    if args.quiet:
        print(volume)
    elif args.verbeux:
        print("Volume du cylindre de hauteur %s et de rayon %s selon SF: %s" % (args.hauteur, args.rayon, volume))
    elif args.précision is not None:
        print("Volume du cylindre selon SF: %s" % round(volume, args.précision))
    else:
        print("Volume du cylindre selon SF: %s" % volume)


def volume_cylindre(rayon, hauteur):
    """Calcule le volume d'un cylindre"""
    vol = math.pi * (rayon ** 2) * hauteur
    return vol


if __name__ == '__main__':
    main()
