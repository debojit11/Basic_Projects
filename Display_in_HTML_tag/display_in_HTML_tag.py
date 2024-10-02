def tagify(tag):
    def decorator_func(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return f"<{tag}>{result}</{tag}>"
        return wrapper
    return decorator_func


@tagify("p")
def greet(name):
    return f"Hello, {name}"

print(greet("Debojit"))