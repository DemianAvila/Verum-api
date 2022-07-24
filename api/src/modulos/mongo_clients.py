
def mongo_client(client_object,
    user,
    passwd,
    port,
    host,
    database
):
    uri = f"mongodb://{user}:{passwd}@{host}:{port}/{database}?authSource=admin"
    print(uri, flush=True)
    """
    return client_object(f"{host}:{port}",
        username = user,
        password = passwd,
        authSource = database,
        authMechanism='SCRAM-SHA-256'
    )
    """
    #uri = f"mongodb://{user}:{passwd}@{host}:{port}/{database}"
    return client_object(uri)

