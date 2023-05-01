from prefect import flow, task
from prefect.tasks import task_input_hash


@task(cache_key_fn=task_input_hash)
def hello_task(name_input):
    print(f"Hello {name_input}!")


@flow
def hello_flow(name_input):
    hello_task(name_input)


if __name__ == "__main__":
    hello_flow("Liz")
