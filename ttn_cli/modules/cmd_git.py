# This file contains all the git related methods
import os

from datetime import date, datetime
from typing import Union, List

from git import Repo, InvalidGitRepositoryError, \
    CheckoutError, GitCommandError, NoSuchPathError


class Command:
    """
    This class contains the operations which refers to Git.
    """
    def __init__(self):
        self.path = os.getcwd()

        # Checks if repo is initialised or not
        try:
            self.repo = Repo(self.path)
        except NoSuchPathError as err:
            print(f"Path '{err}' doesn't exists. "
                  f"Make sure that you provided the correct path.")
        except InvalidGitRepositoryError as err:
            print(f"Invalid Git Repository '{err}'. "
                  "Make sure you are in the correct directory.")

    def _check_repo(self) -> bool:
        """
        This private method checks if
        value exists for self.repo or not
        """
        try:
            if self.repo:
                return True
        except AttributeError:
            return False

    def init_repo(self) -> str:
        """
        This method initialises
        a new git repo to the given path.
        :return: Path where git repo is initialised (or) re-initialised
        """
        self.repo = Repo.init(self.path)
        return f"Repo Initialised to path '{self.path}'"

    def get_all_branches(self) -> Union[List, str]:
        """
        This method return all the branches.
        :return: List of branches or suitable error
        """
        if self._check_repo():
            return [branch.name for branch in self.repo.branches]
        return "Cannot fetch branches. " \
               "Make sure you're in the correct path."

    def get_active_branch(self) -> str:
        """
        This method returns the active branch
        on which you are currently.
        :return: Name of active branch or suitable error
        """
        if self._check_repo():
            return self.repo.active_branch
        return "Cannot fetch active branch. " \
               "Make sure you're in the correct path."

    def get_commits(self) -> Union[List, str]:
        """
        This method returns the list of commits on active branch.
        :return: List of commits or suitable error
        """
        if self._check_repo():
            return list(self.repo.iter_commits(self.get_active_branch()))
        return "Cannot get commits. " \
               "Make sure you're in the correct path."

    def get_commit_count(self) -> Union[int, str]:
        """
        This method returns the total number of commits on a branch.
        :return: Count of commits or suitable error
        """
        if self._check_repo():
            return len(self.get_commits())
        return "Cannot get commit count. " \
               "Make sure you're in the correct path."

    def get_commit_message(self) -> Union[List, str]:
        """
        This method returns the commit
        messages along with the author name.
        :return: List of commit messages or suitable error.
        """
        if self._check_repo():
            commit_list = self.get_commits()
            return list(f"{i.message} -> {i.author}" for i in commit_list)
        return "Cannot get commit messages. " \
               "Make sure you're in the correct path."

    def get_logs(self, author: str = '', from_date: str = None) -> str:
        """
        This method fetch the git logs w.r.t from date.
        :param author: Name of author in form of string
        :param from_date: From date in '%Y-%m-%d' format as string
        :return: git logs in string form or suitable error
        """
        if self._check_repo():
            try:
                from_date = str(datetime.
                                strptime(from_date, '%Y-%m-%d').date())
            except ValueError as err:
                print(err)
                from_date = date.today().strftime('%Y-%m-%d')
            print("Selected date: {}".format(from_date))
            return self.repo.git.log("--oneline",
                                     f'--author={author}',
                                     f'--after={from_date}')

        return "Cannot fetch required logs. " \
               "Make sure you're in the correct path."

    def branch_checkout(self, branch_name: str) -> str:
        """
        This method checkouts to the given branch
        else throws the specific error.
        :param branch_name: Name of the branch
        :return: Checkouts to given branch (or) throws error if any
        """
        if self._check_repo():
            try:
                return self.repo.git.checkout(branch_name)
            except CheckoutError as err:
                return err.args[2].decode('utf-8')
            except GitCommandError as err:
                return err.args[2].decode('utf-8')

        return "Cannot checkout on given branch. " \
               "Make sure you're in the correct path."

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
            return err.args[2].decode("utf-8")


cmd_git = Command()
