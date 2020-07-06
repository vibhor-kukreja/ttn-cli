# This file contains all the git related methods
import os

from git import Repo, InvalidGitRepositoryError


class GithubOperations:
    def __init__(self):
        self.path = os.getcwd()

        # Checks if repo is initialised or not
        try:
            self.repo = Repo('/home/amulya/Desktop/TTN_CLI/ttn-cli/')
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

    def get_logs(self, author=''):
        return self.repo.git.log("--oneline", f"--author={author}")


print(GithubOperations().get_logs())
