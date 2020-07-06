# This file contains all the git related methods

from git import Repo, InvalidGitRepositoryError


class GithubOperations:
    def __init__(self, path=None):
        self.path = path

        # Checks if repo is initialised or not
        try:
            self.repo = Repo('/home/amulya/Desktop/TTN_CLI/ttn-cli/')
            # self.repo = Repo(self.path)
        except InvalidGitRepositoryError:
            print("Git Repository not Initialised!")

    def get_commits(self):
        return list(self.repo.iter_commits("initial_code"))

    def get_commit_count(self):
        return len(self.get_commits())

    def get_commit_message(self):
        commit_list = self.get_commits()
        return list(i.message for i in commit_list)


print(GithubOperations().get_commit_message())
