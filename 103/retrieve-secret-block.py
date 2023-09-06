from prefect.blocks.system import Secret

secret_block = Secret.load("secret-thing")
print(secret_block.get())
