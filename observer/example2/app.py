"""
A reffer from https://www.protechtraining.com/blog/post/tutorial-the-observer-pattern-in-python-879
"""
from publisher import Publisher
from subscriber import Subscriber


if __name__ == "__main__":
    pub = Publisher(['lunch', 'dinner'])
    bob = Subscriber('Bob')
    alice = Subscriber('Alice')
    john = Subscriber('John')

    pub.register("lunch", bob)
    pub.register("dinner", alice)
    pub.register("lunch", john)
    pub.register("dinner", john)

    pub.dispatch("lunch", "It's lunchtime!")
    pub.dispatch("dinner", "Dinner is served")