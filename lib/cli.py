#!/usr/bin/env python3

import click
from helpers import add_task, view_tasks, edit_task, delete_task

@click.group()
def cli():
    pass

@click.command()
@click.argument('to_do')
@click.argument('priority')
def add(to_do, priority):
    try:
        add_task(to_do, priority)
        click.echo('Task added successfully')
    except ValueError as e:
        click.echo(f'Error: {e}')

@click.command()
def view():
    view_tasks()

@click.command()
@click.argument('task_id', type=int)
@click.option('--to_do', default=None)
@click.option('--priority', default=None)
def edit(task_id, to_do, priority):
    try:
        edit_task(task_id, to_do, priority)
        click.echo('Task edited successfully')
    except ValueError as e:
        click.echo(f'Error: {e}')

@click.command()
@click.argument('task_id', type=int)
def delete(task_id):
    try:
        delete_task(task_id)
        click.echo('Task deleted successfully')
    except ValueError as e:
        click.echo(f'Error: {e}')

cli.add_command(add)
cli.add_command(view)
cli.add_command(edit)
cli.add_command(delete)

if __name__ == '__main__':
    cli()

