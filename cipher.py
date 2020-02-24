#!/usr/bin/python3
import click
import importlib

# Add new available modules here.
available_algorithms = [
    'shift',
    'matrix',
]

@click.command('cipher')
@click.option('--algorithm', '-a', 
    help=f'Which algorithm to use ( available ~> {", ".join(available_algorithms)} )', 
    prompt='Please choose the algorithm', 
    required=True)
@click.option('--method', '-m', 
    prompt='Please enter what you want todo (encode, decode)', 
    help='Which method to run (encode, decode)', 
    required=True)
@click.argument('text', required=True, nargs=-1)
def cipher(algorithm, method, text):
    try:
        module = importlib.import_module(algorithm + '.' + method)
    except ModuleNotFoundError as e:
        click.echo("You chose an invalid algorithm or method, please try again.")
    else:
        result = module.run(' '.join(text))
        return click.echo(result)


if __name__ == '__main__':
    cipher()