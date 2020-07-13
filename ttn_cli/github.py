# This file contains all the git related methods
import os

from datetime import date, datetime

from git import Repo, InvalidGitRepositoryError, \
    CheckoutError, GitCommandError


class GithubOperations:
    """
    This class contains the operations which refers to Git
    """
    def __init__(self):
        self.path = os.getcwd()

        # Checks if repo is initialised or not
        try:
            self.repo = Repo('/home/amulya/Desktop/TTN_CLI/ttn-cli/')
            # self.repo = Repo(self.path)
        except InvalidGitRepositoryError as err:
            self.repo = None
            print(f"Invalid Git Repository '{err}'. "
                  "Make sure you are in the correct directory.")

    def init_repo(self):
        """
        This method initialises
        a new git repo to the given path.
        :return: Path where git repo is initialised (or) re-initialised
        """
        self.repo = Repo.init(self.path)
        return f"Repo Initialised to path '{self.path}'"

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

    def branch_checkout(self, branch_name: str) -> str:
        """
        This method checkouts to the given branch
        else throws the specific error.
        :param branch_name: Name of the branch
        :return: Checkouts to given branch (or) throws error if any
        """
        try:
            return self.repo.git.checkout(branch_name)
        except CheckoutError as err:
            return err.args[2].decode('utf-8')
        except GitCommandError as err:
            return err.args[2].decode('utf-8')

    def delete_local_branch(self, branch_name: str) -> str:
        """
        This method deletes the git branch in local
        and throws an error if branch doesn't exists.
        :param branch_name: Name of the branch
        :return: Message if branch is deleted (or) error has occurred.
        """
        try:
            return self.repo.git.branch("-d", branch_name)
        except GitCommandError as err:
            return err.args[2].decode()


git = GithubOperations()
# print(git.get_commit_message())
# print(git.branch_checkout(branch_name='master'))
# print(git.get_logs(author="vibhor", from_date="2020-07-02"))
