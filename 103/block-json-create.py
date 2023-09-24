from prefect.blocks.system import JSON

autos = JSON(value=dict(cars=["tesla", "fiat", "chevy"], trucks=["rivian", "ford"]))
autos.save(name="json-block-ex", overwrite=True)

# careful don't use .save with capital letters or underscores or spaces!
