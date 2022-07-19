import json
#from dotenv import load_dotenv


def var(ruta):
    lines = open(ruta, 'r').readlines()
    lines = list(
        map(
            lambda x: x.strip(),
            lines
        )
    )
    lines = list(
        filter(
            lambda x: not x.startswith('#'),
            lines
        )
    )
    lines = list(
        map(
            lambda x: x.split("="), 
            lines
        )
    )
    
    variables = {}
    for line in lines:
        try:
            variables[line[0].strip()] = line[1].strip()
        except:
            pass

    return variables


    """
    load_dotenv(ruta)
    variables = {}
    variables["MONGOD_VER"] = os.getenv("MONGOD_VER")
    variables["WORKDIR"] = os.getenv("WORKDIR")
    variables["MONGO_NAME"] = os.getenv("MONGO_NAME")
    variables["MONGO_USER"] = os.getenv("MONGO_USER") 
    variables["MONGO_PASS"] = os.getenv("MONGO_PASS")
    variables["DATABASE"] = os.getenv("DATABASE")
    variables["PORT_CONT"] = os.getenv("PORT_CONT")
    variables["PORT_SERV"] = os.getenv("PORT_SERV")
    variables["INTERNAL_STORAGE"] = os.getenv("INTERNAL_STORAGE")
    variables["EXTERNAL_STORAGE"] = os.getenv("EXTERNAL_STORAGE")
    variables["PUBLIC_DNS"] = os.getenv("PUBLIC_DNS")
    return variables
    """

