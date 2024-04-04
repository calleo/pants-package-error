import pbipy


def hello_world() -> str:
    return f"hello world from {pbipy.PowerBI.__name__}"


if __name__ == "__main__":
    print(hello_world())
