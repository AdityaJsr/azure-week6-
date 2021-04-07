from decouple import config
import azure.cosmos.cosmos_client as cosmos_client
import azure.cosmos.exceptions as exceptions

db = config("MASTER_KEY")

def list_Containers():
    print("\n5. List all Container in a Database")

    print('Containers:')

    containers = list(db.list_containers())

    if not containers:
        return

    for container in containers:
        print(container['id'])

def main():
    list_Containers()

if __name__ == "__main__":
    main()