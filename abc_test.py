import abc


class Animal(abc.ABC):

    def run(self):
        # print("正在奔跑...")
        ""
    
    def eat(self, food=None):
        # food = food or ''
        # print(f"正在吃{food}...")
        ""


class Cat(Animal):

    pass


class Dog(Animal):

    pass


def main():
    c = Cat()
    d = Dog()
    c.run()
    print(d.__dict__)

if __name__ == "__main__":
    main()