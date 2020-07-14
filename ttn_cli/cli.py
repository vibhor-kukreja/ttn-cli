import click

from .modules.cmd_network import cmd_network
from .modules.cmd_git import cmd_git


@click.group()
def cli():
    """
    This is the root function of cli module.
    """
    pass


@cli.group()
def git():
    """
    function act as a group which is linked to root cli function.
    """
    pass


@git.command()
def init_repo():
    """
    command used to initialise the repository.
    """
    click.echo(cmd_git.init_repo())


@git.command()
def branch():
    """
    command used to show the current branch.
    """
    click.echo(cmd_git.get_active_branch())


@git.command()
def branches():
    """
    command used to list all the branches in a repository.
    """
    click.echo(cmd_git.get_all_branches())


@git.command()
def commit_count():
    """
    command used to count the total number of commits.
    """
    click.echo(cmd_git.get_commit_count())


@git.command()
def commit_message():
    """
    command used to show the commit messages.
    """
    click.echo(cmd_git.get_commit_message())


@git.command()
@click.option('--from_date', '-f', help='date of log', required=True)
@click.option('--author', '-a', help='name of author', required=True)
def logs(from_date, author):
    """
    command used to fetch user logs from a particular date
    """
    click.echo(cmd_git.get_logs(author=author, from_date=from_date))


@git.command()
@click.option('--branch', '-b', help='branch name', required=True)
def branch_checkout(branch):
    """
    command used to checkout to any particular branch
    """
    click.echo(cmd_git.branch_checkout(branch_name=branch))


@git.command()
@click.option('--branch', '-b', help='branch name', required=True)
def delete_local_branch(branch):
    """
    command used to delete any local branch.
    """
    click.echo(cmd_git.delete_local_branch(branch_name=branch))


@cli.group()
def network():
    """
    function act as a group which is linked to root cli function.
    """
    pass


@network.command()
def show_public_ip():
    """
    command used to fetch your public IP
    """
    click.echo(cmd_network.get_public_ip())


@network.command()
def show_private_ip():
    """
    command used to fetch your private IP
    """
    click.echo(cmd_network.get_private_ip())
