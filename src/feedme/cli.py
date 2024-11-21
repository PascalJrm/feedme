import click

@click.group()
def cli():
    """Simple CLI application with various utilities."""
    pass

@cli.command()
@click.argument('name')
def greet(name):
    """Greet someone by name."""
    return f"Hello, {name}!"

@cli.command()
@click.argument('number', type=int)
def factorial(number):
    """Calculate factorial of a number."""
    if number < 0:
        return "Factorial is not defined for negative numbers"
    result = 1
    for i in range(1, number + 1):
        result *= i
    return str(result)

@cli.command()
@click.argument('text')
def reverse(text):
    """Reverse a string."""
    return text[::-1]

if __name__ == '__main__':
    cli()
