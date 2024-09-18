from prefect import flow, task

@task(name="task1")
def task1():
    print("task1")

@task(name="task2")
def task2():
    print('task2')

@flow(name="first flow")
def first_flow():
    task1()
    task2()
    print("hello prefect")

if __name__ == "__main__":
    first_flow()