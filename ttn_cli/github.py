# This file contains all the git related methods
import os

# import subprocess
from datetime import date, datetime

from git import Repo, InvalidGitRepositoryError


class GithubOperations:
    def __init__(self):
        self.path = os.getcwd()

        # Checks if repo is initialised or not
        try:
            self.repo = Repo(self.path)
            # self.repo = Repo(self.path)
        except InvalidGitRepositoryError:
            print("Git Repository not Initialised. "
                  "Make sure you are in the correct directory.")

    def get_all_branches(self):
        return [branch.name for branch in self.repo.branches]

    def get_active_branch(self):
        return self.repo.active_branch

    def get_commits(self):
        return list(self.repo.iter_commits(self.get_active_branch()))

    def get_commit_count(self):
        return len(self.get_commits())

    def get_commit_message(self):
        commit_list = self.get_commits()
        return list(f"{i.message} -> {i.author}" for i in commit_list)

    def get_logs(self, author: str = '', from_date: str = None) -> str:
        """
        This method fetch the git logs w.r.t from date.
        :param author: Name of author in form of string
        :param from_date: From date in '%Y-%m-%d' format as string
        :return: git logs in string form
        """
        try:
            from_date = str(datetime.strptime(from_date, '%Y-%m-%d').date())
        except ValueError as err:
            print(err)
            from_date = date.today().strftime('%Y-%m-%d')
        print("Selected date: {}".format(from_date))
        return self.repo.git.log("--oneline",
                                 f'--author={author}',
                                 f'--after={from_date}')


git = GithubOperations()
print(git.get_commit_message())
print(git.get_logs(author="vibhor", from_date="2020-07-02"))
