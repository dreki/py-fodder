# Skeleton of a CLI

import click

import fodder


@click.command('fodder')
@click.argument('count', type=int, metavar='N')
def cli(count):
    """Echo a value `N` number of times"""
    for i in range(count):
        click.echo(fodder.has_legs)
