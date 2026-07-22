from abc import ABC, abstractmethod 
class IVersionControl(ABC):
    @abstractmethod
    def commit(self, message):
        pass

    @abstractmethod
    def push(self):
        pass

    @abstractmethod
    def pull(self):
        pass

class GitVersionControl(IVersionControl):
    def commit(self, message):
        print(f"Committing changes with message: '{message}'")

    def push(self):
        print("Pushing changes to remote repository")

    def pull(self):
        print("Pulling latest changes from remote repository")

class DevelopmentTeam:
    def __init__(self, version_control: IVersionControl):
        self.version_control = version_control

    def make_changes(self):
        # Simulate making changes to the codebase
        print("Making changes to the codebase...")
        self.version_control.commit("Implemented new feature")
        self.version_control.push()

    def update_codebase(self):
        print("Updating codebase with latest changes...")
        self.version_control.pull()

def main():
    git_vc = GitVersionControl()
    dev_team = DevelopmentTeam(git_vc)

    dev_team.make_changes()
    dev_team.update_codebase()

if __name__ == "__main__":
    main()

"""
+ IVersionControl Interface:      This defines the operations that any version control system should support, like commit, push, and pull. It serves as an abstraction that decouples high-level code from low-level implementations.
+ GitVersionControl Class:        This class implements the IVersionControl interface, providing specific functionality for managing version control using Git.
+ DevelopmentTeam Class:          This class relies on the IVersionControl interface, meaning it can work with any version control implementation that adheres to the interface. It does not need to know the details of how Git works internally.
"""