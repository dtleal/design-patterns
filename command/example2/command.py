"""
A refferal from https://www.geeksforgeeks.org/command-method-python-design-patterns/
"""

from abc import ABC, abstractmethod


class Command(ABC):
    """Class Dedicated to Command"""

    def __init__(self, receiver):
        self.receiver = receiver

    def process(self):
	    pass


class CommandImplementation(Command):
	
	def __init__(self, receiver):
		self.receiver = receiver

	def process(self):
		self.receiver.perform_action()


class Receiver:
    """
    Class dedicated to Receiver
    """
		
    def perform_action(self):
        print('Action performed in receiver.')


class Invoker:
    """
    Class dedicated to Invoker
    """	

    def command(self, cmd):
        self.cmd = cmd

    """execute method"""
    def execute(self):
        self.cmd.process()


def main():
	"""create Receiver object"""
	receiver = Receiver()
	cmd = CommandImplementation(receiver)
	invoker = Invoker()
	invoker.command(cmd)
	invoker.execute()

if __name__ == "__main__":
    main()
	

