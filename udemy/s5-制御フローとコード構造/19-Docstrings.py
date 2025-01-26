def example_func(p,o):
    """
    ここに関数の説明を書く
    Args:
        p(int):test
        o(str):test
    Returns:
        bool:test
    """
    print(p)
    print(o)
    return True

# __doc__でDocstringsの中身を見ることができる
print(example_func.__doc__)
