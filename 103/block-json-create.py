from prefect.blocks.system import JSON

autos = JSON(value=dict(cars=["tesla", "fiat", "chevy"], trucks=["rivian", "ford"]))
autos.save(name="json-block-ex", overwrite=True)

# careful not try to save with capital letters or underscores or spaces!
